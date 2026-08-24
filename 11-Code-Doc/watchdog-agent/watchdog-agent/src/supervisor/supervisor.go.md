---
source: watchdog-agent/src/supervisor/supervisor.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-08-05 14:15:03.702223
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: supervisor.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/supervisor/supervisor.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsOccupantFleetService]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|KillProcessOnPort]] (function: calls)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|heal.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/postgres_launcher.go.md|postgres_launcher.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/postgres_launcher.go.md|postgres_launcher.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|registry.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|registry.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|MonitorAndSupervise]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|PipeOutput]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|RegisterCmd]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|UnregisterCmd]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
