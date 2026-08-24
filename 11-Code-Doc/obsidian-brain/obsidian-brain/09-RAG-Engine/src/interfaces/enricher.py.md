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
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|Enricher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich_pending]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|start_background_loop]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|stop_background_loop]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->
peline/standard.py.md|standard.py]] (imports)
<!-- SYNC:END -->
