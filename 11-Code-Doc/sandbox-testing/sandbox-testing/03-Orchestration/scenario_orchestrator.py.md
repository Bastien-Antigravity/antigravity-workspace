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
- [[sandbox-testing/sandbox-testing/02-Scenarios/python/rag_seed_schema_test.py.md|rag_seed_schema_test.py]] (calls)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|ScenarioRunner]] (class: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|__init__]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|execute]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|log]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|run_docker]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|run_implementation]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|run_native]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/03-Orchestration/scenario_orchestrator.py.md|stop_all]] (function: belongs_to)
<!-- SYNC:END -->
