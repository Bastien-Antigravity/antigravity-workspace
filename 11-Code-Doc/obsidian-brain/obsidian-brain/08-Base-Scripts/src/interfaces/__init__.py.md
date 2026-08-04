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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/auditor.py.md|auditor.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/command.py.md|command.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/extractor.py.md|extractor.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/interfaces.py.md|interfaces.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/memory_store.py.md|memory_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/sync.py.md|sync.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/architect.py.md|architect.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/developer.py.md|developer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/oracle.py.md|oracle.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/purger.py.md|purger.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/qa.py.md|qa.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/check_coherence.py.md|check_coherence.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/map_feats.py.md|map_feats.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
<!-- SYNC:END -->
