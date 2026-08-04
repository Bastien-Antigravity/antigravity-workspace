

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.SendMessage]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|NewTelegramSender]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender]] (struct: defines_method)
<!-- SYNC:END -->
Sender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|TelegramSender]] (struct: defines_method)
<!-- SYNC:END -->
