---
microservice: obsidian-brain
type: governance
status: active
tags:
- '#zone/3-fleet'
- '#service/obsidian-brain'
- '#type/governance'
- '#state/active'
---
# Knowledge Organization Strategy for Bastien-Antigravity

When dealing with a complex microservice ecosystem, a simple folder hierarchy is insufficient. We need a fluid architecture that supports multiple dimensions: strict categorization, dynamic states, contextual relationships, and algorithmic querying (both for you and me, the AI).

Here is the recommended paradigm for our Obsidian Brain:

## 1. The Core Layers of Organization

Depending on the task, we apply different conceptual layers.

### A. Folders: Structural Boundaries (The "Where")
**Use for:** Broad categorization and strict boundaries. 
**Our Paradigm:** Keep folders shallow. Folders represent the *physical department* of the file. If you have to wonder where a file goes, the folder system is too deep.
*Example:* `01-AI-Assistant/` vs `04-Deployment/`

### B. Tags: Dimensions & States (The "What" and "Status")
**Use for:** Cross-cutting concerns that apply regardless of the folder. Tags allow us to filter files globally.
**Our Paradigm:** Use nested tags.
* Examples of Type Tags: `#type/architecture`, `#type/test-scenario`, `#type/sprint-plan`, `#type/governance`
* Examples of Transversal Tags: `#service/`, `#tech/`, `#tier/`, `#zone/`
* Examples of State Tags: `#state/draft`, `#state/active`, `#state/deprecated`, `#ai/task` 
* Isolation Tags: `#ai/ignore` (Hides document from AI context)

### C. YAML Frontmatter: Programmable Metadata (The "Database")
**Use for:** structured key-value pairs at the very top of your markdown files. Essential for using querying plugins like Dataview.
**Our Paradigm:** Every major system file gets frontmatter so we can track versions and targets.
```yaml
---
microservice: log-server
version: 1.2.0
author: Ruzava
---
```

### D. Bidirectional Links: Conceptual Fabric (The "Why")
**Use for:** connecting ideas contextually. 
**Our Paradigm:** If `log-server` relies on `microservice-toolbox`, the log-server architecture file should include the link `[[05-Microservice-Map]]` or `[[06-Microservices/Microservice-Toolbox-Hub]]`. This naturally builds an interactive dependency graph we can visualize in Obsidian.

---

## 2. Multi-Dimensional Views & Paradigms

How do we view the data depending on the level of complexity we are trying to understand?

### Level 1: The Graph View (Macro / Organic Paradigm)
* **What it is:** Obsidian's native visualizer.
* **When to use:** When you want to see the "Big Picture" or detect forgotten orphans. E.g., visualizing which microservices are highly coupled to `safe-socket` by looking at the node density.

### Level 2: Dataview Matrix (Structured / Algorithmic Paradigm)
* **What it is:** A highly recommended Obsidian Community Plugin that turns Markdown metadata into SQL-like tables.
* **When to use:** Tracking QA or deployment. You can create a file that automatically queries: *"Show me all files tagged `#type/test-scenario` where `status: failed` grouped by `microservice`"*. 

### Level 3: Map of Content (MOC) (Curated / Human Paradigm)
* **What it is:** An index file (like a personalized Wikipedia landing page).
* **When to use:** For onboarding and general navigation. Instead of scrolling through an alphabetical folder list, an MOC is curated. 
*Example MOC format:*
```markdown
# 🗺 AI Microservice Ecosystem MOC
## Core Rules
- [[03-Tech-Stack/03-Project-Coding/00-Coding-Style-Guide]]
- bastien_architecture

## Active Sprints
- Sprint-1-Refactoring-Log-Server
```

## 3. The 5-Dimensional Hybrid System
We employ a fusion of **PARA, Diátaxis, and Zettelkasten** to avoid chaos while maintaining creative flow.

