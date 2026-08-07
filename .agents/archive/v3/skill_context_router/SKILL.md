---
name: Context Router
description: Extracts YAML frontmatter from all project specifications. Trigger this to discover which SPEC files are relevant to a task. Do NOT use this for semantic code search; only use for reading YAML specifications.
---

# Skill: Context Router

The agent must not open `.md` files individually to read frontmatter, as this exhausts context limits.

## Execution
To extract all frontmatter across the project specifications, the agent must execute the following provided script via the `run_command` tool:

```bash
bash .agents/skills/context_router/scripts/extract_frontmatter.sh
```

## Workflow
1. Execute the script above.
2. Review the output to identify which specific `.md` files match the domain/dependencies of the current task.
3. Use the `view_file` tool to read only the identified files.
