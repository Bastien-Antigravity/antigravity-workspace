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
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|service.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|service.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|GRPC_GENERATED_VERSION]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|GRPC_VERSION]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|GetActiveMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|GetStatus]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|RunCommand]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlServiceServicer]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlServiceStub]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SquadControlService]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|SwitchMode]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/squad_control_pb2_grpc.py.md|add_SquadControlServiceServicer_to_server]] (function: belongs_to)
<!-- SYNC:END -->
