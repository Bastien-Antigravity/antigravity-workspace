---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/cmd/universal-logger/main.go.md|main.go]] (imports)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (imports)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|resilience_test.go]] (imports)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (imports)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|logger.go]] (imports)
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|notif_callback.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|logger_handler.go]] (imports)
<!-- SYNC:END -->
