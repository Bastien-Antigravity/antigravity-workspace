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
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/core/controller.go.md|ConfigController]] (interface: belongs_to)
- [[config-server/config-server/src/core/controller.go.md|StatusInfo]] (struct: belongs_to)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[config-server/config-server/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (imports)
- [[config-server/config-server/src/server/connection.go.md|connection.go]] (imports)
- [[config-server/config-server/src/server/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->
