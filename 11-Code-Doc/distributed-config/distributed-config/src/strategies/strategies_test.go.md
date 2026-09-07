

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|CloudStrategy.Load]] (method: calls)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/strategies/strategies_test.go.md|TestCloudStrategy_Production]] (function: belongs_to)
- [[distributed-config/distributed-config/src/strategies/strategies_test.go.md|TestCloudStrategy_Staging]] (function: belongs_to)
- [[distributed-config/distributed-config/src/strategies/strategies_test.go.md|TestStandaloneStrategy]] (function: belongs_to)
<!-- SYNC:END -->
