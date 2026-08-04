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
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|ROW_COUNT_HALF]] (constant: calls)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.detectTickSize]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.setVolumeMap]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|get]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.detectTickSize]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.setVolumeMap]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|checkArr]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (same_package)
<!-- SYNC:END -->
