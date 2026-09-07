

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ateCommandAction(bo]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|b.Context,]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|icText(bot *core.]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ion(bot *core.]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|nMenu(m *models.]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|r {
	menuSta]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|seButton(bo]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|seMenuRow(bo]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|th(root *mode]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|yLabel(m *models.]] (function: belongs_to)
<!-- SYNC:END -->
