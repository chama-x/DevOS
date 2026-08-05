---
name: "Frontier Delegation (Split-Brain Architecture)"
description: "Orchestrates cognitive delegation between the IDE agent (execution, wiring, verification) and a frontier reasoning model (algorithmic design, architectural innovation, constraint engineering). Trigger when a task demands novel algorithms, mathematical rigor, deep architectural decisions, or research-grounded design tradeoffs that exceed standard implementation patterns."
---

# Frontier Delegation: The Split-Brain Protocol

> **v2 — Calibrated for frontier-grade reasoning models with adaptive thinking, XML-native processing, and sustained long-context coherence.**

---

## The Core Principle

This skill governs a **cognitive division of labor** between two AI modalities:

| Role | Strengths | Weaknesses |
|---|---|---|
| **Frontier Model** (The Architect) | Deep sustained reasoning, novel algorithms, mathematical rigor, spec-first design, long-context coherence, adaptive self-verification | No file access, no compiler, no runtime, cannot verify infrastructure details |
| **IDE Agent** (The Engineer) | File system mastery, live compilation, surgical edits, dependency tracing, iterative debugging, build verification | Limited reasoning depth for novel algorithms, prone to architectural shortcuts |

The handshake protocol between them is the **Constraint Surface**: the set of TypeScript interfaces, branded types, readonly annotations, and design-rationale comments that the Architect exports. The Engineer treats this surface as an unbreakable specification.

> The Architect's most valuable output is NOT the algorithm implementations.
> It IS the interface definitions and type contracts. The types ARE the spec.

### Key Insight: Frontier Models Changed

Legacy prompting patterns (imperative commands, step-by-step forcing, capitalized directives) were designed for earlier generation models that needed explicit scaffolding. Current frontier-grade models with adaptive thinking:

- **Reason internally and deeply** — explicit chain-of-thought prompts are redundant and can degrade output
- **Process XML natively** — XML tags create structural boundaries the model uses to separate context from instructions from output specs
- **Respond better to spec-as-interface** — describe the system contract clearly, not the execution steps
- **Self-correct over long outputs** — they maintain coherence across 2000+ line outputs without degrading
- **Need permission to go long** — without explicit license to produce a complete implementation, they self-limit

The Delegation Packet produced by this skill leverages all five of these properties.

---

## Phase 0 — Cognitive Triage

Before any delegation, classify the task. Not everything needs a frontier model. Not everything can be done without one.

**Delegate to the Frontier Model when the task requires:**
- Novel algorithmic design (scoring functions, ML pipelines, optimization, constraint solvers)
- Mathematical modeling (statistical accumulators, signal processing, Bayesian inference)
- Architectural boundary design (invariant hierarchies, concurrency models, failure mode taxonomy)
- Research-grounded tradeoff analysis (requiring synthesis of real-world evidence, not just patterns)
- Domain-specific type system design (branded types, state machines, discriminated unions)
- Complete module redesigns where the entire implementation is being replaced, not patched

**Keep in the IDE Agent when the task requires:**
- Infrastructure wiring (database setup, state management, API routes, build config)
- UI assembly (component composition, CSS, routing, responsive layout)
- Contract verification (type checking, cross-referencing interfaces, build validation)
- Environment management (package installation, dev server, deployment)
- Iterative debugging (fixing type errors, tracing runtime bugs)
- Simple additive changes where the design is already established

**Partial delegation is allowed.** A task like "add a recommendation engine with a UI" should be split: delegate the engine's algorithm to the Frontier Model, keep the UI and wiring for the IDE Agent.

Confirm the triage with the user via `ask_question`:
```
"I've triaged this task. The [specific subtask] requires frontier-level reasoning
(novel algorithm / architectural design / research synthesis). I'll prepare a
Delegation Packet. The remaining work (infrastructure, UI, wiring)
I'll handle directly. Does this split look right?"
```

---

## Phase 1 — Outbound Handoff (IDE → Frontier)

### 1.1 — Security Gate

