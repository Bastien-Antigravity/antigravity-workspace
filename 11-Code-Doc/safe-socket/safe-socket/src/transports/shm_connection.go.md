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
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.Network]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.String]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.LocalAddr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.ReadMessage]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Read]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.RemoteAddr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetWriteDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Write]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.readFromRing]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.refreshReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.refreshWriteDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.writeToRing]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|BufferDataSize]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|MetaSize]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|NewShmTransport]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetClientActivity]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetClientStatus]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetHeadA]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetHeadB]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetServerActivity]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetServerStatus]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetTailA]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|OffsetTailB]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.Network]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.String]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.LocalAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.ReadMessage]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Read]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.RemoteAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.SetWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.readFromRing]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.refreshReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.refreshWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport.writeToRing]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmTransport]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|StatusConnected]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|StatusIdle]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|StatusListening]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|TotalSize]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|shm_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|shm_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->
