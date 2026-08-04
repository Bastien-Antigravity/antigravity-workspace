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
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.applyTheme]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.init]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.toggle]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.applyTheme]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.init]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.toggle]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine]] (class: defines_method)
<!-- SYNC:END -->
