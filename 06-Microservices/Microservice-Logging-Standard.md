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
# 📜 Microservice Logging Standard

This protocol defines the standardized logging behavior for all microservices in the Bastien Ecosystem. It ensures observability, traceability, and security across all supported languages (Go, Rust, Python, C++).

## 1. Core Principles

- **Standardized Identity**: Every service MUST identify itself using its Program Name (via `microservice-toolbox`).
- **Traceability**: All logs MUST propagate a `X-Bastien-Mission-ID` (Trace ID) across service boundaries.
- **Security**: NEVER log PII, secrets, or raw credentials. Use the `ENC(...)` pattern for sensitive config.
- **Non-Blocking**: Heavy I/O logging SHOULD be offloaded to background tasks where performance is critical.

## 2. Log Levels & Usage

| Level | Description | Usage Example |
| :--- | :--- | :--- |
| **DEBUG** | Detailed diagnostic information. | Variable states, packet dumps (non-sensitive). |
| **INFO** | General operational milestones. | Service start/stop, successful high-level actions. |
| **WARNING** | Unusual but non-critical events. | Retries, fallback strategies, potential config issues. |
| **ERROR** | Failed operations that require attention. | Database connection failure, API request failure. |
| **CRITICAL**| System-wide failures or crashes. | Panic recovery, unrecoverable data corruption. |

## 3. Mission Traceability

All logs MUST include the `Mission-ID` in their context. This ID is generated at the entry point of the ecosystem (e.g., `web-interface` or `tele-remote`) and passed through gRPC metadata or HTTP headers.

### 🐹 Go Implementation
```go
// Injected into universal-logger context
logger.Info("[Mission: %s] Processing order...", missionID)
```

## 4. HTTP Service Logging (Standard Format)

Every HTTP-based microservice MUST implement a logging middleware that outputs requests in the following standardized format (Nginx/Gunicorn style):

`{remote_addr} - - [{timestamp}] "{method} {path} {proto}" {user_agent} {duration}`

## 5. Polyglot Initialization

Logging MUST be initialized via the `universal-logger` facade, typically orchestrated by the `microservice-toolbox` during Phase 4 of the Startup Protocol.

### 🐹 Go
```go
_, logger := unilog.InitWithOptions(unilog.BootstrapOptions{
    Name:            "my-service",
    ConfigProfile:   appConfig.Profile,
    InitialLogLevel: "INFO",
})
```

---
*Last Updated: 2026-05-09*
*See also: [[Microservice-Startup-Protocol]], [[Global-Architecture-Rules]], [[Universal-Logger-Hub]]*
