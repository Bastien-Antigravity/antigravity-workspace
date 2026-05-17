---
microservice: docker-deployment
type: service-hub
status: active
tags:
- '#service/docker-deployment'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Docker-Deployment

*Infrastructure Orchestration and Fleet-wide Deployment.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 docker-deployment/](../docker-deployment/)
- **Architecture**: [[03-Tech-Stack/04-Project-Deployment/01-Docker-Infrastructure|🏛️ Docker Infrastructure Standards]]
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/docker-deployment/)
- **Deployment Logs**: [📜 Deployment Logs](https://github.com/Bastien-Antigravity/05-Fleet-Operation)

## 🛠️ Squad Assignment
- **Fleet Architect**: [[07-Core-KMS/Role-Prompts/05-FleetArchitect/Prompt-Fleet-Architect|Fleet-Architect]]
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/docker-deployment"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
