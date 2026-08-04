#!/usr/bin/env python
# coding:utf-8

from typing import Any
from src.agents.base_agent import BaseAgent
from src.interfaces import SquadEventBus

class DocMaintainerAgent(BaseAgent):
    """
    DocMaintainer agent daemon. Specialised in verifying documentation alignment,
    detecting document drift, and suggesting manual corrections.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="docmaintainer",
            prompt_file="06-DocMaintainer/Prompt-DocMaintainer.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
