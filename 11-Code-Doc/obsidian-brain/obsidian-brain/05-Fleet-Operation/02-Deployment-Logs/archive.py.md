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
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|DefaultLogger]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|DeploymentLogsArchiver]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_archive_files]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_ensure_firewall]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_identify_logs]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_update_moc]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|critical]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|error]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|info]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|run_archive]] (function: belongs_to)
<!-- SYNC:END -->
