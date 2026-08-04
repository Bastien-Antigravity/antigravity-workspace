

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|TelegramClient.Start]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/cmd/strategic-nexus/main.go.md|main.go]] (calls)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|Logger]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|NewTelegramClient]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|StrategicController]] (interface: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|TelegramClient.Start]] (method: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|TelegramClient]] (struct: belongs_to)
- [[obsidian-brain/obsidian-brain/01-Strategic-Nexus/src/telegram/telegram_client.go.md|TelegramClient]] (struct: defines_method)
<!-- SYNC:END -->
