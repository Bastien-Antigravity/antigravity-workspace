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
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#cy (div)]] (element: calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|h]] (class: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|w]] (class: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|add]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part25.js.md|CoseBilkentLayout]] (function: belongs_to)
<!-- SYNC:END -->
