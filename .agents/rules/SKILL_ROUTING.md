---
trigger: always_on
---

# Skill Routing

**13 skills. Max 2-3 per task. Load only when the skill adds something you don't already know.**

Before loading any skill, ask: does this task need specialized knowledge that goes beyond my training? If no — skip the skill and work directly.

---

## Deployment & Infrastructure

- **Shipping to production?** → `ship`
- **CI/CD, Kubernetes, IaC, supply-chain security?** → `devsecops-expert`

## Architecture & APIs

- **Entering an unfamiliar codebase and need to map it before touching it?** → `architecture_lens`
- **Testing OpenAPI/GraphQL contracts for drift?** → `api-contract-tester`
- **Agent tool calls need retry/backoff/circuit-breaker patterns?** → `tool-call-resilience`
- **Task requires novel algorithms, deep architectural tradeoffs, or mathematical rigor?** → `frontier_delegation`

## Databases & Backend

- **Next.js + Prisma integration?** → `prisma-next`

## Odoo

- **Writing Odoo models, controllers, or OCA-standard code?** → `odoo-patterns` AND `odoo-rl-rules`
- Do not load both unless you're actively reconciling OCA patterns with CLI constraints.

## UI & Animation

- **Usability audit, form UX, dark patterns, Nielsen heuristics?** → `ux-heuristics`
- **Standard web motion — transitions, micro-interactions, modals?** → `motion-design`
- **GSAP in React/Next.js — ScrollTrigger, timelines, plugins?** → `gsap`
- **Award-quality scroll experiences, custom cursors, 60fps parallax?** → `awwwards-animations` AND `gsap`

---

> Skill limit: 2-3 per task. More causes cognitive overlap and degrades output quality. (SkillsBench; arXiv:2602.12670)
