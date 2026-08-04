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
- None detected

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|main.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Get]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Register]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Unregister]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|socket.go]] (calls)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|socket.go]] (same_package)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (calls)
<!-- SYNC:END -->
