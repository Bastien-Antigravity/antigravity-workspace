#!/usr/bin/env python
# coding:utf-8

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class WorkflowStep:
    """
    AI-CONTEXT: A single step in an automated workflow.
    """
    name: str
    action: str # 'prompt', 'audit', 'shell', 'signoff'
    persona: str
    description: str
    params: Dict[str, Any] = field(default_factory=dict)

@dataclass
class WorkflowSchema:
    """
    AI-CONTEXT: A complete configurable workflow definition.
    """
    name: str
    description: str
    steps: List[WorkflowStep]
