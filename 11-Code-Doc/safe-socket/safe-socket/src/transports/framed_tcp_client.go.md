

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

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|ConnectTLS]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|Connect]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|wrapTCP]] (function: belongs_to)
<!-- SYNC:END -->
