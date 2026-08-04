#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.interfaces import SquadEventBus

class OracleAgent(BaseAgent):
    """
    Oracle agent daemon. Specialised in long-term chronological log auditing,
    historical analysis, and querying temporal knowledge vaults.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="oracle",
            prompt_file="00-Oracle/Prompt-Chronos-Oracle.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
