

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (same_package)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (imports)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (calls)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (imports)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: belongs_to)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)
<!-- SYNC:END -->
