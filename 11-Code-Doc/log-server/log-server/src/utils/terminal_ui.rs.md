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
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls)
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|get_hostname]] (function: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (same_package)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/log-server/src/main.rs.md|main.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_CYAN]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_GREEN]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_MAGENTA]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_RED]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_RESET]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_YELLOW]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|colorize_level]] (function: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|set_internal_logger]] (function: belongs_to)
<!-- SYNC:END -->
