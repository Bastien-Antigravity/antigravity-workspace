#!/usr/bin/env python
# coding:utf-8

"""
Bastien-Antigravity AI Squad: Professional Chat UI
Powered by Chainlit and the Exposed Strategy Engine.
"""

import os
import sys

# --- Bootstrap ---
import os, sys
_vault_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(_vault_root)
try:
    from src.core.bootstrap import init as bootstrap_init
    bootstrap_init(__file__)
except ImportError:
    pass

import chainlit as cl

try:
    from src import EngineFacade as SquadFacade
    from src.models.message import AgentMessage
except ImportError:
    print("❌ Error: Could not import Squad Core. Ensure you are running from the vault root.")
    sys.exit(1)

facade = SquadFacade(_vault_root)

@cl.on_chat_start
async def start():
    # 1. Run Pre-session rituals (Strategy: Pre-treatment)
    facade.governance.run_preflight()
    facade.mcp.configure_mcp()
    
    # 2. Initialize Memory Session
    facade.session_id = facade.memory.create_session(
        facade.ctx.active_mode, 
        facade.ctx.active_client
    )
    
    cl.user_session.set("facade", facade)
    
    await cl.Message(
        content=f"🧠 **Bastien-Antigravity Squad Online**\n"
                f"Protocol: `{facade.ctx.mode_name}`\n"
                f"Client: `{facade.ctx.active_client}`\n"
                f"Memory ID: `{facade.session_id}`"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    f = cl.user_session.get("facade")
    
    # 1. Validate Provider
    provider = f.get_provider()
    if not provider:
        await cl.Message(content="❌ AI Provider not configured. Check your API keys.").send()
        return

    # 2. Add user message to memory
    user_msg = AgentMessage(role="user", content=message.content)
    f.memory.store_message(f.session_id, user_msg)
    
    # 3. Prepare Prompt Logic (Strategy: Persona Selection)
    persona = "orchestrator"  # Default for UI
    system_prompt = f.personas.load_prompt(persona) or "You are a helpful assistant."
    
    # Retrieve history from SQLite
    history = f.memory.get_session_history(f.session_id)
    
    # Construct message list for provider
    messages = [AgentMessage(role="system", content=system_prompt)] + history

    # 4. Execute LLM Completion
    # We send an empty message first to show the user we are working
    response_msg_cl = cl.Message(content="")
    await response_msg_cl.send()
    
    response = await provider.chat(messages)
    
    # Handle Reasoning/Thought if present
    if response.thought:
        async with cl.Step(name="Reasoning") as step:
            step.output = response.thought
    
    # 5. Save assistant response to memory
    f.memory.store_message(f.session_id, response)
    
    # 6. Update UI with final response
    response_msg_cl.content = response.content
    await response_msg_cl.update()
