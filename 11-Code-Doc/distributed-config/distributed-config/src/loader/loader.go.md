

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/core/defaults.go.md|NewDefaultConfig]] (function: calls)
- [[distributed-config/distributed-config/src/core/merger.go.md|DeepMerge]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Decrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/loader/loader.go.md|EnsureFileExists]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFileSafe]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadConfigFromFile]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader.go.md|LoadYAML]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader.go.md|ProcessNode]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loadPublicKey]] (function: belongs_to)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader_test.go.md|loader_test.go]] (same_package)
- [[distributed-config/distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/standalone.go.md|standalone.go]] (calls)
- [[distributed-config/distributed-config/src/strategies/test.go.md|test.go]] (calls)
<!-- SYNC:END -->
