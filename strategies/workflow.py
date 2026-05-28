#!/usr/bin/env python
# coding:utf-8

import os
import yaml
from typing import List, Optional, Any
from ..models.context import SystemContext
from ..models.workflow import WorkflowSchema, WorkflowStep

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
            # provider = facade.get_provider()
            # ...
            
        elif step.action == "shell":
            cmd = step.params.get("cmd")
            if cmd:
                import subprocess
                print(f"🐚 Running shell: {cmd}")
                subprocess.run(cmd, shell=True)
                
        elif step.action == "signoff":
            facade.governance.run_signoff()
