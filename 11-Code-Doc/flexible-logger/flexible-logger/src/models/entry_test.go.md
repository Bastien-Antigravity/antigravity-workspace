---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

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
