#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
DeepSeek API client adapter for the Bastien-Antigravity ecosystem.
Provides two operating modes:
  Mode 1 (Passthrough): Launches the standard CLI binary.
  Mode 2 (DeepSeek SDK): Interactive chat powered by DeepSeek API via OpenAI SDK,
                         with MCP tool calling against the 08-RAG-Engine.

DATA FLOW:
1. Input: User selects mode and optional agent persona.
2. Logic: Mode 1 delegates to subprocess CLI. Mode 2 runs an agentic loop:
   User → DeepSeek API (chat.completions with tools) → MCP tool calls → DeepSeek → User.
3. Output: Interactive terminal chat session.

KEY PARAMETERS:
- DEEPSEEK_API_KEY: Required for Mode 2. Prefer setting it in the shell environment.
- DEEPSEEK_MODEL: Optional override (default: deepseek-chat).
- DEEPSEEK_BASE_URL or DEEPSEEK_API_BASE_URL: Optional API endpoint override.
- agent: Optional agent persona name loaded from .deepseek/agents/.
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

import asyncio
import json
import argparse
from os.path import (
    abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname,
    exists as osPathExists, basename as osPathBasename
)
from subprocess import run as subprocessRun

# Standardize terminal output encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# ———————————————————————————————————————————————————————————————————————————————
# CONSTANTS
# ———————————————————————————————————————————————————————————————————————————————

API_DIR = osPathDirname(osPathAbspath(__file__))
CLIENTS_DIR = osPathAbspath(osPathJoin(API_DIR, ".."))
SCRIPT_DIR = osPathAbspath(osPathJoin(CLIENTS_DIR, ".."))
VAULT_ROOT = osPathAbspath(osPathJoin(SCRIPT_DIR, ".."))
WORKSPACE_ROOT = osPathAbspath(osPathJoin(VAULT_ROOT, ".."))

RAG_DIR = osPathJoin(VAULT_ROOT, "08-RAG-Engine")
RAG_SERVER_SCRIPT = osPathJoin(RAG_DIR, "src", "core", "server.py")

DEFAULT_MODEL = "deepseek-chat"
DEFAULT_API_BASE_URL = "https://api.deepseek.com"

# Terminal colors
C_RESET = "\033[0m"
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_DIM = "\033[2m"
C_BOLD = "\033[1m"

# ———————————————————————————————————————————————————————————————————————————————
# MODE 1: PASSTHROUGH (Standard CLI)
# ———————————————————————————————————————————————————————————————————————————————

def run_passthrough(agent: str = "") -> None:
    """Launches the default CLI binary (gemini) with optional agent persona."""
    clis = ["gemini", "claude", "codex"]
    cli_cmd = [clis[0]]
    if agent:
        cli_cmd.append(agent)

    print(f"🚀 Mode 1 — Passthrough: Launching {cli_cmd[0]}...")

    for cli in clis:
        try:
            cmd_prefix = [] if os.name != 'nt' else ["cmd", "/c"]
            cli_cmd[0] = cli
            subprocessRun(cmd_prefix + cli_cmd)
            return
        except FileNotFoundError:
            continue

    print("❌ No CLI binary found (gemini, claude, codex). Install one or use Mode 2.")

# ———————————————————————————————————————————————————————————————————————————————
# MODE 2: DEEPSEEK SDK (OpenAI-compatible)
# ———————————————————————————————————————————————————————————————————————————————

def _load_env() -> None:
    """
    Load optional .env files without overriding shell variables.

    Preferred configuration is through the user's shell environment:
      export DEEPSEEK_API_KEY="..."
      export DEEPSEEK_BASE_URL="https://api.deepseek.com"
      export DEEPSEEK_MODEL="deepseek-chat"

    .env files are only a local fallback for development machines.
    """
    try:
        from dotenv import load_dotenv
        for env_path in [osPathJoin(VAULT_ROOT, ".env"), osPathJoin(RAG_DIR, ".env")]:
            if osPathExists(env_path):
                load_dotenv(env_path, override=False)
                break
    except ImportError:
        pass

# ———————————————————————————————————————————————————————————————————————————————

