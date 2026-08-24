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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ApplyFileOverride]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.DistConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetCapability]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetLastError]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Get]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Set]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ShareConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/libdistconf.h.md|libdistconf.h]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (same_package)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DISTCONF_HPP]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ApplyFileOverride]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.DistConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetCapability]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetLastError]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Get]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Set]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ShareConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/rust_con.rs.md|rust_con.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/rust_gen.rs.md|rust_gen.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|resolver.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|providers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (calls)
<!-- SYNC:END -->
