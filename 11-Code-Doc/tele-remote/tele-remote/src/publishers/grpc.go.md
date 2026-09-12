

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/grpc_control/teleremote.pb.go.md|BotCommand_CommandType]] (struct: calls)
- [[tele-remote/tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.PublishCommand]] (method: defines_method)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.RequestRefresh]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: calls)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.PublishCommand]] (method: belongs_to)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher.RequestRefresh]] (method: belongs_to)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|GrpcPublisher]] (struct: defines_method)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: belongs_to)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
<!-- SYNC:END -->
