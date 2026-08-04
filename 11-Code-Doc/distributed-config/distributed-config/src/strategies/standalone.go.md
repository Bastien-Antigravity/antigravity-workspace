

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/loader/env_loader.go.md|LoadCommonFromEnv]] (function: calls)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFile]] (function: calls)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|backoff_test.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Close]] (method: defines_method)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.GetHandler]] (method: defines_method)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Load]] (method: defines_method)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Name]] (method: defines_method)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Set]] (method: defines_method)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Sync]] (method: defines_method)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Close]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.GetHandler]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Load]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Name]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Set]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy.Sync]] (method: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy]] (struct: defines_method)
<!-- SYNC:END -->
elongs_to)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|StandaloneStrategy]] (struct: defines_method)
<!-- SYNC:END -->
