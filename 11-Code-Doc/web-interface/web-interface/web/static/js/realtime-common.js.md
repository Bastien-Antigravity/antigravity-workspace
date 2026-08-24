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
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.fetchAnalystConfig]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.fetchTimeframes]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.formatDateUTC]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.initCollapsible]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.initDuplicateView]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.setupEventListeners]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.showLogModal]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.updateStatus]] (method: defines_method)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|BrainGraph.html]] (calls)
- [[web-interface/web-interface/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (calls)
- [[web-interface/web-interface/web/static/analyst/test.js.md|test.js]] (calls)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|websocket.js]] (calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (same_package)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (same_package)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (calls)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (same_package)
- [[web-interface/web-interface/web/static/js/parts/cose_part1.js.md|cose_part1.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part2.js.md|cytoscape_part2.js]] (calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part4.js.md|cytoscape_part4.js]] (calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.fetchAnalystConfig]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.fetchTimeframes]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.formatDateUTC]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.initCollapsible]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.initDuplicateView]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.setupEventListeners]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.showLogModal]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.updateStatus]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|analyst_config]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|changeDatasource]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|infos_connection]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|load_timeframes]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onclose]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onerror]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onopen]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|updateConnectionStatus]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|updateTitle]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|ta-indicators.js]] (calls)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|ta-indicators.js]] (same_package)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|traded-volume.js]] (calls)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|traded-volume.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
<!-- SYNC:END -->
