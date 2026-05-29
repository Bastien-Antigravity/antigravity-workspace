#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS: Fix Feats - Standardizes FEAT markdown files across the obsidian-brain.
DATA FLOW: Scans specified directories -> Parses frontmatter -> Applies domain tags and backlinks -> Updates files.
KEY PARAMETERS: 
    - root_dir: Path to behavior specs.
    - hubs_dir: Path to microservice hubs.
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


import os
from os.path import join as osPathJoin, exists as osPathExists, abspath as osPathAbspath, dirname as osPathDirname, basename as osPathBasename
from typing import Dict, List, Optional

# ### COMPONENT CLASS ###

class FeatFixer:
    Name: str = "FeatFixer"

    def __init__(self, config: Optional[object] = None, logger: Optional[object] = None) -> None:
        self.config = config
        self.logger = logger
        self.vault_root: str = osPathAbspath(osPathJoin(osPathDirname(__file__), ".."))
        self.root_dir: str = osPathJoin(self.vault_root, "02-Business-BDD", "02-Behavior-Specs")
        self.hubs_dir: str = osPathJoin(self.vault_root, "06-Microservices")
        self.domain_map: Dict[str, str] = {
            "config-server": "#domain/networking",
            "data-ingestor": "#domain/analysis",
            "distributed-config": "#domain/networking",
            "enhanced-backtesting": "#domain/analysis",
            "flexible-logger": "#domain/observability",
            "fundamental-analysis": "#domain/analysis",
            "log-server": "#domain/observability",
            "market-observer": "#domain/analysis",
            "microservice-toolbox": "#domain/architecture",
            "notif-server": "#domain/interface",
            "ontime-scheduler": "#domain/architecture",
            "orderbook-aggregator": "#domain/analysis",
            "safe-socket": "#domain/networking",
            "sandbox-testing": "#domain/architecture",
            "tele-remote": "#domain/interface",
            "universal-logger": "#domain/observability",
            "web-interface": "#domain/interface",
            "technical-analysis": "#domain/analysis"
        }

    # -----------------------------------------------------------------------------------------------

    def _log(self, message: str) -> None:
        """Helper to log messages using the injected logger or fallback to print."""
        formatted_msg: str = "{0} : {1}".format(self.Name, message)
        if self.logger and hasattr(self.logger, "info"):
            self.logger.info(formatted_msg)
        else:
            print(formatted_msg)

    # -----------------------------------------------------------------------------------------------

    def _get_hub_link(self, ms: str) -> Optional[str]:
        """Try to find the hub file for a given microservice."""
        if not osPathExists(self.hubs_dir):
            return None
            
        for file in os.listdir(self.hubs_dir):
            if ms.lower() in file.lower() and file.endswith("-Hub.md"):
                return f"[[06-Microservices/{file.replace('.md', '')}|🌐 {ms.capitalize()} Hub]]"
        return None

    # -----------------------------------------------------------------------------------------------

    def _move_root_feats(self) -> None:
        """Move root FEAT files to ontime-scheduler if appropriate."""
        if not osPathExists(self.root_dir):
            return

        root_feats: List[str] = [f for f in os.listdir(self.root_dir) if f.startswith("FEAT-") and f.endswith(".md")]
        if root_feats:
            target_dir: str = osPathJoin(self.root_dir, "ontime-scheduler")
            if not osPathExists(target_dir):
                os.makedirs(target_dir, exist_ok=True)
            for f in root_feats:
                os.rename(osPathJoin(self.root_dir, f), osPathJoin(target_dir, f))

    # -----------------------------------------------------------------------------------------------

    def process_feats(self) -> None:
        """Iterates through all FEAT files and applies standardization rules."""
        self._log("Starting FEAT file standardization...")
        self._move_root_feats()

        for root, dirs, files in os.walk(self.root_dir):
            ms_from_folder: str = osPathBasename(root)
            if ms_from_folder not in self.domain_map:
                continue
            
            domain_tag: str = self.domain_map[ms_from_folder]
            hub_link: Optional[str] = self._get_hub_link(ms_from_folder)
            
            for file in files:
                if file.startswith("FEAT-") and file.endswith(".md"):
                    self._process_single_file(osPathJoin(root, file), ms_from_folder, domain_tag, hub_link)
        
        self._log("FEAT file standardization complete.")

    # -----------------------------------------------------------------------------------------------

    def _process_single_file(self, file_path: str, ms_from_folder: str, domain_tag: str, hub_link: Optional[str]) -> None:
        """Processes a single FEAT file to update frontmatter and backlinks."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines: List[str] = f.readlines()
            
            new_lines: List[str] = []
            in_frontmatter: bool = False
            frontmatter_end: int = -1
            
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    if not in_frontmatter:
                        in_frontmatter = True
                    else:
                        in_frontmatter = False
                        frontmatter_end = i
                
                if in_frontmatter:
                    if line.startswith("microservice:"):
                        new_lines.append(f"microservice: {ms_from_folder}\n")
                    elif line.startswith("type:"):
                        new_lines.append(f"type: behavior-spec\n")
                    elif line.startswith("tags:"):
                        new_lines.append(line)
                    elif line.strip() == "- null":
                        pass # Remove null
                    elif line.strip().startswith("- '#"):
                        new_lines.append(line)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Insert domain tag if not present
            found_tags: bool = False
            for i, line in enumerate(new_lines):
                if line.startswith("tags:"):
                    new_lines.insert(i+1, f"- {domain_tag}\n")
                    found_tags = True
                    break
            
            # Add backlink after frontmatter if not present
            if hub_link:
                link_line: str = f"\n*Back-link: {hub_link}*\n"
                if link_line not in "".join(new_lines):
                    new_lines.insert(frontmatter_end + 1, link_line)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
        except Exception as e:
            self._log(f"Error processing {file_path}: {e}")

# ### MAIN EXECUTION ###

if __name__ == "__main__":
    fixer = FeatFixer()
    fixer.process_feats()
