#!/usr/bin/env python
# coding:utf-8

import os
import asyncio
from typing import List, Optional, Any, Iterable
from openai import AsyncOpenAI
from src.interfaces.llm import ILLMProvider
from src.models.message import AgentMessage

class OpenAIProvider(ILLMProvider):
    """
    AI-CONTEXT: SDK Provider for OpenAI-compatible APIs (DeepSeek, Groq, etc.).
    """
    def __init__(self, api_key: str, model: str, base_url: str = "https://api.openai.com/v1"):
        super().__init__(api_key, model)
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> AgentMessage:
        # Convert our AgentMessage format to OpenAI format
        openai_msgs = []
        for m in messages:
            msg = {"role": m.role, "content": m.content}
            if m.role == "assistant" and m.thought:
                # Some models support thought in content or as a specific field
                msg["content"] = f"<think>\n{m.thought}\n</think>\n{m.content}"
            openai_msgs.append(msg)

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=openai_msgs,
            tools=tools
        )
        
        choice = response.choices[0].message
        content = choice.content or ""
        thought = None
        
        # Extract thought if model uses <think> tags (like DeepSeek R1)
        if content and "<think>" in content and "</think>" in content:
            parts = content.split("</think>", 1)
            thought = parts[0].replace("<think>", "").strip()
            content = parts[1].strip()

        return AgentMessage(
            role="assistant",
            content=content,
            thought=thought,
            tool_calls=[tc.model_dump() for tc in choice.tool_calls] if choice.tool_calls else []
        )

    def stream_chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> Iterable[AgentMessage]:
        # Implementation for streaming (can be added later for UI)
        raise NotImplementedError("Streaming not yet implemented.")
