

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|generate_response]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|llm_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|QueryExpander]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|query_expander.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|LLMQueryExpander]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_LLM_API_KEY]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_LLM_API_URL]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_LLM_MODEL]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_LLM_TIMEOUT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_SYSTEM_PROMPT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|_USER_PROMPT_TMPL]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|expand_query]] (function: belongs_to)
<!-- SYNC:END -->
