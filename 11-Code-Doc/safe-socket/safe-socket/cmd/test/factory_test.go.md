---
source: safe-socket/cmd/test/factory_test.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-07-04 17:57:27.252410
microservice: obsidian-brain
tags:
- '#service/obsidian-brain'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: factory_test.go

## 📝 Description
Automatically generated mirror for `safe-socket/cmd/test/factory_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.ReadMessage]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Accept]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Open]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Read]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Receive]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|SocketClient.Send]] (method: calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|NewHelloProtocol]] (function: calls)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.FromName]] (method: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestSHM_FullExchange]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Hello]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Raw]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTCP_Raw_Write_Method]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestTLS_Hello]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Hello]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Raw]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|TestUDP_Reliable]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|generateSelfSignedCert]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
