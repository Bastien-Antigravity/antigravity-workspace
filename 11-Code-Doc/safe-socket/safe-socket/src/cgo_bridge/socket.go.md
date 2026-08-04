

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Get]] (function: calls)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Register]] (function: calls)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Unregister]] (function: calls)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Accept]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Close]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|CreateWithConfig]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Create]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Listen]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Open]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Receive]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Send]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|SetDeadline]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|SetIdleTimeout]] (function: belongs_to)
<!-- SYNC:END -->
eadline]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|SetIdleTimeout]] (function: belongs_to)
<!-- SYNC:END -->
