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
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|Get]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|Set]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|Sync]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/config.go.md|config.go]] (same_package)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|Close]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|New]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|Decrypt]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|security.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|TestBridge_ExpandedName]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|TestBridge_GetSet]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|TestBridge_LiveUpdate]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|TestBridge_Security]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|TestBridge_Sync]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/bridge_test.go.md|testInit]] (function: belongs_to)
<!-- SYNC:END -->
