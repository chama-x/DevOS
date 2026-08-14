# GroundRules
### Set boundaries for your AI coding agent in 5 seconds.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![Zero Runtime](https://img.shields.io/badge/runtime-zero%20dependencies-brightgreen.svg)]()

Default AI coding agents suffer from 3 inherent behavioral failure modes:
1. **Silent Assumptions:** Guessing your architecture instead of asking when requirements hit breaking trade-offs.
2. **Speculative Abstractions:** Writing unrequested factories, helper sprawl, and premature refactors.
3. **Hallucinated Imports:** Guessing library versions from training memory instead of checking what is installed.

**GroundRules** fixes all three using 2 minimal, factual Markdown files (~250 tokens total).

```bash
npx create-groundrules
```

Zero runtime. Zero dependencies. Works natively with **Antigravity**, **Claude Code**, **Cursor**, **GitHub Copilot**, and **Windsurf**.

---

## The 2-File Architecture

```
AGENTS.md                      → Root router pointing to your guardrails
.agents/
└── rules/
    ├── IDENTITY.md            → Tech stack, test command, & non-negotiable boundaries
    └── GROUNDING.md           → 4 factual cognitive invariants (No guessing, verify lockfiles)
```

### 1. `IDENTITY.md` (Settled Boundaries)
*Facts, not commands. Models resist drift significantly better when rules are stated as settled codebase reality.*

```markdown
## Non-Negotiable Invariants
- Database access: Supabase JS client only. Raw SQL does not exist in this repo.
- Auth boundaries: Authentication files are human-managed and read-only.
- Dependencies: Only packages present in `package-lock.json` exist. No unrequested libraries.
```

### 2. `GROUNDING.md` (Cognitive Invariants)

```markdown
## 1. Ambiguity & Autonomy Threshold
- Standard Implementation: Use native intelligence to make sensible default choices on routine tasks without pausing.
- Architectural Crossroads: When a task involves major structural trade-offs, surface concrete choices via `ask_question`.

## 2. Epistemic Baseline
Import versions derive strictly from `package-lock.json`. If a package is not in the lockfile, it does not exist in this project.

## 3. Scope & Abstraction
Code changes are minimal and surgical. The codebase contains no wrapper factories or unused utilities.

## 4. Communication Rhythm
Responses lead directly with code diffs and verified terminal output. Conversational preambles are omitted.
```

---

## Installation

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

## Why GroundRules Works

Most agent prompt frameworks over-constrain the model with prescriptive micromanagement, leading to instruction paralysis.

GroundRules uses **Perimeter-Based Freedom**:
- **Full Internal Autonomy:** The agent uses its full reasoning power to design the best solution without being micromanaged.
- **Hard Perimeters:** Protects your project's high-risk boundaries (`IDENTITY.md`) and stops hallucinations without adding friction.
- **Zero System Prompt Conflict:** Integrates seamlessly with your IDE's native planning modes and tool calling.

---

[Contributing](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md) · [Changelog](CHANGELOG.md) · MIT License
