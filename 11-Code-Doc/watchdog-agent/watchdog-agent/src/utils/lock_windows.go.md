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
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|registry.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|AcquireLock]] (function: belongs_to)
<!-- SYNC:END -->
