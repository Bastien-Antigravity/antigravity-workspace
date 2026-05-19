import os
import ast
import collections

class CodebaseEssenceVisitor(ast.NodeVisitor):
    def __init__(self):
        self.imports = collections.Counter()
        self.exceptions_caught = collections.Counter()
        self.logging_calls = collections.Counter()
        self.class_names = []
        self.func_names = []

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

    def visit_ExceptHandler(self, node):
        if isinstance(node.type, ast.Name):
            self.exceptions_caught[node.type.id] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        # Looks for patterns like logger.info(), self.logger.error()
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name) and node.func.value.id in ('log', 'logger', 'logging'):
                self.logging_calls[node.func.attr] += 1
            elif isinstance(node.func.value, ast.Attribute) and node.func.value.attr in ('logger', 'log'):
                self.logging_calls[node.func.attr] += 1
        self.generic_visit(node)

def extract_essence(repo_path="."):
    visitor = CodebaseEssenceVisitor()
    
    for root, _, files in os.walk(repo_path):
        # Skip virtual environments and hidden dirs
        if any(part.startswith('.') or part in ('venv', '__pycache__') for part in root.split(os.sep)):
            continue
            
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        tree = ast.parse(f.read(), filename=filepath)
                        visitor.visit(tree)
                except Exception:
                    pass # Skip unparseable files
    
    print("=== TEAM CODING ESSENCE ===")
    print("\n🔥 Core Dependencies:")
    for imp, count in visitor.imports.most_common(5):
        print(f"  - {imp} (used {count} times)")
        
    print("\n🛡️ Error Handling Patterns:")
    for exc, count in visitor.exceptions_caught.most_common(5):
        print(f"  - except {exc}: (found {count} times)")
        
    print("\n📝 Logging Culture:")
    for log_meth, count in visitor.logging_calls.most_common(5):
        print(f"  - logger.{log_meth}() (found {count} times)")

if __name__ == '__main__':
    extract_essence()
