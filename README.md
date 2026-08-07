![DevOS: Predictability Over Perfection](assets/devos-hero.svg?v=1786143843)


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — Give any IDE agent your project's rules, current task, and history in four files.**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```


## What It Does

A fresh IDE agent doesn't know your project, your standards, your
failure patterns, or what happened yesterday. DevOS closes those gaps
with four files:

| File | What It Does |
|---|---|
| `rules/IDENTITY.md` | Your declaration of what the project is, what done looks like, and where the agent has autonomy vs. where you stay in the loop |
| `rules/GROUNDING.md` | Behavioral calibration — how the agent implements, communicates, catches its own mistakes, and starts each session |
| `current.md` | What the agent is working on right now, what it's not touching, when it's done |
| `worklog.md` | What was done before — so the next session doesn't start from zero |

Two rule files are injected into every conversation (~700 tokens). Two
dynamic files are read on session start. That's the entire system.

![DevOS 4-File Context Architecture](assets/devos-architecture.svg?v=1786143843)

## Quickstart

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# Restart your IDE agent — it now reads your project context every chat.
```

## Why DevOS?

IDE agents start every chat from scratch. DevOS gives them a memory — your rules, your task, your history — so they stop guessing and start building.

## DevOS vs. Single-File Prompts (.cursorrules)

| Feature | Raw `.cursorrules` / Prompt Lists | DevOS |
|---|---|---|
| **Architecture** | Single giant file (causes context bloat) | 4 modular files + dynamic skill routing |
| **Session Memory** | Resets on every new chat | Persisted across sessions via `worklog.md` |
| **Token Budget** | ~5,000+ tokens loaded unconditionally | ~700 core tokens; skills load on-demand |
| **Scope Discipline** | Soft suggestions (agents ignore them) | Hard constraints enforced by `GROUNDING.md` |
| **Autonomy Control** | Undefined boundaries | Explicit autonomy levels set in `IDENTITY.md` |

## Features

Beyond the four core files, DevOS is engineered for disciplined execution:

| Feature | How it works |
|---|---|
| **11 Curated Skills** | Load only the reasoning loop a task needs |
| **Skill Calibration** | Route tasks to the right skill automatically |
| **Evolution Governance** | Agents propose new skills; you approve |
| **Context Compression** | Archive history before it grows unbounded |
| **Semantic Dictionary** | Map your shorthand to deterministic behavior |

## Documentation & Community

We prioritize trust, predictability, and collaboration. 
- [Changelog](CHANGELOG.md) - See our release history.
- [Contributing Guidelines](CONTRIBUTING.md) - We review every PR. Start with an issue labeled `good first issue`.
- [Code of Conduct](CODE_OF_CONDUCT.md) - Our community standards.


## Philosophy

DevOS is built on four evidence-backed directives:

1. **Ask, don't assume** — surface uncertainty before proceeding (+3.7%
   task success)
2. **Minimum viable implementation** — smallest code that works, no
   speculative abstraction
3. **Scope discipline** — touch only what the task requires (default
   agents triple their breaking-change rate on maintenance tasks)
4. **Define success, then loop** — know what done looks like before
   writing code

And one design principle: **predictability over perfection.** The human
doesn't need a perfect agent. They need one whose behavior they can
learn, whose scope they can verify, and whose failure modes they can
compensate for.

## Project Structure

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← Fill this for your project
│   ├── GROUNDING.md         ← Agent behavioral calibration
│   └── SKILL_ROUTING.md     ← Skill decision tree
├── current.md               ← Volatile task state
├── worklog.md               ← Append-only history
└── skills/                  ← 11 curated skill directories
```

## License

MIT
