

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|NewHeartbeatConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|heartbeat_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Close]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.SetIdleTimeout]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|TestDynamicHeartbeatRestart]] (function: belongs_to)
<!-- SYNC:END -->
