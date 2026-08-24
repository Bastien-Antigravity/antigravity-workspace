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
- [[web-interface/web-interface/web/static/analyst/charts.js.md|volumeChart.volume]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.SymbolWindow(sym]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.fetchConfig]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.getDisplayData]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.initializeApp]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.mergeData]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.openConnectionLog]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.renderList]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.scheduleUpdate]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.sendSubscription]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.setupTimeframeEventListener]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.setupTimeframeSelector]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.startWebSocket]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateAnalysisBlocks]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateConnectionStatus]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateMetrics]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateSymbolsList]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateUI]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.showLogModal]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.updateStatus]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onclose]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onerror]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onopen]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|onmessage]] (function: calls)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|traded-volume.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getFromElement]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/atoms/MetricBadge.js.md|MetricBadge.updateValue]] (method: calls)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: calls)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_WSS_URL]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|APP_CONFIG]] (constant: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.SymbolWindow(sym]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.fetchConfig]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.getDisplayData]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.initializeApp]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.mergeData]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.openConnectionLog]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.renderList]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.scheduleUpdate]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.sendSubscription]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.setupTimeframeEventListener]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.setupTimeframeSelector]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.startWebSocket]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateAnalysisBlocks]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateConnectionStatus]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateMetrics]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateSymbolsList]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard.updateUI]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|MarketObserverDashboard]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|activityRenderer]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|formatPct]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|gainerLoserRenderer]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|getComp]] (function: belongs_to)
<!-- SYNC:END -->
