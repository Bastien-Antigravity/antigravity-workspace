#!/usr/bin/env python
# coding:utf-8

"""
ESSENTIAL PROCESS:
Initializes the Bastien-Antigravity AI Engine Command Center. Handles MCP binding,
pre-session audits, role synchronization, and launches the selected AI client.

DATA FLOW:
1. Performs Preflight and Governance audits to detect architecture drift.
2. Synchronizes Role-Prompts to agent definitions (convert_agents.py).
3. Invokes the Mode Selector and applies the protocol (switch_mode.py).
4. Configures the MCP server-filesystem based on mode isolation rules.
5. Launches the selected AI client in a re-launchable lifecycle loop.

KEY PARAMETERS:
- vault_root: Resolved path to the Obsidian Brain vault.
- mcp_args: Dynamic arguments for the filesystem MCP server.
"""
import os, sys
# Ensure we are running inside the virtual environment
_venv_dir = os.path.dirname(os.path.abspath(__file__))
while _venv_dir and _venv_dir != '/' and not os.path.exists(os.path.join(_venv_dir, ".venv")):
    _parent = os.path.dirname(_venv_dir)
    if _parent == _venv_dir:
        break
    _venv_dir = _parent
_venv_python = os.path.join(_venv_dir, ".venv", "Scripts", "python.exe") if os.name == "nt" else os.path.join(_venv_dir, ".venv", "bin", "python3")
if os.path.exists(_venv_python):
    try:
        if not os.path.samefile(sys.executable, _venv_python):
            os.execl(_venv_python, _venv_python, *sys.argv)
    except OSError:
        pass

from sys import executable as sysExecutable, path as sysPath, stdout as sysStdout, exit as sysExit
from os import makedirs as osMakedirs, listdir as osListdir, name as osName, getenv as osGetenv 
from json import dump as jsonDump, load as jsonLoad
from subprocess import run as subprocessRun
from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists, \
                    expanduser as osPathExpanduser, isdir as osPathIsdir, basename as osPathBasename

# Add current directory to sys.path to enable library imports
script_dir = osPathDirname(osPathAbspath(__file__))
if script_dir not in sysPath:
    sysPath.append(script_dir)

try:
    from switch_mode import get_mode_choice_interactive, apply_mode_protocol, MODES
    from mission_help import MissionHelper
    from clients.registry import (
        DEFAULT_CLIENT,
        build_launch_command,
        client_names,
        get_client_config,
        is_client_available,
        list_agents,
        normalize_client,
    )
except ImportError:
    print("❌ Error: Could not find required launcher modules in 20-Scripts/")
    sysExit(1)

# Standardize terminal output encoding for Windows
if sysStdout.encoding != 'utf-8':
    try:
        sysStdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# -----------------------------------------------------------------------------------------------

def get_vault_python() -> str:
    """Return the vault virtualenv Python when available, otherwise current Python."""
    return _venv_python if osPathExists(_venv_python) else sysExecutable

