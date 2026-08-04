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
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.ReadMessage]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Read]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Write]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.handleRemoteAck]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.performRetries]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.retryLoop]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.sendAck]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|NewReliableConnection]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.ReadMessage]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Read]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.handleRemoteAck]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.performRetries]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.retryLoop]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection.sendAck]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|ReliableConnection]] (struct: defines_method)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|RudpHeaderSize]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|RudpTypeAck]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|RudpTypeData]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/reliable_connection.go.md|pendingPacket]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
<!-- SYNC:END -->
