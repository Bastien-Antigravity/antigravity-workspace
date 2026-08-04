---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|NewHighPerfLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|StartMockServer]] (function: calls)
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|mock_server.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/test/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
les/high_perf.go.md|NewHighPerfLogger]] (function: calls)
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|StartMockServer]] (function: calls)
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|mock_server.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/test/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
