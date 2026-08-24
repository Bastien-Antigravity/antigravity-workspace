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
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|registry.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindPythonCmd]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindWorkspaceRoot]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|GetLocalIPs]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsLocal]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsOccupantFleetService]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|KillProcessOnPort]] (function: belongs_to)
<!-- SYNC:END -->
