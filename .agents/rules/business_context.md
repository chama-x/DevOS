---
trigger: always_on
---

# Project Name: Business Context & Routing

# Business & Data Context

## Organization Profile
- **Company**: [Company Name]
- **Core Business**: [Describe the business]
- **Key Personnel**:
  - **[Name]**: [Role]

## The Joint Brain Methodology (Knowledge Graph Framework)

We are modeling this business not as flat files, but as an **Enterprise Knowledge Graph (Spider Web Map)**.
To maintain high accuracy without hallucinations, you must strictly map and query data using this vocabulary:

### 1. The Core Pillars
The business is separated into these autonomous areas:
- **[Pillar 1]**: [Description]
- **[Pillar 2]**: [Description]

### 2. The Entity Types (Nodes)
Always categorize things into these buckets:
- `user`: [Description]
- `system`: [Description]

### 3. The Connections (Edges)
Never assume a relationship. Prove it using these edge types:
- `manages`: Person to System
- `flows_to`: Data flowing from one service to another

## Working with this Domain
Never assume data is clean or perfectly structured. Always think in terms of the **Knowledge Graph** (Who + What + How) before touching the codebase. Always rely on fuzzy matching and robust error handling when building data extraction pipelines.

## Technology Stack Mandates
For this specific project, the following tech stack rules apply locally:
- `[NEGATIVE CONSTRAINT - DEPENDENCIES]`: DO NOT use `npm` or `yarn`. `pnpm` is the permanently mandated package manager. Next.js is the mandated web application framework (do not default to standard React or Vite for web apps).
