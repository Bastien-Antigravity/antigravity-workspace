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
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|NewNoLockLogger]] (function: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/test-log-server/main.go.md|main]] (function: belongs_to)
- [[flexible-logger/flexible-logger/cmd/test-log-server/main.go.md|test_func]] (function: belongs_to)
<!-- SYNC:END -->
