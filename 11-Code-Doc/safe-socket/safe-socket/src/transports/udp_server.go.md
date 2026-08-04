---
source: safe-socket/src/transports/udp_server.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-07-04 17:57:27.593028
microservice: obsidian-brain
tags:
- '#service/obsidian-brain'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: udp_server.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/transports/udp_server.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadDeadline]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|NewTransientUdpSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|udp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|ListenUDP]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
