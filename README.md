# GroundRules
### Set boundaries for your AI coding agent in 5 seconds.

Default AI agents suffer from 3 annoying habits:
1. **Silent Assumptions:** Guessing your architecture instead of asking when requirements are ambiguous.
2. **Speculative Abstractions:** Writing unrequested factories, helper sprawl, and premature refactors.
3. **Hallucinated Imports:** Guessing library versions from memory instead of checking what's installed.

**GroundRules** fixes all three with 2 clean Markdown files in `.agents/rules/`.

```bash
npx create-groundrules
```

Zero runtime. Zero dependencies. ~250 tokens. Works natively with Antigravity, Claude Code, Cursor, Copilot, and Windsurf.

---

## What It Installs

```
AGENTS.md                      → Root router pointing to your guardrails
.agents/
└── rules/
    ├── IDENTITY.md            → Tech stack, test command, & "What We Don't Do"
    └── GROUNDING.md           → 4 universal cognitive rules (No guessing, verify lockfiles)
```

### 1. `IDENTITY.md` (Negative Boundaries)
```markdown
## What We Don't Do
- NEVER use raw SQL (use Supabase client).
- NEVER touch auth logic without approval.
- NEVER add unrequested dependencies.
```

### 2. `GROUNDING.md` (Cognitive Discipline)
```markdown
## 1. Never Guess Silently
When requirements are ambiguous, STOP and ask before implementing.

## 2. Verify Lockfiles First
Check package-lock.json before writing imports. Never guess from memory.

## 3. No Speculative Abstractions
Write surgical, minimum viable code. No unrequested helper sprawl.

## 4. High Signal Communication
Lead with the code and diffs. No conversational fluff or preambles.
```

---

## Installation

```bash
# Interactive (takes 5 seconds)
npx create-groundrules

# Or clone manually
npx degit chama-x/DevOS/template .
```

---

[Contributing](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md) · MIT License
