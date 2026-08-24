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
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|DB_DIR]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|IS_DEVEL_MODE]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|RAG_DATABASE_NAME]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantAlignmentServiceProxy]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantGraphDBProxy]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantLexicalStoreProxy]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantParentStoreProxy]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantVectorStoreProxy]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|close]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|RAGFacade]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|PostgresAlignmentService]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|CodeDocSynchronizer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|CodeEngineAnalyzerBridge]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|MarkdownAnalyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|markdown_analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|TextAnalyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|text_analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|CodebaseAnalyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|LLMEnricher]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|PostgresGraphDB]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|StandardIndexingPipeline]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|PostgresLexicalStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|get_llm_client]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|PostgresParentStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|GraphRAGQueryEngine]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|LLMQueryExpander]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|PgVectorStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|patched_get_language]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|patched_get_parser]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
