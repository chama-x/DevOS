---
name: ship
description: Use when deploying code to production. Enforces a strict pre-deployment sequence.
trigger: manual
---

# Ship — Pre-Deployment Sequence

**How we use Ship here:** Run these checks in order. Do not skip. Do not deploy if any step fails.

1. **Typecheck:** `tsc --noEmit` — zero errors required.
2. **Lint:** `eslint . --max-warnings 0` — no warnings allowed in production path.
3. **Tests:** `npm run test` (or project equivalent) — all must pass.
4. **Secret sweep:** Scan `git diff HEAD` for hardcoded API keys, passwords, or tokens.
5. **Log sweep:** Remove `console.log`, `debugger`, `print()` from production paths. Exception: structured loggers (Winston, Pino).
6. **Build:** `npm run build` — must succeed cleanly.
7. **Env check:** Confirm all `.env.production` variables are documented or injected via CI.
