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
- [[web-interface/web-interface/web/html/TradedVolume.html.md|TradedVolume.html]] (same_package)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|onclose]] (function: calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|onerror]] (function: calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|onmessage]] (function: calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|onopen]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|get]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|ROW_COUNT_HALF]] (constant: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|checkArr]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|connectVolumeMechanic]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|connect]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|initMockVolumeProfile]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|logEvent]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|processStats]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|renderDOM]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|renderVolumeProfileOverlay]] (function: belongs_to)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|setStatus]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.js]] (calls)
<!-- SYNC:END -->
