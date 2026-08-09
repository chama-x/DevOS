# Log

<!-- Append only. Never edit past entries. Compress to archive when >50 lines.
     Each entry: timestamp, task, what changed, approach, outcome, lessons. -->

## 2026-08-09T19:41:01+05:30 — DevOS 2.0 Architecture Upgrade

**Task:** Full DevOS 2.0 upgrade per user spec.

**What changed:**
- CREATED `AGENTS.md` (root) — updated to reference `NOW.md`/`LOG.md`.
- CREATED `SKILLS_SPEC.md` — canonical skill format definition (150-word max, config-only, required frontmatter).
- CREATED `bin/create-devos.js` — interactive Node.js CLI installer (readline, 3 prompts, writes IDENTITY.md template + directory scaffolding).
- CREATED `.agents/NOW.md` — new name for volatile task state.
- CREATED `.agents/LOG.md` — new name for append-only session history.
- MODIFIED `.agents/rules/GROUNDING.md` — full overwrite to 300-word constitution (Memory Compaction Protocol added, Epistemic Security, Execution State Machine, Skill Routing pointer).
- MODIFIED `.agents/skills/ship/SKILL.md` — rewritten to SKILLS_SPEC standard: `trigger: manual`, config-only, numbered sequence, under 150 words.
- MODIFIED `SKILL_ROUTING.md` — `trigger: always_on` removed (already done in v2.0a pass).
- MODIFIED `README.md` + all localized READMEs + `CHANGELOG.md` + `EXAMPLES.md` — all `current.md`/`worklog.md` references updated to `NOW.md`/`LOG.md`.
- DELETED `.agents/skills_registry.json` — stale bloat.
- DELETED `.agents/skills/.DS_Store` — bloat.
- RENAMED `current.md` → `NOW.md`, `worklog.md` → `LOG.md`.

**Outcome:** Zero stale references to old filenames. All tasks complete.
