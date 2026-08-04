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
- [[web-interface/web-interface/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.bind]] (method: calls)
- [[web-interface/web-interface/web/static/analyst/charts.js.md|charts.js]] (same_package)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.addActive]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.autocomplete]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.closeAllLists]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.eventListenerStart]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.onmessage]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.removeActive]] (method: defines_method)
- [[web-interface/web-interface/web/static/analyst/websocket.js.md|websocket.js]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.addActive]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.autocomplete]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.closeAllLists]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.eventListenerStart]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.onmessage]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar.removeActive]] (method: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar]] (class: belongs_to)
- [[web-interface/web-interface/web/static/analyst/searchBar.js.md|searchBar]] (class: defines_method)
<!-- SYNC:END -->
