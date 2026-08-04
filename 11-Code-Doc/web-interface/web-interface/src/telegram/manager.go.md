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
- [[web-interface/web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: belongs_to)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: defines_method)
- [[web-interface/web-interface/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to)
- [[web-interface/web-interface/src/telegram/manager.go.md|elegram(appCo]] (function: belongs_to)
<!-- SYNC:END -->
