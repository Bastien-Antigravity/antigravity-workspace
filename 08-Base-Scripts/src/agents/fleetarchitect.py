#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.agents.interfaces import SquadEventBus

class FleetArchitectAgent(BaseAgent):
    """
    FleetArchitect agent daemon. Specialised in cross-service coordination,
    shared configuration management, and microservice layout structures.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="fleetarchitect",
            prompt_file="05-FleetArchitect/Prompt-Fleet-Architect.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
