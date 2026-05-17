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

# Standardize terminal output encoding for Windows
if sysStdout.encoding != 'utf-8':
    try:
        sysStdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass


class VaultSentinel:
    def __init__(self, workspace_root: Path, taxonomy_path: Path, verbose: bool = False):
        self.workspace_root = workspace_root
        self.verbose = verbose
        self.engine = Sovereignty(taxonomy_path)
        self.valid_stems: Set[str] = set()
        self.valid_paths: Set[str] = set()
        self._index_entire_workspace()

    def _index_entire_workspace(self) -> None:
        """Indexes all markdown file stems in the workspace to prevent false positive broken links."""
        for root, dirs, files in osWalk(self.workspace_root):
            # Skip common ignores
            if any(x in root for x in [".git", ".obsidian", "experiments", "node_modules"]):
                continue
            for file in files:
                if file.endswith(".md"):
                    path = Path(root) / file
                    self.valid_stems.add(path.stem)
                    # Support links with relative/absolute folder paths
                    self.valid_paths.add(file)
                    try:
                        rel_path = path.relative_to(self.workspace_root).as_posix()
                        self.valid_paths.add(rel_path)
                    except ValueError:
                        pass

    def check_file_tags_and_links(self, filepath: Path, fix: bool = False) -> Tuple[List[str], List[str]]:
        """
        Audits tags and Obsidian wikilinks inside a single markdown file.
        Optionally repairs malformed tags if fix=True.
        """
        errors = []
        warnings = []
        filename = filepath.name

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            return [f"Could not read file: {e}"], []

        # 1. YAML frontmatter validation & repair
        frontmatter_match = reMatch(r"^---([\s\S]*?)---\n*", content)
        if frontmatter_match:
            frontmatter_text = frontmatter_match.group(1)
            lines = frontmatter_text.splitlines()
            modified_lines = []
            has_fixes = False
            in_tags = False

            for line in lines:
                stripped = line.strip()
                if stripped.startswith("tags:"):
                    in_tags = True
                    modified_lines.append(line)
                    continue
                elif in_tags and stripped.startswith("-"):
                    tag_val = stripped[1:].strip()
                    # A. Check for null values
                    if tag_val.lower() == "null" or not tag_val:
                        errors.append(f"[{filename}] Found invalid null tag in frontmatter.")
                        if fix:
                            has_fixes = True
                            continue # Prune the null tag row
                    
                    # B. Check for tags starting with /
                    clean_tag = tag_val.replace("'", "").replace('"', "").strip()
                    if clean_tag.startswith("/"):
                        errors.append(f"[{filename}] Malformed tag starting with '/': '{clean_tag}'")
                        if fix:
                            corrected_tag = "#" + clean_tag[1:]
                            # Keep quotes format if present
                            if "'" in tag_val:
                                corrected_line = line.replace(tag_val, f"'{corrected_tag}'")
                            elif '"' in tag_val:
                                corrected_line = line.replace(tag_val, f'"{corrected_tag}"')
                            else:
                                corrected_line = line.replace(tag_val, corrected_tag)
                            modified_lines.append(corrected_line)
                            has_fixes = True
                            continue
                    
                    modified_lines.append(line)
                else:
                    if in_tags and not stripped.startswith("-") and ":" in stripped:
                        in_tags = False
                    modified_lines.append(line)

            if has_fixes and fix:
                new_frontmatter = "---\n" + "\n".join(modified_lines) + "\n---\n"
                new_content = new_frontmatter + content[frontmatter_match.end():]
                try:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"  🔧 Repaired malformed frontmatter tags in {filename}")
                    content = new_content
                except Exception as e:
                    errors.append(f"Failed to write repairs to file: {e}")

        # 2. Run standard sovereignty audits (Mandatory Frontmatter & Transversal trinity)
        self.engine.errors = []
        self.engine.warnings = []
        self.engine.audit_file(filepath, self.valid_stems, self.valid_paths)
        errors.extend(self.engine.errors)
        warnings.extend(self.engine.warnings)

        # 3. Deep Obsidian Wikilinks Audit
        # Match [[TargetName]] or [[TargetName|alias]]
        wikilinks = reFindall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
        for link in wikilinks:
            clean_link = link.strip()
            # If the link specifies a path, resolve its stem or check path directly
            link_stem = Path(clean_link).stem
            
            if link_stem not in self.valid_stems and clean_link not in self.valid_paths and f"{clean_link}.md" not in self.valid_paths:
                errors.append(f"[{filename}] BROKEN LINK: Wikilink [[{clean_link}]] does not resolve to any active file stem in workspace.")

        return errors, warnings

    def audit_directory(self, target_dir: Path, fix: bool = False) -> Tuple[int, int]:
        """Audits all markdown files under a specific target directory."""
        print(f"\n📡 Starting Vault Sentinel audit on: {target_dir.resolve()}")
        print(f"   Indexed workspace files: {len(self.valid_stems)} stems")
        
        if not target_dir.exists():
            print(f"❌ Error: Target directory does not exist: {target_dir}")
            return 1, 0

        files_audited = 0
        total_errors = 0
        total_warnings = 0

        for root, dirs, files in osWalk(target_dir):
            if any(x in root for x in [".git", ".obsidian", "experiments", "deployments", "plans"]):
                continue
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
