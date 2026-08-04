

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|controller.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|MODES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|_update_file_field]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|apply_mode_protocol]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|get_mode_choice_interactive]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|manager.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|manager.py]] (imports)
<!-- SYNC:END -->
