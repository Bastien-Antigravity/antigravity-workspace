#!/usr/bin/env python
# coding:utf-8

import os
from typing import Optional
from src.interfaces.llm import ILLMProvider
from src.models.context import SystemContext

class LLMProviderFactory:
    """
    AI-CONTEXT: Factory to instantiate the appropriate LLM provider based on context.
    """
    @staticmethod
    def create(ctx: SystemContext) -> Optional[ILLMProvider]:
        client = ctx.active_client
        
        if client == "deepseek":
            from .openai import OpenAIProvider
            api_key = os.getenv("DEEPSEEK_API_KEY")
            model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
            base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
            if not api_key:
                print("⚠️ DEEPSEEK_API_KEY not found in environment.")
                return None
            return OpenAIProvider(api_key, model, base_url)
            
        elif client == "gemini":
            from .gemini import GeminiProvider
            api_key = os.getenv("GEMINI_API_KEY")
            model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
            if not api_key:
                print("⚠️ GEMINI_API_KEY not found in environment.")
                return None
            return GeminiProvider(api_key, model)
            
        return None
