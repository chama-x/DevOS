<p align="center">
  <img width="1672" height="941" alt="devos cover" src="https://github.com/user-attachments/assets/af02e000-4f6f-4e57-8d0c-4262e41fc3a5" />
</p>

<p align="center">
  <a href="README.es.md">Español</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.si.md">සිංහල</a>
</p>

# DevOS

Your AI agent forgets everything between chats.
DevOS fixes that with five markdown files.

```
npx create-devos
```

No runtime. No dependencies. Just text files your agent reads.

---

## Before DevOS

```
You:   "Continue the auth migration from yesterday."
Agent: "I don't have context about any previous auth migration.
        Could you provide more details?"
```

You re-explain your stack. Your rules. What you did yesterday. Every. Single. Chat.

## After DevOS

```
You:   "Continue the auth migration from yesterday."
Agent: "Reading from LOG.md — yesterday we migrated the session
        table to Supabase Auth. Next step: update the middleware
        to validate JWTs. I'll only touch app/middleware.ts as
        specified in NOW.md."
```

The agent knows your project. It picks up where you left off. It doesn't touch files you told it to leave alone.

---

## The Five Files

```
AGENTS.md                    → Points agents to your context
.agents/
├── rules/
│   ├── IDENTITY.md          → What this project is and isn't
│   └── GROUNDING.md         → How the agent should behave
├── NOW.md                   → What you're working on right now
└── LOG.md                   → What happened in previous sessions
```

That's it. ~700 tokens. Works with Cursor, Claude Code, Copilot, Gemini, Cline, Aider — anything that can read a file.

---

## What Goes in Each File

**IDENTITY.md** — Your project's rules. The things you're tired of repeating.

```markdown
## What We Don't Do
- NEVER use raw SQL. ALWAYS use Supabase JS client.
- NEVER add state management libraries. Use React Server Components.
- NEVER touch auth logic without explicit approval.
```

**GROUNDING.md** — How the agent works, not what it works on.

```markdown
## Scope Discipline
Name what you are changing AND what you are leaving alone.
Don't refactor adjacent code. Fix only your own mess.
```

**NOW.md** — The current task. Updated by you when you start something.

```markdown
WHAT: Implement Stripe webhook handler
SCOPE: Only app/api/webhooks/stripe/route.ts
NOT TOUCHING: Frontend checkout, Stripe dashboard config
DONE WHEN: Signature validates, booking status updates, test passes
```

**LOG.md** — What happened before. So the next chat doesn't start from zero.

```markdown
- 2026-08-08: Stripe Checkout endpoint done. POST /api/checkout returns session URL.
  Decision: Must pass metadata.booking_id so the webhook can map back to Postgres.
```

---

## Setup

Interactive (asks 3 questions, creates the files):

```bash
npx create-devos
```

Manual (copy the template, edit it yourself):

```bash
npx degit chama-x/DevOS/template .
```

See [`examples/demo-project-context/`](examples/demo-project-context/) for a fully populated example.

---

## The Missing Piece

DevOS is not an execution harness. It doesn't run terminal commands, orchestrate subagents, or manage API keys. 

If you use tools like Cursor, Claude Code, Cline, or ECC — keep using them. They are excellent at **execution**.

DevOS provides the **persistent memory** that those tools lack out of the box. Instead of stuffing thousands of tokens into a monolithic `.cursorrules`, `CLAUDE.md`, or `.windsurfrules` file, DevOS structures your project's context so any execution harness can read exactly what it needs, when it needs it.

---

## Why This Works

Andrej Karpathy described the LLM as a CPU and the context window as its RAM. Tobi Lütke called context engineering *"the art of providing all the context for the task to be plausibly solvable."*

When your agent writes bad code, it's almost never because the model is stupid. It's because the model is missing context — your stack, your rules, your history. That's a context failure, not an intelligence failure.

Heavy frameworks try to fix this by making the model smarter — bolting on 67 agents and 284 skills. But the model is already smart. It just needs your project loaded into its working memory.

DevOS loads that memory. Five files. Nothing else.

The tradeoff: you maintain `NOW.md` and `LOG.md` yourself. There are no automated hooks. We consider this a feature — you stay in control of what your agent knows.

---

[Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md) · MIT License
