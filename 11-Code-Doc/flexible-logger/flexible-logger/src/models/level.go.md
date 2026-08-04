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
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level.String]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level.String]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelCritical]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelDebug]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelError]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelInfo]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelLogon]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelLogout]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelNotSet]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelReport]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelSchedule]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelStream]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelTrade]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|LevelWarning]] (constant: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/models/level.go.md|ParseLevel]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level_test.go.md|level_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/models/level_test.go.md|level_test.go]] (same_package)
<!-- SYNC:END -->
