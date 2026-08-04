

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|Analyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|RAGCaptureBridge]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|capture_bridge.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/capture_bridge.py.md|capture_bridge.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|CppParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/cpp_parser.py.md|cpp_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|GoParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/go_parser.py.md|go_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|HtmlParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|html_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/html_parser.py.md|parse_definitions]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|JavaScriptParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/js_parser.py.md|js_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|PythonParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/py_parser.py.md|py_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|RustParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|rs_parser.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|CodeEngineAnalyzerBridge]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|analyze]] (function: belongs_to)
<!-- SYNC:END -->
