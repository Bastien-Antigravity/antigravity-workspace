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
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|heal.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorConfigServer]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorLogServer]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorNotifServer]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorRagDashboard]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorRagEngine]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorReset]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorStartSquad]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorTeleRemote]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorWatchdog]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|ColorWebInterface]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|Service]] (struct: belongs_to)
<!-- SYNC:END -->
