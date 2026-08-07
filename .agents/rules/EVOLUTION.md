---
trigger: always_on
---

# Evolution

## Learning Loop
When you learn a reusable pattern, recurring fix, or workflow correction:
1. Draft it as a Markdown skill in .agents/skills/.drafts/
2. Present it to the user via ask_question for approval
3. If rejected → record in .agents/memory/rejected_proposals.md, delete draft. Check the rejection ledger before proposing anything similar in the future.
4. If approved → move to .agents/skills/, git commit

No silent updates. Every learned pattern goes through the human.

## Semantic Dictionary
When a new preference, shorthand, or subjective definition emerges during work:
1. Propose the keyword → definition mapping via ask_question
2. Only on approval → append to .agents/memory/user_lexicon.md

Live user instructions always override lexicon mappings. Lexicon fills gaps — it never overrules the human.

## Context Compression
When user_lexicon.md exceeds 40 entries or telemetry/runs.md exceeds 100 entries:
1. Archive older content to .agents/archive/ with a timestamped filename
2. Update .agents/archive/index.md with the snapshot path and summary
3. Verify the snapshot exists, then truncate the original
4. Single git commit covering all changes

Before claiming "no prior context exists," check .agents/archive/index.md.

## Telemetry
After each task, append one line to .agents/telemetry/runs.md:
| date | task | outcome |
