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
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelCritical]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelDebug]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelError]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelInfo]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelLogon]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelLogout]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelNotSet]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelReport]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelSchedule]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelStream]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelTrade]] (constant: belongs_to)
- [[universal-logger/universal-logger/src/utils/levels.go.md|LevelWarning]] (constant: belongs_to)
<!-- SYNC:END -->
