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
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.clone]] (method: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|add]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part3.js.md|_classCallCheck]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part3.js.md|layout_part3.js]] (same_package)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|ObjectMap]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|ObjectSet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|baseGetTag]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|cancel]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|debounce]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|debounced]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|flush]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|getRawTag]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|invokeFunc]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|isObjectLike]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|isSymbol]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|leadingEdge]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|objectToString]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|remainingWait]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|shouldInvoke]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|timerExpired]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|toNumber]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|trailingEdge]] (function: belongs_to)
<!-- SYNC:END -->
