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
# 📜 Unified Control Protocol (gRPC/REST Parity)

This protocol mandates that all control and configuration capabilities in the Bastien Ecosystem MUST be accessible via both **gRPC** (for internal automation) and **REST/HTTP** (for the Web Interface).

## 1. The Dual-Interface Mandate

To ensure complete flexibility and decoupled orchestration:
- **tele-remote**: Uses the **gRPC** interface for automated fleet control and remote CLI commands.
- **web-interface**: Uses the **REST/HTTP** interface for user-driven management and dashboard configuration.

**Core Rule**: Every business function that modifies service state or configuration MUST be implemented as a shared internal function that is called by both the gRPC server and the HTTP/REST handler.

## 2. Implementation Pattern (Go)

Services should use a "Service Layer" or "Core" that remains protocol-agnostic.

```go
// Shared logic
func (s *Service) SetConfiguration(newConfig Config) error {
    // ... validation and state update ...
}

// gRPC implementation
func (g *GrpcServer) UpdateConfig(ctx context.Context, req *pb.ConfigReq) (*pb.ConfigResp, error) {
    err := g.core.SetConfiguration(req.ToDomain())
    // ... return response ...
}

// REST implementation
func (h *HttpHandler) UpdateConfig(w http.ResponseWriter, r *http.Request) {
    // ... parse json ...
    err := h.core.SetConfiguration(parsedConfig)
    // ... return json/htmx ...
}
```

## 3. Standard gRPC Controller

Every microservice MUST implement the standard `ProcessController` for lifecycle management, but specialized control (e.g., "Start Ingestion", "Flush Buffer") must also follow the parity rule.

## 4. Discovery & Documentation

- All exposed control APIs MUST be listed in the microservice's `ARCHITECTURE.md`.
- Parity violations (features available in gRPC but not REST, or vice versa) are considered **Architectural Drift**.

---
*Last Updated: 2026-05-09*
*See also: [[Global-Architecture-Rules]], [[Web-Interface-Integration-Protocol]], [[Tele-Remote-Hub]]*
