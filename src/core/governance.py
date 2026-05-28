#!/usr/bin/env python
# coding:utf-8

import os
import sys
import json
import subprocess
from typing import List, Tuple
from src.models.context import SystemContext

class GovernanceManager:
    """
    AI-CONTEXT: Manages the governance protocols (audits, preflights, sign-offs).
    Preserves exact logic from start_engine.py and close_task.py.
    """
    def __init__(self, ctx: SystemContext):
        self.ctx = ctx

    def run_preflight(self) -> None:
        """Executes the governance audit scripts (Preflight-Check, Brain-Health)."""
        governance_scripts = ["Preflight-Check.py", "Brain-Health-Audit.py"]
        
        for script_name in governance_scripts:
            # Standard location in 07-Core-KMS
            standard_path = os.path.join(self.ctx.vault_root, "07-Core-KMS/Scripts", script_name)
            # Legacy fallback
            legacy_path = os.path.join(self.ctx.workspace_root, "core-kms-brain", "Scripts", script_name)
            
            target = None
            if os.path.exists(standard_path):
                target = standard_path
            elif os.path.exists(legacy_path):
                target = legacy_path
                
            if target:
                print(f"📡 Executing Governance Audit: {script_name}...")
                subprocess.run([sys.executable, target])

    def check_session_health(self) -> bool:
        """
        Checks for uncommitted changes across the fleet and verifies mission parking.
        Returns False if a strict block (Mode 3) is triggered.
        """
        # 1. Mode Guardrail: Ensure previous mission is parked
        if self.ctx.mission_status == "active":
            print(f"\n⚠️  MODE GUARDRAIL: Active Mission Detected ({self.ctx.mission_id})")
            if self.ctx.active_mode in ["1", "3"]:
                print(f"In Mode {self.ctx.active_mode}, you MUST park the current mission before starting a new one.")
                confirm = input("Park current mission automatically? [y/N]: ").lower().strip()
                if confirm == 'y':
                    self.ctx.park_mission()
                else:
                    return False

        repos_to_check = []
        
        # Load fleet from inventory
        if os.path.exists(self.ctx.inventory_file):
            try:
                with open(self.ctx.inventory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    repositories = data.get("repositories", [])
                    for repo in repositories:
                        repo_path_rel = repo.get("path")
                        repo_abs_path = os.path.abspath(os.path.join(self.ctx.workspace_root, repo_path_rel))
                        if os.path.exists(repo_abs_path) and os.path.exists(os.path.join(repo_abs_path, ".git")):
                            repos_to_check.append({
                                "name": repo.get("name"),
                                "path": repo_abs_path,
                                "is_vault": (repo.get("name") == "obsidian-brain" or repo_abs_path == self.ctx.vault_root)
                            })
            except Exception as e:
                print(f"⚠️ Warning: Failed to load inventory.json: {e}")
                
        if not repos_to_check:
            repos_to_check.append({"name": "obsidian-brain", "path": self.ctx.vault_root, "is_vault": True})
            
        dirty_repos_info = []
        EXCLUSIONS = [".git", ".obsidian", ".gemini", ".claude", ".codex", ".deepseek", "Templates", "MODE-MANUAL.md"]
        
        for repo in repos_to_check:
            try:
                result = subprocess.run(
                    ["git", "status", "--porcelain"], 
                    cwd=repo["path"], capture_output=True, text=True, check=True
                )
                uncommitted = []
                for line in result.stdout.splitlines():
                    if not line.strip(): continue
                    status_path = line[3:].strip()
                    if repo["is_vault"]:
                        if status_path.endswith(".md") and not any(x in status_path for x in EXCLUSIONS):
                            uncommitted.append(status_path)
                    elif not any(x in status_path for x in EXCLUSIONS):
                        uncommitted.append(status_path)
                            
                if uncommitted:
                    dirty_repos_info.append((repo["name"], len(uncommitted)))
            except Exception:
                pass
                
        if dirty_repos_info:
            if self.ctx.active_mode == "3":
                print("\n🛑 CRITICAL GOVERNANCE VIOLATION: UNCLOSED TASK DETECTED")
                for repo_name, count in dirty_repos_info:
                    print(f"  - {repo_name} ({count} file(s) dirty)")
                print("\nIn Mode 3 (Fleet-Commander), startup is STRICTLY BLOCKED.")
                return False
            
            elif self.ctx.active_mode == "1":
                print("\n⚠️ WARNING: UNCLOSED TASK DETECTED")
                for repo_name, count in dirty_repos_info:
                    print(f"  - {repo_name} ({count} file(s) dirty)")
                confirm = input("Ignore and start session anyway? [y/N]: ").lower().strip()
                if confirm != 'y':
                    return False
                    
            elif self.ctx.active_mode == "2":
                print("\n💡 NOTE: Dirty repositories detected: " + ", ".join(f"{n}({c})" for n, c in dirty_repos_info))
                
        return True

    def manage_kms_permissions(self, protect: bool = True) -> None:
        """Sets 07-Core-KMS to read-only (True) or read-write (False)."""
        kms_dir = os.path.join(self.ctx.vault_root, "07-Core-KMS")
        if not os.path.exists(kms_dir):
            return
            
        mode_dir = 0o555 if protect else 0o755
        mode_file = 0o444 if protect else 0o644
        label = "🔒 Protecting" if protect else "🔓 Unlocking"
        
        print(f"{label} 07-Core-KMS...")
        for root, dirs, files in os.walk(kms_dir):
            for d in dirs:
                try: os.chmod(os.path.join(root, d), mode_dir)
                except Exception: pass
            for f in files:
                try: os.chmod(os.path.join(root, f), mode_file)
                except Exception: pass

    def run_signoff(self) -> bool:
        """Executes the close_task.py sign-off."""
        signoff_script = os.path.join(self.ctx.vault_root, "08-Base-Scripts/close_task.py")
        if not os.path.exists(signoff_script):
            return True
            
        while True:
            result = subprocess.run([sys.executable, signoff_script])
            if result.returncode != 0:
                print("\n🛑 SESSION SIGN-OFF BLOCKED.")
                print("  [r] Retry / [i] Force ignore / [c] Cancel exit")
                choice = input("Choice: ").strip().lower()
                if choice == 'r': continue
                if choice == 'i': break
                if choice == 'c': return False
            else:
                break
        return True
