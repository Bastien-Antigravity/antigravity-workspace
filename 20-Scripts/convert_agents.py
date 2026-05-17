#!/usr/bin/env python
# coding:utf-8
import os, sys
# Ensure we are running inside the virtual environment
_venv_dir = os.path.dirname(os.path.abspath(__file__))
while _venv_dir and _venv_dir != '/' and not os.path.exists(os.path.join(_venv_dir, ".venv")):
    _parent = os.path.dirname(_venv_dir)
    if _parent == _venv_dir:
        break
    _venv_dir = _parent
_venv_python = os.path.join(_venv_dir, ".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(_venv_dir, ".venv", "bin", "python3")
if os.path.exists(_venv_python):
    try:
        if not os.path.samefile(sys.executable, _venv_python):
            os.execl(_venv_python, _venv_python, *sys.argv)
    except OSError:
        pass


"""
ESSENTIAL PROCESS:
Converts the human-readable Role-Prompts from the core-kms-brain into 
compatible Gemini CLI agent definitions in the obsidian-brain vault.

DATA FLOW:
1. Scans core-kms-brain/Role-Prompts for markdown files.
2. Extracts agent names from folder prefixes.
3. Injects mandatory YAML frontmatter and the [SCAN] restoration block.
4. Writes the final agent markdown to obsidian-brain/.gemini/agents/.

KEY PARAMETERS:
- source_dir: Path to the raw role prompts.
- target_dir: Path to the generated Gemini agent definitions.
"""

import os
from os import listdir as osListdir, makedirs as osMakedirs
from os.path import dirname as osPathDirname, abspath as osPathAbspath, join as osPathJoin, isdir as osPathIsdir, exists as osPathExists
from glob import glob as globGlob

# -----------------------------------------------------------------------------------------------

def _find_workspace_root() -> str:
    """
    Walk up from this script's location until we find the workspace root.
    """
    current = osPathDirname(osPathAbspath(__file__))
    while current != osPathDirname(current):
        if osPathExists(osPathJoin(current, "Bastien-Antigravity.code-workspace")):
            return current
        if osPathIsdir(osPathJoin(current, "obsidian-brain")) and osPathIsdir(osPathJoin(current, "fleet-operation-brain")):
            return current
        current = osPathDirname(current)
    return osPathAbspath(osPathJoin(osPathDirname(osPathAbspath(__file__)), "..", ".."))

def main() -> None:
    workspace_root = _find_workspace_root()

    # Try standalone clone first, fall back to submodule inside obsidian-brain
    source_dir = osPathJoin(workspace_root, "core-kms-brain", "Role-Prompts")
    if not osPathIsdir(source_dir):
        source_dir = osPathJoin(workspace_root, "obsidian-brain", "07-Core-KMS", "Role-Prompts")
    
    # Define supported AI CLI adapters and their relative agent paths
    ADAPTERS = {
        "Gemini": ".gemini/agents",
        "Claude": ".claude/agents",
        "OpenAI": ".codex/agents",
        "Mistral": ".mistral/agents",
        "DeepSeek": ".deepseek/agents"
    }

    # Identify active adapters (only sync if the parent tool directory exists)
    active_targets = []
    for name, rel_path in ADAPTERS.items():
        parent_dir = osPathJoin(workspace_root, "obsidian-brain", rel_path.split("/")[0])
        if osPathIsdir(parent_dir):
            target = osPathJoin(workspace_root, "obsidian-brain", rel_path)
            osMakedirs(target, exist_ok=True)
            active_targets.append((name, target))

    if not active_targets:
        print("⚠️ No active AI adapters found (.gemini, .claude, etc.).")
        return

    # Cleanup: Remove orphaned agents in all active targets
    for name, target in active_targets:
        print(f"🧹 Purging old {name} agents in {target}...")
        for f in osListdir(target):
            if f.endswith(".md"):
                os.remove(osPathJoin(target, f))

    # Map folder names to clean agent names
    for folder in osListdir(source_dir):
        folder_path = osPathJoin(source_dir, folder)
        if osPathIsdir(folder_path):
            md_files = globGlob(osPathJoin(folder_path, "*.md"))
            if md_files:
                md_file = md_files[0]
                # e.g. "04-QA" -> "qa"
                agent_name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
                
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Strip existing frontmatter from source content if present
                import re
                content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
                
                yaml_frontmatter = f"""---
name: {agent_name}
description: The {agent_name} persona from the Bastien-Antigravity squad.
---
"""
                
                scan_block = f"""
# 💾 STATE MANAGEMENT RULE (CRITICAL)
Before finishing any major task or concluding a session, you MUST use your available file management tools to append a summary of your actions to the local `AI-Session-State.md` file in the target repository. This acts as our Hard-Stop Context Block to prevent memory loss across sessions.

# 🚨 ATTENTION RESTORATION (SCAN METHOD)
To prevent context degradation, you MUST begin EVERY single response with the following SCAN block:

**[SCAN]** Role: {agent_name} | Source: [Source Verification] | State: [Session Progress]
"""
                
                # Sync to all active targets
                for name, target in active_targets:
                    target_file = osPathJoin(target, f"{agent_name}.md")
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(yaml_frontmatter + content + "\n" + scan_block)
                    print(f"   [{name}] Created agent: {agent_name}")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
