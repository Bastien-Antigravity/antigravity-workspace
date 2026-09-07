

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.ExecuteCleanups]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.LifecycleManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Register]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestShutdown]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.SignalHandler]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Wait]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|Logger.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/utils/Logger.hpp.md|NoOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|CleanupEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.ExecuteCleanups]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.LifecycleManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Register]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestShutdown]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.SignalHandler]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Wait]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|MICROSERVICE_TOOLBOX_LIFECYCLE_MANAGER_HPP]] (macro: belongs_to)
<!-- SYNC:END -->
pp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|MICROSERVICE_TOOLBOX_LIFECYCLE_MANAGER_HPP]] (macro: belongs_to)
<!-- SYNC:END -->
