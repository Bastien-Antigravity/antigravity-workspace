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
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|h]] (class: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.same]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|w]] (class: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|y]] (class: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part11.js.md|cytoscape_part11.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part11.js.md|removeData]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|addChildren]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|addParentAndChildren]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|addParent]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|add]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|computeBiasValues]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|computePaddingValues]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|defineDegreeBoundsFunction]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|defineDegreeFunction]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|forEachCompound]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part13.js.md|update]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part20.js.md|cytoscape_part20.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part20.js.md|cytoscape_part20.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part23.js.md|cytoscape_part23.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part23.js.md|cytoscape_part23.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (same_package)
<!-- SYNC:END -->
