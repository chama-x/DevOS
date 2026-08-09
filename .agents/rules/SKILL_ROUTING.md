# Skill Routing

*Do not load this file unless a task requires a specialized framework. Skills are configuration profiles, not textbooks.*

**11 skills. Max 2-3 per task. Load only when the skill adds behavioral configuration or fills a specific knowledge gap.**

> **Architectural Principle:** Skills are NOT textbooks. The model already knows general concepts (like Nielsen's heuristics, REST principles, or GSAP documentation). Skills exist ONLY to provide:
> 1. **Configuration Profiles:** "Format the audit this specific way", "Use this specific sequence for deployment".
> 2. **Gap Fillers:** "Here are the strict OCA naming conventions for Odoo that differ from official docs".
> Do NOT load a skill just because the topic matches. Load it only if you need its specific constraints.

---

## Deployment & Infrastructure

- **Shipping to production?** → `ship` (Enforces strict pre-deployment checklist sequence)
- **CI/CD, Kubernetes, IaC, supply-chain security?** → `devsecops-expert` (Enforces specific pipeline sequence and tool constraints)

## Architecture & APIs

- **Entering an unfamiliar codebase and need to map it before touching it?** → `architecture_lens` (Configures Mermaid output depth and focus)
- **Testing OpenAPI/GraphQL contracts for drift?** → `api-contract-tester` (Specific workflow for contract testing)
- **Task requires novel algorithms, deep architectural tradeoffs, or mathematical rigor?** → `frontier_delegation` (Specific orchestration protocol)

## Databases & Backend

- **Next.js + Prisma integration?** → `prisma-next` (Specific Prisma patterns and deviations)

## Odoo

- **Writing Odoo models, controllers, or OCA-standard code?** → `odoo-patterns` AND `odoo-rl-rules` (Bridges the gap between official Odoo docs and strict OCA conventions)
- Do not load both unless you're actively reconciling OCA patterns with CLI constraints.

## UI & Animation

- **GSAP in React/Next.js — ScrollTrigger, timelines, plugins?** → `gsap` (Configures GSAP architecture constraints for this project)
- **Award-quality scroll experiences, custom cursors, 60fps parallax?** → `awwwards-animations` (Sets the quality bar and specific techniques to use/avoid)

## Content & Copywriting

- **Writing product copy, headlines, taglines, or UI text?** → `apple-writing-philosophy` (Enforces strict reasoning process for Apple-style clarity and concreteness)

---

> Skill limit: 2-3 per task. More causes cognitive overlap and degrades output quality. (SkillsBench; arXiv:2602.12670)
