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
