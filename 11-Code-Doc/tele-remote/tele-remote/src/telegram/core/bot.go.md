

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Config]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (calls)
<!-- SYNC:END -->
