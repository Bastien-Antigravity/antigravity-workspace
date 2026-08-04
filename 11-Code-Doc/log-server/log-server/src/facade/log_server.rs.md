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
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.new]] (method: defines_method)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.run]] (method: defines_method)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (same_package)
- [[log-server/log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/utils/helpers.rs.md|create_log_folder]] (function: calls)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|set_internal_logger]] (function: calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.new]] (method: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.run]] (method: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer]] (struct: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer]] (struct: defines_method)
- [[log-server/log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/log-server/src/main.rs.md|main.rs]] (imports)
<!-- SYNC:END -->
