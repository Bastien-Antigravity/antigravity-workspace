---
microservice: sandbox-testing
type: service-hub
status: active
tags:
- '#service/sandbox-testing'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Sandbox-Testing

*Central Validation Hub for Behavioral Behavioral Testing.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 sandbox-testing/](../sandbox-testing/)
- **Architecture**: [[03-Tech-Stack/02-Project-Architecture/10-Testing-Sandbox-Standards|🏛️ Testing & Sandbox Standards]]
- **Behavior Specs**: [[02-Business-BDD/Behavior-Specs-MOC]]
- **Scenario Orchestrator**: `03-Orchestration/scenario_orchestrator.py`
- **Primary Tool**: `Makefile` (Root entry point)

## 📐 Project Structure (2-Digit Standard)
- **`00-Environment`**: Infrastructure topologies and NATS configs.
- **`01-Specifications`**: YAML scenario definitions.
- **`02-Scenarios`**: Polyglot validation logic (Go, Python).
- **`03-Orchestration`**: Management engine and lifecycle scripts.
- **`04-Reporting`**: Test logs and audit results.

## 🛠️ Squad Assignment
- **QA Specialist**: [[07-Core-KMS/Role-Prompts/04-QA/Prompt-QA|QA-Specialist]]
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/sandbox-testing"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
