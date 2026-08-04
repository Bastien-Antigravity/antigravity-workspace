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
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls)
- [[notif-server/notif-server/src/server/server.go.md|Server.Start]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|Server.Stop]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (same_package)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.AddMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Close]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Error]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.GetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Info]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Log]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Logon]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Logout]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Report]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Schedule]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.SetCallerSkip]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Stream]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Trade]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/server/connection.go.md|connection.go]] (calls)
- [[notif-server/notif-server/src/server/connection.go.md|connection.go]] (same_package)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (same_package)
- [[notif-server/notif-server/src/server/server_test.go.md|TestServerConnection]] (function: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.AddMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Close]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.GetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Log]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Logon]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Logout]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Report]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Schedule]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.SetCallerSkip]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Stream]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Trade]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger]] (struct: belongs_to)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->
