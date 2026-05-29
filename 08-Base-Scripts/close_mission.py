#!/usr/bin/env python
# coding:utf-8
"""
🚀 CLOSE MISSION (Governance Gate)
Finalizes the AI session by verifying state updates and documentation health.
Run this before concluding any major task.
"""
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

from pathlib import Path
from datetime import datetime, timedelta
from subprocess import run as subprocessRun
import json

# Add lib directory to sys.path
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir / "lib"))

try:
    from sovereignty import Sovereignty
except ImportError:
    print("❌ Error: Could not find sovereignty.py in lib/")
    sys.exit(1)

def get_active_mode(vault_root: Path) -> str:
    mode = os.environ.get("SQUAD_ACTIVE_MODE")
    if mode:
        return mode
    mode_file = vault_root / "00-AI-Orchestration" / "MODE-MANUAL.md"
    if mode_file.exists():
        try:
            with open(mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("active_mode:"):
                        return line.split(":")[1].strip()
        except Exception:
            pass
    return "4"

def get_fleet_repositories(vault_root: Path) -> list:
    inventory_path = vault_root / "05-Fleet-Operation" / "00-Repo-Control" / "inventory.json"
    if not inventory_path.exists():
        return []
    try:
        with open(inventory_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("repositories", [])
    except Exception as e:
        print(f"⚠️ Failed to load inventory.json: {e}")
        return []

def get_current_branch(repo_path: Path) -> str:
    try:
        result = subprocessRun(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_path, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception:
        return ""

def confirm_step(prompt: str) -> bool:
    choice = input(f"   ❓ {prompt} [y/N]: ").strip().lower()
    return choice == 'y'

def main():
    print("\n" + "═"*60)
    print("🎭 BASTIEN-ANTIGRAVITY: MISSION SIGN-OFF RITUAL")
    print("═"*60)
    
    vault_root = script_dir.parent
    workspace_root = vault_root.parent
    
    active_mode = get_active_mode(vault_root)
    print(f"📡 Active Mode Detected: Mode {active_mode}")
    
    EXCLUSIONS = [".git", ".obsidian", ".gemini", "Templates", "MODE-MANUAL.md"]
    engine = Sovereignty(workspace_root=workspace_root)
    
    repositories = get_fleet_repositories(vault_root)
    repos_to_check = []
    
    has_vault_in_inventory = False
    for repo in repositories:
        repo_name = repo.get("name")
        repo_path_rel = repo.get("path")
        repo_abs_path = (workspace_root / repo_path_rel).resolve()
        if repo_abs_path.exists() and (repo_abs_path / ".git").exists():
            is_vault = (repo_name == vault_root.name or repo_abs_path.resolve() == vault_root.resolve())
            if is_vault:
                has_vault_in_inventory = True
            repos_to_check.append({
                "name": repo_name,
                "path": repo_abs_path,
                "is_vault": is_vault
            })
            
    if not has_vault_in_inventory and vault_root.exists():
        repos_to_check.insert(0, {
            "name": vault_root.name,
            "path": vault_root.resolve(),
            "is_vault": True
        })
        
    dirty_repos = []
    all_hot_files = []
    
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
        except Exception:
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
            if not session_state_modified:
                engine.log_error(f"[{repo_name}] Dirty repository lacks updates to its local AI-Session-State.md.")
            for path in repo_hot_files:
                engine.auto_fix_file(path)
                engine.audit_file(path)
                all_hot_files.append(path)
                
    if not dirty_repos:
        print("✨ Fleet is Clean: No uncommitted session work detected in any repository.")
        return
        
    report = engine.get_report()
    state_ok = True
    for err in engine.errors:
        if "AI-Session-State.md" in err:
            state_ok = False
            
    print("\n" + "─"*60)
    print("📊 SOVEREIGNTY GATE STATUS")
    print("─"*60)
    
    metadata_icon = "✅" if report["success"] else "❌"
    state_icon = "✅" if state_ok else "❌"
    print(f"  {metadata_icon} METADATA  : {'PASSED' if report['success'] else 'VIOLATED'}")
    print(f"  {state_icon} STATE LOG : {'SYNCED' if state_ok else 'MISSING'}")
    
    if report["file_errors"] or report["file_warnings"]:
        print("\n📂 DETAILED AUDIT REPORT:")
        for file_path, errors in report["file_errors"].items():
            print(f"  ❌ {Path(file_path).name}")
            for err in errors:
                print(f"     - {err}")
        for file_path, warnings in report["file_warnings"].items():
            print(f"  ⚠️  {Path(file_path).name}")
            for warn in warnings:
                print(f"     - {warn}")

    if report["success"] and state_ok:
        print("\n✨ VERDICT: MISSION ACCOMPLISHED")
        mission_id = datetime.now().strftime("M-%Y%m%d-%H%M")
        print("\n📜 SESSION SIGN-OFF SEAL:")
        print("   " + "─"*40)
        print(f"   Mission-ID : {mission_id}")
        print(f"   Status     : SEALED-AND-SYNCED")
        print(f"   Taxonomy   : Trinity-Compliant")
        print("   " + "─"*40)
        
        # 5. GIT RITUAL (STRICTLY ON DEVELOP)
        print("\n🚀 Initiating Fleet Synchronization Ritual...")
        for repo in dirty_repos:
            repo_name = repo["name"]
            repo_path = repo["path"]
            branch = get_current_branch(repo_path)
            
            if branch != "develop":
                if branch in ["main", "master"]:
                    print(f"   🛑 PROHIBITED: Automatic ritual is FORBIDDEN on the '{branch}' branch.")
                else:
                    print(f"   ⚠️  SKIPPED: Ritual only allowed on 'develop'. Current branch is '{branch}'.")
                continue

            try:
                print(f"   📦 Preparing updates for '{repo_name}' on 'develop'...")
                subprocessRun(["git", "add", "."], cwd=repo_path, check=True)
                
                if confirm_step(f"Commit changes to '{repo_name}'?"):
                    commit_msg = f"chore: mission sign-off {mission_id}"
                    subprocessRun(["git", "commit", "-m", commit_msg], cwd=repo_path, check=True)
                    print(f"   ✅ Changes committed.")
                    
                    if confirm_step(f"Push changes for '{repo_name}' to origin develop?"):
                        subprocessRun(["git", "push", "origin", "develop"], cwd=repo_path, check=True)
                        print(f"   ✅ Pushed successfully.")
                    else:
                        print(f"   ➡️  Push skipped.")
                else:
                    print(f"   ➡️  Commit skipped.")
            except Exception as e:
                print(f"   ⚠️  Sync failed for '{repo_name}': {e}")
    else:
        print("\n🛑 VERDICT: MISSION BLOCKED")
        for err in engine.errors:
            print(f"   [!] {err}")
            
    if report["warnings"] and not report["file_warnings"]:
        print("\n💡 HYGIENE SUGGESTIONS:")
        for warn in report["warnings"]:
            print(f"   [~] {warn}")
            
    print("\n" + "═"*60 + "\n")
    if not (report["success"] and state_ok):
        sys.exit(1)

if __name__ == "__main__":
    main()
