---
source: safe-socket/src/protocols/hello_protocol.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-07-04 17:57:27.867397
microservice: obsidian-brain
tags:
- '#service/obsidian-brain'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: hello_protocol.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/protocols/hello_protocol.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Decapsulate]] (method: defines_method)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Encapsulate]] (method: defines_method)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Initiate]] (method: defines_method)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.WaitInitiation]] (method: defines_method)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.SetFromAddress]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.SetFromHost]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.SetFromName]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.SetFromPublicIP]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.SetToAddress]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|HelloMsg.String]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|NewRootHelloMsg]] (function: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|NewRootPacketEnvelope]] (function: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|PacketEnvelope.Payload]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|PacketEnvelope.SenderID]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|PacketEnvelope.SetPayload]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|PacketEnvelope.SetSenderID]] (method: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|ReadRootHelloMsg]] (function: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|ReadRootPacketEnvelope]] (function: calls)
- [[safe-socket/safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (calls)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (imports)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Decapsulate]] (method: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Encapsulate]] (method: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.Initiate]] (method: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol.WaitInitiation]] (method: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|HelloProtocol]] (struct: defines_method)
- [[safe-socket/safe-socket/src/protocols/hello_protocol.go.md|NewHelloProtocol]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
