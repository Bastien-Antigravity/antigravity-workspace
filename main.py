#!/usr/bin/env python
# coding:utf-8

"""
🧠 Bastien-Antigravity: Orchestration Engine (Main Entry)
Unified launcher following the logic and behavior of legacy start_engine.py.
"""

import os
import sys
import asyncio
import subprocess
from datetime import datetime

# --- Bootstrap ---
import os, sys
_vault_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(_vault_root)
try:
    from src.core.bootstrap import init as bootstrap_init
    bootstrap_init(__file__)
except ImportError:
    pass

from src import EngineFacade as SquadFacade

def main():
    facade = SquadFacade(_vault_root)
    
    facade.mcp.backup_settings()
    try:
        while True:
            facade.print_header()
            
            # 1. PRE-TREATMENT (Protocols & Sync)
            facade.governance.manage_kms_permissions(protect=False)
            facade.governance.run_preflight()
            facade.personas.sync_to_adapters()
            facade.governance.manage_kms_permissions(protect=True)
            
            # 2. STRATEGY SELECTION (Mode Selector)
            facade.handle_mode_selection()
            
            # 3. GOVERNANCE (Session Health)
            if not facade.governance.check_session_health():
                print("\n🛑 Session blocked by Governance protocols. Please resolve uncommitted changes.")
                decision = input("Force start anyway? [y/N]: ").strip().lower()
                if decision != 'y':
                    break
                
            facade.mcp.configure_mcp()
            
            # 4. EXECUTION ENGINE
            facade.session_id = facade.memory.create_session(facade.ctx.active_mode, facade.ctx.active_client)
            mission_id = f"M-{datetime.now().strftime('%Y%m%d-%H%M')}-{facade.session_id}"
            facade.ctx.start_mission(mission_id)
            print(f"📁 Session Memory Active: ID {facade.session_id} | Mission: {mission_id}")
            
            print("\n--- 🎯 Task Routing ---")
            print("[1] Run Configurable Workflow (Automation)")
            print("[2] Run Agentic LangGraph (Graph)")
            print("[3] Start Manual Persona Session (Interactive)")
            
            has_rag = facade.check_rag_attached()
            if has_rag:
                print("[r] Reset ChromaDB RAG Index")
            print("[p] Extract Personas (Background Daemon)")
            
            choice = input("\nSelect execution strategy [1-3] or action [r/p] (Enter for Manual): ").strip().lower()
            
            if choice == "1":
                asyncio.run(facade.handle_workflow_execution())
            elif choice == "2":
                try:
                    from strategies.graph import GraphWorkflowManager
                    graph = GraphWorkflowManager(facade.ctx, facade)
                    task = input("\nEnter task for Agentic Graph: ").strip()
                    if task:
                        asyncio.run(graph.execute_graph("orchestrator", task))
                except ImportError:
                    print("❌ LangGraph strategy not available.")
            elif choice == "r" and has_rag:
                facade.reset_rag_index()
                continue
            elif choice == "p":
                facade.extract_personas()
                continue
            else:
                selected_persona = facade.handle_persona_selection()
                facade.execute_legacy_cli(selected_persona)
                
            # 5. POST-TREATMENT (Lifecycle & Sign-off)
            if not facade.handle_post_session():
                break
    finally:
        facade.mcp.restore_settings()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
        sys.exit(0)
