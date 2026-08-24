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
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|HandshakeConnection.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|HandshakeConnection.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|HandshakeConnection]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|HandshakeConnection]] (struct: defines_method)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|NewHandshakeConnection]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
<!-- SYNC:END -->
