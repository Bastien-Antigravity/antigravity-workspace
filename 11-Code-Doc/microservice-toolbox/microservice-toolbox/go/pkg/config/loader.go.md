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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Get]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.DecryptSecret]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCMgmtAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetRESTAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetServiceName]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnLiveConfUpdate]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnRegistryUpdate]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.SetLogger]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ShareConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.UnmarshalLocal]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ValidateUniquePorts]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIGRPCOverrides]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIOverrides]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyFileOverride]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ensurePath]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.getAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.loadPublicKey]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|DeepMerge]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|merger.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.DecryptSecret]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCMgmtAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetRESTAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetServiceName]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnLiveConfUpdate]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnRegistryUpdate]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.SetLogger]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ShareConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.UnmarshalLocal]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ValidateUniquePorts]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIGRPCOverrides]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIOverrides]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyFileOverride]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ensurePath]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.getAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.loadPublicKey]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfigWithLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfig]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|endpointKey]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|getIP]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|getPort]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|normalizeIP]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (same_package)
<!-- SYNC:END -->