Before compiling the packet, grep all target files for credentials, API keys, `.env` references, and tokens. Redact them. Never export secrets to external models.

```bash
grep -rn "sk-\|api_key\|API_KEY\|secret\|password\|token" src/core/
```

### 1.2 — Compile the Delegation Packet

Create an artifact named `frontier_delegation_prompt.md`.

Use the template from `resources/frontier_prompt_template.md` as the structural backbone. The template is XML-first — this is not aesthetic, it is functional. Frontier-grade reasoning models with adaptive thinking process XML tags as semantic boundaries, not as formatting. They use these boundaries to separate role framing from context from constraints from output specifications, maintaining coherence across long, complex outputs.

Make sure to include context on all necessary data points, APIs, internal data APIs, and adherance to current codebase envoirnment so fresh context frontier model can adhere to our setup here better.

The packet has **seven XML sections** in this exact order:

#### `<system>` — Role and Depth Signal

Frame the model's role with precision. The `<system>` tag is the most privileged semantic frame — its content governs the model's operating posture for the entire response.

Include:
- The specific expertise domain (e.g., "computational linguistics and formal language theory")
- That the output will be injected verbatim — "no cleanup, no editing"
- An explicit depth signal: "Let your thinking be comprehensive. Design the type system before writing algorithms. Design the algorithms before writing code."
- Do NOT include command-style directives here — state the context, not the rules

#### `<context>` — Architecture and Boundaries

Provide:
- What module is being built and where it sits in the system architecture
- An ASCII architecture diagram showing the module's seam in the system
- The absolute boundaries (what the module is NOT allowed to do — expressed as design constraints, not commands)
- Which external imports are permitted

#### `<existing_implementation>` — The Starting Point

For evolving modules (not greenfield): paste the current implementation verbatim inside a fenced code block. Provide a brief framing note ("Study this carefully — your design must preserve the exported API surface while replacing the internals"). Do not summarize — the full code gives the model the exact invariants and vocabulary to preserve.

#### `<downstream_contracts>` — Downstream Consumer Types

Paste the exact type signatures of any modules that consume this module's output. These are the non-negotiable interface constraints. The model must see the exact field names, types, and annotations its outputs must satisfy.

#### `<gaps_to_close>` — Specific Failures to Correct

List the specific architectural failures in the current system, with:
- A clear description of the gap
- Concrete failing examples (input → wrong output → correct output)
- The design principle that should govern the fix

This section is the model's primary design brief. It is more important than the objective section — the objective says what to build, this section says what problem to actually solve.

#### `<specification>` — Layer-by-Layer Architecture

Describe each layer of the module in order. For each layer:
- Name it and describe its purpose
- Specify the algorithm class to use (e.g., "Bayesian evidence accumulator", "greedy weighted-interval selection")
- Provide design notes and specific examples of inputs and expected outputs
- Do NOT prescribe implementation code — describe the design contract

This section is where the IDE agent's research and architectural knowledge is distilled into a spec the frontier model can reason against.

#### `<output_contract>` — Exact Exported API

Specify the exact exported names, types, and function signatures the module must export. This is the backward-compatibility guarantee. Include:
- All type and interface names (with exact field names for new interfaces)
- All function signatures (including sync/async nature)
- Any new discriminated union members
- The full shape of any new container types

### 1.3 — The Pause

Once the artifact is generated, stop execution. Tell the user:

```
"The Delegation Packet is ready at frontier_delegation_prompt.md.
Copy its full content into your frontier reasoning model.
Paste the response back here and I'll handle injection, wiring, and verification."
```

---

## Phase 2 — Anchor Code Reception (Frontier → IDE)

When the user pastes the Frontier Model's response:

### 2.1 — Quarantine Branch

Create a checkpoint commit on a working branch before modifying any files:

```bash
git checkout -b agent/frontier-inject-$(date +%Y%m%dT%H%M)
git add -A && git commit -m "chore: checkpoint before frontier injection"
```

### 2.2 — Verbatim Injection

