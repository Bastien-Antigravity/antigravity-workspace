#!/usr/bin/env python
# coding:utf-8

"""
Bastien-Antigravity AI Squad: Professional Chat UI
Powered by Chainlit and the OOP Squad Core.
"""

import os
import sys
import chainlit as cl

# Ensure we can find the core package
vault_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if vault_root not in sys.path:
    sys.path.append(vault_root)

try:
    from src import EngineFacade as SquadOrchestrator
    from src.models.message import AgentMessage as Message
except ImportError:
    print("❌ Error: Could not import Squad Core. Ensure you are running from the vault root.")
    sys.exit(1)

orchestrator = SquadOrchestrator(vault_root)

@cl.on_chat_start
async def start():
    # 1. Run Pre-session rituals
    orchestrator.governance.run_preflight()
    orchestrator.mcp.configure_mcp()

    # 2. Initialize Memory Session
    orchestrator.session_id = orchestrator.memory.create_session(
        orchestrator.ctx.active_mode,
        orchestrator.ctx.active_client
    )

    cl.user_session.set("orchestrator", orchestrator)

    await cl.Message(
        content=f"🧠 **Bastien-Antigravity Squad Online**\n"
                f"Protocol: `{orchestrator.ctx.mode_name}`\n"
                f"Client: `{orchestrator.ctx.active_client}`\n"
                f"Memory ID: `{orchestrator.session_id}`"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    orch = cl.user_session.get("orchestrator")
    provider = orch.get_provider()

    if not provider:
        await cl.Message(content="❌ Error: AI Provider not configured. Check your API keys.").send()
        return

    # Load Persona Prompt
    # (In a full implementation, we'd allow selecting persona via UI)
    persona_prompt = orch.personas.load_prompt("orchestrator") or "You are a helpful assistant."

    # Standard history retrieval from Memory
    history = orch.memory.get_session_history(orch.session_id)

    # Prepare messages for SDK
    msgs = [Message(role="system", content=persona_prompt)] + history
    msgs.append(Message(role="user", content=message.content))

    # Store user message
    orch.memory.store_message(orch.session_id, msgs[-1])
    # Agent Thought Processing
    thought_msg = cl.Message(content="")
    await thought_msg.send()
    
    # (Simplification: In a full SDK loop, we'd handle tool calls here)
    response_msg = await provider.chat(msgs)
    
    # Store and Display Thought
    if response_msg.thought:
        async with cl.Step(name="Reasoning") as step:
            step.output = response_msg.thought
    
    # Display Response
    await cl.Message(content=response_msg.content).send()
    
    # Persist Response
    orch.memory.store_message(orch.session_id, response_msg)
