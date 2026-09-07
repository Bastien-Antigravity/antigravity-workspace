

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterMockSender]] (method: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.SendMessage]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|TestWorkerPoolDispatch]] (function: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|TestWorkerPoolIsolation]] (function: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|counterMockSender]] (struct: defines_method)
<!-- SYNC:END -->
