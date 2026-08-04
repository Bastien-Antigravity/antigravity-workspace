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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|ShutdownFunc]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.execute_cleanups]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.register]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.wait]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|connection.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|CleanupEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.execute_cleanups]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.register]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.wait]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|new_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->
