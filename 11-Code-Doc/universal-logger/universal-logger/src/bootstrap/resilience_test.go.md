

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.GetLastMessage]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.Stop]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.acceptLoop]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.handleConnection]] (method: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|InitWithOptions]] (function: calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (same_package)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.GetLastMessage]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.Stop]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.acceptLoop]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer.handleConnection]] (method: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|MockServer]] (struct: defines_method)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|NewMockServerOnPort]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|NewMockServer]] (function: belongs_to)
- [[universal-logger/universal-logger/src/bootstrap/resilience_test.go.md|TestFullEcosystemResilience]] (function: belongs_to)
<!-- SYNC:END -->
