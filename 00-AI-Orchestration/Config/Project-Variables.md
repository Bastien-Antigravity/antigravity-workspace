---
microservice: ecosystem-core
type: configuration
status: active
ecosystem_name: Bastien-Antigravity
architecture_rules_path: 03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules.md
coding_standards_path: 03-Tech-Stack/03-Project-Coding/00-Coding-Style-Guide.md
behavior_specs_path: 02-Business-BDD/02-Behavior-Specs
domain_glossary_path: 02-Business-BDD/01-Domain-Glossary/00-Glossary.md
master_moc_path: Ecosystem-Map-MOC.md
tag_taxonomy_path: 00-AI-Orchestration/Config/tags.yaml
process_manifest_path: 00-AI-Orchestration/Config/process-manifest.json
mode_manual_path: 00-AI-Orchestration/Config/MODE-MANUAL.md
session_state_path: 00-AI-Orchestration/AI-Session-State.md
roles_path: 07-Core-KMS/Role-Prompts
templates_path: 00-AI-Orchestration/Templates
scripts_path: 08-Base-Scripts
labs_brain_path: 04-Rapid-Prototyping
ops_brain_path: 05-Fleet-Operation
tags:
- '#zone/0-orchestration'
- '#service/ecosystem-core'
- '#type/configuration'
- '#state/active'
---
# ⚙️ Project Context & Variables

This registry defines the core identity and path mappings for the Bastien-Antigravity ecosystem. 

AI agents MUST read this file at initialization to resolve the location of governance protocols, architectural rules, and operational registries.

## 🗺️ Key Mappings
- **Registry**: [[00-AI-Orchestration/Config/process-manifest.json|Process Manifest]]
- **Taxonomy**: [[00-AI-Orchestration/Config/tags.yaml|Global Tag Taxonomy]]
- **Protocol**: [[00-AI-Orchestration/Config/MODE-MANUAL|MODE-MANUAL]]
- **State**: [[00-AI-Orchestration/AI-Session-State|AI Session State]]