def _missing_python_packages(python_executable: str) -> list:
    """Check required import modules using the target Python interpreter."""
    module_to_package = {
        "yaml": "PyYAML",
        "mcp": "mcp",
        "openai": "openai",
        "dotenv": "python-dotenv",
    }
    check_code = (
        "import importlib.util\n"
        f"mods = {list(module_to_package.keys())!r}\n"
        "print('\\n'.join(m for m in mods if importlib.util.find_spec(m) is None))\n"
    )
    result = subprocessRun(
        [python_executable, "-B", "-c", check_code],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return list(module_to_package.values())
    missing_modules = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return [module_to_package[module] for module in missing_modules]

def ensure_python_requirements() -> None:
    """
    Ensures the vault-level Python dependencies are installed in the active venv.
    This covers launcher/runtime dependencies such as PyYAML, OpenAI SDK, MCP client,
    and python-dotenv. RAG-specific dependencies remain managed by 08-RAG-Engine.
    """
    requirements_path = osPathAbspath(osPathJoin(script_dir, "..", "requirements.txt"))
    if not osPathExists(requirements_path):
        return

    pip_python = get_vault_python()
    missing_packages = _missing_python_packages(pip_python)
    if not missing_packages:
        return

    print("\n📦 Missing Python dependencies detected:")
    for package in missing_packages:
        print(f"   - {package}")
    print("   Installing vault requirements...")

    result = subprocessRun([pip_python, "-m", "pip", "install", "-r", requirements_path])
    if result.returncode != 0:
        print("⚠️ Warning: dependency installation failed. Install manually with:")
        print(f"   {pip_python} -m pip install -r {requirements_path}")

# -----------------------------------------------------------------------------------------------

def setup_mcp(mode_choice: str) -> None:
    """
    DATA FLOW:
    Resolves vault root and configures the MCP filesystem and RAG servers.
    Registers servers in both Gemini and Claude configurations dynamically (AI-agnostic).
    Allows root access to fix 'path not allowed' errors for Ecosystem Map and manuals.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    workspace_root = osPathAbspath(osPathJoin(vault_root, ".."))
    
    # 1. Check if RAG Engine option is available
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "core", "server.py")
    has_rag = osPathExists(rag_dir) and osPathExists(rag_server_script)
    
    obsidian_rag_config = None
    mcp_args = None
    
    if has_rag:
        # Determine the Python virtual environment path dynamically:
        # 1. If local 08-RAG-Engine/.venv exists, use it (contains specific RAG packages).
        # 2. Otherwise, fallback to the central obsidian-brain/.venv.
        local_venv = osPathJoin(rag_dir, ".venv")
        local_python = osPathJoin(local_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(local_venv, "bin", "python3")
        
        if osPathExists(local_python):
            resolved_python = local_python
            print(f"📡 RAG using local 08-RAG-Engine virtual environment: {resolved_python}")
        else:
            parent_venv = osPathJoin(vault_root, ".venv")
            parent_python = osPathJoin(parent_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(parent_venv, "bin", "python3")
            resolved_python = parent_python
            print(f"📡 RAG using central obsidian-brain virtual environment: {resolved_python}")
            
        obsidian_rag_config = {
            "command": resolved_python,
            "args": [rag_server_script],
            "env": {
                "ENGINE_ACTIVE_MODE": str(mode_choice),
                "PYTHONPATH": rag_dir
            }
        }
    else:
        # Fallback to standard basic filesystem MCP server
        # --- Dynamic Context Exclusion Logic (The Firewall) ---
        global_excludes = {
            ".obsidian", ".git", ".gemini", ".claude", ".codex", ".deepseek",
            "node_modules", "99-Humans", "quick-overview"
        }
        mode_excludes_map = {
            "1": {"01-Strategic-Nexus", "04-Rapid-Prototyping", "05-Fleet-Operation"},
            "2": {"01-Strategic-Nexus", "02-Business-BDD", "05-Fleet-Operation", "06-Microservices"},
            "3": {"01-Strategic-Nexus", "02-Business-BDD", "04-Rapid-Prototyping"},
            "4": set()
        }
        
        current_excludes = mode_excludes_map.get(mode_choice, set())
        allowed_dirs = [workspace_root, vault_root]
        
        try:
            for item in osListdir(vault_root):
                if item in global_excludes or item in current_excludes:
                    continue
                item_path = osPathJoin(vault_root, item)
                if osPathIsdir(item_path):
                    allowed_dirs.append(item_path)
        except Exception as e:
            print(f"⚠️ Warning: Could not scan vault_root for exclusions: {e}")
                
        mcp_args = ["-y", "@modelcontextprotocol/server-filesystem"] + allowed_dirs
    
    # 2. Update MCP configs (AI-Agnostic: Gemini and Claude)
    configs_to_update = [
        # (filepath, label)
        (osPathJoin(osPathExpanduser("~/.gemini"), "settings.json"), "Gemini Settings"),
    ]
    if osName != "nt":  # Claude desktop is Mac/Windows, but on Mac we definitely expand it
        configs_to_update.append(
            (osPathJoin(osPathExpanduser("~/Library/Application Support/Claude"), "claude_desktop_config.json"), "Claude Settings")
        )
    else:
        configs_to_update.append(
            (osPathJoin(osPathExpanduser("~/AppData/Roaming/Claude"), "claude_desktop_config.json"), "Claude Settings Windows")
        )
        
    for config_file, label in configs_to_update:
        config_dir = osPathDirname(config_file)
        if not osPathExists(config_dir):
            try:
                osMakedirs(config_dir, exist_ok=True)
            except Exception:
                continue # Skip if directory cannot be created
                
        settings = {}
        if osPathExists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    settings = jsonLoad(f)
            except Exception:
                print(f"⚠️ Warning: Corruption detected in {label}. Starting fresh.")
                
        if "mcpServers" not in settings:
            settings["mcpServers"] = {}
            
        # Clean up old workspace_code_editor name
        settings["mcpServers"].pop("workspace_code_editor", None)
        
        if has_rag:
            # Unified RAG Server: register it, clean up standard filesystem MCP
            settings["mcpServers"]["obsidian_rag"] = obsidian_rag_config
            settings["mcpServers"].pop("obsidian_vault", None)
        else:
            # Fallback standard filesystem server: register it, clean up RAG
            settings["mcpServers"]["obsidian_vault"] = {
                "command": "npx",
                "args": mcp_args
            }
            settings["mcpServers"].pop("obsidian_rag", None)
            
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                jsonDump(settings, f, indent=2)
            print(f"✅ {label} configured successfully.")
        except Exception as e:
            print(f"⚠️ Warning: Could not write {label}: {e}")

# -----------------------------------------------------------------------------------------------

def run_preflight() -> None:
    """
    ESSENTIAL PROCESS:
    Runs the full audit chain to ensure the brain is healthy before session start.
    """
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    
    # Priority paths (07-Core-KMS is the standardized location)
    governance_scripts = ["Preflight-Check.py", "Brain-Health-Audit.py"]
    
    for script_name in governance_scripts:
        standard_path = osPathJoin(script_dir, "../07-Core-KMS/Scripts", script_name)
        legacy_path = osPathJoin(workspace_root, "core-kms-brain", "Scripts", script_name)
        
        target = None
        if osPathExists(standard_path):
            target = standard_path
        elif osPathExists(legacy_path):
            target = legacy_path
            
        if target:
            print(f"📡 Executing Governance Audit: {script_name}...")
            subprocessRun([sysExecutable, target])

def check_session_health(mode_choice: str) -> None:
    """
    Checks if there are uncommitted changes across the entire fleet from a previous session.
    Enforces mode-specific rules for unclosed tasks.
    """
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    inventory_path = osPathJoin(vault_root, "05-Fleet-Operation", "00-Repo-Control", "inventory.json")
    
    repos_to_check = []
    
    # 1. Load fleet repositories from inventory
    if osPathExists(inventory_path):
        try:
            with open(inventory_path, 'r', encoding='utf-8') as f:
                data = jsonLoad(f)
                repositories = data.get("repositories", [])
                for repo in repositories:
                    repo_path_rel = repo.get("path")
                    repo_abs_path = osPathAbspath(osPathJoin(workspace_root, repo_path_rel))
                    if osPathExists(repo_abs_path) and osPathExists(osPathJoin(repo_abs_path, ".git")):
                        repos_to_check.append({
                            "name": repo.get("name"),
                            "path": repo_abs_path,
                            "is_vault": (repo.get("name") == "obsidian-brain" or repo_abs_path == vault_root)
                        })
        except Exception as e:
            print(f"⚠️ Warning: Failed to load inventory.json: {e}")
            
    # Fallback to checking vault if inventory is missing or empty
    if not repos_to_check:
        repos_to_check.append({
            "name": "obsidian-brain",
            "path": vault_root,
            "is_vault": True
        })
        
    dirty_repos_info = []
    EXCLUSIONS = [".git", ".obsidian", ".gemini", ".claude", ".codex", ".deepseek", "Templates", "MODE-MANUAL.md"]
    
    for repo in repos_to_check:
        repo_name = repo["name"]
        repo_path = repo["path"]
        is_vault = repo["is_vault"]
        
        try:
            result = subprocessRun(
                ["git", "status", "--porcelain"], 
                cwd=repo_path, capture_output=True, text=True, check=True
            )
            uncommitted = []
            for line in result.stdout.splitlines():
                if not line.strip():
                    continue
                status_path = line[3:].strip()
                # Apply exclusions for the vault
                if is_vault:
                    if status_path.endswith(".md"):
                        if any(x in status_path for x in EXCLUSIONS):
                            continue
                        uncommitted.append(status_path)
                else:
                    # Sibling repos: any uncommitted change matters
                    if not any(x in status_path for x in EXCLUSIONS):
                        uncommitted.append(status_path)
                        
            if uncommitted:
                dirty_repos_info.append((repo_name, len(uncommitted)))
        except Exception:
            pass # Git not found or repo missing
            
    if dirty_repos_info:
        if mode_choice == "3":
            # Mode 3 - Strict Block
            print("\n" + "🛑"*30)
            print("🛑 CRITICAL GOVERNANCE VIOLATION: UNCLOSED TASK DETECTED")
            print("="*60)
            print("The following repositories have uncommitted changes:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("\nIn Mode 3 (Fleet-Commander), startup is STRICTLY BLOCKED to prevent multi-repository drift.")
            print("Please run 'python3 ./obsidian-brain/20-Scripts/close_mission.py' to verify and sign-off.")
            print("="*60)
            print("🛑"*30 + "\n")
            print("👋 Session should be aborted...")
        
        elif mode_choice == "1":
            # Mode 1 - Big warning with confirmation
            print("\n" + "⚠️"*30)
            print("⚠️  WARNING: UNCLOSED TASK DETECTED")
            print("="*60)
            print("The following repositories have uncommitted changes:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("\nRunning in Mode 1 (Spec-First) with uncommitted changes can lead to state drift and integrity issues.")
            print("It is highly recommended to run 'python3 ./obsidian-brain/20-Scripts/close_mission.py' first.")
            print("="*60)
            print("⚠️"*30 + "\n")
            
            confirm = input("Ignore and start session anyway? [y/N]: ").lower().strip()
            if confirm != 'y':
                print("👋 Session aborted. Please close the previous task first.")
                sysExit(0)
                
        elif mode_choice == "2":
            # Mode 2 - Simple warning
            print("\n💡 NOTE: The following repositories have uncommitted changes from a previous session:")
            for repo_name, count in dirty_repos_info:
                print(f"  - {repo_name} ({count} file(s) dirty)")
            print("")

def regenerate_agents() -> None:
    """
    DATA FLOW:
    Triggers the multi-AI agent converter to ensure prompts are synchronized.
    """
    convert_script = osPathJoin(script_dir, "convert_agents.py")
    if osPathExists(convert_script):
        print("🔄 Synchronizing AI Engine Roles across adapters...")
        subprocessRun([sysExecutable, convert_script])

def unlock_core_kms() -> None:
    """
    Restores write permissions to 07-Core-KMS to allow audits and updates.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    kms_dir = osPathJoin(vault_root, "07-Core-KMS")
    if not osPathExists(kms_dir):
        return
    print("🔓 Restoring write permissions to 07-Core-KMS for audit phase...")
    for root, dirs, files in os.walk(kms_dir):
        for d in dirs:
            dir_path = osPathJoin(root, d)
            try:
                os.chmod(dir_path, 0o755)
            except Exception:
                pass
        for f in files:
            file_path = osPathJoin(root, f)
            try:
                os.chmod(file_path, 0o644)
            except Exception:
                pass

def protect_core_kms() -> None:
    """
    Sets the 07-Core-KMS directory and files to read-only
    at the OS level to protect them against modifications.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    kms_dir = osPathJoin(vault_root, "07-Core-KMS")
    if not osPathExists(kms_dir):
        return
    print("🔒 Enforcing read-only permissions on 07-Core-KMS directory...")
    for root, dirs, files in os.walk(kms_dir):
        for d in dirs:
            dir_path = osPathJoin(root, d)
            try:
                os.chmod(dir_path, 0o555)
            except Exception:
                pass
        for f in files:
            file_path = osPathJoin(root, f)
            try:
                os.chmod(file_path, 0o444)
            except Exception:
                pass

def check_rag_attached() -> bool:
    """Returns True if the 08-RAG-Engine and its server.py exist."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    rag_server_script = osPathJoin(rag_dir, "src", "core", "server.py")
    return osPathExists(rag_dir) and osPathExists(rag_server_script)

def reset_rag_index() -> None:
    """
    DATA FLOW:
    Resolves the RAG virtual environment python executable and runs main.py index --reset.
    """
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    rag_dir = osPathJoin(vault_root, "08-RAG-Engine")
    rag_main_script = osPathJoin(rag_dir, "main.py")
    
    if not osPathExists(rag_main_script):
        print("❌ Error: 08-RAG-Engine/main.py not found. Cannot reset RAG index.")
        return
        
    local_venv = osPathJoin(rag_dir, ".venv")
    local_python = osPathJoin(local_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(local_venv, "bin", "python3")
    
    if osPathExists(local_python):
        resolved_python = local_python
    else:
        parent_venv = osPathJoin(vault_root, ".venv")
        parent_python = osPathJoin(parent_venv, "Scripts", "python.exe") if osName == "nt" else osPathJoin(parent_venv, "bin", "python3")
        resolved_python = parent_python
        
    if resolved_python and osPathExists(resolved_python):
        print(f"🗑️  Resetting RAG database via {resolved_python} {rag_main_script} index --reset...")
        indexer_env = os.environ.copy()
        indexer_env["PYTHONPATH"] = rag_dir
        indexer_env["ANONYMIZED_TELEMETRY"] = "False"
        indexer_env["CHROMA_TELEMETRY"] = "False"
        indexer_env["HF_HUB_OFFLINE"] = "1"
        indexer_env["TRANSFORMERS_OFFLINE"] = "1"
        subprocessRun([resolved_python, rag_main_script, "index", "--reset"], env=indexer_env)
    else:
        print("❌ Error: Python executable not found for RAG Engine.")

def get_available_agents(active_cli: str) -> list:
    """Reads available agents from the respective agent directory."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    return list_agents(vault_root, active_cli)

def get_active_client_name() -> str:
    """Resolve the active AI client from MODE-MANUAL.md or environment overrides."""
    clients = client_names()
    active_client = DEFAULT_CLIENT

    mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
    if osPathExists(mode_file):
        try:
            with open(mode_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith("active_cli:") or line.strip().startswith("active_client:"):
                        candidate = normalize_client(
                            line.split(":", 1)[1].strip().lower().replace("'", "").replace('"', '')
                        )
                        if candidate in clients:
                            active_client = candidate
                            break
        except Exception:
            pass

    for env_name in ("ACTIVE_CLIENT", "ACTIVE_CLI"):
        env_override = normalize_client(osGetenv(env_name, ""))
        if env_override in clients:
            active_client = env_override
            break

    return active_client

def run_client_with_fallback(active_client: str, agent_choice: str, mode_choice: str) -> None:
    """Launch the selected AI client, then fall back to other available clients if needed."""
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    launch_order = [active_client] + [name for name in client_names() if name != active_client]
    cmd_prefix = [] if osName != 'nt' else ["cmd", "/c"]

    for client_name in launch_order:
        config = get_client_config(client_name)
        if not config:
            continue

        if client_name != active_client and not is_client_available(client_name, vault_root):
            continue

        fallback_agents = get_available_agents(client_name)
        selected_agent = agent_choice if agent_choice and agent_choice in fallback_agents else ""

        try:
            cli_cmd = build_launch_command(
                client_name,
                selected_agent,
                squad_mode=mode_choice,
                vault_root=vault_root,
                python_executable=get_vault_python(),
            )
        except ValueError as e:
            print(f"⚠️ Warning: {e}")
            continue

        if client_name != active_client:
            print(f"⚠️ Warning: {active_client} unavailable. Trying fallback client: {client_name}")

        subprocessRun(cmd_prefix + cli_cmd)
        return

    raise FileNotFoundError(f"No available AI client found. Tried: {', '.join(launch_order)}")

# -----------------------------------------------------------------------------------------------

def start_engine() -> None:
    """
    FUNCTIONAL ANALYSE:
    Implements the Master Lifecycle Loop. This allows the user to re-launch
    the engine or switch modes without manually restarting the script.
    """
    while True:
        print("\n" + "="*60)
        print("🧠 BASTIEN-ANTIGRAVITY: AI ENGINE COMMAND")
        print("="*60)

        # 1. Verification & Sync
        ensure_python_requirements()
        unlock_core_kms()
        run_preflight()
        regenerate_agents()
        protect_core_kms()

        # 2. Mode Management
        has_rag = check_rag_attached()
        while True:
            print("\n--- 🕹️ Bastien-Antigravity: Mode Selector ---")
            for key, (name, desc) in MODES.items():
                print(f"[{key}] {name.ljust(18)} : {desc}")
            if has_rag:
                print(f"[r] {'🗑️  Reset RAG'.ljust(18)} : Reset and rebuild ChromaDB RAG index.")
            print(f"[p] {'🎭 Extract Personas'.ljust(18)} : Extract polyglot codebase context in background.")
            
            choice = input("\nSelect new active mode [1-4] or action (Enter to skip): ").strip().lower()
            if choice == 'r' and has_rag:
                reset_rag_index()
                continue
            elif choice == 'p':
                persona_extractor_script = osPathJoin(script_dir, "persona_extractor.py")
                lock_path = osPathAbspath(osPathJoin(script_dir, "..", "07-Core-KMS", "quick-overview", "ast-patterns", ".persona_running"))
                if osPathExists(lock_path):
                    print("⚠️ Persona Extractor is already running. Please wait.")
                elif osPathExists(persona_extractor_script):
                    try:
                        from subprocess import Popen as subProcessPopen, DEVNULL as subProcessDEVNULL
                        subProcessPopen(
                            [sysExecutable, persona_extractor_script, "--daemon"],
                            stdout=subProcessDEVNULL,
                            stderr=subProcessDEVNULL
                        )
                        print("✅ Persona Extractor started in background. It will notify when ready.")
                    except Exception as e:
                        print(f"⚠️ Warning: Could not spawn Persona Extractor: {e}")
                continue
            break

        if choice in MODES:
            apply_mode_protocol(choice)
        else:
            # Re-read current mode if skip
            choice = "4"
            mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
            if osPathExists(mode_file):
                with open(mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith("active_mode:"):
                            choice = line.split(":")[1].strip()
                            break
        
        # 3. Protocol Enforcement
        check_session_health(choice)
        setup_mcp(choice)
        
        # 4. Display Guidance
        helper = MissionHelper()
        helper.print_cheat_sheet()
        
        # 5. AI Client Execution
        active_cli = get_active_client_name()
        active_config = get_client_config(active_cli) or {}
        active_label = active_config.get("label", active_cli)
        
        # Select Agent Persona dynamically
        available_agents = get_available_agents(active_cli)
        agent_choice = ""
        
        # Universal entry point: Orchestrator
        if "orchestrator" in available_agents:
            agent_choice = "orchestrator"
            print(f"\n🎭 Mode {choice} active: Routing via Orchestrator (Universal Gateway).")
        elif available_agents:
            print("\n🎭 Orchestrator persona not found. Available Agent Personas:")
            for idx, agent in enumerate(sorted(available_agents), 1):
                print(f"[{idx}] {agent}")
            print("[0] Generic (Default Session)")
            
            try:
                agent_input = input(f"\nSelect Agent Persona [0-{len(available_agents)}] (Enter for Default): ").strip()
                if agent_input.isdigit():
                    val = int(agent_input)
                    if 1 <= val <= len(available_agents):
                        agent_choice = sorted(available_agents)[val - 1]
            except (KeyboardInterrupt, EOFError):
                pass
        
        if agent_choice:
            print(f"\n🚀 Firing up {active_label} [Protocol: {choice} | Agent: {agent_choice}]...")
        else:
            print(f"\n🚀 Firing up {active_label} [Protocol: {choice} | Agent: Generic]...")
            
        try:
            run_client_with_fallback(active_cli, agent_choice, choice)
        except FileNotFoundError:
            print("❌ No supported AI client is available. Install Gemini, Claude, Codex, or configure DeepSeek.")
        except Exception as e:
            print(f"❌ CLI Execution Error: {e}")
            break
            
        # Check if Persona Extraction is ready
        persona_flag_path = osPathAbspath(osPathJoin(script_dir, "..", "07-Core-KMS", "quick-overview", "ast-patterns", ".persona_ready"))
        if osPathExists(persona_flag_path):
            print("\n" + "✨" * 30)
            print("🚀 NEW PERSONA CONTEXT EXTRACTED AND READY FOR RAG !!")
            print("✨" * 30 + "\a")
            try:
                from os import remove as osRemove
                osRemove(persona_flag_path)
            except Exception:
                pass

        # 6. Lifecycle Decision
        print("\n--- 🏁 Session Paused ---")
        
        has_rag = check_rag_attached()
        prompt_suffix = " / r: Reset RAG" if has_rag else ""
        decision = input(f"Re-launch Engine? [y: Yes / n: Exit & Sign-off / s: Switch Mode{prompt_suffix}]: ").lower().strip()
        
        if decision == 'r' and has_rag:
            reset_rag_index()
            continue
        elif decision == 's' or decision == 'y':
            continue
        else:
            print("\n📡 Initiating Session Sign-off Protocol...")
            signoff_script = osPathJoin(script_dir, "close_mission.py")
            cancelled_exit = False
            if osPathExists(signoff_script):
                while True:
                    result = subprocessRun([sysExecutable, signoff_script])
                    if result.returncode != 0:
                        print("\n🛑 SESSION SIGN-OFF BLOCKED DUE TO GOVERNANCE VIOLATIONS.")
                        print("Options:")
                        print("  [r] Retry: Run sign-off again.")
                        print("  [i] Force ignore: Exit anyway, bypassing violations.")
                        print("  [c] Cancel exit: Return to the main command loop menu.")
                        user_choice = input("Choice: ").strip().lower()
                        if user_choice == 'r':
                            continue
                        elif user_choice == 'i':
                            print("⚠️ Bypassing governance violations. Exiting.")
                            break
                        elif user_choice == 'c':
                            print("Returning to main menu.")
                            cancelled_exit = True
                            break
                        else:
                            print("Invalid option. Retrying sign-off by default.")
                            continue
                    else:
                        break
            if cancelled_exit:
                continue
            print("👋 Engine resting. Task concluded.")
            break

# -----------------------------------------------------------------------------------------------

def get_settings_paths():
    paths = [osPathJoin(osPathExpanduser("~/.gemini"), "settings.json")]
    if osName != "nt":
        paths.append(osPathJoin(osPathExpanduser("~/Library/Application Support/Claude"), "claude_desktop_config.json"))
    else:
        paths.append(osPathJoin(osPathExpanduser("~/AppData/Roaming/Claude"), "claude_desktop_config.json"))
    return paths

def backup_settings():
    for path in get_settings_paths():
        if osPathExists(path):
            try:
                import shutil
                shutil.copy2(path, path + ".bak")
                print(f"📦 Created backup of {osPathBasename(path)}")
            except Exception as e:
                print(f"⚠️ Warning: Could not backup {path}: {e}")

def restore_settings():
    for path in get_settings_paths():
        bak_path = path + ".bak"
        if osPathExists(bak_path):
            try:
                import shutil
                shutil.move(bak_path, path)
                print(f"📦 Restored original {osPathBasename(path)} from backup")
            except Exception as e:
                print(f"⚠️ Warning: Could not restore {path}: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bastien-Antigravity AI Engine Command Center")
    parser.add_argument("--reset-rag", action="store_true", help="Reset and rebuild the ChromaDB RAG index before starting.")
    args, unknown = parser.parse_known_args()

    if args.reset_rag:
        if check_rag_attached():
            reset_rag_index()
        else:
            print("⚠️ Warning: --reset-rag was ignored because 08-RAG-Engine is not attached.")

    backup_settings()
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
    finally:
        restore_settings()
        sysExit(0)
