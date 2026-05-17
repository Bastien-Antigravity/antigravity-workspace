---
microservice: ontime-scheduler
type: service-hub
status: active
tags:
- '#service/ontime-scheduler'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Ontime-Scheduler

*The ecosystem-wide task scheduler and job execution engine.*

## 🏗️ Architecture
- **Language**: Go
- **Transport**: SafeSocket (TCP)
- **Persistence**: SQLite (Local State)

## 🔗 Knowledge Map
- **Behavior Specs**: [[02-Business-BDD/02-Behavior-Specs/ontime-scheduler/FEAT-001-Go-Migration|📜 BDD Specifications]]
- **GitHub**: [📂 ontime-scheduler](https://github.com/Bastien-Antigravity/ontime-scheduler)
- **CI/CD**: [[05-Fleet-Operation/05-Fleet-Strategy/04-CICD-Standards|CI/CD Standards]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/ontime-scheduler"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
