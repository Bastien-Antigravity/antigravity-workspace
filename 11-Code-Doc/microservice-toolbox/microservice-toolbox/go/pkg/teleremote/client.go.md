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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote_grpc.pb.go.md|NewTeleRemoteServiceClient]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|Action]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|NewTeleClient]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|btnDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|rowDef]] (struct: belongs_to)
<!-- SYNC:END -->
