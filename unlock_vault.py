import os
from pathlib import Path

vault_root = Path(__file__).resolve().parent
for folder in ["03-Tech-Stack", "07-Core-KMS"]:
    prompts_dir = vault_root / folder / "Role-Prompts"
    if prompts_dir.exists():
        print(f"Unlocking {prompts_dir}...")
        for root, dirs, files in os.walk(prompts_dir):
            for d in dirs:
                try: os.chmod(os.path.join(root, d), 0o755)
                except Exception as e: print(f"Error chmod dir {d}: {e}")
            for f in files:
                try: os.chmod(os.path.join(root, f), 0o644)
                except Exception as e: print(f"Error chmod file {f}: {e}")
print("Unlock complete!")
