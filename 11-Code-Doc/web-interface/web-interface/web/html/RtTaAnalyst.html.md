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
- [[web-interface/web-interface/web/static/js/prism.js.md|prism.js]] (imports)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: calls)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_WSS_URL]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#AnalystConfigForm (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#AnalystConfigFormBody (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#AnalystTickersList (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#ConnnectionInfos (h4)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#IndicatorsInfos (h3)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#TableConnnectionInfos (table)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#Tick_Datas (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#broker_ticker (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#collapsibleDiv (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#connectionIcon (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#connectionLogModal (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#connectionStatus (p)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#duplicateView (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#modalContent (tbody)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#patternChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#searchBar (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#volatilityChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|#volumeChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|analyst_config]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|changeDatasource]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|formatDateUTC]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|indicators]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|infos_connection]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|onclose]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|onerror]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|onmessage]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|onopen]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|pattern]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|updateConnectionStatus]] (function: belongs_to)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|updateTitle]] (function: belongs_to)
<!-- SYNC:END -->
