

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand_async]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlServiceServicer]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|add_SquadControlServiceServicer_to_server]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|squad_control_pb2_grpc.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|GetActiveMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|GetStatus]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|RunCommand]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|SquadControlServiceImpl]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|SwitchMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|start_grpc_server]] (function: belongs_to)
<!-- SYNC:END -->
