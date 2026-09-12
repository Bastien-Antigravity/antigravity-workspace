

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|CheckProductionIPs]] (function: calls)
- [[distributed-config/distributed-config/src/loader/validator.go.md|CheckTestIPs]] (function: calls)
- [[distributed-config/distributed-config/src/loader/validator.go.md|ValidateCommonConfig]] (function: calls)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/validator_test.go.md|TestValidator]] (function: belongs_to)
<!-- SYNC:END -->
