

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|resolve_symbol_reference]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|BaseParser]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/base_parser.py.md|base_parser.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|RustParser]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|__getstate__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|__setstate__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_extract_uses]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_init_tree_sitter]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_resolve_ref]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_resolve_rust_use]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_walk_definitions]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|_walk_references]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|parse_definitions]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/parsers/rs_parser.py.md|parse_references]] (function: belongs_to)
<!-- SYNC:END -->
