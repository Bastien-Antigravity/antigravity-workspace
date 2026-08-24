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
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion.mount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion.toggle]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion.mount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion.toggle]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/Accordion.js.md|Accordion]] (class: defines_method)
<!-- SYNC:END -->
