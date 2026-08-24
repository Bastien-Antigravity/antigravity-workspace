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
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Debug]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Debug]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestBot_MenuRegistration]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|newMockTelegramServer]] (function: belongs_to)
<!-- SYNC:END -->
