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
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls)
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.handle_tcp_connection]] (method: defines_method)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.name]] (method: defines_method)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.new]] (method: defines_method)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.run]] (method: defines_method)
- [[log-server/log-server/src/transport/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: calls)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: calls)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: calls)
- [[log-server/log-server/src/transport/safe_socket.rs.md|safe_socket.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.handle_tcp_connection]] (method: belongs_to)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.name]] (method: belongs_to)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.new]] (method: belongs_to)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.run]] (method: belongs_to)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer]] (struct: belongs_to)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer]] (struct: defines_method)
<!-- SYNC:END -->
