---
microservice: obsidian-brain
type: configuration
status: active
ecosystem_name: Bastien-Antigravity
architecture_rules_path: 03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules.md
coding_standards_path: 03-Tech-Stack/03-Project-Coding/00-Coding-Style-Guide.md
behavior_specs_path: 02-Business-BDD/02-Behavior-Specs
domain_glossary_path: 02-Business-BDD/01-Domain-Glossary/00-Glossary.md
master_moc_path: Ecosystem-Map-MOC.md
tag_taxonomy_path: 07-Core-KMS/tag_taxonomy.md
roles_path: 07-Core-KMS/Role-Prompts
templates_path: 00-AI-Orchestration/Templates
labs_brain_path: 04-Rapid-Prototyping
ops_brain_path: 05-Fleet-Operation
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#state/active'
- '#type/configuration'
---
# Project Context Map

This file links the agnostic `00-AI-Engine` to the specific project it is currently embedded in.

When an AI Agent is instantiated, it MUST read the YAML frontmatter of this file to understand:

1. The `ecosystem_name` it is working on.
2. The paths to the critical rule documents.
