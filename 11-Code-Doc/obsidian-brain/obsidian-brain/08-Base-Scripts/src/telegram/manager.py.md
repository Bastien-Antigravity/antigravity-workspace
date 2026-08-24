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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_mode_details]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|list_commands]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand_async]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|MODES]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|switch_mode.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|MenuManager]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|SetupTelegram]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|cmd_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|handle_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|make_cmd_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|make_mode_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|mode_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|push]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|rebuild_menu]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|start_tc]] (function: belongs_to)
<!-- SYNC:END -->
