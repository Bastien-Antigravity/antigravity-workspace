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
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart.connectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart.disconnectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart.connectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart.disconnectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart]] (class: belongs_to)
- [[web-interface/web-interface/web/static/analyst/test.js.md|patternChart]] (class: defines_method)
<!-- SYNC:END -->
