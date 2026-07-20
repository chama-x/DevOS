# Agent Skill Routing Decision Tree

This rule set resolves triggering conflicts across the 62 available agent skills in this workspace. 
**When determining which skill to load, follow this decision tree top-to-bottom.**

---

## 1. ERP & Odoo Ecosystem
If the task involves Odoo modules, addons, XML views, or OWL frontend, use this matrix:

- **Is the task about migrating an existing Odoo addon between versions?**
  👉 Load `odoo-migration`
- **Is the task about writing or debugging OWL frontend components/assets?**
  👉 Load `odoo-owl`
- **Are you writing new backend models, controllers, or evaluating code against OCA standards?**
  👉 Load `odoo-development-skill` (for architectural patterns) AND `odoo-rl-rules` (to enforce strict CLI naming/formatting constraints).
- **Are you writing tests for an Odoo module?**
  👉 Load `odoo-test-writer`
- **Are you trying to trace execution flow through Odoo's ORM and controllers?**
  👉 Load `odoo-code-tracer`
- **For all general Odoo workflow questions, debugging, or exploring an unfamiliar Odoo codebase:**
  👉 Load `odoo` (The core workflow skill)

> [!WARNING]
> Do not load `odoo` AND `odoo-development-skill` simultaneously unless explicitly resolving a conflict between Odoo official patterns and OCA strict patterns.

---

## 2. Web Development & Architecture
If the task involves generic web applications, Next.js, or backend architecture:

- **Is the task demanding novel mathematical algorithms or deep architectural tradeoffs?**
  👉 Load `frontier_delegation`
- **Is the task about setting up CI/CD, Kubernetes, or Infrastructure as Code?**
  👉 Load `devsecops-expert`
- **Is the task about integrating Prisma with Next.js?**
  👉 Load `prisma-next`
- **Is the task about testing OpenAPI/GraphQL endpoints for drift?**
  👉 Load `api-contract-tester`
- **Are you preparing to deploy code to production?**
  👉 Load `ship` (Pre-deployment checklist)
- **Are you configuring how the agent itself calls APIs (backoff, retries)?**
  👉 Load `tool-call-resilience`
- **Are you working with Payload CMS (schemas, webhooks, ecommerce)?**
  👉 Load `payload` (Core) or `payload-ecommerce` (If Stripe/Carts are involved).

---

## 3. UI, UX, & Motion Design
If the task involves styling, animation, or user experience heuristics:

- **Is the task about evaluating an e-commerce checkout or product page?**
  👉 Load `baymard-custom` (Strict Baymard Institute e-commerce rules).
- **Is the task about auditing general form usability or dark patterns?**
  👉 Load `ux-heuristics` (Nielsen's 10).
- **Are you building 60fps, award-winning scroll animations using GSAP/Lenis/Framer?**
  👉 Load `awwwards-animations` AND `gsap`.
- **Are you designing standard web motion (pop-ups, modals, page transitions)?**
  👉 Load `motion-design` AND `emil-design-eng`.
- **Are you tasked with auditing a codebase for jank or missing micro-interactions?**
  👉 Load `improve-animations` OR `find-animation-opportunities`.
- **Do you need to know the exact name of an animation effect to search for it?**
  👉 Load `animation-vocabulary`.

---

## 4. Apple Human Interface Guidelines (HIG)
If the task involves native or cross-platform design meant to match Apple standards:

- **Which platform?**
  👉 Load the specific platform skill: `ios`, `macos`, `watchos`, `tvos`, `visionos`, or `ipados`.
- **General Apple aesthetics (translucency, momentum scrolling) on Web:**
  👉 Load `apple-design`.

---

> [!IMPORTANT]
> **Skill Limit Enforcement**: You must strictly limit yourself to 2-3 loaded skills per task. Loading more causes cognitive overlap and degrades performance. See `AGENTS.md` for full Calibration Rules.
