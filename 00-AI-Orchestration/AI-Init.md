---
microservice: obsidian-brain
type: governance
status: active
tags:
- '#type/governance'
- '#state/active'
- '#zone/3-fleet'
- '#service/obsidian-brain'
---
# ⚡ AI Initialization: obsidian-brain

> [!IMPORTANT] MANDATORY INITIALIZATION
> Copy and paste this prompt when starting a new session in this vault:
> 
> "1. Read the ecosystem map in **[[Ecosystem-Map-MOC]]**."
> "2. Load project constraints from **[[00-AI-Orchestration/AI-Project-DNA]]**."
> "3. Restore session state from **[[00-AI-Orchestration/AI-Session-State]]**."
> "4. **AI-Ignore Rule**: Immediately ignore any files containing the `#ai/ignore` tag. Do not read them unless explicitly asked."
> "5. **Sentinel Audit**: From the workspace root, run `python obsidian-brain/07-Core-KMS/Scripts/Brain-Health-Audit.py` and resolve any drift."

> [!TIP] Cross-Platform Notes
> - On Windows, use `python` instead of `python3`.
> - Always run scripts from the **workspace root** (`Bastien-Antigravity/`), not from inside `obsidian-brain/`.
> - The Preflight Check runs automatically at squad startup via `start_squad.py`.