Inject every code block from the Frontier Model's response exactly as-is. Do not:
- Rename variables
- Refactor structure
- Remove comments
- "Clean up" formatting
- Add infrastructure imports

The only permitted modification is adding the file path header comment if the model didn't include one (e.g., `// src/core/brain/module.ts`).

Rationale: The frontier model's comments ARE the architectural documentation. Its naming choices reflect invariants. Silently cleaning either destroys information the IDE agent does not fully understand yet.

### 2.3 — Injection Verification

After injection, run `pnpm build` (or the project's type checker). The anchor code modules should compile in isolation. If they don't:

1. Collect the exact type errors
2. Escalate to the user with the error list
3. Do NOT attempt to fix the anchor code

Anchor code errors are a signal that the Delegation Packet was incomplete (missing a downstream contract, an incorrect type signature, a missing import). The fix goes back to the packet, not into the anchor code.

---

## Phase 3 — Contract Extraction (The Constraint Surface)

This is the critical phase. It produces the integration specification the IDE agent uses for all downstream wiring.

### 3.1 — Extract the Constraint Surface

For each injected anchor module, systematically extract via grep:

```bash
# Exported interfaces (dependency injection points)
grep -n "export interface" src/core/**/*.ts

# Exported types (domain vocabulary — especially branded types and discriminated unions)
grep -n "export type" src/core/**/*.ts

# Function signatures with deps parameters (wiring points)
grep -n "deps:" src/core/**/*.ts

# Invariant comments (correctness/performance constraints)
grep -niE "(invariant|guarantee|<[0-9]+ms|completes in|never throws|always returns|pure function)" src/core/**/*.ts
```

### 3.2 — Build the Constraint Surface Artifact

Create `constraint_surface.md` using this format per module:

```markdown
## Module: src/core/brain/example.ts

### Exports (what it provides):
- `functionName(params): ReturnType`
- Types: `TypeA`, `TypeB`, `InterfaceC`

### Requires (what infrastructure must provide):
- [List each interface the infrastructure layer must implement]

### Sync/Async contracts:
- `functionName` returns `T` (not Promise<T>) → infrastructure implementation MUST be synchronous

### Invariants:
- [Quoted from anchor code comments]

### Wiring points:
- [Each `deps: SomeDeps` parameter, listing what needs to be provided]
```

This artifact is the integration spec. Every item in it becomes a verification checkbox in Phase 5.

---

## Phase 4 — Infrastructure Wiring

### 4.1 — Wiring Plan

Before writing any infrastructure code, create `implementation_plan.md` mapping each Constraint Surface entry to a concrete implementation:

```markdown
| Interface | Concrete Implementation | Sync/Async | Rationale |
|---|---|---|---|
| `ExampleDeps.persist` | Dexie table wrapper | Async (only called by background task) | |
| `ExampleDeps.apply` | Zustand synchronous reducer | Sync (anchor code returns `T`, not `Promise<T>`) | AP-001 pattern |
```

Get user approval on this plan before writing any code. This is where async/sync contract violations (the most common integration bug) are caught cheaply.

### 4.2 — Implementation Rules

These rules are derived from the anti-patterns registered in `references/anti_patterns.md`. Review that file before wiring.

1. **Preserve anchor code types** — never add infrastructure fields to the frontier model's types. Use separate Maps or wrapper types for infrastructure metadata (see AP-002).

2. **Call anchor code functions, don't reimplement them** — if the frontier model provided a function for a workflow, call it. Its invariants are embedded in its implementation (see AP-003).

3. **Honor sync/async contracts** — if the anchor code's interface returns `T` (not `Promise<T>`), the infrastructure implementation must be synchronous. This is the most common integration failure (see AP-001).

4. **Read exact interfaces before wiring** — use `grep_search` to pull the exact type definitions. Never guess prop names, parameter orders, or return types from memory (see AP-004).

---

## Phase 5 — Cross-Reference Audit

After wiring is complete, before presenting results to the user, run this audit checklist against the Constraint Surface artifact from Phase 3.

### 5.1 — Type Contract Verification
- [ ] Every exported interface has a concrete implementation
- [ ] Every function signature matches (sync/async, parameter types, return types)
- [ ] Branded types are preserved — not widened to `string`
- [ ] Readonly annotations are honored — not assigned to mutable arrays

### 5.2 — Invariant Verification
- [ ] Every invariant comment in the anchor code is satisfied by the infrastructure
- [ ] Document HOW each invariant is maintained (e.g., "Write-Through Cache ensures sync contract while IndexedDB mirrors async")

### 5.3 — Anti-Pattern Scan
- [ ] No `as any` casts on anchor code types
- [ ] No anchor code types extended with infrastructure fields
- [ ] No anchor code functions reimplemented instead of called
- [ ] No async wrappers around synchronous contracts

### 5.4 — Mismatch Report

If any mismatches are found, compile them into a structured report artifact before attempting fixes. Present the report to the user. Fix only after approval.

### 5.5 — Build Verification

Run `pnpm build`. At this point, type errors should be infrastructure bugs (Phase 4 work), not contract bugs (anchor code). If the build passes, the Constraint Surface has been fully satisfied.

---

## Phase 6 — Reverse Handoff (Evolution)

When anchor code needs to evolve (new features, bug fixes, design changes), package the following for the frontier model:

1. The current anchor modules (raw text, all files verbatim)
2. The Constraint Surface artifact from Phase 3
3. The concrete infrastructure implementations (so the model understands what downstream code depends on its interfaces)
4. Any mismatch reports, runtime bugs, or user feedback
5. The new requirements, clearly framed

Frame the packet as:
> "Here is your previous architecture. Here is how it was wired by the IDE agent. Here is what the user wants to change. Produce updated anchor code that either preserves all existing interface contracts OR explicitly marks breaking changes with `@deprecated` and replacement interfaces."

This framing leverages the frontier model's sustained-context coherence — it reasons about the full delta from the previous design, not just the new requirements in isolation.

---

## Packet Quality Checklist

Before handing the packet to the user, verify:

- [ ] All secrets scrubbed from embedded code
- [ ] `<system>` tag frames the role and depth signal (no commands, no imperatives)
- [ ] `<context>` tag includes an architecture diagram
- [ ] `<existing_implementation>` contains full verbatim code (no summaries)
- [ ] `<downstream_contracts>` contains exact type signatures (not paraphrases)
- [ ] `<gaps_to_close>` has concrete failing examples per gap
- [ ] `<specification>` describes algorithm classes and design notes, not implementation code
- [ ] `<output_contract>` has exact exported names (not descriptions of names)
- [ ] No capitalized command language: no `YOU MUST`, `NEVER`, `HARD CONSTRAINT`, `CRITICAL`
- [ ] No chain-of-thought forcing: no "think step by step", "list your assumptions first"
- [ ] Explicit license to produce complete output: "If it requires 2000 lines, write 2000 lines"

---

## Quick Reference: The Full Lifecycle

```
┌─────────────────────────────────────────────────┐
│  Phase 0: Cognitive Triage                      │
│  "Does this need the Architect?"                │
└──────────────────────┬──────────────────────────┘
                       │ yes
┌──────────────────────▼──────────────────────────┐
│  Phase 1: Outbound Handoff                      │
│  Security gate → XML packet → User carries      │
└──────────────────────┬──────────────────────────┘
                       │ user returns with output
┌──────────────────────▼──────────────────────────┐
│  Phase 2: Anchor Code Reception                 │
│  Quarantine branch → Verbatim injection         │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  Phase 3: Contract Extraction                   │
│  Build the Constraint Surface artifact          │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  Phase 4: Infrastructure Wiring                 │
│  Wiring Plan → Approval → Implementation        │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  Phase 5: Cross-Reference Audit                 │
│  Verify every contract → Build check            │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  Phase 6: Reverse Handoff (when needed)         │
│  Package full state → User carries back         │
└─────────────────────────────────────────────────┘
```
