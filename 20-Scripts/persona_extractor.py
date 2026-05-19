#!/usr/bin/env python3
# coding:utf-8
"""
Polyglot Persona Extractor
Extracts codebase patterns for Python (via AST), Go (via Regex), and Rust (via Regex)
to build RAG context for AI Personas.
"""
import os
import ast
import re
import collections
import argparse
import datetime
import sys

# --- PYTHON EXTRACTOR (AST) ---
class PythonExtractor(ast.NodeVisitor):
    def __init__(self):
        self.imports = collections.Counter()
        self.exceptions_caught = collections.Counter()
        self.logging_calls = collections.Counter()
        self.class_names = []
        self.func_names = []
        self.async_funcs = 0

    def visit_Import(self, node):
        for alias in node.names:
            self.imports[alias.name] += 1
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.imports[node.module] += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.class_names.append(node.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.func_names.append(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.async_funcs += 1
        self.func_names.append(node.name)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.type:
            names = self._get_exception_names(node.type)
            for name in names:
                self.exceptions_caught[name] += 1
        self.generic_visit(node)

    def _get_exception_names(self, node):
        if isinstance(node, ast.Name):
            return [node.id]
        elif isinstance(node, ast.Attribute):
            val = getattr(node.value, 'id', '')
            if val:
                return [f"{val}.{node.attr}"]
            return [node.attr]
        elif isinstance(node, ast.Tuple):
            res = []
            for elt in node.elts:
                res.extend(self._get_exception_names(elt))
            return res
        return []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id in ('log', 'logger', 'logging'):
                self.logging_calls[node.func.attr] += 1
            elif isinstance(node.func.value, ast.Attribute) and getattr(node.func.value, 'attr', None) in ('logger', 'log'):
                self.logging_calls[node.func.attr] += 1
        self.generic_visit(node)

# --- GO EXTRACTOR (REGEX) ---
class GoExtractor:
    def __init__(self):
        self.interfaces = collections.Counter()
        self.structs = collections.Counter()
        self.goroutines = 0
        self.panics = 0
        self.error_checks = 0

    def parse(self, content):
        # type Name interface
        for match in re.finditer(r'type\s+([A-Z]\w*)\s+interface', content):
            self.interfaces[match.group(1)] += 1
        # type Name struct
        for match in re.finditer(r'type\s+([A-Z]\w*)\s+struct', content):
            self.structs[match.group(1)] += 1
        # go func
        self.goroutines += len(re.findall(r'go\s+func', content))
        # panic(
        self.panics += len(re.findall(r'panic\(', content))
        # if err != nil
        self.error_checks += len(re.findall(r'if\s+err\s*!=\s*nil', content))

# --- RUST EXTRACTOR (REGEX) ---
class RustExtractor:
    def __init__(self):
        self.traits = collections.Counter()
        self.structs = collections.Counter()
        self.unwraps = 0
        self.matches = 0

    def parse(self, content):
        for match in re.finditer(r'(?:pub(?:\([^)]+\))?\s+)?trait\s+([A-Z]\w*)', content):
            self.traits[match.group(1)] += 1
        for match in re.finditer(r'(?:pub(?:\([^)]+\))?\s+)?struct\s+([A-Z]\w*)', content):
            self.structs[match.group(1)] += 1
        self.unwraps += len(re.findall(r'\.unwrap\(\)', content))
        self.matches += len(re.findall(r'match\s+', content))

def extract_personas(repo_path, output_dir, is_daemon):
    lock_path = os.path.join(output_dir, ".persona_running")
    os.makedirs(output_dir, exist_ok=True)
    if os.path.exists(lock_path):
        if not is_daemon:
            print("❌ Persona Extractor is already running in the background.")
        sys.exit(1)
        
    with open(lock_path, 'w', encoding='utf-8') as f:
        f.write(str(os.getpid()))

    py_ext = PythonExtractor()
    go_ext = GoExtractor()
    rs_ext = RustExtractor()
    
    for root, dirs, files in os.walk(repo_path):
        # Prune directories in-place to prevent traversing massive technical folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('venv', '.venv', '__pycache__', 'node_modules', 'target', 'dist', 'build', 'vendor')]
            
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # Skip large files (e.g. log files or datasets accidentally named code extensions)
                if os.path.getsize(filepath) > 1024 * 1024:
                    continue
                if file.endswith('.py'):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        tree = ast.parse(f.read(), filename=filepath)
                        py_ext.visit(tree)
                elif file.endswith('.go'):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        go_ext.parse(f.read())
                elif file.endswith('.rs'):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        rs_ext.parse(f.read())
            except Exception:
                pass

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Generate Python Persona
    py_content = [
        f"# 🐍 Python Persona RAG Context",
        f"*Generated: {datetime.datetime.now().isoformat()}*",
        f"## ⚙️ Architecture Trends",
        f"- **Async Adoptions**: {py_ext.async_funcs} asynchronous functions defined.",
        f"## 🔥 Core Dependencies (Top 10)",
        "\n".join([f"- `{imp}` ({c} times)" for imp, c in py_ext.imports.most_common(10)]),
        f"## 🛡️ Error Handling (Top 10)",
        "\n".join([f"- `except {exc}:` ({c} times)" for exc, c in py_ext.exceptions_caught.most_common(10)]),
        f"## 📝 Logging Culture (Top 10)",
        "\n".join([f"- `logger.{meth}()` ({c} times)" for meth, c in py_ext.logging_calls.most_common(10)])
    ]
    with open(os.path.join(output_dir, f"persona_python_{timestamp}.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(py_content))

    # Generate Go Persona
    go_content = [
        f"# 🐹 Go Persona RAG Context",
        f"*Generated: {datetime.datetime.now().isoformat()}*",
        f"## ⚙️ Architecture Trends",
        f"- **Standard Error Checks (`if err != nil`)**: {go_ext.error_checks}",
        f"- **Panics**: {go_ext.panics}",
        f"- **Goroutines (`go func`)**: {go_ext.goroutines}",
        f"## 🧩 Top Interfaces",
        "\n".join([f"- `type {i} interface`" for i, c in go_ext.interfaces.most_common(10)]),
        f"## 🏗️ Top Structs",
        "\n".join([f"- `type {s} struct`" for s, c in go_ext.structs.most_common(10)])
    ]
    with open(os.path.join(output_dir, f"persona_go_{timestamp}.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(go_content))

    # Generate Rust Persona
    rs_content = [
        f"# 🦀 Rust Persona RAG Context",
        f"*Generated: {datetime.datetime.now().isoformat()}*",
        f"## ⚙️ Architecture Trends",
        f"- **Pattern Matching (`match`)**: {rs_ext.matches}",
        f"- **Unwraps (`.unwrap()`)**: {rs_ext.unwraps} (Hint: try to minimize these!)",
        f"## 🧩 Top Traits",
        "\n".join([f"- `pub trait {t}`" for t, c in rs_ext.traits.most_common(10)]),
        f"## 🏗️ Top Structs",
        "\n".join([f"- `struct {s}`" for s, c in rs_ext.structs.most_common(10)])
    ]
    with open(os.path.join(output_dir, f"persona_rust_{timestamp}.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(rs_content))

    # Cleanup old persona files (keep 3 most recent per language)
    try:
        for lang in ['python', 'go', 'rust']:
            files = [f for f in os.listdir(output_dir) if f.startswith(f"persona_{lang}_") and f.endswith(".md")]
            files.sort(reverse=True)
            for old_file in files[3:]:
                os.remove(os.path.join(output_dir, old_file))
    except Exception:
        pass

    # Drop a .ready flag for start_squad.py
    flag_path = os.path.join(output_dir, ".persona_ready")
    with open(flag_path, 'w', encoding='utf-8') as f:
        f.write(timestamp)
        
    if os.path.exists(lock_path):
        os.remove(lock_path)
        
    if not is_daemon:
        print(f"✅ Persona Extraction complete. Saved to {output_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fleet Persona Extractor")
    parser.add_argument("--daemon", action="store_true", help="Run silently in background")
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    output_dir = os.path.join(script_dir, "..", "07-Core-KMS", "quick-overview", "ast-patterns")
    
    extract_personas(workspace_root, output_dir, args.daemon)
