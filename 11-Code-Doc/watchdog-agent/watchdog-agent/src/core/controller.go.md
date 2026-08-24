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
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|ServiceStatus]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|WatchdogController]] (interface: belongs_to)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|WatchdogStatusInfo]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->
