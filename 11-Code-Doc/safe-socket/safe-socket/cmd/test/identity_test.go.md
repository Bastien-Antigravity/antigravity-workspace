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
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.LocalAddr]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.ReadMessage]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.RemoteAddr]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetWriteDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: defines_method)
- [[safe-socket/safe-socket/safe_socket.go.md|GetIdentity]] (function: calls)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/facade/handshake_connection.go.md|NewHandshakeConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/heartbeat_connection.go.md|NewHeartbeatConnection]] (function: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (same_package)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (same_package)
- [[safe-socket/safe-socket/cmd/test/heartbeat_audit_test.go.md|heartbeat_audit_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/heartbeat_audit_test.go.md|heartbeat_audit_test.go]] (same_package)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.LocalAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.ReadMessage]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.RemoteAddr]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport]] (struct: belongs_to)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport]] (struct: defines_method)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|TestGetIdentity]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/scenario_test.go.md|scenario_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/scenario_test.go.md|scenario_test.go]] (same_package)
- [[safe-socket/safe-socket/cmd/test/stress_test.go.md|stress_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/stress_test.go.md|stress_test.go]] (same_package)
<!-- SYNC:END -->
tress_test.go.md|stress_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/stress_test.go.md|stress_test.go]] (same_package)
<!-- SYNC:END -->
