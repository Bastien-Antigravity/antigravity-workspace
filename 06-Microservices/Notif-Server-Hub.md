---
microservice: notif-server
type: service-hub
status: active
tags:
- '#service/notif-server'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
---
# 🌐 Service Hub: Notif-Server

*Central Notification Dispatcher: Telegram, Discord, Matrix, Gmail.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 notif-server](https://github.com/Bastien-Antigravity/notif-server)
- **Behavior Specs**: [📜 BDD Specifications](02-Business-BDD/02-Behavior-Specs/notif-server/)

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Go-Systems-Specialist|Go-Systems]]
- **Integration Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Python-Integration-Specialist|Python-Integration]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/notif-server"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```
