

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Set]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: defines_method)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: defines_method)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: defines_method)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: defines_method)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.updateLiveConfig]] (method: defines_method)
- [[distributed-config/distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (calls)
- [[distributed-config/distributed-config/src/network/client.go.md|client.go]] (same_package)
- [[distributed-config/distributed-config/src/network/network_test.go.md|network_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/network_test.go.md|network_test.go]] (same_package)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.updateLiveConfig]] (method: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler]] (struct: defines_method)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: belongs_to)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (calls)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (same_package)
<!-- SYNC:END -->
