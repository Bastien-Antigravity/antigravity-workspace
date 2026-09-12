

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.Notify]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.serialize]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.worker]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|NewRootNotifierMsg]] (function: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|NotifierMsg.NewTags]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|NotifierMsg.SetAttachment]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|NotifierMsg.SetLevel]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|NotifierMsg.SetMessage_]] (method: calls)
- [[flexible-logger/flexible-logger/src/schemas/capnp/notifier/notifier.go.md|notifier.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|NewRemoteNotifier]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.Notify]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.serialize]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier.worker]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|RemoteNotifier]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
<!-- SYNC:END -->
