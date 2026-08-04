

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Close]] (method: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Notify]] (method: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.SetQueue]] (method: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|NewLocalNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|local_notifier.go]] (same_package)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|NewRemoteNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|remote_notifier.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|TestLocalNotifier_NoQueue]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|TestLocalNotifier_Notify]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|TestRemoteNotifier_Notify]] (function: belongs_to)
<!-- SYNC:END -->
