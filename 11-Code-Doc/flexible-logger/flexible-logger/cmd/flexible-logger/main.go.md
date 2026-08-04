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
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|NewStandardLogger]] (function: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/flexible-logger/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/flexible-logger/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
