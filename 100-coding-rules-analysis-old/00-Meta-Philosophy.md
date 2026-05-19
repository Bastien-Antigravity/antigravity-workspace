# Bastien-Antigravity Ecosystem: Core Concepts & Architectural Philosophy

The Bastien-Antigravity fleet operates under a strict, language-agnostic architectural philosophy. Whether writing Python, Go, Rust, or C++, the fundamental principles of system design remain constant.

## 1. Aggressive Decoupling via Interfaces (The Facade & Provider Pattern)
Components are strictly prohibited from instantiating their own dependencies. 
- **Dependency Injection**: Services receive `Logger`, `ConfigProvider`, `IDataSource`, and network managers directly into their constructors.
- **Universal Logging Principle**: Services do not depend on concrete logging libraries (like the deprecated `flexible-logger`). Instead, they implement against a standardized `interfaces.Logger` facade, ensuring metadata, timestamping, and client identification are automatically aligned across the fleet.

## 2. Defensive Network Resilience
No microservice assumes stable connectivity. 
- **Toolbox Standardization**: All networking must pass through the `microservice-toolbox` wrappers.
- **Mandatory Retry Logic**: Network requests must implement **Multiplicative Backoff**, **Randomized Jitter** (to prevent thundering herds on recovery), and **Indefinite Retry Support** for critical dependencies to ensure the fleet can cold-boot autonomously.
- **Fail-Safe Initialization**: System bootstraps gracefully handle initial fetch failures (logging a warning rather than panicking), allowing secondary fallback loops to take over.

## 3. Environment Awareness (Docker Guard)
Every connectivity layer contains "Docker Guard Logic".
- If `/.dockerenv` or `DOCKER_ENV` is detected, specific local bindings (like `127.0.0.1`) are aggressively overridden to `0.0.0.0`. This ensures container-to-host orchestration works flawlessly in Kubernetes/Docker without requiring manual configuration tweaks.

## 4. Strict Data Model Demarcation
- **The "M" Prefix**: All pure data structures and message schemas must be prefixed with an `M` (e.g., `models.MConfig`, `models.MAggregation`, `models.MStockPrice`). This instantly differentiates memory structs from behavioral classes across all languages.
- **The "I" Prefix**: All contracts are prefixed with `I` (e.g., `ICalculator`, `IDataSource`) to enforce interface segregation.

## 5. Visual Source Organization
Across all languages, vertical readability is enforced using standardized character dividers (e.g., `# ----------` or `// ---------`). Code must look uniform regardless of the underlying compiler.
