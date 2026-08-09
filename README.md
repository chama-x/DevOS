<img width="1672" height="941" alt="devos cover" src="https://github.com/user-attachments/assets/af02e000-4f6f-4e57-8d0c-4262e41fc3a5" />


![DevOS: Predictability Over Perfection](assets/devos-hero-v2.svg)


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — Give any IDE agent your project's rules, current task, and history in four files.**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/LOG.md... [Session history restored]
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
| `NOW.md` | What the agent is working on right now, what it's not touching, when it's done |
| `LOG.md` | What was done before — so the next session doesn't start from zero |

Two rule files are injected into every conversation (~700 tokens). Two
dynamic files are read on session start. That's the entire system.

![DevOS 4-File Context Architecture](assets/devos-architecture-v3.svg?v=1786144986)

## Quickstart

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# Restart your IDE agent — it now reads your project context every chat.
```

## Why DevOS?

IDE agents start every chat from scratch. DevOS gives them a memory — your rules, your task, your history — so they stop guessing and start building.

## DevOS vs. Raw Prompts

Single-file `.cursorrules` and prompt packs dump thousands of tokens into every chat. DevOS replaces them with four structured files and on-demand skill routing.

| Capability | Raw Prompts (.cursorrules / CLAUDE.md) | DevOS |
|---|---|---|
| **Context footprint** | 5,000+ tokens loaded every chat | ~700 core tokens loaded |
| **Session history** | Resets to zero on new chat | Restores progress from `LOG.md` |
| **Skill loading** | All rules loaded at once | Max 2–3 skills loaded on demand |
| **Scope discipline** | Soft suggestions agent can ignore | Hard constraints checked before first response |
| **Project boundary** | Unstated | Defined in `IDENTITY.md` |


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
├── NOW.md               ← Volatile task state
├── LOG.md               ← Append-only history
└── skills/                  ← 11 curated skill directories
```

## Documentation & Community

We prioritize trust, predictability, and collaboration.

- [Changelog](CHANGELOG.md) - See our release history.
- [Contributing Guidelines](CONTRIBUTING.md) - We review every PR. Start with an issue.
- [Code of Conduct](CODE_OF_CONDUCT.md) - Our community standards.

## License

MIT
