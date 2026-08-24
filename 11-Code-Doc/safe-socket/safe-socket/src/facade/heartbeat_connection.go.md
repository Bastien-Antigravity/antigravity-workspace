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
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.ReadMessage]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Read]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Write]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.start]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.ReadMessage]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Read]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection.start]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|HeartbeatConnection]] (struct: defines_method)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|NewHeartbeatConnection]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
<!-- SYNC:END -->
