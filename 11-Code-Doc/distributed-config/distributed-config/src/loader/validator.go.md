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
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|CheckProductionIPs]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/validator.go.md|CheckTestIPs]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/validator.go.md|ValidateCommonConfig]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/validator_test.go.md|validator_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/validator_test.go.md|validator_test.go]] (same_package)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (imports)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (imports)
<!-- SYNC:END -->
