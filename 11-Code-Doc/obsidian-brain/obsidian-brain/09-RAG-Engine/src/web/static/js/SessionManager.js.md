

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.getNodeById]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.push]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.updateButtons]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.closeSession]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.createSession]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.getActiveSession]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.renderTabs]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.switchSession]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/graph/NodeRenderer.js.md|NodeRenderer.isWebGLAvailable]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/graph/NodeRenderer.js.md|NodeRenderer.js]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isFile]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|models.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.closeSession]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.createSession]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.getActiveSession]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.renderTabs]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.switchSession]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager]] (class: defines_method)
<!-- SYNC:END -->
