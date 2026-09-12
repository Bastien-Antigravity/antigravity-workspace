

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/env_loader.go.md|LoadCommonFromEnv]] (function: belongs_to)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (calls)
<!-- SYNC:END -->
