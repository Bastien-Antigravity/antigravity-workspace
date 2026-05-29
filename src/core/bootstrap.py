#!/usr/bin/env python
# coding:utf-8

"""
Centralized Bootstrap Module
Dynamically discovers and activates the nearest virtual environment,
normalizes sys.path for the Obsidian-Brain vault, and ensures required
dependencies are installed.
"""

import os
import sys
import subprocess
import re
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

def _check_and_install_deps(vault_root: Path) -> None:
    # Always check the root requirements
    req_files = [vault_root / "requirements.txt"]
    
    # Dynamically include RAG Engine requirements if present (for unified env)
    rag_req = vault_root / "09-RAG-Engine" / "requirements.txt"
    if rag_req.exists():
        req_files.append(rag_req)
        
    missing_packages = []
    
    # Parse requirements files dynamically
    for req_file in req_files:
        if not req_file.exists():
            continue
        try:
            with open(req_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    # Skip comments or empty lines
                    if not line or line.startswith("#"):
                        continue
                    # Extract the package name (handles name==version, name>=version, name[extra])
                    match = re.match(r"^([a-zA-Z0-9_\-]+)", line)
                    if match:
                        package_name = match.group(1)
                        try:
                            # Verify if the package is installed in the current environment
                            version(package_name)
                        except PackageNotFoundError:
                            missing_packages.append(package_name)
        except Exception as e:
            # Fail-safe: if parsing fails, assume we need to run install
            print(f"⚠️ Error reading {req_file.name}: {e}. Forcing dependency check...")
            missing_packages.append("unknown-fallback")
            break
            
    if missing_packages:
        print(f"\n📦 Missing dependencies detected: {', '.join(missing_packages)}")
        print("   Installing required packages...")
        
        # macOS compatibility: set compile flag to bypass Apple Silicon compilation errors in chroma-hnswlib
        if os.name != "nt" and sys.platform == "darwin":
            os.environ["HNSWLIB_NO_NATIVE"] = "1"
            
        for req_file in req_files:
            if req_file.exists():
                subprocess.run([sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", str(req_file)])

def init(caller_file: str) -> None:
    """
    Ensures the script is running inside the correct virtual environment.
    If not, it re-executes the script using the virtual environment's Python.
    Also ensures that the project root is in sys.path.
    """
    script_path = Path(caller_file).resolve()
    
    # Walk up to find the vault root (.venv or requirements.txt marker)
    current = script_path.parent
    vault_root = None
    
    while current and current != current.parent:
        if (current / ".venv").exists() or (current / "requirements.txt").exists():
            vault_root = current
            break
        current = current.parent
        
    if not vault_root:
        vault_root = script_path.parent # Fallback
        
    venv_dir = vault_root / ".venv"
    if not venv_dir.exists():
        print(f"📦 Virtual environment not found at {venv_dir}")
        print("   Creating new virtual environment...")
        try:
            import venv
            venv.create(str(venv_dir), with_pip=True)
            print("   Virtual environment created successfully.")
        except Exception as e:
            print(f"⚠️ Failed to automatically create virtual environment: {e}")

    if venv_dir.exists():
        venv_python = venv_dir / "Scripts" / "python.exe" if os.name == "nt" else venv_dir / "bin" / "python3"
        
        if venv_python.exists():
            try:
                if not os.path.samefile(sys.executable, str(venv_python)):
                    # Propagate virtual environment variables to environment
                    os.environ["VIRTUAL_ENV"] = str(venv_dir)
                    venv_bin = str(venv_python.parent)
                    os.environ["PATH"] = venv_bin + os.path.pathsep + os.environ.get("PATH", "")
                    os.execl(str(venv_python), str(venv_python), *sys.argv)
            except OSError:
                pass
                
    # We are now in the venv (or no venv exists). Normalize paths.
    if str(vault_root) not in sys.path:
        sys.path.append(str(vault_root))
        
    src_path = vault_root / "src"
    if str(src_path) not in sys.path:
        sys.path.append(str(src_path))
        
    # Check if dependencies need installing
    _check_and_install_deps(vault_root)
