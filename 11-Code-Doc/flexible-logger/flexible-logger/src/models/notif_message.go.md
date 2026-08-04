

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/see-console-output/example_text_output.go.md|example_text_output.go]] (imports)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (imports)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/factory/factory_test.go.md|factory_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/logger.go.md|logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/notifier.go.md|notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/serializer.go.md|serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|NotifMessage]] (struct: belongs_to)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|local_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/notifier_test.go.md|notifier_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|remote_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|capn_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/json_serializer.go.md|json_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|async.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|multi.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (imports)
<!-- SYNC:END -->
/src/sink/sink_test.go.md|sink_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|writer.go]] (imports)
<!-- SYNC:END -->
