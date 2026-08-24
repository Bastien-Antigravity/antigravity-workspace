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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.GetNextDelay]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NetworkManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewCritical]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewPerformance]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewStandard]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|Logger.hpp]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.hpp]] (same_package)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|MICROSERVICE_TOOLBOX_CONN_MANAGER_NETWORK_MANAGER_HPP]] (macro: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|ManagedConnection]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.GetNextDelay]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NetworkManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewCritical]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewPerformance]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.NewStandard]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager]] (class: defines_method)
<!-- SYNC:END -->
