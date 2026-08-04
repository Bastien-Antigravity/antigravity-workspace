---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|ParseSharePayload]] (function: calls)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/core/defaults.go.md|NewDefaultConfig]] (function: calls)
- [[distributed-config/distributed-config/src/core/merger.go.md|DeepMerge]] (function: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.ApplyFileOverride]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Close]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnLiveConfUpdate]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnRegistryUpdate]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Reload]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.SetSingle]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Set]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.ShareConfig]] (method: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Sync]] (method: defines_method)
- [[distributed-config/distributed-config/src/factory/config_factory.go.md|NewStrategy]] (function: calls)
- [[distributed-config/distributed-config/src/factory/config_factory.go.md|config_factory.go]] (imports)
- [[distributed-config/distributed-config/src/interfaces/config_strategy.go.md|config_strategy.go]] (imports)
- [[distributed-config/distributed-config/src/loader/validator.go.md|validator.go]] (imports)
- [[distributed-config/distributed-config/src/network/backoff_test.go.md|backoff_test.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|logger.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.ApplyFileOverride]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Close]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnLiveConfUpdate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnRegistryUpdate]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Reload]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.SetSingle]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Set]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.ShareConfig]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.Sync]] (method: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config]] (struct: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config]] (struct: defines_method)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|NewConfig]] (function: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|config_facade_test.go]] (calls)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|config_facade_test.go]] (same_package)
<!-- SYNC:END -->
