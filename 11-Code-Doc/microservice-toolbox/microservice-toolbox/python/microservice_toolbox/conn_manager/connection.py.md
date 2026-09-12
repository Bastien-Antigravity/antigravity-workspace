

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|MaxRetriesReachedError]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|WriteFailedError]] (class: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/errors.py.md|errors.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|establish_connection]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|get_next_delay]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|acquire]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|release]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|ManagedConnection]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|close]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|reconnect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|write]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/manager.py.md|manager.py]] (same_package)
<!-- SYNC:END -->
