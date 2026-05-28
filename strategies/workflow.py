#!/usr/bin/env python
# coding:utf-8

import os
import yaml
from typing import List, Optional, Any
from src.models.context import SystemContext
from src.models.workflow import WorkflowSchema, WorkflowStep
from src.models.message import AgentMessage

class WorkflowManager:
    """
    AI-CONTEXT: Loads and executes configurable workflows from YAML definitions.
    Enables multi-step automation (e.g. Spec -> Code -> Test -> Doc).
    """
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx
        self.workflows_dir = os.path.join(ctx.vault_root, "00-AI-Orchestration", "workflows")
        os.makedirs(self.workflows_dir, exist_ok=True)

    def list_workflows(self) -> List[str]:
        if not os.path.exists(self.workflows_dir):
            return []
        return [f[:-5] for f in os.listdir(self.workflows_dir) if f.endswith(".yaml")]

    def load_workflow(self, name: str) -> Optional[WorkflowSchema]:
        path = os.path.join(self.workflows_dir, f"{name}.yaml")
        if not os.path.exists(path):
            return None
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            steps = []
            for s in data.get('steps', []):
                steps.append(WorkflowStep(
                    name=s['name'],
                    action=s['action'],
                    persona=s.get('persona', 'orchestrator'),
                    description=s.get('description', ''),
                    params=s.get('params', {})
                ))
            
            return WorkflowSchema(data['name'], data.get('description', ''), steps)
        except Exception as e:
            print(f"⚠️ Error loading workflow {name}: {e}")
            return None

    async def execute_step(self, step: WorkflowStep, facade: Any):
        """Logic to execute a single workflow step."""
        print(f"🏁 Executing Step: {step.name} ({step.description})")
        
        if step.action == "audit":
            facade.governance.run_preflight()
            
        elif step.action == "prompt":
            print(f"🤖 [AI: {step.persona}] Processing prompt logic...")
            provider = facade.get_provider()
            if not provider:
                print("❌ Error: AI Provider not configured.")
                return

            persona_prompt = facade.personas.load_prompt(step.persona) or "You are a helpful assistant."
            user_input = step.params.get("prompt", "Please proceed with the next step.")
            
            messages = [
                AgentMessage(role="system", content=persona_prompt),
                AgentMessage(role="user", content=user_input)
            ]
            
            response = await provider.chat(messages)
            print(f"\n💬 [AI Response ({step.persona})]:\n{response.content}\n")
            
            if facade.session_id:
                facade.memory.store_message(facade.session_id, messages[-1])
                facade.memory.store_message(facade.session_id, response)
            
        elif step.action == "shell":
            cmd = step.params.get("cmd")
            if cmd:
                import subprocess
                print(f"🐚 Running shell: {cmd}")
                subprocess.run(cmd, shell=True)
                
        elif step.action == "signoff":
            facade.governance.run_signoff()
