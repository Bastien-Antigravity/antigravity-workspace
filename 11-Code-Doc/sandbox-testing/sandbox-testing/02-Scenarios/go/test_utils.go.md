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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_adversarial_test.go.md|config_adversarial_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_persistence_test.go.md|config_persistence_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_persistence_test.go.md|config_persistence_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_server_hardening_test.go.md|config_server_hardening_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_server_hardening_test.go.md|config_server_hardening_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_stress_test.go.md|config_stress_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_stress_test.go.md|config_stress_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_sync_on_arrival_test.go.md|config_sync_on_arrival_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/config_sync_on_arrival_test.go.md|config_sync_on_arrival_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/log_server_resilience_test.go.md|log_server_resilience_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/notif_server_hardening_test.go.md|notif_server_hardening_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|contains]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|doHandshake]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/test_utils.go.md|getDockerLogs]] (function: belongs_to)
<!-- SYNC:END -->
