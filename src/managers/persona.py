#!/usr/bin/env python
# coding:utf-8

import os
import re
from typing import List, Dict, Optional
from ..models.context import SystemContext

class PersonaManager:
    """
    AI-CONTEXT: Manages AI Personas (Roles).
    Loads prompts directly from Core-KMS Role-Prompts.
    """
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx
        self.source_dir = self._resolve_source_dir()

    def _resolve_source_dir(self) -> str:
        # Priority 1: Standalone core-kms-brain
        path = os.path.abspath(os.path.join(self.ctx.workspace_root, "core-kms-brain", "Role-Prompts"))
        if os.path.isdir(path):
            return path
        # Priority 2: Submodule inside obsidian-brain
        return os.path.join(self.ctx.vault_root, "07-Core-KMS", "Role-Prompts")

    def list_personas(self) -> List[str]:
        """Returns list of available agent names based on folder prefixes."""
        if not os.path.exists(self.source_dir):
            return []
        
        personas = []
        for folder in os.listdir(self.source_dir):
            if os.path.isdir(os.path.join(self.source_dir, folder)):
                # e.g. "04-QA" -> "qa"
                name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
                personas.append(name)
        return sorted(personas)

    def load_prompt(self, persona_name: str) -> Optional[str]:
        """
        Loads the system prompt for a persona.
        Applies the mandatory [SCAN] block for parity.
        """
        if not os.path.exists(self.source_dir):
            return None

        # Find the folder matching the persona name
        target_folder = None
        for folder in os.listdir(self.source_dir):
            name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
            if name == persona_name.lower():
                target_folder = os.path.join(self.source_dir, folder)
                break
        
        if not target_folder:
            return None

        # Find the .md file (prefer Prompt-*.md)
        md_files = [f for f in os.listdir(target_folder) if f.endswith(".md")]
        if not md_files:
            return None
        
        prompt_files = [f for f in md_files if f.startswith("Prompt-")]
        md_file = os.path.join(target_folder, prompt_files[0] if prompt_files else md_files[0])

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. Strip Frontmatter
            content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
            
            # 2. Append parity blocks ([SCAN] and State Management)
            scan_block = f"""
# 💾 STATE MANAGEMENT RULE (CRITICAL)
Before finishing any major task or concluding a session, you MUST use your available file management tools to append a summary of your actions to the local `AI-Session-State.md` file in the target repository. This acts as our Hard-Stop Context Block to prevent memory loss across sessions.

# 🚨 ATTENTION RESTORATION (SCAN METHOD)
To prevent context degradation, you MUST begin EVERY single response with the following SCAN block:

**[SCAN]** Role: {persona_name} | Source: [Source Verification] | State: [Session Progress]
"""
            return content + "\n" + scan_block
        except Exception as e:
            print(f"⚠️ Error loading persona {persona_name}: {e}")
            return None

    def sync_to_adapters(self) -> None:
        """Triggers the legacy convert_agents.py for CLI compatibility."""
        convert_script = os.path.join(self.ctx.vault_root, "20-Scripts/convert_agents.py")
        if os.path.exists(convert_script):
            import subprocess
            import sys
            print("🔄 Synchronizing AI Engine Roles across legacy adapters...")
            subprocess.run([sys.executable, convert_script])