* **WHERE (PARA Method):** Shallow folders (`04-Deployment`). No deep nesting!
* **WHAT & HOW (Diátaxis):** Tags classify the type of knowledge (`#type/tutorial`, `#type/how-to`, `#type/reference`, `#type/architecture`).
* **WHY (Zettelkasten):** Use `Bidirectional Links` to connect concepts to Architecture Decision Records (ADRs) or design philosophies.
* **HOW MANY (Metadata):** YAML frontmatter (`dependencies: 4`, `version: 1.2`) to empower Dataview queries.

## 4. AI Interaction & Session States
As your AI assistant, this system allows us to work together fluidly.

### A. How to initialize a coding session:
* Simply say: *"Read `00-Master-MOC.md` and `AI-Session-State.md` then let's begin."*
* Because I have filesystem access, I automatically load the rules, architecture, and current sprint goals directly from those documents.

### B. Session State Management
We don't need to lose our train of thought between days.
* **Save State:** At the end of a session, ask me to *"Save session state"*. I will summarize our progress, known bugs, and the next steps into `00-AI-Orchestration/AI-Session-State.md`.
* **Restore State:** Next time you engage with me, just say *"Restore session state"*. I will pick up right where we left off based on that file!

---
> [!TIP] Progressive Disclosure (Level-based Organization)
> While atomicity is good for human zettelkasten, for AI interaction, we organize knowledge by **depth levels**. This allows the AI to fetch exactly the context it needs without loading irrelevant details or getting lost in hundreds of tiny files.
> - **Level 1 (Macro)**: High-level concepts, MOCs, and system topologies (e.g., `Ecosystem-Map-MOC`).
> - **Level 2 (Cluster)**: Component or domain-specific documentation (e.g., `Log-Server-Hub`).
> - **Level 3 (Micro)**: Deep implementation details and data structures.
> *Only split information if it genuinely belongs to a different Level of depth. Otherwise, consolidate related info into cohesive documents.*

---

## 5. Ecosystem Patterns & Global Decisions

This section records fundamental architectural and governance choices that apply to the entire Bastien-Antigravity ecosystem.

### A. The "Super-Bridge" Pattern
**Decision Date:** 2026-05-02
**Context:** Multi-language facades (Python, Rust, etc.) were causing "Multiple Go Runtime" panics and memory isolation issues when loading separate shared libraries for logging and configuration.
**Decision:** Consolidated all shared infrastructure into a single binary (`universal-logger`). All language-specific facades now bridge to this single source of truth via CGO.
**Impact:** 100% memory synchronization between Logger and Config; stable FFI boundaries.

### B. The AI Governance Framework
**Decision Date:** 2026-05-02
**Decision:** Implementation of three core governance layers per repository:
1. **AI-Project-DNA.md**: Repository-specific role overlays and intent (The "Compass").
2. **Spec Gate**: Mandatory "Spec-First" protocol. No code implementation without an approved BDD spec in `02-Business-BDD`.
3. **Lifecycle Hardening**: Mandatory branch/version audit at session start via `AI-Init.md` and `AI-Session-State.md`.

### C. The "Spec-First" Protocol
**Role: Spec Specialist**
When the user requests a feature, the AI MUST first act as a "Spec Specialist" to:
1. Identify the target repo folder in `02-Business-BDD/02-Behavior-Specs/`.
2. Draft a detailed Gherkin spec (`Given/When/Then`) based on the user's intent.
3. Account for edge cases and technical constraints.
4. Obtain user approval (`status: approved`) before transitioning to the "Developer" role.

### D. The Documentation Isolation Protocol
**Decision Date:** 2026-05-16
**Context:** AI agents were becoming overwhelmed by human-centric notes, causing context window bloat and task drift.
**Decision:** Implementation of `#ai/ignore` tags and mandatory isolation folders.
1. **Rule:** AI agents MUST ignore any file tagged with `#ai/ignore`.
2. **Standard:** Every repository must have an isolation folder for human-centric documentation.
   - **Fleet Standard**: `quick-overview/`
   - **Brain Specific**: `99-Humans/` (For the `obsidian-brain` repository only).
**Impact:** 100% isolation of technical "Human-only" data; cleaner AI context windows.
