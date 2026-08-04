

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetKeepAlive]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetNoDelay]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Accept]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Addr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Accept]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Addr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|ListenTLS]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|Listen]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->
