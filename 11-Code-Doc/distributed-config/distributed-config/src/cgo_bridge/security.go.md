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
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizeString]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|bridge_test.go]] (calls)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|bridge_test.go]] (same_package)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|Decrypt]] (function: belongs_to)
<!-- SYNC:END -->
