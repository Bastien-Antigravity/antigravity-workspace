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
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Start]] (method: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Stop]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Start]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient.Stop]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient]] (struct: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|MFEClient]] (struct: defines_method)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|NewMFEClient]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/rest/mfe_client.go.md|StrategicController]] (interface: belongs_to)
<!-- SYNC:END -->
