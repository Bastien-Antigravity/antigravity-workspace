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
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level.String]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/level.go.md|ParseLevel]] (function: calls)
- [[flexible-logger/flexible-logger/src/models/level.go.md|level.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/models/level_test.go.md|TestLevel_String]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/models/level_test.go.md|TestParseLevel]] (function: belongs_to)
<!-- SYNC:END -->
