#!/usr/bin/env python
# coding:utf-8
"""
🚀 CLOSE MISSION (Governance Gate)
Finalizes the AI session by verifying state updates and documentation health.
Run this before concluding any major task.
"""
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

from pathlib import Path
from datetime import datetime, timedelta

# Add lib directory to sys.path
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir / "lib"))

try:
    from sovereignty import Sovereignty
except ImportError:
    print("❌ Error: Could not find sovereignty.py in lib/")
    sys.exit(1)

import json

def get_active_mode(vault_root: Path) -> str:
    # 1. Check environment variable
    mode = os.environ.get("SQUAD_ACTIVE_MODE")
    if mode:
        return mode
    # 2. Check MODE-MANUAL.md
    mode_file = vault_root / "00-AI-Orchestration" / "MODE-MANUAL.md"
    if mode_file.exists():
        try:
            with open(mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("active_mode:"):
                        return line.split(":")[1].strip()
        except Exception:
            pass
    return "4"  # Default fallback to Mode 4

def get_fleet_repositories(workspace_root: Path) -> list:
    inventory_path = workspace_root / "obsidian-brain" / "05-Fleet-Operation" / "00-Repo-Control" / "inventory.json"
    if not inventory_path.exists():
        return []
    try:
        with open(inventory_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("repositories", [])
    except Exception as e:
        print(f"⚠️ Failed to load inventory.json: {e}")
        return []

def main():
    print("\n" + "═"*60)
    print("🎭 BASTIEN-ANTIGRAVITY: MISSION SIGN-OFF RITUAL")
    print("═"*60)
    
    workspace_root = script_dir.parents[1]
    vault_root = workspace_root / "obsidian-brain"
    
    active_mode = get_active_mode(vault_root)
    print(f"📡 Active Mode Detected: Mode {active_mode}")
    
    # Exclude internal folders, templates, and programmatic manuals from the mandatory audit
    EXCLUSIONS = [".git", ".obsidian", ".gemini", "Templates", "MODE-MANUAL.md"]
    
    engine = Sovereignty(workspace_root=workspace_root)
    
    # Discover repositories to check
    repositories = get_fleet_repositories(workspace_root)
    repos_to_check = []
    
    # Ensure obsidian-brain itself is in the check list if it exists
    has_vault_in_inventory = False
    for repo in repositories:
        repo_name = repo.get("name")
        repo_path_rel = repo.get("path")
        repo_abs_path = (workspace_root / repo_path_rel).resolve()
        if repo_abs_path.exists() and (repo_abs_path / ".git").exists():
            is_vault = (repo_name == "obsidian-brain" or repo_abs_path == vault_root.resolve())
            if is_vault:
                has_vault_in_inventory = True
            repos_to_check.append({
                "name": repo_name,
                "path": repo_abs_path,
                "is_vault": is_vault
            })
            
    if not has_vault_in_inventory and vault_root.exists():
        repos_to_check.insert(0, {
            "name": "obsidian-brain",
            "path": vault_root.resolve(),
            "is_vault": True
        })
        
    dirty_repos = []
    all_hot_files = []
    
    from subprocess import run as subprocessRun
    
    for repo in repos_to_check:
        repo_name = repo["name"]
        repo_path = repo["path"]
        
        is_dirty = False
        repo_hot_files = []
        session_state_modified = False
        
        try:
            result = subprocessRun(
                ["git", "status", "--porcelain"], 
                cwd=repo_path, capture_output=True, text=True, check=True
            )
            status_lines = [line for line in result.stdout.splitlines() if line.strip()]
            if status_lines:
                is_dirty = True
                for line in status_lines:
                    status_path = line[3:].strip()
                    if "AI-Session-State.md" in status_path:
                        session_state_modified = True
                    
                    if status_path.endswith(".md"):
                        if any(x in status_path for x in EXCLUSIONS):
                            continue
                        full_path = repo_path / status_path
                        if full_path.exists() and not engine.is_ignored_by_firewall(full_path):
                            repo_hot_files.append(full_path)
        except Exception as e:
            # Fallback to time-based detection
            print(f"⚠️ Git status failed for {repo_name}: {e}. Falling back to 2-hour window...")
            hot_threshold = datetime.now() - timedelta(hours=2)
            for path in repo_path.rglob("*.md"):
                if any(x in path.parts for x in EXCLUSIONS):
                    continue
                if engine.is_ignored_by_firewall(path):
                    continue
                try:
                    mtime = datetime.fromtimestamp(path.stat().st_mtime)
                    if mtime > hot_threshold:
                        is_dirty = True
                        repo_hot_files.append(path)
                        if "AI-Session-State.md" in path.name:
                            session_state_modified = True
                except Exception:
                    pass
                    
        if is_dirty:
            dirty_repos.append(repo)
            print(f"📡 Repo '{repo_name}' is dirty. Auditing...")
            
            # Verify AI-Session-State.md modification
            if not session_state_modified:
                engine.log_error(f"[{repo_name}] Dirty repository lacks updates to its local AI-Session-State.md.")
                
            # Audit and auto-fix files
            for path in repo_hot_files:
                engine.auto_fix_file(path)
                engine.audit_file(path)
                all_hot_files.append(path)
                
    if not dirty_repos:
        print("✨ Fleet is Clean: No uncommitted session work detected in any repository.")
        return
        
    report = engine.get_report()
    
    # Check if all dirty repositories had their session states updated
    state_ok = True
    for err in engine.errors:
        if "AI-Session-State.md" in err:
            state_ok = False
            
    # 4. Ritual Reporting
    print("\n" + "─"*60)
    print("📊 SOVEREIGNTY GATE STATUS")
    print("─"*60)
    
    metadata_icon = "✅" if report["success"] else "❌"
    state_icon = "✅" if state_ok else "❌"
    print(f"  {metadata_icon} METADATA  : {'PASSED' if report['success'] else 'VIOLATED'}")
    print(f"  {state_icon} STATE LOG : {'SYNCED' if state_ok else 'MISSING'}")
    
    if report["success"] and state_ok:
        print("\n✨ VERDICT: MISSION ACCOMPLISHED")
        print("   The fleet remains synchronized and sovereign.")
        
        # Generate the Seal
        mission_id = datetime.now().strftime("M-%Y%m%d-%H%M")
        print("\n📜 SESSION SIGN-OFF SEAL:")
        print("   " + "─"*40)
        print(f"   Mission-ID : {mission_id}")
        print(f"   Status     : SEALED-AND-SYNCED")
        print(f"   Taxonomy   : Trinity-Compliant")
        print("   " + "─"*40)
        
        # 5. AUTOMATIC PUSH RITUAL
        print("\n🚀 Initiating Fleet Synchronization (Git Push)...")
        for repo in dirty_repos:
            repo_name = repo["name"]
            repo_path = repo["path"]
            
            if repo["is_vault"]:
                try:
                    print(f"   Syncing vault repository '{repo_name}'...")
                    subprocessRun(["git", "add", "."], cwd=repo_path, check=True)
                    commit_msg = f"chore(governance): mission sign-off {mission_id}"
                    subprocessRun(["git", "commit", "-m", commit_msg], cwd=repo_path, check=True)
                    subprocessRun(["git", "push"], cwd=repo_path, check=True)
                    print(f"   ✅ Vault '{repo_name}' pushed successfully.")
                except Exception as e:
                    print(f"   ⚠️  Push failed for '{repo_name}': {e}")
                    print("      Please push manually to complete the sync.")
            else:
                if active_mode == "3":
                    try:
                        print(f"   Syncing sibling repository '{repo_name}'...")
                        subprocessRun(["git", "add", "."], cwd=repo_path, check=True)
                        commit_msg = f"chore(governance): mission sign-off {mission_id}"
                        subprocessRun(["git", "commit", "-m", commit_msg], cwd=repo_path, check=True)
                        subprocessRun(["git", "push"], cwd=repo_path, check=True)
                        print(f"   ✅ Sibling '{repo_name}' pushed successfully.")
                    except Exception as e:
                        print(f"   ⚠️  Push failed for sibling '{repo_name}': {e}")
                        print("      Please push manually to complete the sync.")
                else:
                    print(f"   ⚠️  Mode {active_mode} Active: Skipped automatic push for sibling repository '{repo_name}'. Please push manually.")
    else:
        print("\n🛑 VERDICT: MISSION BLOCKED")
        print("   Please resolve the following governance violations:")
        for err in engine.errors:
            print(f"   [!] {err}")
            
    if report["warnings"]:
        print("\n💡 HYGIENE SUGGESTIONS:")
        for warn in report["warnings"]:
            print(f"   [~] {warn}")
            
    print("\n" + "═"*60 + "\n")
    
    if not (report["success"] and state_ok):
        sys.exit(1)

if __name__ == "__main__":
    main()
