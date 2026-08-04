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
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.LocalAddr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.ReadMessage]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Read]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.RemoteAddr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetWriteDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Write]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.refreshReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.refreshWriteDeadline]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|udp_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|udp_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|NewTransientUdpSocket]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|NewUdpSocket]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.LocalAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.ReadMessage]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Read]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.RemoteAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.SetWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.refreshReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket.refreshWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|UdpSocket]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (same_package)
<!-- SYNC:END -->
