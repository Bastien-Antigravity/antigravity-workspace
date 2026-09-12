

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.ReadMessage]] (method: calls)
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
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|TestOOMProtection]] (function: belongs_to)
<!-- SYNC:END -->
