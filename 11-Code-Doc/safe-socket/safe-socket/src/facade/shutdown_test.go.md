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
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetAddress]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetConnectTimeout]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetProtocol]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetTransport]] (method: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Accept]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Close]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Listen]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|NewSocketServer]] (function: calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|SocketServer.GetAddr]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|TestSynchronousShutdown]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetAddress]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetConnectTimeout]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetProtocol]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile.GetTransport]] (method: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/facade/shutdown_test.go.md|mockProfile]] (struct: defines_method)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
<!-- SYNC:END -->
