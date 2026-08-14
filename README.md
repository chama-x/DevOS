# GroundRules
### Two files. ~250 tokens. Zero drift.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Zero Runtime](https://img.shields.io/badge/runtime-zero%20dependencies-brightgreen.svg)]()

AI coding agents don't fail from lack of intelligence. They fail from lack of boundaries.

Without explicit project invariants, frontier models default to three behaviors:
- **Silent Assumptions:** Guessing architecture on ambiguous tasks rather than asking.
- **Speculative Code:** Writing unrequested factories, wrappers, and adjacent refactors.
- **Version Confabulation:** Importing APIs from pre-training memory instead of installed packages.

GroundRules fixes all three with two flat Markdown files in `.agents/rules/`.

```bash
npx create-groundrules
```

Zero runtime. Zero dependencies. Works natively with **Antigravity**, **Claude Code**, **Cursor**, **GitHub Copilot**, and **Windsurf**.

---

## Why Facts Beat Commands

Prompt frameworks shout imperative rules at the model:
> *"YOU MUST NEVER USE RAW SQL AND YOU MUST ALWAYS CHECK PACKAGE.JSON!"*

As conversation context grows, models negotiate with imperative commands and drift.

GroundRules states boundaries as **settled codebase reality**:
> *"Database access: Supabase JS client only. Raw SQL does not exist in this codebase."*
> *"Dependencies: The lockfile is the sole source of truth for packages."*

When stated as environmental facts, the model treats them as immutable laws of physics. Adherence stays high across long sessions with zero prompt tension.

---

## The Architecture

```
AGENTS.md                      → Universal router pointing agents to guardrails
.agents/
└── rules/
    ├── IDENTITY.md            → Settled project boundaries & "What We Don't Do"
    └── GROUNDING.md           → 4 cognitive invariants
```

### 1. `IDENTITY.md` — Project Invariants
```markdown
## Non-Negotiable Invariants
- Database access: Supabase JS client only. Raw SQL does not exist in this repo.
- Auth boundaries: Authentication files are human-managed and read-only.
- Dependencies: Only packages present in `package-lock.json` exist.
```

### 2. `GROUNDING.md` — Cognitive Invariants
```markdown
## 1. Ambiguity & Autonomy Threshold
- Standard Implementation: Use native intelligence on routine tasks without pausing.
- Architectural Crossroads: When a task involves major structural trade-offs, surface concrete choices via `ask_question`.

## 2. Epistemic Baseline
Import versions derive strictly from `package-lock.json`. If a package is not in the lockfile, it does not exist in this project.

## 3. Scope & Abstraction
Code changes are minimal and surgical. The codebase contains no wrapper factories or unused utilities.

## 4. Communication Rhythm
Responses lead directly with code diffs and verified terminal output. Conversational preambles are omitted.
```

---

## Quickstart

### Interactive (5 seconds)
```bash
npx create-groundrules
```
*Prompts for stack, test command, and your non-negotiables, then creates the files.*

### Manual (Clone Template)
```bash
npx degit chama-x/GroundRules/template .
```

---

## Universal Portability

GroundRules is not an execution harness. It manages no API keys and runs no background daemons.

It is a pure Git-committed specification. Whether your team runs Antigravity, Claude Code, Cursor, or Copilot, every agent reads the exact same project reality.

---

[Contributing](.github/CONTRIBUTING.md) · [Code of Conduct](.github/CODE_OF_CONDUCT.md) · [Changelog](CHANGELOG.md) · [License](LICENSE)
