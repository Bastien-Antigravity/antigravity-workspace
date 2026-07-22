#!/usr/bin/env python
# coding:utf-8

from typing import Any, Dict
from src.agents.interfaces import SquadEventBus
from src.agents.base_agent import BaseAgent

def run_squad_tests(test_command: str) -> str:
    """
    Runs the specified unit or integration test suite in the workspace.
    
    Args:
        test_command: The CLI command to run tests (e.g. 'pytest src/tests' or 'go test ./...').
    """
    return ""


class QAAgent(BaseAgent):
    """
    QA Engineer agent daemon. Specialised in verifying logic implementation,
    auditing unit tests, and reporting verification reports.
    """
    def __init__(self, *, config: Any, logger: Any, pg_pool: Any, event_bus: SquadEventBus):
        super().__init__(
            role_name="qa",
            prompt_file="04-QA/Prompt-QA.md",
            config=config,
            logger=logger,
            pg_pool=pg_pool,
            event_bus=event_bus
        )
        self.tools = [run_squad_tests]

    async def execute_tool(self, name: str, args: Dict[str, Any]) -> str:
        """Executes a function call requested by the model."""
        if name == "run_squad_tests":
            cmd_arg = args.get("test_command", "")
            return await super().execute_tool("execute_shell_command", {"command": cmd_arg})

        return await super().execute_tool(name, args)
