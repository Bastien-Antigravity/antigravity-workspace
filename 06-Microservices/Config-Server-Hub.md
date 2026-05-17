---
microservice: config-server
type: service-hub
status: active
tags:
- '#service/config-server'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Config-Server

*The Central Nerve System for Configuration Distribution.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 config-server](https://github.com/Bastien-Antigravity/config-server)
- **Architecture**: config-server/ARCHITECTURE.md
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/config-server/)
- **Action Plan**: [📅 Local TODO](https://github.com/Bastien-Antigravity/config-server/blob/develop/TODO.md)

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Go-Systems-Specialist|Go-Systems]]
- **Data Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Timescale-Data-Specialist|Timescale-Data]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/config-server"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
