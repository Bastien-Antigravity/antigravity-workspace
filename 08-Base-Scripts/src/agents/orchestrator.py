#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.interfaces import SquadEventBus
from src.agents.base_agent import BaseAgent

class OrchestratorAgent(BaseAgent):
    """
    Orchestrator agent daemon responsible for decomposing user goals,
    delegating tasks to specific agents, and reporting progress.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="orchestrator",
            prompt_file="01-Orchestrator/Prompt-Orchestrator.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
