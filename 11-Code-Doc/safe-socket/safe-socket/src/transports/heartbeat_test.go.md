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
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.ReadMessage]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Read]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Write]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|Listen]] (function: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|framed_tcp_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.String]] (method: calls)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|shm_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: calls)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: calls)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|TestFramedTCPHeartbeatReadMessage]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|TestFramedTCPHeartbeatRead]] (function: belongs_to)
<!-- SYNC:END -->
