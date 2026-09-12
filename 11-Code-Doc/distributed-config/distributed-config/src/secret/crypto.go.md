

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|main.go]] (calls)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|main.go]] (imports)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loader.go]] (calls)
- [[distributed-config/distributed-config/src/loader/loader.go.md|loader.go]] (imports)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Decrypt]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Encrypt]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|ProcessConfigSecrets]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|getPrivateKey]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|crypto_test.go]] (calls)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|crypto_test.go]] (same_package)
<!-- SYNC:END -->
