---
source: watchdog-agent/src/supervisor/registry.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-08-05 14:15:03.698925
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: registry.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/supervisor/registry.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindPythonCmd]] (function: calls)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|RegisterServices]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|ValidateRegistry]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|resolveServiceAddr]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
