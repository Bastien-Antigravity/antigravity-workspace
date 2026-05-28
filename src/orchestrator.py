#!/usr/bin/env python
# coding:utf-8

import os
import sys
import asyncio
import subprocess
from typing import Optional, Any
from ..models.context import SystemContext, MODES
from ..core.governance import GovernanceManager
from ..managers.persona import PersonaManager
from ..core.mcp import MCPManager
from ..core.security import AccessController
from ..core.memory import MemoryManager
from ..strategies.workflow import WorkflowManager
from ..providers.factory import LLMProviderFactory
from ..interfaces.llm import ILLMProvider

class EngineFacade:
    """
    AI-CONTEXT: Master Lifecycle Loop Controller (Facade Pattern).
    Ties together Context, Governance, Personas, MCP, Security, Memory, and Workflows.
    """
    def __init__(self, vault_root: str):
        workspace_root = os.path.abspath(os.path.join(vault_root, ".."))
        self.ctx = SystemContext(vault_root, workspace_root)
        self.governance = GovernanceManager(self.ctx)
        self.personas = PersonaManager(self.ctx)
        self.mcp = MCPManager(self.ctx)
        self.security = AccessController(self.ctx)
        self.memory = MemoryManager(vault_root)
        self.workflows = WorkflowManager(self.ctx)
        self.session_id: Optional[int] = None

    def get_provider(self) -> Optional[ILLMProvider]:
        """Instantiates the SDK-based provider based on context."""
        return LLMProviderFactory.create(self.ctx)

    def launch(self) -> None:
        """Implements the interactive lifecycle loop."""
        # 0. Initial Mission Briefing
        self.print_mission_help()
        
        while True:
            self.print_header()
            
            # 1. Sync & Verification
            self.governance.manage_kms_permissions(protect=False)
            self.governance.run_preflight()
            self.personas.sync_to_adapters()
            self.governance.manage_kms_permissions(protect=True)
            
            # 2. Mode Selection
            self.handle_mode_selection()
            
            # 3. Governance Protocols
            if not self.governance.check_session_health():
                print("👋 Session aborted by governance protocol.")
                break
                
            self.mcp.configure_mcp()
            
            # 4. Persistence Initialization
            self.session_id = self.memory.create_session(self.ctx.active_mode, self.ctx.active_client)
            print(f"📁 Session Memory Active: ID {self.session_id}")
            
            # 5. Task Routing (Workflows vs Manual Persona)
            print("\n--- 🎯 Task Routing ---")
            print("[1] Run Configurable Workflow (Automation)")
            print("[2] Start Manual Persona Session (Interactive)")
            task_choice = input("\nSelect routing [1-2] (Enter for Manual): ").strip()

            if task_choice == "1":
                asyncio.run(self.handle_workflow_execution())
            else:
                selected_persona = self.handle_persona_selection()
                self.execute_legacy_cli(selected_persona)
            
            # 6. Lifecycle Decision
            if not self.handle_post_session():
                break

    async def handle_workflow_execution(self):
        available = self.workflows.list_workflows()
        if not available:
            print("⚠️ No workflows found in 00-AI-Orchestration/workflows/")
            return

        print("\n📜 Available Workflows:")
        for idx, w in enumerate(available, 1):
            print(f"[{idx}] {w}")

        choice = input(f"\nSelect Workflow [1-{len(available)}]: ").strip()
        if choice.isdigit():
            val = int(choice)
            if 1 <= val <= len(available):
                wf_name = available[val-1]
                wf = self.workflows.load_workflow(wf_name)
                if wf:
                    print(f"\n🚀 Starting Workflow: {wf.name}")
                    for step in wf.steps:
                        await self.workflows.execute_step(step, self)
                    print(f"\n✅ Workflow '{wf.name}' completed.")

    def print_header(self) -> None:
        print("\n" + "="*60)
        print("🧠 BASTIEN-ANTIGRAVITY: AI ENGINE (CORE)")
        print("="*60)

    def print_mission_help(self) -> None:
        """Displays ASCII cheat sheets and guidelines."""
        try:
            # Add scripts directory to sys.path temporarily to import MissionHelper
            scripts_dir = os.path.join(self.ctx.vault_root, "20-Scripts-new")
            if scripts_dir not in sys.path:
                sys.path.append(scripts_dir)
            from engine_help import MissionHelper
            helper = MissionHelper()
            helper.print_cheat_sheet()
        except ImportError:
            print("\n💡 Tip: Use 'Mission Planning' for complex task delegation.")

    def check_rag_attached(self) -> bool:
        """Returns True if the 08-RAG-Engine and its server.py exist."""
        rag_dir = os.path.join(self.ctx.vault_root, "08-RAG-Engine")
        rag_server_script = os.path.join(rag_dir, "src", "core", "server.py")
        return os.path.exists(rag_dir) and os.path.exists(rag_server_script)

    def reset_rag_index(self) -> None:
        """Resets and rebuilds ChromaDB RAG index."""
        rag_dir = os.path.join(self.ctx.vault_root, "08-RAG-Engine")
        rag_main_script = os.path.join(rag_dir, "main.py")
        if not os.path.exists(rag_main_script):
            print("❌ Error: 08-RAG-Engine/main.py not found.")
            return

        local_venv = os.path.join(rag_dir, ".venv")
        local_python = os.path.join(local_venv, "Scripts", "python.exe") if os.name == "nt" else os.path.join(local_venv, "bin", "python3")
        if not os.path.exists(local_python):
            local_python = sys.executable

        print("🗑️ Resetting RAG Index...")
        subprocess.run([local_python, rag_main_script, "index", "--reset"])

    def extract_personas(self) -> None:
        """Spawns persona_extractor.py context-gathering engine in the background."""
        persona_script = os.path.join(self.ctx.vault_root, "20-Scripts-new", "persona_extractor.py")
        if not os.path.exists(persona_script):
            persona_script = os.path.join(self.ctx.vault_root, "20-Scripts", "persona_extractor.py")

        if not os.path.exists(persona_script):
            print("❌ Error: persona_extractor.py not found.")
            return

        lock_path = os.path.abspath(os.path.join(self.ctx.vault_root, "07-Core-KMS", "quick-overview", "ast-patterns", ".persona_running"))
        if os.path.exists(lock_path):
            print("⚠️ Persona Extractor is already running. Please wait.")
            return

        print("🎭 Launching Persona Extractor in background...")
        subprocess.Popen([sys.executable, persona_script, "--daemon"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)

    def handle_mode_selection(self) -> None:
        has_rag = self.check_rag_attached()
        while True:
            print("\n--- 🕹️ Mode Selector ---")
            for key, (name, desc) in MODES.items():
                print(f"[{key}] {name.ljust(18)} : {desc}")
            if has_rag:
                print(f"[r] {'🗑️  Reset RAG'.ljust(18)} : Reset and rebuild ChromaDB RAG index.")
            print(f"[p] {'🎭 Extract Personas'.ljust(18)} : Extract polyglot codebase context in background.")

            choice = input(f"\nSelect mode [1-4] or action (Current: {self.ctx.active_mode}): ").strip().lower()
            if not choice:
                break
            if choice in MODES:
                self.ctx.switch_mode(choice)
                break
            elif choice == 'r' and has_rag:
                self.reset_rag_index()
            elif choice == 'p':
                self.extract_personas()
            else:
                print("❌ Invalid selection.")

    def handle_persona_selection(self) -> str:
        available = self.personas.list_personas()
        if "orchestrator" in available:
            print(f"\n🎭 Protocol {self.ctx.active_mode} active: Routing via Orchestrator.")
            return "orchestrator"
            
        print("\n🎭 Available Personas:")
        for idx, p in enumerate(available, 1):
            print(f"[{idx}] {p}")
        
        choice = input(f"\nSelect Persona [1-{len(available)}] (Enter for Generic): ").strip()
        if choice.isdigit():
            val = int(choice)
            if 1 <= val <= len(available):
                return available[val-1]
        return ""

    def execute_legacy_cli(self, persona: str) -> None:
        """Temporary bridge to the old CLI clients."""
        print(f"\n🚀 Launching {self.ctx.active_client} [Mode: {self.ctx.active_mode} | Persona: {persona or 'Generic'}]...")
        
        try:
            # The registry is now in the root 'clients' folder
            if self.ctx.vault_root not in sys.path:
                sys.path.append(self.ctx.vault_root)
            
            from clients.registry import build_launch_command
            cmd = build_launch_command(
                self.ctx.active_client,
                persona,
                squad_mode=self.ctx.active_mode,
                vault_root=self.ctx.vault_root
            )
            cmd_prefix = [] if os.name != 'nt' else ["cmd", "/c"]
            subprocess.run(cmd_prefix + cmd)
        except Exception as e:
            print(f"❌ CLI Launch Error: {e}")

    def handle_post_session(self) -> bool:
        print("\n--- 🏁 Session Paused ---")
        decision = input("Re-launch Engine? [y: Yes / n: Exit / s: Switch Mode]: ").lower().strip()
        if decision == 'n':
            return self.governance.run_signoff()
        return True
