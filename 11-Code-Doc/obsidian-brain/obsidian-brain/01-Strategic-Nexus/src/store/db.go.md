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
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.GetDecisions]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.InitSchema]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/core/controller.go.md|controller.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/evolution/pipeline.go.md|pipeline.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.Close]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.GetDecisions]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.InitSchema]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.LogAction]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.ProposeSkill]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager.UpsertDecision]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager]] (struct: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|DBManager]] (struct: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/store/db.go.md|NewDBManager]] (function: belongs_to)
<!-- SYNC:END -->
