# DevOS Examples

Real-world code and execution examples demonstrating how the DevOS context files transform agent behavior. Each example shows what default LLM agents commonly do wrong, and how DevOS forces them to act correctly.

---

## 1. IDENTITY.md: Setting Project Boundaries

**User Request:** "Add a date picker to the booking form."

**❌ What Default LLMs Do (The "Clever" Trap)**
They immediately run `npm install react-datepicker` or start building a complex custom component, introducing unnecessary dependencies and bloat because they assume "more is better."

**✅ What DevOS Does (Guided by IDENTITY.md)**
Before taking action, the agent reads `rules/IDENTITY.md`, which contains the following user-defined anti-pattern:
> What We Don't Do:
> - No custom date pickers — native HTML input only.

```
[Agent Output]
I will add a native HTML `<input type="date">` to the booking form, adhering to the anti-pattern in IDENTITY.md to avoid custom date pickers.
```
*Result: The agent delivers exactly what the project needs, without the user having to re-explain their preferences.*

---

## 2. GROUNDING.md: Scope Discipline

**User Request:** "Fix the typo in the checkout header."

**❌ What Default LLMs Do (Scope Creep)**
While fixing the typo, the agent notices the component isn't using the latest React hooks or Tailwind syntax. It rewrites the entire file, breaking three unrelated tests in the process.

**✅ What DevOS Does (Guided by GROUNDING.md)**
The agent follows the `GROUNDING.md` directive on Scope Discipline:
> "Name what you're changing AND what you're leaving alone... Don't refactor adjacent code. Fix only your own mess."

```
[Agent Output]
I will fix the typo in the checkout header. I am deliberately leaving the rest of the file untouched, including the legacy class components, to maintain strict scope discipline.
```
*Result: The bug is fixed with zero collateral damage. The human's trust in the agent grows.*

---

## 3. worklog.md: Cross-Session Continuity

**User Request:** "Continue with the payment integration we started yesterday."

**❌ What Default LLMs Do (Amnesia)**
The agent asks: "What payment integration? What stack are we using? Do you have the API keys?" The user has to spend 10 minutes re-explaining the entire context.

**✅ What DevOS Does (Guided by worklog.md)**
Upon waking up in a fresh session, the agent automatically reads `.agents/worklog.md` and orientates itself.

```
[Agent Output]
Orienting from worklog.md: Yesterday, we successfully implemented the Stripe checkout session endpoint. The next pending task is to handle the `checkout.session.completed` webhook. I'll begin drafting the webhook handler now.
```
*Result: The agent picks up exactly where it left off. The workflow is uninterrupted.*

---

## 4. Configuration Skills: Strict Behavior Enforcement

**User Request:** "Set up the CI/CD pipeline for this repo."

**❌ What Default LLMs Do (Improvisation)**
The agent creates a basic GitHub Actions workflow that builds the code and runs tests. It completely forgets to add security scanning or provenance, because it wasn't explicitly told to do so in the prompt.

**✅ What DevOS Does (Guided by `devsecops-expert` skill)**
The agent recognizes this is an infrastructure task and loads the `devsecops-expert` skill, which acts as a strict configuration profile.

```
[Agent Output]
Following the DevSecOps pipeline sequence configuration: I am adding Trivy for secret scanning as the very first step, before any dependencies are installed. I am also adding Sigstore provenance generation to the final step.
```
*Result: The agent produces a production-ready, highly secure pipeline that adheres to enterprise standards, without the user needing to be a security expert.*
