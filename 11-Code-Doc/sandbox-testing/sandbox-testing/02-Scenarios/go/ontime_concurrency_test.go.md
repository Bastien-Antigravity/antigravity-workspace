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
- None detected

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|TestOntimeConcurrentExecutionLock]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|TestOntimeConcurrentJobCreation]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|ontimeBaseURL]] (constant: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|setOntimeDistributedMode]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/ontime_concurrency_test.go.md|waitForOntimeServer]] (function: belongs_to)
<!-- SYNC:END -->
