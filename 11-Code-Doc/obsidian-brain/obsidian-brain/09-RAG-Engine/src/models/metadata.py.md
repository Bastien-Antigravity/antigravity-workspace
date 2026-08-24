

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/chunk.py.md|chunk.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|validate_source_path]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (imports)
<!-- SYNC:END -->
