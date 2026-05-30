#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS: Vault Sentinel - Tag Taxonomy & Obsidian Link Coherence Auditor
DATA FLOW: Scans target directories -> Validates frontmatter tags & Obsidian wikilinks -> Fixes malformed tags
KEY PARAMETERS:
    - --path: Target path to audit (defaults to obsidian-brain root)
    - --fix: Automatically correct malformed tags in frontmatter
    - --verbose: Detailed output for warnings and successful files
"""
import os, sys
# --- Bootstrap ---
import os, sys
_vault_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
while not os.path.exists(os.path.join(_vault_root, ".venv")) and _vault_root != os.path.dirname(_vault_root):
    _vault_root = os.path.dirname(_vault_root)
if _vault_root not in sys.path:
    sys.path.append(_vault_root)

_orch_dir = os.path.join(_vault_root, "00-AI-Orchestration")
if _orch_dir not in sys.path:
    sys.path.append(_orch_dir)

from orchestration_lib import setup_terminal
setup_terminal()

from sys import exit as sysExit, stdout as sysStdout, path as sysPath
from os import walk as osWalk
from re import match as reMatch, findall as reFindall
from argparse import ArgumentParser as argparseArgumentParser
from pathlib import Path
from typing import List, Set, Tuple

# --- Environment Setup ---
SCRIPT_DIR = Path(__file__).resolve().parent
sysPath.append(str(SCRIPT_DIR / "lib"))

try:
    from sovereignty import Sovereignty
except ImportError:
    print("❌ Error: sovereignty.py not found in lib/")
    sysExit(1)


class VaultSentinel:
    def __init__(self, workspace_root: Path, taxonomy_path: Path, verbose: bool = False):
        self.workspace_root = workspace_root
        self.verbose = verbose
        self.engine = Sovereignty(taxonomy_path, workspace_root)

    def check_file_tags_and_links(self, filepath: Path, fix: bool = False) -> Tuple[List[str], List[str]]:
        """
        Audits tags and Obsidian wikilinks inside a single markdown file using Sovereignty.
        Optionally repairs malformed tags if fix=True.
        """
        if fix:
            self.engine.auto_fix_file(filepath)

        self.engine.errors = []
        self.engine.warnings = []
        
        self.engine.audit_file(filepath)
        
        return self.engine.errors.copy(), self.engine.warnings.copy()

    def audit_directory(self, target_dir: Path, fix: bool = False) -> Tuple[int, int]:
        """Audits a single markdown file or all markdown files under a target directory."""
        print(f"\n📡 Starting Vault Sentinel audit on: {target_dir.resolve()}")
        
        if not target_dir.exists():
            print(f"❌ Error: Target path does not exist: {target_dir}")
            return 1, 0

        files_audited = 0
        total_errors = 0
        total_warnings = 0

        if target_dir.is_file():
            if target_dir.suffix == ".md":
                files_audited += 1
                errs, warns = self.check_file_tags_and_links(target_dir, fix)
                if errs or warns:
                    print(f"\n⚠️  Issues found in: {target_dir.relative_to(self.workspace_root).as_posix()}")
                    for err in errs:
                        print(f"   [!] Error  : {err}")
                        total_errors += 1
                    for warn in warns:
                        print(f"   [~] Warning: {warn}")
                        total_warnings += 1
                elif self.verbose:
                    print(f"   [OK] {target_dir.name}")
            else:
                print(f" [SKIP] File is not a markdown (.md) file: {target_dir.name}")
        else:
            ignore_dirs = {
                ".git", ".obsidian", ".gemini", ".venv", "venv", "node_modules",
                "experiments", "deployments", "plans", "Templates", "04-Templates", "99-Humans", "quick-overview",
                "09-RAG-Engine"
            }
            for root, dirs, files in osWalk(target_dir):
                # Prune ignored directories in-place
                dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ignore_dirs]
                
                for file in files:
                    if file.endswith(".md"):
                        filepath = Path(root) / file
                        files_audited += 1
                        errs, warns = self.check_file_tags_and_links(filepath, fix)
                        
                        if errs or warns:
                            print(f"\n⚠️  Issues found in: {filepath.relative_to(self.workspace_root).as_posix()}")
                            for err in errs:
                                print(f"   [!] Error  : {err}")
                                total_errors += 1
                            for warn in warns:
                                print(f"   [~] Warning: {warn}")
                                total_warnings += 1
                        elif self.verbose:
                            print(f"   [OK] {file}")

        print("\n" + "="*80)
        print(f"📋 SENTINEL AUDIT COMPLETE for {target_dir.name}")
        print(f"   Files Audited : {files_audited}")
        print(f"   Total Errors  : {total_errors}")
        print(f"   Total Warnings: {total_warnings}")
        print("="*80)
        
        return total_errors, total_warnings


if __name__ == "__main__":
    parser = argparseArgumentParser(description="Vault Sentinel - Tag & Obsidian Link Auditor")
    parser.add_argument("--path", "-p", type=str, help="Target directory path to audit (defaults to obsidian-brain)")
    parser.add_argument("--fix", "-f", action="store_true", help="Automatically correct malformed frontmatter tags")
    parser.add_argument("--verbose", "-v", action="store_true", help="Display successful file status")
    args = parser.parse_args()

    # Determine paths relative to base workspace root (parent of obsidian-brain)
    base_workspace = SCRIPT_DIR.parent.parent
    
    target_path_str = args.path
    if not target_path_str:
        # Default to obsidian-brain
        target_path = SCRIPT_DIR.parent
    else:
        target_path = Path(target_path_str).resolve()
        
    taxonomy = SCRIPT_DIR.parent / "07-Core-KMS" / "tag_taxonomy.md"
    
    sentinel = VaultSentinel(base_workspace, taxonomy, args.verbose)
    err_count, warn_count = sentinel.audit_directory(target_path, args.fix)
    
    if err_count > 0:
        sysExit(1)
    sysExit(0)
