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
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.mount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.render]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.updateMetric]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.mount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.render]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.updateMetric]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard]] (class: defines_method)
<!-- SYNC:END -->
