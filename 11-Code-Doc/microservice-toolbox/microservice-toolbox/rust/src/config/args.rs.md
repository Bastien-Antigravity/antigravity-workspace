

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs.parse_cli_args]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|RawArgs]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs.parse_cli_args]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
<!-- SYNC:END -->
