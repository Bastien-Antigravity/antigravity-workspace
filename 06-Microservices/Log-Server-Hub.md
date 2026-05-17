---
microservice: log-server
type: service-hub
status: active
tags:
- '#service/log-server'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Log-Server

*High-Performance ordered logging and rotation engine.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 log-server](https://github.com/Bastien-Antigravity/log-server)
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/log-server/)
- **Protocols**: log-server/capnp/logger.capnp

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[Rust-Safety-Specialist|Rust-Safety]]
- **Systems Specialist**: [[CPP-Low-Latency-Specialist|CPP-Low-Latency]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/log-server"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

## 🏗️ Architecture Decision Records (ADR)

### ADR-001: Liveness over Completeness (Gap Timeout)
*   **Context**: Out-of-order delivery via TCP/UDP can cause sequence gaps in the BTreeMap buffer.
*   **Decision**: Enforce a **500ms timeout** on missing sequences. If the missing sequence doesn't arrive within this window, the server forces progress to the next available sequence.
*   **Rationale**: Service availability is prioritized over perfect sequential integrity. A blocked writer stops the entire fleet from logging (back-pressure).
*   **Consequence**: Small gaps in logs are possible under high packet loss, but service uptime is guaranteed.
