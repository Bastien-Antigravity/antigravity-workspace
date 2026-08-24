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
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizeString]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/sanitizer.go.md|sanitizer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetAddress]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetCapability]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetFullConfig]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetGRPCAddress]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetGRPCMgmtAddress]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/networking.go.md|GetRESTAddress]] (function: belongs_to)
<!-- SYNC:END -->
