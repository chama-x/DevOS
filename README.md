![DevOS: Predictability Over Perfection](assets/devos-bento-hero.jpg)


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

**DevOS gives your AI coding agents persistent memory, behavioral discipline, and strict project boundaries.** 

Drop the `.agents` folder into any workspace, and the next agent that opens it reads four files before its first response—transforming it from a generic chatbot into a predictable, context-aware engineering partner.

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

![DevOS 4-File Context Architecture](assets/devos-architecture-infographic.jpg)

## Quickstart

The fastest way to install DevOS is to pull the `.agents` directory directly into your project root using `degit`:

```bash
npx degit chama-x/DevOS/.agents .agents
```

Then, open `rules/IDENTITY.md` and define your project's boundaries. You're done.

## Features

Beyond the four core files, DevOS is engineered for disciplined execution:

| Feature | How it works |
|---|---|
| **11 Curated Skills** | Narrow reasoning loops for specific tasks, replacing generic reference docs. |
| **Skill Calibration** | Dynamic routing loads *only* what a task needs, preventing context overload. |
| **Evolution Governance** | Agents can propose new rules and vocabulary, but only humans approve them. |
| **Context Compression** | Automatic archiving keeps memory files from growing unbounded over time. |
| **Semantic Dictionary** | Maps your shorthand preferences into deterministic agent behaviors. |

## Documentation & Community

We prioritize trust, predictability, and collaboration. 
- [Changelog](CHANGELOG.md) - See our release history.
- [Contributing Guidelines](CONTRIBUTING.md) - Learn how to add new Skills safely.
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
