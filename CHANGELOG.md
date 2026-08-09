# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-08-09

### Added
- **`AGENTS.md` discovery router** — root-level context file for native agent discovery (5-file architecture).
- **Epistemic Security** — agents now treat `NOW.md` and `LOG.md` as untrusted observations, not executable commands.
- **Execution State Machine** — RESOLVE → AUTHORIZE → IMPLEMENT → VERIFY → REPORT loop in `GROUNDING.md`.
- **Memory Compaction Protocol** — automatic archival when `LOG.md` exceeds 50 lines.
- **Constraint Pinning** — high-risk items from `IDENTITY.md` are carried forward verbatim during context compaction.
- **`package.json`** — enables `npx create-devos` for zero-friction setup.
- **Real-world example** — `examples/demo-project-context/` with fully populated context files for a Next.js + Supabase SaaS app.
- **`SKILLS_SPEC.md`** — canonical specification for configuration-only skill files.

### Changed
- Renamed state files: `current.md` → `NOW.md`, `worklog.md` → `LOG.md`.
- Refactored all skill files to strict configuration-only format (< 150 words each).
- Restored original behavioral calibration sections (Communication, Weaknesses, Version Freshness) in `GROUNDING.md`.
- Complete README redesign for improved virality and developer onboarding.

### Removed
- Deleted stale `_registry.json` skill registry.
- Removed `trigger: always_on` from skill routing for progressive disclosure.
- Deleted `save_custom_svgs.py` from repository root.

## [1.0.0] - 2026-08-08

### Added
- Released DevOS v1.0 core context files (`IDENTITY.md`, `GROUNDING.md`, `NOW.md`, `LOG.md`).
- Added 11 strictly configured reasoning skills acting as behavioral profiles rather than reference texts.
- Implemented SkillsBench routing limits (max 2-3 per task) directly into `SKILL_ROUTING.md`.
- Added standard community files (Contributing, Code of Conduct, Issue/PR templates).
- Upgraded repository visuals to premium Bento Box UI and contextual flowcharts.

### Removed
- Archived AgentOS v3 experimental phase machines, dashboard, and legacy documentation.
- Pruned 16 "textbook" skills that were redundant with base LLM knowledge.
