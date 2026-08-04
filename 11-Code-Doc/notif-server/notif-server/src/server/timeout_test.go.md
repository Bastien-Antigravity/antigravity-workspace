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
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.ConsumeRawMessages]] (method: calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|NewNotifHandler]] (function: calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapSerialize]] (method: calls)
- [[notif-server/notif-server/src/interfaces/notifier.go.md|notifier.go]] (imports)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls)
- [[notif-server/notif-server/src/server/server.go.md|Server.Start]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|Server.Stop]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/server/timeout_test.go.md|TestIdleTimeoutFix]] (function: belongs_to)
<!-- SYNC:END -->
