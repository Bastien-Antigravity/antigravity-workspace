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
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent._subscribe]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.onThemeChange]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card.mount]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card.mount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card]] (class: defines_method)
<!-- SYNC:END -->
