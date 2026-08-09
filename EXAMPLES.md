# DevOS Examples

Four requests, run twice — once with a stock agent, once with DevOS
context files loaded. Each pair traces the exact line that changed the
outcome.

---

## 1. IDENTITY.md: Setting Project Boundaries

**User Request:** "Add a date picker to the booking form."

**❌ What Default LLMs Do (The "Clever" Trap)**

They run `npm install react-datepicker`, or hand-roll a custom component —
new code for something the browser already does natively.

**✅ What DevOS Does (Guided by IDENTITY.md)**

Before acting, the agent reads `rules/IDENTITY.md`, which contains this
user-defined anti-pattern:

> What We Don't Do:
> - No custom date pickers — native HTML input only.

```
[Agent Output]
I will add a native HTML `<input type="date">` to the booking form, adhering to the anti-pattern in IDENTITY.md to avoid custom date pickers.
```

*Result: Zero new dependencies. Nothing to re-explain next time.*

---

## 2. GROUNDING.md: Scope Discipline

**User Request:** "Fix the typo in the checkout header."

**❌ What Default LLMs Do (Scope Creep)**

Fixing the typo, it also notices outdated hooks and old Tailwind syntax
nearby — and rewrites the whole file. Three unrelated tests break.

**✅ What DevOS Does (Guided by GROUNDING.md)**

The agent follows the `GROUNDING.md` directive on Scope Discipline:

> "Name what you're changing AND what you're leaving alone... Don't
> refactor adjacent code. Fix only your own mess."

```
[Agent Output]
I will fix the typo in the checkout header. I am deliberately leaving the rest of the file untouched, including the legacy class components, to maintain strict scope discipline.
```

*Result: One line changed. Three tests still pass.*

---

## 3. LOG.md: Cross-Session Continuity

**User Request:** "Continue with the payment integration we started
yesterday."

**❌ What Default LLMs Do (Amnesia)**

The agent asks: "What payment integration? What stack are we using? Do
you have the API keys?" The user spends 10 minutes re-explaining context
it already gave.

**✅ What DevOS Does (Guided by LOG.md)**

In a new session, before responding, the agent reads
`.agents/LOG.md`.

```
[Agent Output]
Orienting from LOG.md: Yesterday, we successfully implemented the Stripe checkout session endpoint. The next pending task is to handle the `checkout.session.completed` webhook. I'll begin drafting the webhook handler now.
```

*Result: Zero re-explaining. Zero minutes lost.*

---

## 4. Configuration Skills: Strict Behavior Enforcement

**User Request:** "Set up the CI/CD pipeline for this repo."

**❌ What Default LLMs Do (Improvisation)**

A basic GitHub Actions workflow: build, test. No security scanning, no
provenance — nothing that wasn't spelled out in the prompt.

**✅ What DevOS Does (Guided by `devsecops-expert` skill)**

The agent matches the task to infrastructure work and loads the
`devsecops-expert` skill — a fixed configuration profile, not a
suggestion.

```
[Agent Output]
Following the DevSecOps pipeline sequence configuration: I am adding Trivy for secret scanning as the very first step, before any dependencies are installed. I am also adding Sigstore provenance generation to the final step.
```

*Result: Secret scanning before install. Provenance before ship. The two
steps default agents skip.*
