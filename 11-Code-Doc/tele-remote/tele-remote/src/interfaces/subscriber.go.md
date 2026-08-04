

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|ISubscriberCallbacks]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|ISubscriber]] (interface: belongs_to)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
<!-- SYNC:END -->
