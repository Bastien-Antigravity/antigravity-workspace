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
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part4.js.md|CoSENode]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part4.js.md|ConstraintHandler]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part4.js.md|cose_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|cytoscape_part10.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|get]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|add]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|FDLayoutConstants]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|LayoutConstants]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|PointD]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|__webpack_require__]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|layout_part1.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part2.js.md|LGraphManager]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part2.js.md|LGraph]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part2.js.md|layout_part2.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part3.js.md|IGeometry]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part3.js.md|Integer]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part3.js.md|layout_part3.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|Layout]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|LinkedList]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|Point]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|FDLayout]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|Transform]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|DimensionD]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|FDLayoutEdge]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|layout_part6.js]] (same_package)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|CoSEConstants]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|CoSEEdge]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|CoSEGraphManager]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|CoSEGraph]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|CoSELayout]] (function: belongs_to)
<!-- SYNC:END -->
