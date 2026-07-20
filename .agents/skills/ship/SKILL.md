---
name: ship
description: A pre-deployment release-readiness checklist skill. Triggers before deploying code to production to enforce tests, typecheck, secret scanning, and console.log sweeps.
---

# Pre-Deployment Release Readiness (Ship)

You are an expert release engineer enforcing a strict checklist before any code reaches production.

## 1. Static Analysis
*   Ensure the project passes all type checks (e.g., `tsc --noEmit`).
*   Ensure the project passes all linters (e.g., `eslint . --max-warnings 0`).

## 2. Test Coverage
*   Run the full test suite (`npm run test` or equivalent). Do not deploy if any tests are failing.

## 3. Secret and Log Sweeps
*   Scan the git diff for leaked secrets, API keys, or hardcoded passwords.
*   Ensure all debugging statements (`console.log`, `debugger`, `print()`) are removed from the production path, excluding structured logging frameworks (like Winston, Pino, or native system logs).

## 4. Build Artifact Validation
*   Ensure the production build succeeds (`npm run build`).
*   Verify that environment variables required for production (`.env.production`) are properly documented or injected in the CI pipeline.
