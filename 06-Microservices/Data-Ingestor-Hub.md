---
microservice: data-ingestor
type: service-hub
status: active
tags:
- '#service/data-ingestor'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Data-Ingestor

*Pipeline for high-volume data transformation and storage.*

## 🚀 Status: Integrated & Standardized
- **Logger**: Integrated with `universal-logger` for ecosystem-wide telemetry.
- **Config**: Using `microservice-toolbox` for layered configuration and lifecycle management.
- **Initialization**: Following the standard `AI-Init.md` and `AI-Project-DNA.md` patterns.

## 🔗 Knowledge Map
- **Code Repository**: [📂 data-ingestor](https://github.com/Bastien-Antigravity/data-ingestor)
- **Behavior Specs**: [[02-Business-BDD/Behavior-Specs-MOC]]

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Go-Systems-Specialist|Go-Systems]]
- **Data Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Timescale-Data-Specialist|Timescale-Data]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/data-ingestor"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
