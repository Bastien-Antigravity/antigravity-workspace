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
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|NewShmTransport]] (function: calls)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|shm_connection.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (imports)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|ConnectShm]] (function: belongs_to)
<!-- SYNC:END -->
