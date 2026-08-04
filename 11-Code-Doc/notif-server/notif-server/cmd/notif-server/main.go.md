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
- [[notif-server/notif-server/src/core/controller.go.md|NewController]] (function: calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls)
- [[notif-server/notif-server/src/rest/mfe.js.md|mfe.js]] (imports)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
