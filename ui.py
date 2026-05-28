#!/usr/bin/env python
# coding:utf-8

"""
Bastien-Antigravity AI Squad: Professional Chat UI
Powered by Chainlit and the Exposed Strategy Engine.
"""

import os
import sys
import chainlit as cl

# --- Virtual Environment Bootstrap ---
_vault_root = os.path.dirname(os.path.abspath(__file__))
if _vault_root not in sys.path:
    sys.path.append(_vault_root)

try:
    from src.squad import SquadFacade
    from src.models.message import MSquadMessage
except ImportError:
    print("❌ Error: Could not import Squad Core. Ensure you are running from the vault root.")
    sys.exit(1)

facade = SquadFacade(_vault_root)

@cl.on_chat_start
async def start():
    # 1. Run Pre-session rituals (Strategy: Pre-treatment)
    facade.rituals.run_preflight()
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
    provider = f.get_provider()
    
    if not provider:
        await cl.Message(content="❌ Error: AI Provider not configured. Check your API keys.").send()
        return

    # Strategy: Persona Selection
    persona_prompt = f.personas.load_prompt("orchestrator") or "You are a helpful assistant."
    
    history = f.memory.get_session_history(f.session_id)
    
    msgs = [MSquadMessage(role="system", content=persona_prompt)] + history
    msgs.append(MSquadMessage(role="user", content=message.content))
    
    f.memory.store_message(f.session_id, msgs[-1])

    thought_msg = cl.Message(content="")
    await thought_msg.send()
    
    # SDK execution
    response_msg = await provider.chat(msgs)
    
    if response_msg.thought:
        async with cl.Step(name="Reasoning") as step:
            step.output = response_msg.thought
    
    await cl.Message(content=response_msg.content).send()
    f.memory.store_message(f.session_id, response_msg)
