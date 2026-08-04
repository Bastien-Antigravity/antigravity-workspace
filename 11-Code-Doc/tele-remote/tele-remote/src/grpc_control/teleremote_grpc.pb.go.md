---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.Connect]] (method: defines_method)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.mustEmbedUnimplementedTeleRemoteServiceServer]] (method: defines_method)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.testEmbeddedByValue]] (method: defines_method)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|teleRemoteServiceClient.Connect]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|NewTeleRemoteServiceClient]] (function: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|RegisterTeleRemoteServiceServer]] (function: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|TeleRemoteServiceClient]] (interface: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|TeleRemoteServiceServer]] (interface: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|TeleRemoteService_Connect_FullMethodName]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.Connect]] (method: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.mustEmbedUnimplementedTeleRemoteServiceServer]] (method: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer.testEmbeddedByValue]] (method: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnimplementedTeleRemoteServiceServer]] (struct: defines_method)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|UnsafeTeleRemoteServiceServer]] (interface: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|_TeleRemoteService_Connect_Handler]] (function: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|_]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|teleRemoteServiceClient.Connect]] (method: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|teleRemoteServiceClient]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|teleRemoteServiceClient]] (struct: defines_method)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
<!-- SYNC:END -->
