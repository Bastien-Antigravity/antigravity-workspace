---
microservice: ecosystem-wide
type: protocol
status: active
tags:
- '#service/ecosystem-wide'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
---
# 📜 Microservice Startup Protocol

This protocol defines the standardized initialization sequence for all microservices in the Bastien Ecosystem. It ensures parity in configuration loading, argument handling, and logging across **Go, Rust, Python, and C++**.

## 1. The Startup Sequence (The 4-Phase Truth)

Every microservice MUST follow this sequence during the `main()` initialization phase, managed by the `microservice-toolbox`:

1.  **Phase 1: Base Configuration**: Load `{profile}.yaml` as the foundation.
2.  **Phase 2: Local Overrides**: If in `standalone` or `test` profile, re-apply the local YAML file as a hard override to ensure developer-intent parity.
3.  **Phase 3: CLI Arguments**: Apply command-line flags. **CLI always wins.**
4.  **Phase 4: Remote Sync**: If the bridge is active, synchronize with the global configuration state (Service Discovery).

### 1.1 Level 3 Hybrid Logic (Standalone vs. Connected)
For Level 3 services (Analysis/Observation), an additional logic gate is required during Phase 2:
- **If `profile == standalone`**:
    - Initialize local SQLite3 engine.
    - Mount file-system data providers.
    - Disable NATS/Bus initializers.
- **If `profile == production/develop`**:
    - Connect to NATS endpoint.
    - Initialize gRPC remote consumers.
    - Disable local file-based overrides.

## 2. Standard CLI Interface

The following flags are mandatory and handled automatically by the toolbox:

| Flag | Shorthand | Description | Priority |
| :--- | :--- | :--- | :--- |
| `--profile` | `-p` | Selects the config profile (standalone, production, etc.) | Critical |
| `--name` | | Overrides the service identity | High |
| `--host` | | Overrides the listening IP (ignored in Docker) | High |
| `--port` | | Overrides the listening port (ignored in Docker) | High |
| `--conf` | | Path to an explicit configuration file | Medium |
| `--log_level`| | Sets the initial logging threshold (DEBUG, INFO, etc.) | Medium |
| `--key` | | Path to RSA private key for secret decryption | Security |

## 3. Polyglot Implementation Examples

### 🐹 Go
```go
func main() {
    // Toolbox handles --profile and standard flags automatically
    appConfig, err := config.LoadConfig("standalone", nil) 
    // Access custom flags via appConfig.Args.Extra["my-flag"]
}
```

### 🦀 Rust
```rust
fn main() {
    let ac = AppConfig::load_config("standalone", None)?;
    // Access custom flags via ac.cli_args.extras
}
```

### 🐍 Python
```python
def main():
    ac = load_config("standalone")
    # Access custom flags via ac.args.extras
```

### 🧊 C++
```cpp
int main(int argc, char** argv) {
    auto ac = LoadConfig("standalone", argc, argv);
    // Access custom flags via ac->GetArgs().extras
}
```

## 4. The Docker Guard
All toolbox implementations MUST implement the **Docker Guard**. If `DOCKER_ENV=true` or `.dockerenv` is detected, CLI overrides for `--host` and `--port` are ignored to prevent breaking internal network-aware resolution.

---
*Last Updated: 2026-05-08*
*See also: [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Architecture-Patterns]], [[Web-Interface-Integration-Protocol]]*
