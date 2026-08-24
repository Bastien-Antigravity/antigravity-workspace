---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|MemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|query_brain]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|improved_transformer.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|DualLayerMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|PostgresMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|RAGMemoryStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|ShortTermMemory]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|_format_results]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|_init_db]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|add]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|clear]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|retrieve]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|sovereignty.py]] (same_package)
<!-- SYNC:END -->
vereignty.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|sovereignty.py]] (same_package)
<!-- SYNC:END -->
