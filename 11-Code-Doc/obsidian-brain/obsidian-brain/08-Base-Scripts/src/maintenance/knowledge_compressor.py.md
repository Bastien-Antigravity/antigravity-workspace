

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|KnowledgeCompressor]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|distill_to_pattern]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|extract_recent_sessions]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|run]] (function: belongs_to)
<!-- SYNC:END -->
