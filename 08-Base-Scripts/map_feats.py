#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS: Map Feats - Generates a mapping of microservices to their behavior specs (FEAT files).
DATA FLOW: Scans the BDD Behavior Specs directory -> Parses 'microservice' frontmatter -> Aggregates and prints the mapping.
KEY PARAMETERS: 
    - root_dir: Relative path to the behavior specs folder.
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

import os
from os.path import join as osPathJoin, exists as osPathExists, abspath as osPathAbspath, dirname as osPathDirname
import re
import sys

# -----------------------------------------------------------------------------------------------

def extract_microservice(file_path: str) -> str:
    """Parses the YAML frontmatter to find the microservice name."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'microservice:\s*(.*)', content)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

# -----------------------------------------------------------------------------------------------

def main() -> None:
    """Scans the specs and builds the microservice-to-feat mapping."""
    vault_root = osPathAbspath(osPathJoin(osPathDirname(__file__), ".."))
    root_dir = osPathJoin(vault_root, "02-Business-BDD", "02-Behavior-Specs")
    
    mapping = {}
    
    if not osPathExists(root_dir):
        print(f"Error: Directory not found: {root_dir}")
        return

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.startswith("FEAT-") and file.endswith(".md"):
                file_path = osPathJoin(root, file)
                ms = extract_microservice(file_path)
                if ms:
                    if ms not in mapping:
                        mapping[ms] = []
                    mapping[ms].append(file.replace(".md", ""))
    
    # Print report
    for ms, feats in mapping.items():
        print(f"[{ms}]")
        for feat in feats:
            print(f"  - {feat}")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
