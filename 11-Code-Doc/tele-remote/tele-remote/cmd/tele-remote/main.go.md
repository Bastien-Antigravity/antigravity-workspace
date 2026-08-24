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
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|SetupRoutes]] (function: calls)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|TeleRemoteCap]] (struct: belongs_to)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
