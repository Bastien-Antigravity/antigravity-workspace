#!/usr/bin/env python
# coding:utf-8

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class AgentMessage:
    """
    AI-CONTEXT: Standardized message format for all SDK providers.
    """
    role: str # 'user', 'assistant', 'system', 'tool'
    content: str
    thought: Optional[str] = None # For models with reasoning (e.g. DeepSeek R1)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    tool_result: Optional[Dict[str, Any]] = None
