#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.interfaces import SquadEventBus

class SentinelAgent(BaseAgent):
    """
    Sentinel agent daemon. Specialised in real-time system monitoring, security audits,
    and enforcing access constraints.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="sentinel",
            prompt_file="09-Sentinel/Prompt-Sentinel.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
