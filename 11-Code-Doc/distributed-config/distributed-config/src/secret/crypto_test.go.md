

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Decrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Encrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|ProcessConfigSecrets]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestEncryptionRoundTrip]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestProcessConfigSecrets]] (function: belongs_to)
<!-- SYNC:END -->
