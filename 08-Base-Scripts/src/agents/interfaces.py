#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
Provides the SquadEventBus interface and DualSquadEventBus concrete class
routing multi-agent communications via NATS or LocalEventBus in offline mode.
"""

import json
import asyncio
from typing import Dict, Any, List, Callable, Awaitable
from nats.aio.client import Client as NATS

class SquadEventBus:
    """Abstract interface defining the pub/sub event bus contract for AI squad coordination."""
    async def connect(self) -> None:
        """Initializes connection to the underlying message bus."""
        raise NotImplementedError

    async def publish(self, topic: str, payload: Dict[str, Any]) -> None:
        """Broadcasts a payload JSON dictionary onto a topic channel."""
        raise NotImplementedError

    async def subscribe(self, topic: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]) -> None:
        """Registers a non-blocking async callback listener for a topic channel."""
        raise NotImplementedError

    async def close(self) -> None:
        """Cleans up resources and disconnects from the transit layer."""
        raise NotImplementedError


class EventDeduplicator:
    _seen = set()
    _seen_list = []
    MAX_SIZE = 1000

    @classmethod
    def is_duplicate(cls, event_id: str) -> bool:
        if not event_id:
            return False
        if event_id in cls._seen:
            return True
        cls._seen.add(event_id)
        cls._seen_list.append(event_id)
        if len(cls._seen_list) > cls.MAX_SIZE:
            oldest = cls._seen_list.pop(0)
            cls._seen.discard(oldest)
        return False


class LocalEventBus:
    """In-memory fallback event bus for NATS-offline/local testing."""
    _subscribers = None

    @classmethod
    def _get_subscribers(cls):
        if cls._subscribers is None:
            cls._subscribers = {}
        return cls._subscribers

    @classmethod
    def subscribe(cls, topic: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]):
        subs = cls._get_subscribers()
        if topic not in subs:
            subs[topic] = []
        subs[topic].append(callback)

    @classmethod
    def publish(cls, topic: str, payload: Dict[str, Any]):
        # Deduplicate local events
        event_id = payload.get("event_id")
        if event_id and EventDeduplicator.is_duplicate(event_id):
            return

        subs = cls._get_subscribers()
        subscribers = subs.get(topic, [])
        for cb in subscribers:
            try:
                asyncio.create_task(cb(payload))
            except Exception:
                pass


class DualSquadEventBus(SquadEventBus):
    """
    Unified hybrid event bus that attempts NATS broker routing but cleanly falls back
    to in-memory LocalEventBus if NATS is offline, avoiding noisy traceback logs.
    """
    def __init__(self, nats_url: str, logger: Any):
        self.nats_url = nats_url
        self.logger = logger
        self.nc = NATS()
        self.nats_connected = False

    async def connect(self) -> None:
        """Attempts a resilient 1-try connection to NATS, falling back to Local otherwise."""
        try:
            # Resilient 1-try connect without background loop reconnect attempts
            await self.nc.connect(self.nats_url, timeout=0.5, max_reconnect_attempts=1, allow_reconnect=False)
            self.nats_connected = True
            self.logger.info(f"SquadEventBus connected to NATS at {self.nats_url}")
        except Exception:
            self.logger.warning("SquadEventBus: NATS server is offline. Falling back to in-memory LocalEventBus.")
            self.nats_connected = False
            try:
                await self.nc.close()
            except Exception:
                pass

    async def publish(self, topic: str, payload: Dict[str, Any]) -> None:
        """Routes message broadcast depending on NATS connection state."""
        import uuid
        if "event_id" not in payload:
            payload["event_id"] = str(uuid.uuid4())

        if self.nats_connected:
            try:
                await self.nc.publish(topic, json.dumps(payload).encode("utf-8"))
            except Exception as e:
                self.logger.error(f"SquadEventBus failed to publish to NATS: {e}. Falling back to Local.")
                LocalEventBus.publish(topic, payload)
        else:
            LocalEventBus.publish(topic, payload)

    async def subscribe(self, topic: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]) -> None:
        """Subscribes callback to the correct event provider."""
        # Always register local fallback subscription to ensure seamless offline state routing
        LocalEventBus.subscribe(topic, callback)
        
        if self.nats_connected:
            async def nats_callback(msg):
                try:
                    payload = json.loads(msg.data.decode("utf-8"))
                    # Deduplicate NATS events
                    event_id = payload.get("event_id")
                    if event_id and EventDeduplicator.is_duplicate(event_id):
                        return
                    await callback(payload)
                except Exception as e:
                    self.logger.error(f"SquadEventBus subscriber failed to process NATS payload: {e}")
            try:
                await self.nc.subscribe(topic, cb=nats_callback)
                self.logger.info(f"SquadEventBus subscribed to NATS topic '{topic}'")
            except Exception as e:
                self.logger.error(f"SquadEventBus failed NATS subscription to '{topic}': {e}")

    async def close(self) -> None:
        """Closes connection cleanly."""
        if self.nats_connected:
            try:
                await self.nc.close()
            except Exception:
                pass
            self.nats_connected = False
