---
name: "Frontier Delegation (External Brain)"
description: "Trigger this skill when a task requires high-level algorithmic generation, massive outputs (40k+ tokens), or when the user requests delegating to a frontier model."
---

# Frontier Delegation Protocol

As an integrated IDE agent, your primary strengths are context navigation, surgical edits, and environment execution. However, some tasks require extreme algorithmic complexity that exceeds your optimal reasoning window. 

When you encounter such a task, or when the user explicitly requests an "expert" or "frontier model," you MUST execute the following protocol:

## 1. The Delegation Gate
Do NOT attempt to guess complex logic if it is beyond standard boilerplate. Use the `ask_question` tool to ask the user:
*"This task requires high-level algorithmic generation. Shall I attempt it, or shall I prepare a Delegation Prompt for a frontier model?"*

## 2. Compile the Handoff Packet
If the user approves delegation, create an artifact named `frontier_delegation_prompt.md`. 
*   `[HARD CONSTRAINT - SECRET SCRUB]`: Before compiling the Handoff Packet, grep target files for credentials, keys, or `.env` patterns and redact them. Never export secrets to external models.

This artifact MUST contain:
1. **The Meta-Prompt**: Instruct the frontier model on its role (e.g., "You are a Principal Architect. You are writing code that will be injected into a local IDE by an orchestration agent.")
2. **The OS Constraints**: Copy the critical constraints from `AGENTS.md` (e.g., `[NEGATIVE CONSTRAINT - DEPENDENCIES]`: must use pnpm) so the frontier model does not hallucinate incompatible tech stacks.
3. **The Target Files**: Output the raw text of the files that need modification, clearly labeled with their absolute file paths.
4. **The Objective**: Clearly state what logic needs to be generated.

## 3. The Pause
Once the artifact is generated, stop execution. Tell the user to copy the artifact into their frontier model (e.g., z.ai, Claude Opus, GLM-5.2) and paste the response back into the chat.

## 4. Verbatim Integration & Quarantine
When the user returns with the frontier model's output, you MUST follow this strict quarantine sequence:
1. `[HARD CONSTRAINT - QUARANTINE]`: Create a checkpoint commit or a new branch (e.g., `agent/frontier-inject-<ts>`) *before* touching any files.
2. `[IDEMPOTENCY]`: Before applying any hunk, grep for its signature in the target file. If already present, skip it.
3. Use your surgical editing tools (`multi_replace_file_content` or `replace_file_content`) to inject the expert's code **verbatim**. Do not summarize or clean it up.
4. Run linters, static analysis, and tests on the injected code.
5. Present the final Git DIFF to the user for a **T3 Red Team review**. External code gets MORE scrutiny than internal code. Only merge the quarantine branch upon explicit user approval.
