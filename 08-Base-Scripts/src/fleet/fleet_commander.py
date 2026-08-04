#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS: Fleet Commander - Mass Git & Single Repo Operations
DATA FLOW: Scans repository folders -> Audits Architecture & Docs -> Commits & Pushes changes
KEY PARAMETERS: 
    - repos: List of repositories to process (or single repo via --repo)
    - commit_msg: Standardized commit message
"""

import os
import sys
from pathlib import Path
from lib.bootstrap import ensure_virtualenv, prepend_venv_bin, ensure_import_paths
from lib.orchestration_lib import setup_terminal, get_logger, resolve_vault_and_workspace

script_dir = Path(__file__).resolve().parent
vault_root = ensure_virtualenv(str(script_dir))
prepend_venv_bin(vault_root)

ensure_import_paths(script_dir, vault_root)

setup_terminal()

from os.path import join as osPathJoin, exists as osPathExists, abspath as osPathAbspath, dirname as osPathDirname
import subprocess as subProcess
import argparse
from typing import List, Optional, Tuple, Union

# Add the lib directory to sys.path to import sovereignty
lib_path = script_dir.parent / "lib"
sys.path.append(str(lib_path))

# --- Environment Setup ---
try:
    from sovereignty import Sovereignty
except ImportError:
    print("❌ Error: sovereignty.py not found in lib/")
    sys.exit(1)



# ### COMPONENT CLASS ###

class FleetCommander:
    Name: str = "FleetCommander"

    def __init__(self, base_path: str, config: Optional[object] = None, logger: Optional[object] = None, dry_run: bool = False, target_repo: Optional[str] = None, is_fleet: bool = False, commit_msg: Optional[str] = None, tag: Optional[str] = None) -> None:
        self.config = config
        self.logger = logger or get_logger(self.Name)
        self.base_path: str = base_path
        self.dry_run: bool = dry_run
        self.engine = Sovereignty(workspace_root=Path(self.base_path))
        self.excluded_repos = set()
        
        vault_root, workspace_root = resolve_vault_and_workspace(__file__)
        self.vault_root = vault_root
        self.workspace_root = workspace_root
        
        self.inventory_path = osPathJoin(str(self.vault_root), "05-Fleet-Operation", "00-Repo-Control", "inventory.json")
        if not osPathExists(self.inventory_path):
            self.inventory_path = osPathJoin(str(self.workspace_root), "fleet-operation-brain", "00-Repo-Control", "inventory.json")
        
        self.repo_name_to_path = {}
        all_repos = self._load_inventory()
        
        if target_repo:
            resolved_path = self.repo_name_to_path.get(target_repo, target_repo)
            self.repos = [resolved_path]
            self.single_mode = True
        elif is_fleet:
            self.repos = all_repos
            self.single_mode = False
        else:
            print("❌ Error: You must explicitly specify either --repo <name> or --fleet.")
            sys.exit(1)
            
        self.commit_msg: str = commit_msg or "chore(fleet): standardized fleet operation"
        self.tag: Optional[str] = tag

    def _load_inventory(self) -> List[str]:
        """Loads repository paths from inventory.json and populates compliance exclusions."""
        from json import load as jsonLoad
        if not osPathExists(self.inventory_path):
            self._log(f"Inventory not found at {self.inventory_path}", "error")
            return []
            
        try:
            with open(self.inventory_path, "r", encoding='utf-8') as f:
                data = jsonLoad(f)
                repos = []
                for repo in data.get("repositories", []):
                    # inventory.json stores paths relative to workspace root (e.g., ./config-server)
                    # We need to clean up the "./" for internal consistency if needed
                    repo_path = repo.get("path", "")
                    if repo_path.startswith("./"):
                        repo_path = repo_path[2:]
                    repos.append(repo_path)
                    
                    repo_name = repo.get("name", "")
                    if repo_name:
                        self.repo_name_to_path[repo_name] = repo_path
                    
                    if repo.get("exclude_from_compliance", False):
                        self.excluded_repos.add(repo_path)
                        self.excluded_repos.add(repo_name)
                return repos
        except Exception as e:
            self._log(f"Failed to load inventory: {e}", "error")
            return []

    # -----------------------------------------------------------------------------------------------

    def _log(self, message: str, level: str = "info") -> None:
        """Helper to log messages using the injected logger."""
        if hasattr(self.logger, level):
            getattr(self.logger, level)(message)
        else:
            self.logger.info(message)

    def _step(self, repo: str, action: str) -> None:
        """Verbose step indicator."""
        print(f"    {repo.ljust(35)} | {action}...")

    # -----------------------------------------------------------------------------------------------

    def _run_command(self, cmd: Union[str, List[str]], cwd: str) -> Tuple[str, Optional[str]]:
        """Helper to run shell commands within a specific directory safely without shell=True."""
        import shlex
        if isinstance(cmd, str):
            cmd_list = shlex.split(cmd)
        else:
            cmd_list = cmd
            
        cmd_str = " ".join(cmd_list)
        if self.dry_run and any(x in cmd_list for x in ["push", "commit", "add"]):
            return f"[DRY-RUN] Executing: {cmd_str}", None
            
        try:
            result = subProcess.run(
                cmd_list, cwd=cwd, shell=False, 
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip(), None
        except subProcess.CalledProcessError as e:
            return e.stdout.strip() or "No stdout", e.stderr.strip() or "No stderr"

    # --- COMPLIANCE AUDITS ---

    def audit_docs(self, repo_path: Path, repo_name: str) -> bool:
        self._step(repo_name, "Auditing documentation")
        mandatory_files = ["AI-Init.md", "AI-Project-DNA.md", "AI-Session-State.md", "TODO.md", "README.md"]
        success = True

        for filename in mandatory_files:
            file_path = repo_path / filename
            if not file_path.exists():
                self._log(f"[{repo_name}] Missing mandatory file: {filename}", "error")
                success = False
            else:
                self.engine.audit_file(file_path)
        
        report = self.engine.get_report()
        if report["errors"]:
            for err in report["errors"]:
                self._log(f"[{repo_name}] {err}", "error")
            success = False
        
        return success

    def audit_isolation_zone(self, repo_path: Path, repo_name: str) -> bool:
        self._step(repo_name, "Auditing isolation zone compliance")
        return self.engine.validate_isolation_zone(repo_path, repo_name)

    def validate_architecture(self, repo_path: Path, repo_name: str) -> bool:
        self._step(repo_name, "Validating fleet architecture rules")
        workflow_dir = repo_path / ".github" / "workflows"
        if not workflow_dir.exists():
            self._log(f"[{repo_name}] No GitHub workflows found.", "warning")
            return True

        for wf in workflow_dir.glob("*.yml"):
            with open(wf, "r", encoding="utf-8") as f:
                content = f.read()
                if "[FLEET-ARCHITECT]" not in content:
                    self._log(f"[{repo_name}] Workflow {wf.name} missing [FLEET-ARCHITECT] header.", "error")
                    return False
                if "Sync-ID:" not in content:
                    self._log(f"[{repo_name}] Workflow {wf.name} missing Sync-ID.", "error")
                    return False
        return True

    # -----------------------------------------------------------------------------------------------

    def execute_fleet_push(self) -> None:
        """Main execution loop for mass git operations."""
        mode_str = " (DRY RUN MODE)" if self.dry_run else ""
        scope_str = "Single Repo" if self.single_mode else "Mass Push"
        self._log(f"Starting {scope_str} Operation{mode_str} ---", "info")
        
        # Automatically trigger deployment logs & action plans housekeeping
        try:
            log_archiver = osPathJoin(str(self.vault_root), "05-Fleet-Operation", "02-Deployment-Logs", "archive.py")
            if not osPathExists(log_archiver):
                log_archiver = osPathJoin(str(self.workspace_root), "fleet-operation-brain", "02-Deployment-Logs", "archive.py")
            if osPathExists(log_archiver):
                self._run_command(f"python3 {log_archiver}", self.base_path)
                
            plan_archiver = osPathJoin(str(self.vault_root), "05-Fleet-Operation", "01-Fleet-Action-Plans", "archive.py")
            if not osPathExists(plan_archiver):
                plan_archiver = osPathJoin(str(self.workspace_root), "fleet-operation-brain", "01-Fleet-Action-Plans", "archive.py")
            if osPathExists(plan_archiver):
                self._run_command(f"python3 {plan_archiver}", self.base_path)
        except Exception:
            pass
            
        # Pre-flight check
        git_ver, err = self._run_command("git --version", self.base_path)
        if err:
            self._log(f"Git not found! {err}", "error")
            return
        self._log(f"Using {git_ver}", "success")

        results: List[str] = []

        for repo in self.repos:
            repo_path_str: str = osPathJoin(self.base_path, repo)
            repo_path: Path = Path(repo_path_str)
            self._log(f"Processing repository: {repo}", "info")
            
            if not osPathExists(repo_path_str):
                results.append(f"{repo}: [SKIP] Path does not exist")
                continue

            if not osPathExists(osPathJoin(repo_path_str, ".git")):
                results.append(f"{repo}: [SKIP] Not a git repository")
                continue

            # 1. Get current branch
            self._step(repo, "Detecting branch")
            branch, err = self._run_command("git rev-parse --abbrev-ref HEAD", repo_path_str)
            if err or branch == "HEAD":
                # Handle detached HEAD or errors
                branch, err = self._run_command("git branch --show-current", repo_path_str)
                if not branch or branch == "HEAD":
                    self._log(f"[{repo}] is in a detached HEAD state. Push blocked.", "error")
                    results.append(f"{repo}: [ERROR] Detached HEAD state")
                    continue
            
            self._step(repo, f"Active branch: {branch}")

            if branch != "develop":
                self._log(f"Not on 'develop' branch. Push blocked for {repo}.", "error")
                results.append(f"{repo}: [ERROR] Not on develop branch")
                continue

            # 2. Compliance Audits
            is_excluded = repo in self.excluded_repos or repo.split("/")[-1] in self.excluded_repos
            if is_excluded:
                self._log(f"[{repo}] Skipping strict compliance audits (Knowledge-Base).", "info")
            else:
                docs_ok = self.audit_docs(repo_path, repo)
                arch_ok = self.validate_architecture(repo_path, repo)
                iso_ok = self.audit_isolation_zone(repo_path, repo)

                if not (docs_ok and arch_ok and iso_ok):
                    print("\n\033[91m" + "🔥"*20)
                    print(f"🔥 QUARANTINE ALERT: {repo}")
                    print("🔥 This repository has failed strict compliance audits.")
                    print("🔥 It will be SKIPPED from the fleet push.")
                    print("🔥"*20 + "\033[0m\n")
                    self._log(f"{repo} failed compliance audits. Skipping.", "error")
                    results.append(f"{repo}: [ERROR] Compliance check failed (QUARANTINED)")
                    continue

            # 3. Stage changes
            self._step(repo, "Staging changes (git add .)")
            self._run_command("git add .", repo_path_str)

            # 4. Check for changes
            self._step(repo, "Checking status")
            status, _ = self._run_command("git status --porcelain", repo_path_str)
            has_changes = bool(status)
            
            commit_ok = True
            if has_changes:
                # 5. Commit
                self._step(repo, f"Committing changes: {self.commit_msg[:30]}...")
                out, err = self._run_command(f'git commit -m "{self.commit_msg}"', repo_path_str)
                if err:
                    self._log(f"{repo} commit failed: {err}", "error")
                    results.append(f"{repo}: [ERROR] Commit failed")
                    commit_ok = False
                
                if commit_ok:
                    # 6. Push
                    self._step(repo, f"Pushing to origin {branch}")
                    out, err = self._run_command(f"git push origin {branch}", repo_path_str)
                    if err:
                        self._log(f"{repo} push failed: {err}", "error")
                        results.append(f"{repo}: [ERROR] Push failed")
                        commit_ok = False
            else:
                self._step(repo, "No changes detected")

            if commit_ok:
                # 7. Tagging
                if self.tag:
                    self._step(repo, f"Tagging commit with {self.tag}")
                    self._run_command(f"git tag -d {self.tag}", repo_path_str)
                    self._run_command(f"git push origin :refs/tags/{self.tag}", repo_path_str)
                    tag_out, tag_err = self._run_command(f'git tag -a {self.tag} -m "Release version {self.tag}"', repo_path_str)
                    if tag_err:
                        self._log(f"{repo} tagging failed: {tag_err}", "error")
                        results.append(f"{repo}: [ERROR] Tagging failed")
                    else:
                        push_tag_out, push_tag_err = self._run_command(f"git push origin {self.tag}", repo_path_str)
                        if push_tag_err:
                            self._log(f"{repo} tag push failed: {push_tag_err}", "error")
                            results.append(f"{repo}: [ERROR] Tag push failed")
                        else:
                            self._log(f"{repo} successfully tagged with {self.tag} and pushed", "success")
                            results.append(f"{repo}: [SUCCESS] Pushed changes & tag {self.tag}")
                else:
                    if has_changes:
                        results.append(f"{repo}: [SUCCESS] Pushed to {branch}")
                    else:
                        results.append(f"{repo}: [OK] No changes")

        print("\n" + "="*80)
        self._log("FINAL FLEET SUMMARY", "info")
        print("="*80)
        for res in results:
            print(res)

# ### MAIN EXECUTION ###

def main():
    parser = argparse.ArgumentParser(description="FleetCommander - Mass Git & Single Repo Operations")
    parser.add_argument("--dry-run", action="store_true", help="Simulate operations without making changes")
    parser.add_argument("--repo", "-r", type=str, help="Target a specific repository")
    parser.add_argument("--fleet", action="store_true", help="Explicitly target the entire fleet")
    parser.add_argument("--message", "-m", type=str, help="Commit message")
    parser.add_argument("--tag", "-t", type=str, help="Attach a Git tag to the commit and push it")
    args = parser.parse_args()

    vault_root, workspace_root = resolve_vault_and_workspace(__file__)
    base_dir: str = str(workspace_root)
    
    commander = FleetCommander(base_dir, dry_run=args.dry_run, target_repo=args.repo, is_fleet=args.fleet, commit_msg=args.message, tag=args.tag)
    commander.execute_fleet_push()


if __name__ == "__main__":
    main()
