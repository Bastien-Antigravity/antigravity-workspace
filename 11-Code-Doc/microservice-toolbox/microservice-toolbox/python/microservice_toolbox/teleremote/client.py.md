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
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|ComponentMessage]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|Registration]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/grpc_client/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/grpc_client/teleremote_pb2_grpc.py.md|TeleRemoteServiceStub]] (class: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|Action]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|TeleClient]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_command_dispatcher]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_connection_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_convert_action_to_btn]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_disconnect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_register_handlers_recursive]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_run_handler]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_send_registration]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|add_action]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|close]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|generate_menu_json]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|push_menu_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|send_telemetry]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|start]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|update_actions]] (function: belongs_to)
<!-- SYNC:END -->
