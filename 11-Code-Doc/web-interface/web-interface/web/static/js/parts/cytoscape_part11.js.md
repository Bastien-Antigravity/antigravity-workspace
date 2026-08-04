---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|_.triggerEvent]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|add]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part11.js.md|removeData]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|cytoscape_part13.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|cytoscape_part13.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part24.js.md|cytoscape_part24.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part24.js.md|cytoscape_part24.js]] (same_package)
<!-- SYNC:END -->
