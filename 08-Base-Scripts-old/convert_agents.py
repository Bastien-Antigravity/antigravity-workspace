#!/usr/bin/env python
# coding:utf-8
import os, sys
# --- Bootstrap ---
import os, sys
_vault_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
while not os.path.exists(os.path.join(_vault_root, ".venv")) and _vault_root != os.path.dirname(_vault_root):
    _vault_root = os.path.dirname(_vault_root)
sys.path.append(_vault_root)
try:
    from src.core.bootstrap import init as bootstrap_init
    bootstrap_init(__file__)
except ImportError:
    pass


"""
ESSENTIAL PROCESS:
Converts the human-readable Role-Prompts from the core-kms-brain into 
compatible Gemini CLI agent definitions in the obsidian-brain vault.

DATA FLOW:
1. Scans core-kms-brain/Role-Prompts for markdown files.
2. Extracts agent names from folder prefixes.
3. Injects mandatory YAML frontmatter and the [SCAN] restoration block.
4. Writes the final agent markdown to obsidian-brain/ :
    gemini      : .gemini/agents/ 
    claude      : .claude/agents 
    deepseek    : .deepseek/agents
    openai      : .codex/agents 

KEY PARAMETERS:
- source_dir: Path to the raw role prompts.
- target_dir: Path to the generated Gemini agent definitions.
"""

import os
from os import listdir as osListdir, makedirs as osMakedirs
from os.path import dirname as osPathDirname, abspath as osPathAbspath, join as osPathJoin, isdir as osPathIsdir, exists as osPathExists
from glob import glob as globGlob

SCRIPT_DIR = osPathDirname(osPathAbspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.append(SCRIPT_DIR)

try:
    from clients.registry import iter_clients
except ImportError:
    iter_clients = None

# -----------------------------------------------------------------------------------------------

def _find_workspace_root() -> str:
    """
    Walk up from this script's location until we find the workspace root.
    """
    current = osPathDirname(osPathAbspath(__file__))
    while current != osPathDirname(current):
        if globGlob(osPathJoin(current, "*.code-workspace")):
            return current
        if osPathIsdir(osPathJoin(current, "obsidian-brain")) and osPathIsdir(osPathJoin(current, "fleet-operation-brain")):
            return current
        current = osPathDirname(current)
    return osPathAbspath(osPathJoin(osPathDirname(osPathAbspath(__file__)), "..", ".."))

def main() -> None:
    workspace_root = _find_workspace_root()

    # Precedence:
    # 1. 01-Strategic-Nexus (Source of Truth for Strategic Identities)
    # 2. 07-Core-KMS (Central Repository for Operational Personas)
    
    source_dirs = [
        osPathJoin(workspace_root, "obsidian-brain", "01-Strategic-Nexus", "Role-Prompts"),
        osPathJoin(workspace_root, "obsidian-brain", "02-Business-BDD", "Role-Prompts"),
        osPathJoin(workspace_root, "obsidian-brain", "03-Tech-Stack", "Role-Prompts"),
        osPathJoin(workspace_root, "obsidian-brain", "07-Core-KMS", "Role-Prompts"),
        # Standalone clones support
        osPathJoin(workspace_root, "core-kms-brain", "Role-Prompts"),
        osPathJoin(workspace_root, "nexus-strategic-brain", "Role-Prompts"),
    ]
    
    # Filter only existing directories
    active_source_dirs = [d for d in source_dirs if osPathIsdir(d)]
    
    vault_root = osPathJoin(workspace_root, "obsidian-brain")

    # Sync every supported adapter directory from the central client registry.
    if iter_clients:
        active_targets = []
        for client_name, config in iter_clients():
            target = osPathJoin(vault_root, config["agents_dir"])
            try:
                osMakedirs(target, exist_ok=True)
                active_targets.append((config["label"], target))
            except OSError as e:
                print(f"   ⚠️ Could not prepare {config['label']} agents at {target}: {e}")
    else:
        active_targets = []
        for name, rel_path in {
            "Gemini": ".gemini/agents",
            "Claude": ".claude/agents",
            "DeepSeek": ".deepseek/agents",
            "OpenAI Codex": ".codex/agents",
        }.items():
            target = osPathJoin(vault_root, rel_path)
            try:
                osMakedirs(target, exist_ok=True)
                active_targets.append((name, target))
            except OSError as e:
                print(f"   ⚠️ Could not prepare {name} agents at {target}: {e}")

    if not active_targets:
        print("⚠️ No active AI adapters found (.gemini, .claude, etc.).")
        return

    # Cleanup: Remove orphaned agents in all active targets
    for name, target in active_targets:
        print(f"🧹 Purging old {name} agents in {target}...")
        if "skills" in target or name == "Antigravity":
            if osPathExists(target):
                for f in osListdir(target):
                    dir_path = osPathJoin(target, f)
                    if osPathIsdir(dir_path):
                        skill_md = osPathJoin(dir_path, "SKILL.md")
                        if osPathExists(skill_md):
                            try:
                                os.remove(skill_md)
                                os.rmdir(dir_path)
                            except OSError as e:
                                print(f"   ⚠️ Could not purge skill {f}: {e}")
        else:
            for f in osListdir(target):
                if f.endswith(".md"):
                    try:
                        os.remove(osPathJoin(target, f))
                    except OSError as e:
                        print(f"   ⚠️ Could not purge {f}: {e}")

    # Track processed agents to ensure Source of Truth precedence
    processed_agents = set()

    # Process all active source directories in precedence order
    for source_dir in active_source_dirs:
        print(f"📥 Processing roles from: {os.path.basename(os.path.dirname(source_dir))}")
        for folder in osListdir(source_dir):
            folder_path = osPathJoin(source_dir, folder)
            if osPathIsdir(folder_path):
                # e.g. "04-QA" -> "qa"
                agent_name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
                
                # Precedence check: if we already processed this agent from a higher-priority source, skip
                if agent_name in processed_agents:
                    continue

                md_files = globGlob(osPathJoin(folder_path, "*.md"))
                if md_files:
                    # Prioritize files starting with "Prompt-"
                    prompt_files = [f for f in md_files if os.path.basename(f).startswith("Prompt-")]
                    md_file = prompt_files[0] if prompt_files else md_files[0]
                    
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Strip existing frontmatter from source content if present
                    from re import sub as reSub, DOTALL as reDotAll
                    content = reSub(r'^---.*?---\s*', '', content, flags=reDotAll)
                    
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
                        if "skills" in target or name == "Antigravity":
                            skill_dir = osPathJoin(target, agent_name)
                            osMakedirs(skill_dir, exist_ok=True)
                            target_file = osPathJoin(skill_dir, "SKILL.md")
                        else:
                            target_file = osPathJoin(target, f"{agent_name}.md")
                        try:
                            with open(target_file, 'w', encoding='utf-8') as f:
                                f.write(yaml_frontmatter + content + "\n" + scan_block)
                            print(f"   [{name}] Created agent: {agent_name}")
                        except OSError as e:
                            print(f"   ⚠️ Could not write agent {agent_name} to {name}: {e}")
                    
                    processed_agents.add(agent_name)

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
