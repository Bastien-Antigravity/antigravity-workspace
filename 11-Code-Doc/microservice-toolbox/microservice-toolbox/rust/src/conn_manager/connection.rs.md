

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.close]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.reconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.set_stream]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.write]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|Error]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/errors.rs.md|errors.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.establish_connection]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager.get_next_delay]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|NetworkManager]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|manager.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.close]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.reconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.set_stream]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection.write]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/connection.rs.md|ManagedConnection]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->
rs.md|manager.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->
