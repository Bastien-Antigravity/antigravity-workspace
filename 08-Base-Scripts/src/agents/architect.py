#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.interfaces import SquadEventBus
from src.agents.base_agent import BaseAgent, query_rag_engine

class ArchitectAgent(BaseAgent):
    """
    Architect agent daemon. Specialised in codebase layout design,
    design patterns, and referencing architectural specifications (ADRs).
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="architect",
            prompt_file="02-Architect/Prompt-Architect.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
        # Inherit query_rag_engine from BaseAgent
        self.tools = [query_rag_engine]
