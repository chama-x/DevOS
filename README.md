# DevOS

Drop the `.agents` folder into any workspace. The next agent that opens
it reads four files before its first response — not a generic chatbot
with terminal access.

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

## Installation

Copy `.agents/` into your project root. Fill in `rules/IDENTITY.md` for
your project. Done.

## What's Included

Beyond the four core files, DevOS ships with:

- **11 curated skills** — narrow reasoning loops and output constraints
  for specific tasks, not generic reference docs the agent might skim.
- **Skill calibration** — SkillsBench routing loads only the skills a
  task needs, instead of stacking all eleven into context.
- **Evolution governance** — agents propose new skills and vocabulary,
  but only the human approves.
- **Context compression** — automatic archiving prevents memory files
  from growing unbounded.
- **Semantic dictionary** — maps your shorthand and preferences to
  deterministic agent behavior.

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
│   ├── EVOLUTION.md         ← Governed learning loop
│   ├── SKILL_ROUTING.md     ← Skill decision tree
│   └── business_context.md  ← Knowledge graph template
├── AGENTS.md                ← Skill calibration rules
├── current.md               ← Volatile task state
├── worklog.md               ← Append-only history
├── memory/
│   ├── user_lexicon.md      ← Semantic dictionary
│   └── rejected_proposals.md
├── skills/                  ← 11 curated skill directories
├── telemetry/
│   └── runs.md
└── archive/
    └── index.md
```

## License

MIT
