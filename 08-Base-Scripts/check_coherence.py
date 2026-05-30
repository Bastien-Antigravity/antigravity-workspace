#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Checks coherence between runtime agent definitions (.agents/skills/) 
and the static source Role-Prompts inside the obsidian-brain submodules.

DATA FLOW:
1. Resolves the vault root dynamically relative to the script path.
2. Iterates over active roles and finds the highest precedence prompt file.
3. Compares the raw contents after stripping frontmatter and sandbox headers.
4. If --fix is set, auto-rebuilds the drifted skill files.
5. Outputs a consistency status report.
"""
import os
import sys
from pathlib import Path
import re
import argparse

# --- Bootstrap ---
_vault_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
while not os.path.exists(os.path.join(_vault_root, ".venv")) and _vault_root != os.path.dirname(_vault_root):
    _vault_root = os.path.dirname(_vault_root)
if _vault_root not in sys.path:
    sys.path.append(_vault_root)

_orch_dir = os.path.join(_vault_root, "00-AI-Orchestration")
if _orch_dir not in sys.path:
    sys.path.append(_orch_dir)

from orchestration_lib import setup_terminal, resolve_vault_and_workspace
setup_terminal()
VAULT_ROOT, WORKSPACE_ROOT = resolve_vault_and_workspace(__file__)
skills_dir = VAULT_ROOT / ".agents" / "skills"

# Precedence matching mapping
ROLES = {
    "oracle": ("01-Strategic-Nexus/Role-Prompts/00-Oracle", "Prompt-Chronos-Oracle.md"),
    "orchestrator": ("07-Core-KMS/Role-Prompts/01-Orchestrator", "Prompt-Orchestrator.md"),
    "architect": ("03-Tech-Stack/Role-Prompts/02-Architect", "Prompt-Architect.md"),
    "developer": ("03-Tech-Stack/Role-Prompts/03-Developer", "Prompt-Lead-Developer.md"),
    "qa": ("02-Business-BDD/Role-Prompts/04-QA", "Prompt-QA.md"),
    "fleetarchitect": ("07-Core-KMS/Role-Prompts/05-FleetArchitect", "Prompt-Fleet-Architect.md"),
    "docmaintainer": ("07-Core-KMS/Role-Prompts/06-DocMaintainer", "Prompt-DocMaintainer.md"),
    "fleetcommander": ("07-Core-KMS/Role-Prompts/07-FleetCommander", "Prompt-FleetCommander.md"),
    "purger": ("07-Core-KMS/Role-Prompts/08-Purger", "Mister-Straight-to-Goal.md"),
    "sentinel": ("07-Core-KMS/Role-Prompts/09-Sentinel", "Prompt-Sentinel.md"),
    "docindexer": ("07-Core-KMS/Role-Prompts/10-DocIndexer", "Prompt-DocIndexer.md"),
    "codeindexer": ("07-Core-KMS/Role-Prompts/11-CodeIndexer", "Prompt-CodeIndexer.md"),
    "patternsentinel": ("07-Core-KMS/Role-Prompts/12-PatternSentinel", "Prompt-Pattern-Sentinel.md")
}

def strip_frontmatter(content: str) -> str:
    """Removes the YAML frontmatter block from markdown content."""
    lines = content.splitlines()
    if not lines:
        return ""
    if lines[0].strip() == "---":
        try:
            closing_idx = lines.index("---", 1)
            return "\n".join(lines[closing_idx+1:]).strip()
        except ValueError:
            return content.strip()
    return content.strip()

def strip_sandbox_headers(content: str) -> str:
    """Removes attention restoration and state management rules added to skills."""
    # Remove attention restoration [SCAN] block at the end
    content = re.sub(r'#\s*🚨\s*ATTENTION\s*RESTORATION.*', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Remove state management rule block
    content = re.sub(r'#\s*💾\s*STATE\s*MANAGEMENT.*', '', content, flags=re.DOTALL | re.IGNORECASE)
    return content.strip()

def fix_mismatch(skill_name: str, prompt_file: Path, skill_file: Path) -> bool:
    """Auto-resolves prompt-skill mismatches by copying/formatting source prompt."""
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip existing frontmatter
        content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
        
        yaml_frontmatter = f"""---
