

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|FeatFixer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|_get_hub_link]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|_move_root_feats]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|_process_single_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fix_feats.py.md|process_feats]] (function: belongs_to)
<!-- SYNC:END -->
