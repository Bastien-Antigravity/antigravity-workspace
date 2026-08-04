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
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/CV.html.md|#outline (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|#page-container (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|#pf1 (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|#sidebar (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|Page]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|Viewer]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|b]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|clone_and_extend_objs]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|disable_dragstart]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|get_page_number]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|invert]] (function: belongs_to)
- [[web-interface/web-interface/web/html/CV.html.md|transform]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/base.js.md|base.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part2.js.md|cose_part2.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part16.js.md|cytoscape_part16.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part1.js.md|layout_part1.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
<!-- SYNC:END -->
