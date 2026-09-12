

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/config/config.rs.md|Config.new]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/config/config.rs.md|Config.new]] (method: belongs_to)
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: belongs_to)
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: defines_method)
- [[log-server/log-server/src/config/config.rs.md|test_config_new]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
