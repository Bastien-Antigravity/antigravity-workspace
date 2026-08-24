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
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: defines_method)
- [[notif-server/notif-server/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to)
- [[notif-server/notif-server/src/telegram/manager.go.md|config.AppCon]] (function: belongs_to)
<!-- SYNC:END -->
nuManager]] (function: belongs_to)
- [[notif-server/notif-server/src/telegram/manager.go.md|config.AppCon]] (function: belongs_to)
<!-- SYNC:END -->
Manager]] (function: belongs_to)
- [[notif-server/notif-server/src/telegram/manager.go.md|config.AppCon]] (function: belongs_to)
<!-- SYNC:END -->
