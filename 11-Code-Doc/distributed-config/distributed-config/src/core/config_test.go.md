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
- [[distributed-config/distributed-config/src/core/config.go.md|Config.GetGRPCAddress]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Set]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ShareConfig]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.ValidateMandatoryServices]] (method: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/core/config_test.go.md|TestConfig_Concurrency]] (function: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|TestConfig_SetAndGet]] (function: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|TestConfig_ShadowPort]] (function: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|TestConfig_ShareConfig]] (function: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|TestConfig_ValidateMandatoryServices]] (function: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|iterations]] (constant: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|workers]] (constant: belongs_to)
<!-- SYNC:END -->
ons]] (constant: belongs_to)
- [[distributed-config/distributed-config/src/core/config_test.go.md|workers]] (constant: belongs_to)
<!-- SYNC:END -->
