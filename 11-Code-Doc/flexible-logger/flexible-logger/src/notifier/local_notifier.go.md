

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Notify]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.SetQueue]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.Notify]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier.SetQueue]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|LocalNotifier]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|NewLocalNotifier]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
<!-- SYNC:END -->
