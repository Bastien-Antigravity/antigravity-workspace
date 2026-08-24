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
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|*toolbox_conf]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager]] (struct: defines_method)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to)
<!-- SYNC:END -->
