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
- [[safe-socket/safe-socket/safe_socket.go.md|Create]] (function: calls)
- [[safe-socket/safe-socket/safe_socket.go.md|GetIdentity]] (function: calls)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.FromHost]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.FromName]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.FromPublicIP]] (method: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/matrix_server/main.go.md|handleConnection]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/matrix_server/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
