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
- [[tele-remote/tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|RegisterTeleRemoteServiceServer]] (function: calls)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: calls)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: defines_method)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: calls)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: belongs_to)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: belongs_to)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: defines_method)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: belongs_to)
<!-- SYNC:END -->
riber]] (struct: defines_method)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: belongs_to)
<!-- SYNC:END -->
