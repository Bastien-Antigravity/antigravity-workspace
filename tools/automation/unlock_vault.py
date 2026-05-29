#!/usr/bin/env python3
# coding:utf-8
import os
import sys
from pathlib import Path

# Setup encoding
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# Resolve vault root: two levels up from tools/automation/
vault_root = Path(__file__).resolve().parent.parent.parent
print(f"🔓 Vault Root: {vault_root}")

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

# Clean up test_chmod.py in vault root if it exists
test_script = vault_root / "test_chmod.py"
if test_script.exists():
    try:
        os.remove(test_script)
        print("Removed test_chmod.py")
    except Exception as e:
        print(f"Error removing test_chmod.py: {e}")

print("Unlock complete! 🎉")
