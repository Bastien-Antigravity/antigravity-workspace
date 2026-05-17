--- 
microservice: {{microservice}}
type: idea-pitch
status: pending
role: orchestrator
tags:
- "#tech/TO-DO"
- "#tier/TO-DO"
- "#zone/TO-DO"
- #service/{{microservice}}
- '#type/idea-pitch'
- '#state/pending'
---
# Idea Pitch: [Feature/Bug Name]

## 1. Feature Description
*Explain in plain language what you want to achieve or what bug you are experiencing.*
- 

## 2. Expected Behavior (BDD)
*Provide a high-level Given/When/Then expectation so the QA Agent knows exactly what to test for later.*
- **Given** [Initial State]
- **When** [Action]
- **Then** [Expected Output]

## 3. Target Microservices
*If you know which microservices need to be touched, list them here. If not, the Orchestrator will figure it out.*
- [ ] `config-server`
- [ ] `log-server`
- [ ] `sandbox-testing`
- [ ] Other: ...

---
*Once this file is filled out and saved in `Inbox/`, the Orchestrator will analyze it. Simple tasks (Score 1-2) will be **Fast-Tracked** directly to implementation, while complex tasks (Score 3+) will generate a full Master Plan.*