name: {skill_name}
description: The {skill_name} persona from the Bastien-Antigravity squad.
---
"""
        scan_block = f"""
# 💾 STATE MANAGEMENT RULE (CRITICAL)
Before finishing any major task or concluding a session, you MUST use your available file management tools to append a summary of your actions to the local `AI-Session-State.md` file in the target repository. This acts as our Hard-Stop Context Block to prevent memory loss across sessions.

# 🚨 ATTENTION RESTORATION (SCAN METHOD)
To prevent context degradation, you MUST begin EVERY single response with the following SCAN block:

**[SCAN]** Role: {skill_name} | Source: [Source Verification] | State: [Session Progress]
"""
        skill_file.parent.mkdir(parents=True, exist_ok=True)
        with open(skill_file, 'w', encoding='utf-8') as f:
            f.write(yaml_frontmatter + content + "\n" + scan_block)
            
        print(f"🔧 AUTO-FIXED:      Rebuilt [skills/{skill_name}/SKILL.md] from source.")
        return True
    except Exception as e:
        print(f"❌ Fix Failed:      Could not auto-repair skill {skill_name}: {e}")
        return False

def run_coherence_check(should_fix: bool = False) -> bool:
    print("\n" + "="*70)
    print("🔍 RUNTIME AGENT SKILLS VS SOURCE PROMPTS COHERENCE AUDIT")
    print("="*70 + "\n")
    
    mismatches = 0
    fixed_count = 0
    
    for skill_name, (rel_dir, filename) in ROLES.items():
        skill_file = skills_dir / skill_name / "SKILL.md"
        prompt_file = VAULT_ROOT / rel_dir / filename
        
        if not skill_file.exists():
            print(f"❌ Missing Skill:    [skills/{skill_name}/SKILL.md]")
            if should_fix:
                if fix_mismatch(skill_name, prompt_file, skill_file):
                    fixed_count += 1
                else:
                    mismatches += 1
            else:
                mismatches += 1
            continue
        if not prompt_file.exists():
            print(f"❌ Missing Source:   [{rel_dir}/{filename}]")
            mismatches += 1
            continue
            
        with open(skill_file, "r", encoding="utf-8") as f:
            skill_raw = f.read()
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt_raw = f.read()
            
        skill_clean = strip_sandbox_headers(strip_frontmatter(skill_raw))
        prompt_clean = strip_sandbox_headers(strip_frontmatter(prompt_raw))
        
        # Normalize line endings
        skill_clean = skill_clean.replace("\r\n", "\n").strip()
        prompt_clean = prompt_clean.replace("\r\n", "\n").strip()
        
        if skill_clean == prompt_clean:
            print(f"✅ COHERENT:        {skill_name:<16} <-> {filename}")
        else:
            print(f"⚠️  MISMATCH:        {skill_name:<16} <-> {filename}")
            if should_fix:
                if fix_mismatch(skill_name, prompt_file, skill_file):
                    fixed_count += 1
                else:
                    mismatches += 1
            else:
                mismatches += 1
                
                # Show visual line diff
                s_lines = skill_clean.splitlines()
                p_lines = prompt_clean.splitlines()
                min_len = min(len(s_lines), len(p_lines))
                for idx in range(min_len):
                    if s_lines[idx] != p_lines[idx]:
                        print(f"     └─ First difference at line {idx+1}:")
                        print(f"        Skill:  {repr(s_lines[idx])}")
                        print(f"        Prompt: {repr(p_lines[idx])}")
                        break
                    
    print("\n" + "="*70)
    if mismatches == 0:
        if fixed_count > 0:
            print(f"✨ SUCCESS: ALL AGENTS COHERENT (AUTO-REPAIRED {fixed_count} SKILLS)")
        else:
            print("✨ SUCCESS: ALL RUNTIME AGENT SKILLS ARE 100% COHERENT WITH VAULT PROMPTS")
        print("="*70 + "\n")
        return True
    else:
        print(f"⚠️  WARNING: DETECTED {mismatches} DRIFTED OR MISALIGNED AGENTS")
        print("="*70 + "\n")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit agent prompt coherence")
    parser.add_argument("--fix", action="store_true", help="Auto-resolve prompt-skill mismatches")
    args = parser.parse_args()
    
    success = run_coherence_check(should_fix=args.fix)
    sys.exit(0 if success else 1)
