

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/matrix_server/main.go.md|main.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/matrix_server/main.go.md|main.go]] (imports)
- [[safe-socket/safe-socket/safe_socket.go.md|CreateWithConfig]] (function: belongs_to)
- [[safe-socket/safe-socket/safe_socket.go.md|Create]] (function: belongs_to)
- [[safe-socket/safe-socket/safe_socket.go.md|GetIdentity]] (function: belongs_to)
- [[safe-socket/safe-socket/safe_socket.go.md|TransportFramedTCP]] (constant: belongs_to)
- [[safe-socket/safe-socket/safe_socket.go.md|TransportSHM]] (constant: belongs_to)
- [[safe-socket/safe-socket/safe_socket.go.md|TransportUDP]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|socket.go]] (imports)
<!-- SYNC:END -->
