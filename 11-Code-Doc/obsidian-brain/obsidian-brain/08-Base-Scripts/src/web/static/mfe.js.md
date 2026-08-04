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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.        const r]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.    const resp ]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.   const body = t]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.   const r]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.');
    ]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.connectedCallback]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.disconnectedCallback]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadActiveMode]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadAll]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadCommands]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadStatus]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.ntSource) ]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.renderSkeleton]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.ssages = this.que]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.tSource) {
    ]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.tching
        cons]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.setupEventListeners]] (method: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.   ]] (method: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.        const r]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.    const resp ]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.   const body = t]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.   const r]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.');
    ]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.connectedCallback]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.disconnectedCallback]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadActiveMode]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadAll]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadCommands]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.loadStatus]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.ntSource) ]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.renderSkeleton]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.ssages = this.que]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.tSource) {
    ]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE.tching
        cons]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|BaseScriptsMFE]] (class: defines_method)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/static/mfe.js.md|nst tex]] (function: belongs_to)
<!-- SYNC:END -->
