

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|NewConfig]] (function: calls)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|config_facade_test.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|main.go]] (calls)
- [[distributed-config/distributed-config/cmd/config-cli/main.go.md|main.go]] (imports)
- [[distributed-config/distributed-config/distributed_config.go.md|Decrypt]] (function: belongs_to)
- [[distributed-config/distributed-config/distributed_config.go.md|New]] (function: belongs_to)
- [[distributed-config/distributed-config/distributed_config.go.md|ProcessConfigSecrets]] (function: belongs_to)
- [[distributed-config/distributed-config/distributed_config.go.md|ProcessNode]] (function: belongs_to)
- [[distributed-config/distributed-config/distributed_config.go.md|ResolveConfigPath]] (function: belongs_to)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[distributed-config/distributed-config/src/cgo_bridge/security.go.md|security.go]] (imports)
<!-- SYNC:END -->
