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
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#cy (div)]] (element: calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|y]] (class: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|ease]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part19.js.md|headlessStep]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part19.js.md|startAnimation]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part19.js.md|stepAll]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part19.js.md|stepOne]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part19.js.md|valid]] (function: belongs_to)
<!-- SYNC:END -->
