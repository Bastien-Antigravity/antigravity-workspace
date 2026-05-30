---
title: TESTING - obsidian-brain
type: ritual
status: active
microservice: obsidian-brain
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#state/active'
- '#type/ritual'
---
# 🧪 Testing Playbook: Obsidian Brain

## Knowledge Testing
- **Link Integrity**: Use Obsidian's built-in tools or scripts in `07-Core-KMS` to find broken links.
- **Metadata Compliance**: Run the Sentinel audit to verify YAML frontmatter.

## Script Testing
- **Squad Launcher**: Run `./08-Base-Scripts/start_squad.py` to verify engine availability.
- **RAG Engine**: Test semantic queries via the FastMCP server tools.

## Rituals
- **Brain-Health-Audit**: Run `python obsidian-brain/07-Core-KMS/Scripts/Brain-Health-Audit.py` regularly.
