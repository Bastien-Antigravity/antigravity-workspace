# 🐹 Go (Golang) Standards
*Focus areas: High-Concurrency Brokers, Orchestration, Configuration Servers, Ingestion pipelines*

## 1. Constructor Registration Pattern
Brokers and core components utilize an `init()` registration pattern. This allows dynamic instantiation based on configuration without hardcoding dependencies, facilitating the Facade pattern.

```go
func init() {
	Register("finnhub", NewFinnhub)
}
```

## 2. Dependency Injection & Interface Segregation
- **Facades**: Extensive use of Facades (e.g., `AnalysisFacade` in `market-observer`) to abstract complex domain logic away from orchestration sequences.
- **Interfaces**: High reliance on interfaces (e.g., `unilog_interfaces.Logger`, `interfaces.ISerializer`). Interfaces are passed directly into constructors to ensure strict decoupling, returning `interfaces.IBroker` or `interfaces.IDataSource`.

## 3. Environment & Orchestration Guard Logic
Networking tools contain explicit logic to detect orchestration environments. 
If the application detects Docker execution, local bindings are forcefully overridden to `0.0.0.0` to ensure Kubernetes port mapping functions flawlessly, overriding potentially erroneous configuration file settings.

## 4. Visual Dividers
Go code uses structural dividers for logical blocks to mimic the visual structure established in Python:
`// -----------------------------------------------------------------------------`

## 5. Structs and Pointers
Consistent use of pointers for complex configuration structures (`*models.MDataSourceConfig`) to avoid unnecessary allocations, while keeping primitive state returns passed by value.
