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
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|QueryExpander]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|expand_query]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (imports)
<!-- SYNC:END -->
