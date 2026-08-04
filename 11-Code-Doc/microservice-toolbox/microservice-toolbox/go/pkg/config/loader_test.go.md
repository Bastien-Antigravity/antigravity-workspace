

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfig]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|AppConfig_CLIOverrideScope(t *]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|AppConfig_DuplicatePorts(t *]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|AppConfig_GRPCMissingReturnsError(t *]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|AppConfig_SetLogger(t *]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_AddressResolution]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_LoadConfigFactory]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_MissingFileReturnsError]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|nfig s]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_AutoLoadPublicKey(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_DecryptPlaintextPassthrough(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_EnsurePath(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_GetLocal(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_GetLocalEmpty(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_KeyFlag(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_Secrets(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stAppConfig_UnmarshalLocal(t]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|stDeepMerge(t]] (function: belongs_to)
<!-- SYNC:END -->
