

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_mode_details]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|list_commands]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|publish_user_message]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|SquadRESTHandler]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|event_generator]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_active_mode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_chat_history]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_commands]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|msg_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|post_chat_message]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|run_command_stream]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|stream_chat_messages]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|switch_mode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
