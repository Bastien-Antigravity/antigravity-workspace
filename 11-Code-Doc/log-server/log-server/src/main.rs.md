

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.new]] (method: calls)
- [[log-server/log-server/src/facade/log_server.rs.md|LogServer.run]] (method: calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: calls)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/main.rs.md|main]] (function: belongs_to)
- [[log-server/log-server/src/main.rs.md|run_server]] (function: belongs_to)
<!-- SYNC:END -->
