#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.agents.interfaces import SquadEventBus

class PrototyperAgent(BaseAgent):
    """
    Prototyper agent daemon. Specialised in generating boilerplate templates,
    one-off scripts, and layout mocks.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="prototyper",
            prompt_file="13-Prototyper/Prompt-Prototyper.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
