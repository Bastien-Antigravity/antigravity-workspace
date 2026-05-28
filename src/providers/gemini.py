#!/usr/bin/env python
# coding:utf-8

import os
from typing import List, Optional, Any, Iterable
import google.generativeai as genai
from ..interfaces.llm import ILLMProvider
from ..models.message import AgentMessage

class GeminiProvider(ILLMProvider):
    """
    AI-CONTEXT: SDK Provider for Google Gemini.
    """
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model_name=model)

    async def chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> AgentMessage:
        # Note: google-generativeai has its own history management
        # For simplicity in this stateless abstraction, we rebuild the chat session
        history = []
        for m in messages[:-1]:
            role = "user" if m.role == "user" else "model"
            history.append({"role": role, "parts": [m.content]})
        
        chat_session = self.client.start_chat(history=history)
        last_msg = messages[-1].content
        
        # Tools integration in Gemini SDK is via the GenerativeModel constructor or start_chat
        response = chat_session.send_message(last_msg)
        
        content = ""
        try:
            content = response.text
        except ValueError:
            # Handle cases where response might only be a tool call
            pass
        
        tool_calls = []
        if response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.function_call:
                    tool_calls.append({
                        "name": part.function_call.name,
                        "args": dict(part.function_call.args)
                    })

        return AgentMessage(
            role="assistant",
            content=content,
            tool_calls=tool_calls
        )

    def stream_chat(self, messages: List[AgentMessage], tools: Optional[List[Any]] = None) -> Iterable[AgentMessage]:
        raise NotImplementedError("Streaming not yet implemented.")
