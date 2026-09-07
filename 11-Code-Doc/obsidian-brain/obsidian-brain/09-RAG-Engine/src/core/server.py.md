

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_watcher]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|register_tool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|ALL_TOOLS]] (constant: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
