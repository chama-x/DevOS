# Contributing to DevOS

Thank you for considering contributing to DevOS! We're building the simplest possible context layer for AI coding agents, and every contribution matters.

## The Core Philosophy

DevOS prioritizes **predictability over perfection.** Before submitting a PR, please ensure your contribution aligns with the four directives in the README:

1. Ask, don't assume
2. Minimum viable implementation
3. Scope discipline
4. Define success, then loop

## Good First Contributions

- Improve documentation or fix typos
- Add a new localized README translation
- Propose a new curated skill (see below)

## Adding Skills

Skills are strict **configuration profiles**, not reference manuals. If you are submitting a new skill:

1. It **must** enforce a behavioral or formatting constraint.
2. It **must not** simply dump API documentation (the model already knows the API).
3. It **must** be under 150 words (per `SKILLS_SPEC.md`).
4. It **must** be added to `SKILL_ROUTING.md` with a clear trigger condition.

## Submitting Pull Requests

1. Fork the repo and create your branch from `master`.
2. Update the README or documentation if you change functionality.
3. Keep the scope of the PR focused. (Scope discipline applies to humans too!)
4. Issue that pull request!

## What We Won't Accept

- Runtime dependencies of any kind (npm packages, Python libraries, etc.)
- IDE-specific code or configurations
- Skills that exceed 150 words or contain generic advice the model already knows
