

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|GoExtractor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|PythonExtractor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|RustExtractor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|_get_exception_names]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|extract_personas]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|parse]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_AsyncFunctionDef]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_Call]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_ClassDef]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_ExceptHandler]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_FunctionDef]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_ImportFrom]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|visit_Import]] (function: belongs_to)
<!-- SYNC:END -->
