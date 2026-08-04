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
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.find]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onerror]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|DISCOVERY_SERVICE_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|fetchServices]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|init]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|injectNavigation]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|loadMFE]] (function: belongs_to)
<!-- SYNC:END -->
