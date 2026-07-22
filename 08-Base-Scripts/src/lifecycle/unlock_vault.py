#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
Restores read/write permissions (chmod 0755/0644) to role prompts in Tech Stack and Core KMS,
enabling AI adapters and templates to be synchronized/edited.

DATA FLOW:
1. Bootstraps the virtual environment.
2. Scans Role-Prompts subdirectories in 03-Tech-Stack and 07-Core-KMS.
3. Recursively updates permissions on directories (0755) and files (0644).
4. Cleans up any leftover testing scripts (test_chmod.py).

KEY PARAMETERS:
- folders: List of directories within the vault root to unlock.
"""

import os
import sys
from pathlib import Path
from lib.bootstrap import ensure_virtualenv, prepend_venv_bin, ensure_import_paths

def main():
    script_dir = Path(__file__).resolve().parent
    vault_root_path = ensure_virtualenv(str(script_dir))
    prepend_venv_bin(vault_root_path)
    ensure_import_paths(script_dir, vault_root_path)

    vault_root = Path(vault_root_path)

    for folder in ["03-Tech-Stack", "07-Core-KMS"]:
        prompts_dir = vault_root / folder / "Role-Prompts"
        if prompts_dir.exists():
            print(f"Unlocking {prompts_dir}...")
            for root, dirs, files in os.walk(prompts_dir):
                for d in dirs:
                    try:
                        os.chmod(os.path.join(root, d), 0o755)
                    except Exception as e:
                        print(f"Error chmod dir {d}: {e}")
                for f in files:
                    try:
                        os.chmod(os.path.join(root, f), 0o644)
                    except Exception as e:
                        print(f"Error chmod file {f}: {e}")

    test_script = vault_root / "test_chmod.py"
    if test_script.exists():
        try:
            os.remove(test_script)
            print("Removed test_chmod.py")
        except Exception as e:
            print(f"Error removing test_chmod.py: {e}")

    print("Unlock complete!")

if __name__ == '__main__':
    main()
