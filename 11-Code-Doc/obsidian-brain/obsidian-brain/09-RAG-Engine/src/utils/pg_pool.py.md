

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|RAG_DATABASE_NAME]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|close_pg_pool]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: belongs_to)
<!-- SYNC:END -->
