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
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.clear]] (method: calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|extend]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|RtTaAnalyst.html]] (calls)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|TAIndicatorsAll.html]] (calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|TradedVolume.html]] (calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (calls)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|cose_part1.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|cose_part1.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cose_part2.js.md|cose_part2.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part2.js.md|cose_part2.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cose_part4.js.md|cose_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part4.js.md|cose_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cose_part5.js.md|cose_part5.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cose_part5.js.md|cose_part5.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|ListCache]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|MapCache]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|arrayMap]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|assignValue]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|baseAssignValue]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|baseGet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|baseSet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|baseToString]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|castPath]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|copyArray]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|getMapData]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|get]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|isIndex]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|isKeyable]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|listCacheHas]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|listCacheSet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|mapCacheClear]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|mapCacheDelete]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|mapCacheGet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|mapCacheHas]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|mapCacheSet]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|memoizeCapped]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|memoize]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|toKey]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|toPath]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|toString$1]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part15.js.md|cytoscape_part15.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part15.js.md|cytoscape_part15.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part17.js.md|cytoscape_part17.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part17.js.md|cytoscape_part17.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part18.js.md|cytoscape_part18.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part4.js.md|cytoscape_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part4.js.md|cytoscape_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part6.js.md|cytoscape_part6.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part6.js.md|cytoscape_part6.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part9.js.md|cytoscape_part9.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part9.js.md|cytoscape_part9.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part4.js.md|layout_part4.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part5.js.md|layout_part5.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|layout_part6.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/layout_part6.js.md|layout_part6.js]] (same_package)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/EventBus.js.md|EventBus.js]] (calls)
<!-- SYNC:END -->
