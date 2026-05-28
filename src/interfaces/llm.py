#!/usr/bin/env python
# coding:utf-8

from abc import ABC, abstractmethod
from typing import List, Optional, Any, Iterable
from src.models.message import AgentMessage

class ILLMProvider(ABC):
    """
    AI-CONTEXT: Abstract Base Class for SDK-based AI Providers.
    Ensures a unified interface for chat and tool orchestration.
    """
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    async def chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> AgentMessage:
        """Sends a conversation history and returns the next message."""
        pass

    @abstractmethod
    def stream_chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> Iterable[AgentMessage]:
        """Streams a conversation (useful for UI responsiveness)."""
        pass
