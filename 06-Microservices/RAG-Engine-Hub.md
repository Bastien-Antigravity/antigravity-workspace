---
microservice: rag-engine
type: service-hub
status: active
tags:
- '#service/rag-engine'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🧠 Service Hub: RAG-Engine

*The local search and semantic graph indexer for the Bastien-Antigravity fleet: Multi-tenant, schema-partitioned, and FFI-aligned.*

## 🔗 Knowledge Map
- **Code Repository**: [[09-RAG-Engine]]
- **Architecture & Multi-Tenancy**: [[09-RAG-Engine/quick-overview/Multi-Tenant-RAG-Architecture|Multi-Tenant RAG Architecture]]
- **Features & Flow**: [[09-RAG-Engine/quick-overview/Features-Behavior|RAG Features & Behavior]]
- **Verification Playbook**: [[09-RAG-Engine/quick-overview/Testing-Playbook|RAG Testing Playbook]]
- **General Configuration**: [[09-RAG-Engine/quick-overview/General-Misc|RAG Configuration & Misc]]

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Python-Integration-Specialist|Python-Integration]]
- **Sentinel Sentinel**: [[Prompt-Sentinel|Sentinel]]

## 📊 Database Topology (obsidiandb)
The service stores RAG vectors and codebase structures partitioned into PostgreSQL schemas per-repository workspace (e.g. `01-Strategic-Nexus`, `08-Base-Scripts`, `09-RAG-Engine`). All operations are routed dynamically based on source paths via proxy layers.

---
*Last Audit: [[00-AI-Orchestration/AI-Session-State|Restore Session State]]*
