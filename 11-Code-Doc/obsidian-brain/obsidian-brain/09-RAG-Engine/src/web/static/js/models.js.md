---
microservice: obsidian-brain
type: note
status: active
---



## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isCalls]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isDefines]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isImports]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isSamePackage]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getBadgeClass]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getColors]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getShape]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isClassOrStruct]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isFile]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isCalls]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isDefines]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isImports]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge.isSamePackage]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseEdge]] (class: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getBadgeClass]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getColors]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.getShape]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isClassOrStruct]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isFile]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode]] (class: defines_method)
<!-- SYNC:END -->
