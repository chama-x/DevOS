# DevOS Skill Specification
DevOS natively discovers any folder in `.agents/skills/` containing a `SKILL.md` file. 
To be a valid DevOS skill, the file must adhere to this spec:

## 1. YAML Frontmatter (Required)
- `name`: lowercase, no spaces (e.g., `ship`)
- `description`: One sentence. "Use when [trigger condition]."
- `trigger`: `manual` or `on-demand`

## 2. Body (Strict Rules)
- **Configuration Only:** Do not explain what the technology is. The LLM already knows.
- **Maximum 150 words.**
- State only project-specific deviations, sequences, and constraints (e.g., "In this project, we use X instead of Y").
