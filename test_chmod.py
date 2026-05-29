import os
import sys

path = "/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain/03-Tech-Stack/Role-Prompts/03-Developer/Squad/Web-UI-Specialist.md"
try:
    print(f"Current permissions: {oct(os.stat(path).st_mode)}")
    os.chmod(path, 0o644)
    print(f"New permissions: {oct(os.stat(path).st_mode)}")
    print("SUCCESS")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
