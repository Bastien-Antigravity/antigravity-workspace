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
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: calls)
- [[log-server/log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (imports)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls)
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.name]] (method: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.new]] (method: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.run]] (method: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.log_message]] (method: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.new]] (method: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry.from]] (method: defines_method)
- [[log-server/log-server/src/transport/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.name]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.new]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway.run]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway]] (struct: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeGateway]] (struct: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.log_message]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl.new]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl]] (struct: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogBridgeServiceImpl]] (struct: defines_method)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry.from]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry]] (struct: defines_method)
<!-- SYNC:END -->
LogEntry.from]] (method: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|LogEntry]] (struct: defines_method)
<!-- SYNC:END -->
