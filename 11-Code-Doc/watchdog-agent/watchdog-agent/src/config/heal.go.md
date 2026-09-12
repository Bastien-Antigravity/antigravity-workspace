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
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|HealSymlinks]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|SymlinkTarget]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|safeLinkOrCopy]] (function: belongs_to)
<!-- SYNC:END -->
