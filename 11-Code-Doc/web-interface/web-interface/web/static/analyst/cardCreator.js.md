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
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.connectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.disconnectedCallback]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.handleChoiceClick]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.bind]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (imports)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.connectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.disconnectedCallback]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard.handleChoiceClick]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard]] (class: belongs_to)
- [[web-interface/web-interface/web/static/analyst/cardCreator.js.md|ChoiceCard]] (class: defines_method)
<!-- SYNC:END -->
