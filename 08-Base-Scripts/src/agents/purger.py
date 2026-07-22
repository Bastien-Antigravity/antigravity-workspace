#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.agents.interfaces import SquadEventBus

class PurgerAgent(BaseAgent):
    """
    Purger agent daemon. Specialised in code cleanup, removing deprecated modules,
    and enforcing minimalistic design patterns.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="purger",
            prompt_file="08-Purger/Mister-Straight-to-Goal.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
