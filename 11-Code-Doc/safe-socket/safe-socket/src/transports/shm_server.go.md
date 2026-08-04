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
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|NewShmTransport]] (function: calls)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|shm_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Accept]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Addr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ListenShm]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Accept]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Addr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener]] (struct: defines_method)
<!-- SYNC:END -->
