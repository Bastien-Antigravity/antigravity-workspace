---
microservice: obsidian-brain
type: note
status: active
tags:
- '#service/obsidian-brain'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.ConsumeRawMessages]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.EnsureSafeLogger]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetConfig]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterMockSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.stopSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier_test.go.md|mockSender.GetTag]] (method: calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|mockSender.SendMessage]] (method: calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/notif-server/src/core/request_handler.go.md|DeserializeNotifMsg]] (function: calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[notif-server/notif-server/src/interfaces/notifier.go.md|notifier.go]] (imports)
- [[notif-server/notif-server/src/notifiers/discord.go.md|NewDiscordSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (imports)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|NewTelegramSender]] (function: calls)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|NotifRequest.String]] (method: calls)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.ConsumeRawMessages]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.EnsureSafeLogger]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterMockSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.stopSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|NotifierStatus]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier]] (struct: defines_method)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (calls)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (same_package)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (calls)
<!-- SYNC:END -->
