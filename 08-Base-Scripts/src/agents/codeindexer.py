#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.interfaces import SquadEventBus

class CodeIndexerAgent(BaseAgent):
    """
    CodeIndexer agent daemon. Specialised in code symbol parsing, cross-referencing,
    and semantic dependency indexing.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="codeindexer",
            prompt_file="11-CodeIndexer/Prompt-CodeIndexer.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
