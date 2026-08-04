

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|entry.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/models/entry_test.go.md|TestEntryPool_Reuse]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/models/entry_test.go.md|TestLogEntry_Reset]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/models/entry_test.go.md|TestLogEntry_RetainRelease]] (function: belongs_to)
<!-- SYNC:END -->
