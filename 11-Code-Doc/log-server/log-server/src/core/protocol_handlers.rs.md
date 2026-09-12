

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|le_grpc_message(
  ]] (function: belongs_to)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|le_tcp_message(
  ]] (function: belongs_to)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|tify_client_from_handshake(dat]] (function: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
