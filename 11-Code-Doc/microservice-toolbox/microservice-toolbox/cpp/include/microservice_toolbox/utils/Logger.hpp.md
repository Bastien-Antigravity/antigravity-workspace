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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.AddMetadata]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Critical]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Debug]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Error]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Info]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Logon]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Logout]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Report]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Schedule]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Stream]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Trade]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Warning]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.AddMetadata]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Critical]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Debug]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Error]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Info]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Logon]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Logout]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Report]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Schedule]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Stream]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Trade]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|EnsureSafeLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|Logger]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|MICROSERVICE_TOOLBOX_UTILS_LOGGER_HPP]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.AddMetadata]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Critical]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Debug]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Error]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Info]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Logon]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Logout]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Report]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Schedule]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Stream]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Trade]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Warning]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.AddMetadata]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Critical]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Debug]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Error]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Info]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Logon]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Logout]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Report]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Schedule]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Stream]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Trade]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger.Warning]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger]] (class: defines_method)
<!-- SYNC:END -->
roservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|StdOutLogger]] (class: defines_method)
<!-- SYNC:END -->
