---
trigger: always_on
---

# DevOS Project Identity

## What We're Building
We are building "DevOS", a minimal, prompt-based operating system for IDE agents. It uses five core files to give AI agents a project-specific memory, behavioral calibration, and strict scope boundaries, ensuring predictable and reliable execution across sessions.

## Tech Stack
- Markdown (for rules, skills, and context files)
- Node.js (for the interactive CLI installer)

## Test Command
`npm run test` (Note: tests will be added in a future PR, run manual Git checks for now)

## What We Don't Do
- No runtime dependencies. The entire system must remain flat files.
- No complex UI components or frontend frameworks.
- No IDE-specific hacks (DevOS must remain universally portable across all major AI coding agents like Cursor, Cline, Antigravity, etc).

## What Matters to Me
- High-risk: Anything that touches the core rule files (`GROUNDING.md`, `IDENTITY.md`). These form the brain of the system.
- Non-negotiable: Progressive disclosure. Agents should not load textbooks of information they already know. Skills must be strict configuration profiles < 150 words.
- Move fast: Documentation, READMEs, and localized translations.

## Where I Stay in the Loop
- Any architectural changes to the 5-file structure.
- Any modifications to the `SKILLS_SPEC.md` or the core `GROUNDING.md` constitution.

## Where You Have Full Autonomy
- Refactoring internal skill files to adhere strictly to `SKILLS_SPEC.md`.
- Updating the `bin/create-devos.js` CLI installer to improve usability.
- Managing your own task state in `NOW.md` and appending to `LOG.md`.
