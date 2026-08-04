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
- None detected

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/heartbeat_audit_test.go.md|heartbeat_audit_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/scenario_test.go.md|scenario_test.go]] (imports)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/protocol.go.md|protocol.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|SocketConfig]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
<!-- SYNC:END -->
