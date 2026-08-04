

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (same_package)
- [[distributed-config/distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|TestMergeBugReproduction]] (function: belongs_to)
<!-- SYNC:END -->
