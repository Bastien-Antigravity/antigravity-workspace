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

def main():
    print("\n" + "═"*60)
    print("🎭 BASTIEN-ANTIGRAVITY: MISSION SIGN-OFF RITUAL")
    print("═"*60)
    
    workspace_root = script_dir.parents[1]
    vault_root = workspace_root / "obsidian-brain"
    
    # Exclude internal folders, templates, and programmatic manuals from the mandatory audit
    EXCLUSIONS = [".git", ".obsidian", ".gemini", "Templates", "MODE-MANUAL.md"]
    
    engine = Sovereignty(workspace_root=workspace_root)
    
    # 2. Session Work Detection (Git-Aware)
    from subprocess import run as subprocessRun
    hot_files = []
    try:
        # Get list of modified and untracked files
        result = subprocessRun(
            ["git", "status", "--porcelain"], 
            cwd=vault_root, capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            status_path = line[3:].strip()
            if status_path.endswith(".md"):
                # Filter out exclusions
                if any(x in status_path for x in EXCLUSIONS):
                    continue
                full_path = vault_root / status_path
                if full_path.exists() and not engine.is_ignored_by_firewall(full_path):
                    hot_files.append(full_path)
    except Exception as e:
        print(f"⚠️  Git Detection Failed: {e}. Falling back to 2-hour window...")
        hot_threshold = datetime.now() - timedelta(hours=2)
        for path in vault_root.rglob("*.md"):
            if any(x in path.parts for x in EXCLUSIONS):
                continue
            if engine.is_ignored_by_firewall(path):
                continue
            mtime = datetime.fromtimestamp(path.stat().st_mtime)
            if mtime > hot_threshold:
                hot_files.append(path)
            
    if not hot_files:
        print("✨ Fleet is Clean: No uncommitted session work detected.")
        return

    print(f"📡 Auditing Session Payload: {len(hot_files)} files...")
    
    # 3. Governance Audit
    state_updated = False
    for path in hot_files:
        # Enforce rigid frontmatter formatting and correct links automatically
        engine.auto_fix_file(path)
        engine.audit_file(path)
        if "AI-Session-State" in path.name:
            state_updated = True
            
    report = engine.get_report()
    
    # 4. Ritual Reporting
    print("\n" + "─"*60)
    print("📊 SOVEREIGNTY GATE STATUS")
    print("─"*60)
    
    metadata_icon = "✅" if report["success"] else "❌"
    state_icon = "✅" if state_updated else "❌"
    print(f"  {metadata_icon} METADATA  : {'PASSED' if report['success'] else 'VIOLATED'}")
    print(f"  {state_icon} STATE LOG : {'SYNCED' if state_updated else 'MISSING'}")
    
    if report["success"] and state_updated:
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
        try:
            subprocessRun(["git", "add", "."], cwd=vault_root, check=True)
            commit_msg = f"chore(governance): mission sign-off {mission_id}"
            subprocessRun(["git", "commit", "-m", commit_msg], cwd=vault_root, check=True)
            
            # Check current branch
            branch_result = subprocessRun(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=vault_root, capture_output=True, text=True, check=True
            )
            branch_name = branch_result.stdout.strip()
            
            if branch_name == "HEAD":
                print("⚠️  Warning: Detached HEAD state detected. Skipping auto-push.")
            else:
                # Check if there is an upstream configured
                upstream_result = subprocessRun(
                    ["git", "rev-parse", "--abbrev-ref", "@{u}"],
                    cwd=vault_root, capture_output=True, text=True
                )
                if upstream_result.returncode != 0:
                    # No upstream branch configured
                    print(f"📡 No upstream branch configured for '{branch_name}'. Pushing to origin '{branch_name}'...")
                    subprocessRun(["git", "push", "-u", "origin", branch_name], cwd=vault_root, check=True)
                else:
                    subprocessRun(["git", "push"], cwd=vault_root, check=True)
                print("✅ Changes pushed to GitHub successfully.")
        except Exception as e:
            print(f"⚠️  Push Ritual Failed: {e}")
            print("   Please push manually to complete the sync.")
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
    
    if not (report["success"] and state_updated):
        sys.exit(1)

if __name__ == "__main__":
    main()
