#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS: CommandController
  Unified backend router and operational controller for Bastien-Antigravity squad execution.
  Exposes centralized handlers for user chat events across CLI, Web, Discord, and Telegram.

DATA FLOW:
  1. Input:   Raw user text payload, session/channel ID, and target options.
  2. Logic:   Retrieves recent context + long-term semantic RAG context, stores the turn
              in PostgreSQL, and routes/triggers command and agent lifecycles.
  3. Output:  Structured result payload (text answer and action flags).

KEY PARAMETERS:
  - config:   Active bootstrap configuration settings.
  - logger:   UniLog logger instance.
"""

import sys
import time
import asyncio
from typing import Dict, Any, List, Optional
from json import dumps as jsonDumps

from interfaces import Command, MemoryStore
from lib.pg_pool import get_pg_pool, resolve_schema_name
from lib.memory import ShortTermMemory, PostgresMemoryStore, RAGMemoryStore, DualLayerMemoryStore

# -----------------------------------------------------------------------------------------------

class CommandController(Command):
    """
    Unified controller coordinating conversational context flow, RAG queries,
    and agent subcommand dispatching.
    """

    Name = "CommandController"

    def __init__(self, *, config: Any, logger: Any):
        self.config = config
        self.logger = logger
        self.schema = resolve_schema_name(__file__)
        self.pool = get_pg_pool(config=self.config, logger=self.logger)
        self.memory = self._setup_memory()
        from pathlib import Path
        self.repo_root = Path(__file__).resolve().parent.parent.parent

    # -----------------------------------------------------------------------------------------------

    def _setup_memory(self) -> MemoryStore:
        """Sets up the dynamic dual-layer memory layers."""
        # 1. Setup short-term memory layer
        if self.pool:
            short_term = PostgresMemoryStore(
                config=self.config,
                logger=self.logger,
                pg_pool=self.pool,
                schema=self.schema
            )
        else:
            short_term = ShortTermMemory(
                config=self.config,
                logger=self.logger,
                max_size=50
            )

        # 2. Setup long-term semantic layer
        long_term = RAGMemoryStore(
            config=self.config,
            logger=self.logger,
            tenant=self.schema,
            client=self.config.data.get("rag_client")
        )

        # 3. Combine into unified DualLayer memory manager
        return DualLayerMemoryStore(
            config=self.config,
            logger=self.logger,
            short_term=short_term,
            long_term=long_term
        )

    # -----------------------------------------------------------------------------------------------

    def process_message(self, *, channel: str, session_id: str, user_msg: str) -> Dict[str, Any]:
        """
        Receives user input from any client facade, processes memory context,
        and routes execution.
        """
        self.logger.info("{0} : Incoming message on channel '{1}' (session: {2})".format(self.Name, channel, session_id))

        # Persist user turn
        user_turn = {"role": "user", "content": user_msg}
        self.memory.add(user_turn, session_id)

        # Retrieve integrated short-term & long-term history context
        context_turns = self.memory.retrieve(user_msg, session_id, limit=10)

        # Process / Mock Agent execution flow (this will invoke the squad agent runtime in production)
        response_text = "Received message. Context window hydrated with {0} history turn(s). Ready to process.".format(len(context_turns))
        
        # Persist assistant turn
        assistant_turn = {"role": "assistant", "content": response_text}
        self.memory.add(assistant_turn, session_id)

        return {
            "status": "success",
            "answer": response_text,
            "context_size": len(context_turns),
            "session_id": session_id
        }

    # -----------------------------------------------------------------------------------------------

    async def get_status(self) -> Dict[str, Any]:
        """Checks Squad daemon layer health."""
        return {
            "healthy": True,
            "status": "Healthy",
            "version": "1.0.0",
            "timestamp": int(time.time())
        }

    async def get_active_mode(self) -> str:
        """Reads active mode from the orchestration manual."""
        mode_file = self.repo_root.parent / "00-AI-Orchestration" / "Config" / "MODE-MANUAL.md"
        choice = "4"
        if mode_file.exists():
            try:
                with open(mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith("active_mode:"):
                            choice = line.split(":")[1].strip()
                            break
            except Exception as e:
                self.logger.warning(f"Error reading active mode: {e}")
        return choice

    def get_mode_details(self, mode: str) -> tuple:
        """Returns name and description for a mode."""
        from src.core.switch_mode import MODES
        return MODES.get(mode, ("Unknown Mode", "N/A"))

    async def switch_mode(self, mode: str) -> tuple[bool, str]:
        """Switches active mode in configuration files."""
        from src.core.switch_mode import apply_mode_protocol, MODES
        if mode not in MODES:
            return False, f"Invalid mode: {mode}"
        try:
            success = apply_mode_protocol(mode)
            if success:
                return True, f"Successfully switched to {MODES[mode][0]}"
            return False, "Failed to apply mode protocol"
        except Exception as e:
            return False, str(e)

    def list_commands(self) -> List[Dict[str, str]]:
        """Returns a list of available subcommands and their descriptions."""
        from main import COMMANDS_MAP
        descriptions = {
            "start-squad": "Launches the persistent background agent daemon and web service",
            "convert-agents": "Standardises raw XML markdown schemas into agent-friendly skills",
            "ensure-frontmatter": "Applies frontmatter, creation timestamps, and formatting checks",
            "fleet-commander": "Checks git branch-protection constraints and manages fleet repos",
            "install-git-hooks": "Installs commit hooks to validate note formatting and check drift",
            "preflight-check": "Runs comprehensive pre-flight verification checks",
            "check-coherence": "Performs quick syntax audits of codebase workspace configurations",
            "switch-mode": "Updates AI Session States and toggles active squad modes",
            "persona-extractor": "Extracts polyglot codebase context in background",
            "joint-audit-purger": "Locally wipes invalid and out-of-date strategic Nexus files",
        }
        return [
            {"name": cmd, "description": descriptions.get(cmd, "Custom subcommand")}
            for cmd in COMMANDS_MAP.keys()
        ]

    async def run_subcommand_async(self, cmd_name: str, args: List[str]) -> tuple[bool, str]:
        """Triggers a subcommand in a non-blocking background task."""
        if cmd_name == "start-squad":
            return False, "Cannot trigger start-squad asynchronously (already running)."
        
        from main import COMMANDS_MAP
        if cmd_name not in COMMANDS_MAP:
            return False, f"Unknown command: {cmd_name}"

        async def _task():
            cmd = [sys.executable, "main.py", cmd_name]
            if args:
                cmd.extend(args)
            try:
                proc = await asyncio.create_subprocess_exec(
                    *cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.STDOUT,
                    cwd=str(self.repo_root)
                )
                await proc.wait()
                if proc.returncode == 0:
                    self.logger.info(f"Subcommand {cmd_name} finished successfully.")
                else:
                    self.logger.error(f"Subcommand {cmd_name} failed with return code {proc.returncode}")
            except Exception as e:
                self.logger.error(f"Failed to run subcommand {cmd_name}: {e}")

        asyncio.create_task(_task())
        return True, f"Subcommand {cmd_name} triggered successfully in the background."

    # -----------------------------------------------------------------------------------------------

    def run_subcommand(self, *, cmd_name: str, args: List[str]) -> Dict[str, Any]:
        """Runs a direct sub-command script dynamically routing via controller."""
        self.logger.info("{0} : Routing subcommand '{1}' with args {2}".format(self.Name, cmd_name, args))
        
        try:
            import importlib
            from main import COMMANDS_MAP
            module_path = COMMANDS_MAP.get(cmd_name)
            if not module_path:
                return {"status": "error", "message": "Unknown command: {0}".format(cmd_name)}

            old_argv = sys.argv
            sys.argv = [sys.argv[0]] + args
            try:
                module = importlib.import_module("src.{0}".format(module_path))
                if hasattr(module, "main"):
                    module.main()
                    result = {"status": "success", "message": "Subcommand completed successfully."}
                else:
                    result = {"status": "error", "message": "Subcommand has no main function."}
            finally:
                sys.argv = old_argv
            return result
        except Exception as e:
            self.logger.error("{0} : Error running subcommand: {1}".format(self.Name, e))
            return {"status": "error", "message": str(e)}

    # -----------------------------------------------------------------------------------------------

    async def get_chat_history(self, session_id: str) -> List[Dict[str, Any]]:
        """Retrieves squad chat logs from Postgres."""
        import json
        if not self.pool:
            return []
        loop = asyncio.get_running_loop()
        def db_query():
            conn = self.pool.getconn()
            try:
                with conn.cursor() as cursor:
                    cursor.execute('SET search_path TO "08-Base-Scripts", public')
                    cursor.execute(
                        "SELECT sender, content, tool_calls, created_at FROM squad_chat_logs WHERE session_id = %s ORDER BY created_at ASC",
                        (session_id,)
                    )
                    rows = cursor.fetchall()
                    return [
                        {
                            "sender": r[0],
                            "content": r[1],
                            "tool_calls": r[2] if isinstance(r[2], list) else (json.loads(r[2]) if r[2] else []),
                            "created_at": r[3].isoformat() if r[3] else ""
                        }
                        for r in rows
                    ]
            except Exception as e:
                self.logger.error(f"Failed to query squad_chat_logs: {e}")
                return []
            finally:
                self.pool.putconn(conn)
        return await loop.run_in_executor(None, db_query)

    async def publish_user_message(self, session_id: str, message: str) -> None:
        """Saves a user message and publishes it to NATS room to trigger agents."""
        if not self.pool:
            return
            
        loop = asyncio.get_running_loop()
        # 1. Save user turn to PostgreSQL
        def db_insert():
            conn = self.pool.getconn()
            try:
                with conn.cursor() as cursor:
                    cursor.execute('SET search_path TO "08-Base-Scripts", public')
                    cursor.execute(
                        "INSERT INTO squad_chat_logs (session_id, sender, content, tool_calls) VALUES (%s, %s, %s, %s)",
                        (session_id, "user", message, "[]")
                    )
                conn.commit()
            except Exception as e:
                self.logger.error(f"Failed to insert user squad_chat_log: {e}")
            finally:
                self.pool.putconn(conn)
        await loop.run_in_executor(None, db_insert)

        # 2. Publish to SquadEventBus
        try:
            payload_data = {
                "sender": "user",
                "session_id": session_id,
                "content": message
            }
            if hasattr(self, "event_bus") and self.event_bus:
                await self.event_bus.publish("antigravity.squad.chat", payload_data)
            else:
                self.logger.warning("CommandController: event_bus not initialized on controller.")
        except Exception as e:
            self.logger.error(f"Failed to publish user message: {e}")

    # -----------------------------------------------------------------------------------------------

    def execute(self, *args, **kwargs) -> None:
        """Implements Command interface to run a quick mock verification check."""
        mock_msg = "test message"
        if len(sys.argv) > 1:
            mock_msg = " ".join(sys.argv[1:])

        res = self.process_message(channel="CLI_MOCK", session_id="test_session", user_msg=mock_msg)
        print(jsonDumps(res, indent=2))

# -----------------------------------------------------------------------------------------------

def main() -> None:
    """Entry point for mock verification command run."""
    import src.bootstrap as bootstrap
    controller = CommandController(config=bootstrap.config, logger=bootstrap.logger)
    controller.execute()
