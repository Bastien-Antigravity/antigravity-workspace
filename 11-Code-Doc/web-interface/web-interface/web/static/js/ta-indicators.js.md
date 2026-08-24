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
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.addRow]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.onMessage]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.renderIndicators]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.renderPatterns]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.addRow]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.onMessage]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.renderIndicators]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard.renderPatterns]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|TAIndicatorsDashboard]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|onmessage]] (function: belongs_to)
<!-- SYNC:END -->
