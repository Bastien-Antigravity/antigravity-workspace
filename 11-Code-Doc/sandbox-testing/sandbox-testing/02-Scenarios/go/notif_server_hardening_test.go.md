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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|doHandshake]] (function: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|getDockerLogs]] (function: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|test_utils.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|TestNotifServerHardeningScenario]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|getDockerPort]] (function: belongs_to)
<!-- SYNC:END -->
