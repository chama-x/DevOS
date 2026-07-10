---
name: Architecture Lens (Mermaid)
description: Automatically generates a Mermaid.js dependency graph of a codebase. Trigger this when you enter a new directory and need to "see" how the components and files connect before modifying them.
---

# Skill: Architecture Lens

AI agents are blind to visual dependency graphs. Do not blindly read files to guess the component hierarchy. Instead, use this skill to generate a textual `.mmd` map that you can read to instantly understand the architecture.

## Execution
Use the `run_command` tool to execute the generation script. You can optionally pass the target directory as an argument (defaults to `business-map/src`):

```bash
bash .agents/skills/architecture_lens/scripts/generate_diagram.sh business-map/src
```

## Workflow
1. Execute the script above.
2. The script uses `dependency-cruiser` to map all import/export paths and outputs them as Mermaid `graph TD` syntax.
3. Use the `view_file` tool to read the resulting `.agents/skills/architecture_lens/architecture.mmd` file.
4. You now have a complete, accurate dependency graph in your context window.
