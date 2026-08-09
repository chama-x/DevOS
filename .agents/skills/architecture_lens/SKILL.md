---
name: architecture_lens
description: Configuration profile for generating codebase dependency graphs. Enforces specific depth, focus, and Mermaid formatting rules.
---

# Architecture Lens Configuration

**How we use Architecture Lens here:** Follow these strict constraints for mapping unfamiliar codebases:

## Abstraction Rules
1. **Focus:** Map ONLY the primary data flow layer, state management, and core routing.
2. **Ignore:** Exclude utility functions, helpers, pure UI components, types/interfaces, and test files.
3. **Depth Limit:** Maximum 2 levels of nesting. Do not attempt to map every function call.

## Mermaid Formatting
1. **Type:** Use `flowchart TD` (Top-Down) or `LR` (Left-Right) based on which creates fewer intersecting lines.
2. **Grouping:** Group related modules into `subgraph` blocks (e.g., "Frontend", "State", "API", "Database").
3. **Nodes:** Keep node labels concise. Use IDs and labels separately (e.g., `db[(Database)]`).

## Output Protocol
1. Render the Mermaid graph in a standard markdown block.
2. Provide a 3-bullet summary of the most critical structural bottleneck or insight revealed by the graph.
