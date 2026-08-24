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
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|llm_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|OpenAILLMClient]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|openai_client.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|get_llm_client]] (function: belongs_to)
<!-- SYNC:END -->
