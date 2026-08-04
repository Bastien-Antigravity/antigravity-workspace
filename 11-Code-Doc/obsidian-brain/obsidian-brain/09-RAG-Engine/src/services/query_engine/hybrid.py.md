

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|QueryEngine]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|query_engine.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|MChunk]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/result.py.md|MQueryResult]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|HybridQueryEngine]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_apply_cross_encoder]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_apply_rrf]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|_re_rank_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|query]] (function: belongs_to)
<!-- SYNC:END -->