def _load_agent_prompt(agent_name: str) -> str:
    """Load agent persona markdown as system prompt."""
    if not agent_name:
        return "You are a helpful AI assistant for the Bastien-Antigravity ecosystem."

    # Try the native DeepSeek persona first, then compatible generated adapters.
    for adapter_dir in [".deepseek", ".gemini", ".claude", ".codex"]:
        agent_file = osPathJoin(VAULT_ROOT, adapter_dir, "agents", f"{agent_name}.md")
        if osPathExists(agent_file):
            try:
                with open(agent_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Strip YAML frontmatter if present
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        content = parts[2].strip()
                print(f"🎭 Loaded agent persona: {agent_name} (from {adapter_dir})")
                return content
            except Exception as e:
                print(f"⚠️ Warning: Could not load agent {agent_name}: {e}")

    print(f"⚠️ Agent '{agent_name}' not found. Using generic persona.")
    return "You are a helpful AI assistant for the Bastien-Antigravity ecosystem."

# ———————————————————————————————————————————————————————————————————————————————

def _resolve_active_repo_dir() -> str:
    """Dynamically determine the active target project folder based on current working directory."""
    cwd = osPathAbspath(os.getcwd())
    inventory_path = osPathJoin(VAULT_ROOT, "05-Fleet-Operation", "00-Repo-Control", "inventory.json")
    default_repo = osPathJoin(WORKSPACE_ROOT, "obsidian-brain")
    if not osPathExists(inventory_path):
        return default_repo
    try:
        with open(inventory_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        repos = data.get("repositories", [])
        best_match = None
        best_len = -1
        for r in repos:
            repo_path = osPathAbspath(osPathJoin(WORKSPACE_ROOT, r.get("path", "")))
            if cwd == repo_path or cwd.startswith(repo_path + os.sep) or cwd.startswith(repo_path + "/"):
                if len(repo_path) > best_len:
                    best_match = repo_path
                    best_len = len(repo_path)
        if best_match:
            return best_match
    except Exception as e:
        print(f"⚠️ Warning: Error resolving active repository directory: {e}")
    return default_repo

def _load_governance_context(active_repo_dir: str) -> str:
    """Loads global and local project governance context files for pre-injection."""
    lines = []
    lines.append("=== GOVERNANCE & ACTIVE REPOSITORY CONTEXT ===")
    lines.append(f"Active Target Repository: {active_repo_dir}")
    
    # 1. Global context
    global_files = [
        ("Global Ecosystem Map MOC", osPathJoin(WORKSPACE_ROOT, "obsidian-brain", "Ecosystem-Map-MOC.md")),
        ("Global AI Session State", osPathJoin(WORKSPACE_ROOT, "obsidian-brain", "00-AI-Orchestration", "AI-Session-State.md"))
    ]
    for label, path in global_files:
        if osPathExists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                lines.append(f"\n--- GLOBAL FILE: {label} ({osPathBasename(path)}) ---")
                lines.append(content)
            except Exception as e:
                lines.append(f"⚠️ Warning: Error reading global context {path}: {e}")
                
    # 2. Local Project Specific
    local_files = [
        ("AI Project DNA", osPathJoin(active_repo_dir, "AI-Project-DNA.md")),
        ("Local AI Session State", osPathJoin(active_repo_dir, "AI-Session-State.md")),
        ("AI Init Instructions", osPathJoin(active_repo_dir, "AI-Init.md"))
    ]
    for label, path in local_files:
        if osPathExists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                lines.append(f"\n--- LOCAL PROJECT FILE: {label} ({osPathBasename(path)}) ---")
                lines.append(content)
            except Exception as e:
                lines.append(f"⚠️ Warning: Error reading local context {path}: {e}")
                
    lines.append("==============================================")
    return "\n".join(lines)

def _build_system_prompt(agent_prompt: str, agent_name: str, mode_choice: str) -> str:
    """Wrap the selected squad persona with DeepSeek/RAG operating context."""
    agent_label = agent_name or "generic"
    active_repo = _resolve_active_repo_dir()
    gov_context = _load_governance_context(active_repo)
    
    return f"""You are running as the DeepSeek API client adapter for the Bastien-Antigravity AI Squad.

Active squad mode: {mode_choice}
Selected persona: {agent_label}
Workspace root: {WORKSPACE_ROOT}
Vault root: {VAULT_ROOT}
Active repository: {active_repo}

Operational rules:
- Use the available MCP/RAG tools for vault and workspace context instead of guessing.
- Prefer `query_brain` for architectural, governance, BDD, and project-memory questions.
- Use `read_workspace_file`, `list_workspace_directory`, `write_workspace_file`, or `append_workspace_file` only when needed and respect tool errors from the access matrix.
- Preserve the selected persona's SCAN and session-state instructions.
- Never expose API keys, environment secrets, or local credential contents.

{gov_context}

Selected squad persona follows:

{agent_prompt}
"""

# ———————————————————————————————————————————————————————————————————————————————

def _get_api_base_url() -> str:
    """Resolve the DeepSeek OpenAI-compatible endpoint from shell env or default."""
    return (
        os.getenv("DEEPSEEK_BASE_URL")
        or os.getenv("DEEPSEEK_API_BASE_URL")
        or DEFAULT_API_BASE_URL
    ).rstrip("/")

# ———————————————————————————————————————————————————————————————————————————————

def _mcp_tool_to_openai(mcp_tool) -> dict:
    """Convert an MCP tool definition to OpenAI function-calling schema."""
    return {
        "type": "function",
        "function": {
            "name": mcp_tool.name,
            "description": mcp_tool.description or "",
            "parameters": mcp_tool.inputSchema if mcp_tool.inputSchema else {"type": "object", "properties": {}}
        }
    }

# ———————————————————————————————————————————————————————————————————————————————

def _resolve_rag_python() -> str:
    """Resolve the Python executable for the RAG engine (local or central venv)."""
    local_venv_python = osPathJoin(RAG_DIR, ".venv", "bin", "python3")
    if os.name == "nt":
        local_venv_python = osPathJoin(RAG_DIR, ".venv", "Scripts", "python.exe")

    if osPathExists(local_venv_python):
        return local_venv_python

    central_venv_python = osPathJoin(VAULT_ROOT, ".venv", "bin", "python3")
    if os.name == "nt":
        central_venv_python = osPathJoin(VAULT_ROOT, ".venv", "Scripts", "python.exe")

    if osPathExists(central_venv_python):
        return central_venv_python

    return sys.executable

# ———————————————————————————————————————————————————————————————————————————————

async def run_deepseek_session(agent: str = "", mode_choice: str = "4") -> None:
    """
    ESSENTIAL PROCESS:
    Runs the interactive DeepSeek chat session with MCP tool calling.
    Connects to the RAG MCP server via stdio, converts tool schemas,
    and loops: user input → DeepSeek API → tool calls → response.
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ openai package not installed. Run: pip install openai")
        return

    try:
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client
    except ImportError:
        print("❌ mcp package not installed. Run: pip install mcp")
        return

    # Load environment
    _load_env()
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    if not api_key:
        print("❌ DEEPSEEK_API_KEY not set.")
        print("Preferred setup:")
        print("  export DEEPSEEK_API_KEY=\"sk-...\"")
        print("Optional overrides:")
        print("  export DEEPSEEK_BASE_URL=\"https://api.deepseek.com\"")
        print("  export DEEPSEEK_MODEL=\"deepseek-chat\"")
        return

    model = os.getenv("DEEPSEEK_MODEL", DEFAULT_MODEL)
    api_base_url = _get_api_base_url()
    system_prompt = _build_system_prompt(_load_agent_prompt(agent), agent, mode_choice)

    # Initialize DeepSeek client (OpenAI-compatible)
    client = OpenAI(api_key=api_key, base_url=api_base_url)

    # Check if RAG server is available
    has_rag = osPathExists(RAG_DIR) and osPathExists(RAG_SERVER_SCRIPT)
    if not has_rag:
        print("⚠️ RAG Engine not found. Running without MCP tools.")
        await _chat_loop(client, model, system_prompt, tools=[], mcp_session=None)
        return

    # Connect to RAG MCP Server via stdio
    rag_python = _resolve_rag_python()
    print(f"📡 Connecting to RAG MCP Server via {osPathBasename(rag_python)}...")

    server_params = StdioServerParameters(
        command=rag_python,
        args=[RAG_SERVER_SCRIPT],
        env={
            **os.environ,
            "BRAIN_DIR": WORKSPACE_ROOT,
            "SQUAD_ACTIVE_MODE": str(mode_choice),
            "SQUAD_ACTIVE_CLIENT": "deepseek",
            "PYTHONPATH": (
                RAG_DIR
                if not os.environ.get("PYTHONPATH")
                else RAG_DIR + os.pathsep + os.environ["PYTHONPATH"]
            ),
            "ANONYMIZED_TELEMETRY": "False",
            "CHROMA_TELEMETRY": "False",
            "HF_HUB_OFFLINE": "1",
            "TRANSFORMERS_OFFLINE": "1",
        }
    )

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                # Discover MCP tools
                tools_result = await session.list_tools()
                mcp_tools = tools_result.tools if tools_result.tools else []
                openai_tools = [_mcp_tool_to_openai(t) for t in mcp_tools]

                tool_names = [t.name for t in mcp_tools]
                print(f"✅ MCP connected — {len(mcp_tools)} tools: {', '.join(tool_names)}")

                await _chat_loop(client, model, system_prompt, openai_tools, session)

    except Exception as e:
        print(f"❌ MCP connection error: {e}")
        print("⚠️ Falling back to chat without tools...")
        await _chat_loop(client, model, system_prompt, tools=[], mcp_session=None)

# ———————————————————————————————————————————————————————————————————————————————

async def _chat_loop(client, model: str, system_prompt: str, tools: list, mcp_session) -> None:
    """
    DATA FLOW:
    Interactive agentic loop: reads user input, sends to DeepSeek with tools,
    executes any tool_calls via MCP, feeds results back, streams final response.
    """
    messages = [{"role": "system", "content": system_prompt}]

    print(f"\n{'='*60}")
    print(f"🧠 {C_BOLD}DEEPSEEK AGENT SESSION{C_RESET}")
    print(f"   Model: {C_CYAN}{model}{C_RESET}")
    print(f"   API: {C_CYAN}{_get_api_base_url()}{C_RESET}")
    print(f"   Tools: {C_CYAN}{len(tools)}{C_RESET} MCP tools loaded")
    print(f"   Type {C_YELLOW}/quit{C_RESET} to exit, {C_YELLOW}/clear{C_RESET} to reset context")
    print(f"{'='*60}\n")

    while True:
        # Read user input
        try:
            user_input = input(f"{C_GREEN}You ▸ {C_RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C_DIM}👋 Session ended.{C_RESET}")
            break

        if not user_input:
            continue
        if user_input.lower() in ("/quit", "/exit", "/q"):
            print(f"{C_DIM}👋 Session ended.{C_RESET}")
            break
        if user_input.lower() == "/clear":
            messages = [{"role": "system", "content": system_prompt}]
            print(f"{C_DIM}🗑️  Context cleared.{C_RESET}\n")
            continue

        messages.append({"role": "user", "content": user_input})

        # Agentic loop: call DeepSeek, execute tools, repeat until text response
        try:
            while True:
                # Call DeepSeek API
                api_kwargs = {
                    "model": model,
                    "messages": messages,
                    "stream": False,
                }
                if tools:
                    api_kwargs["tools"] = tools

                response = client.chat.completions.create(**api_kwargs)
                choice = response.choices[0]
                assistant_msg = choice.message

                # Check for tool calls
                if assistant_msg.tool_calls:
                    # Add assistant message (with tool_calls) to history
                    messages.append(assistant_msg.model_dump())

                    for tool_call in assistant_msg.tool_calls:
                        fn_name = tool_call.function.name
                        try:
                            fn_args = json.loads(tool_call.function.arguments) if tool_call.function.arguments else {}
                        except json.JSONDecodeError as e:
                            fn_args = {}
                            print(f"  {C_RED}❌ Invalid tool arguments for {fn_name}: {e}{C_RESET}")

                        print(f"  {C_YELLOW}🧰 Calling: {fn_name}({json.dumps(fn_args, ensure_ascii=False)[:120]}){C_RESET}")

                        # Execute via MCP
                        if mcp_session:
                            try:
                                result = await mcp_session.call_tool(fn_name, fn_args)
                                tool_output = ""
                                if result.content:
                                    for block in result.content:
                                        if hasattr(block, "text"):
                                            tool_output += block.text
                                        else:
                                            tool_output += str(block)
                            except Exception as e:
                                tool_output = f"Error calling tool '{fn_name}': {e}"
                                print(f"  {C_RED}❌ Tool error: {e}{C_RESET}")
                        else:
                            tool_output = f"Error: MCP session not available. Tool '{fn_name}' cannot be executed."

                        # Truncate long outputs for display
                        display_output = tool_output[:200] + "..." if len(tool_output) > 200 else tool_output
                        print(f"  {C_DIM}   ↳ {display_output}{C_RESET}")

                        # Add tool result to messages
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": tool_output
                        })

                    # Continue the loop — DeepSeek will process tool results
                    continue

                else:
                    # No tool calls — this is the final text response
                    content = assistant_msg.content or ""
                    messages.append({"role": "assistant", "content": content})
                    print(f"\n{C_CYAN}🤖 DeepSeek ▸{C_RESET} {content}\n")
                    break

        except Exception as e:
            print(f"{C_RED}❌ API Error: {e}{C_RESET}\n")
            # Remove the failed user message to keep history clean
            if messages and messages[-1]["role"] == "user":
                messages.pop()

# ———————————————————————————————————————————————————————————————————————————————
# MAIN ENTRY POINT
# ———————————————————————————————————————————————————————————————————————————————

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Bastien-Antigravity DeepSeek API Client Adapter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  1  Passthrough — Launch standard CLI binary (gemini/claude/codex)
  2  DeepSeek SDK — Interactive chat via DeepSeek API + MCP tools

Examples:
  export DEEPSEEK_API_KEY="sk-..."
  export DEEPSEEK_BASE_URL="https://api.deepseek.com"   # optional
  export DEEPSEEK_MODEL="deepseek-chat"                 # optional

  python3 20-Scripts/clients/API/deepseek_client.py
  python3 20-Scripts/clients/API/deepseek_client.py --mode 2
  python3 20-Scripts/clients/API/deepseek_client.py --mode 2 developer
  python3 20-Scripts/clients/API/deepseek_client.py --mode 1 oracle
        """
    )
    parser.add_argument("agent", nargs="?", default="", help="Agent persona name (e.g. developer, architect, oracle)")
    parser.add_argument("--mode", "-m", type=int, choices=[1, 2], help="Operating mode: 1=Passthrough, 2=DeepSeek SDK")
    parser.add_argument("--squad-mode", "-s", type=str, default="4", help="Squad active mode for MCP (default: 4)")
    args = parser.parse_args()

    mode = args.mode
    if mode is None:
        # Interactive mode selector
        print(f"\n{'='*50}")
        print(f"🧠 {C_BOLD}BASTIEN-ANTIGRAVITY: DeepSeek API Client{C_RESET}")
        print(f"{'='*50}")
        print(f"  [{C_CYAN}1{C_RESET}] Passthrough  — Launch standard CLI (gemini/claude)")
        print(f"  [{C_CYAN}2{C_RESET}] DeepSeek SDK — Chat via DeepSeek API + MCP tools")
        print()

        try:
            choice = input("Select mode [1/2]: ").strip()
            if choice == "1":
                mode = 1
            elif choice == "2":
                mode = 2
            else:
                print("Invalid choice. Defaulting to Mode 2 (DeepSeek SDK).")
                mode = 2
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Exiting.")
            return

    if mode == 1:
        run_passthrough(args.agent)
    elif mode == 2:
        asyncio.run(run_deepseek_session(args.agent, args.squad_mode))

# ———————————————————————————————————————————————————————————————————————————————

if __name__ == "__main__":
    main()
