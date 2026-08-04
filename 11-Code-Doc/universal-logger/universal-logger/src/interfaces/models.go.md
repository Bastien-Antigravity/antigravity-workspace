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
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (imports)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelCritical]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelDebug]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelError]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelInfo]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelLogon]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelLogout]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelNotSet]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelReport]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelSchedule]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelStream]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelTrade]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|LevelWarning]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|logger_handler.go]] (imports)
- [[universal-logger/universal-logger/src/utils/levels.go.md|levels.go]] (imports)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|logger_utils.go]] (imports)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)
<!-- SYNC:END -->
