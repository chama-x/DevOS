---
trigger: always_on
---

# GroundRules Project Identity

## Project
GroundRules is an ultra-minimal, prompt-based cognitive grounding and boundaries layer for AI coding agents. It provides a clean 2-file architecture (`IDENTITY.md` and `GROUNDING.md`) to stop agents from making silent assumptions, writing speculative abstractions, and hallucinating dependencies.

## Tech Stack
- Markdown (for rules and templates)
- Node.js (for the interactive CLI installer)

## Test Command
`npm test`

## Non-Negotiable Invariants
- Zero runtime dependencies. The entire system must remain flat markdown files.
- Zero bloat. No complex state machines, no task log files, no runtime daemons.
- Universal portability across Antigravity, Claude Code, Cursor, Copilot, Windsurf, Cline.
