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
- [[web-interface/web-interface/web/static/analyst/charts.js.md|volumeChart.volume]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|get]] (function: calls)
- [[web-interface/web-interface/web/static/js/parts/cytoscape_part10.js.md|set]] (function: calls)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: calls)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_WSS_URL]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#AnalystTickersList (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#IndicatorsInfos (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#TableIndicators (table)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#TablePatterns (table)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#broker_ticker (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#connectionIcon (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#connectionStatus (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#default-chart (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#duplicateView (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#searchBar (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#tableIndicators (tbody)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|#tablePatterns (tbody)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|analyst_config]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|changeDatasource]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|formatDateUTC]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|indicators]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|infos_connection]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|onclose]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|onerror]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|onmessage]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|onopen]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|pattern]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|updateConnectionStatus]] (function: belongs_to)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|updateTitle]] (function: belongs_to)
<!-- SYNC:END -->
