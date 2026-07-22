#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.agents.interfaces import SquadEventBus

class PatternSentinelAgent(BaseAgent):
    """
    PatternSentinel agent daemon. Specialised in layout coherence checks,
    identifying anti-patterns, and enforcing strategic rules.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="patternsentinel",
            prompt_file="12-PatternSentinel/Prompt-Pattern-Sentinel.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
