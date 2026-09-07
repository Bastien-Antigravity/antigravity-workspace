

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|NewDevelLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|NewMinimalLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NewNotifLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper.SetLocalNotifQueue]] (method: calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|NewStandardLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|SlowSink]] (struct: defines_method)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|TestAllProfiles]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|TestAuditLogger_Blocking]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|TestNotifLogger_LocalQueue]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|TestProfile_AppNamePropagation]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|startTestServer]] (function: belongs_to)
<!-- SYNC:END -->
