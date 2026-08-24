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
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Unwrap]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|logger.go]] (calls)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|GetUnderlyingLogger]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|Log]] (function: belongs_to)
<!-- SYNC:END -->
hMetadata]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|Log]] (function: belongs_to)
<!-- SYNC:END -->
