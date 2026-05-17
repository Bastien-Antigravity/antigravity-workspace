--- 
microservice: {{microservice}}
type: task-plan
status: pending
role: orchestrator
tags:
- "#tech/TO-DO"
- "#tier/TO-DO"
- "#zone/TO-DO"
- #service/{{microservice}}
- '#type/task-plan'
- '#state/pending'
---
# Master Plan: [Feature/Bug Name]

## 1. Goal Overview
*A brief summary of what the user wants to achieve.*

## 2. Context & Constraints
*Links to relevant Domain Dashboards, existing issues, or user-defined constraints.*

## 3. Hand-off Tasks
*The breakdown of what each subsequent role needs to do.*

### 🛠️ Architect Tasks
- [ ] Read existing implementation of `[Service Name]`
- [ ] Define interfaces for `[Feature]`
- [ ] Output `Template-02-Architecture-Blueprint.md`

### 💻 Developer Tasks
- [ ] Implement Go/Rust/Python logic according to Blueprint.
- [ ] Add inline documentation.

### 🧪 QA Tasks
- [ ] Write integration test in `sandbox-testing` for `[Feature]`.

### 🚀 DevOps Tasks
- [ ] (If applicable) Update Dockerfile/Config for `[Feature]`.

## 4. Next Step
Pass this document to the **Architect**.
