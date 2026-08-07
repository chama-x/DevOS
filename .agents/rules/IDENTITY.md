---
trigger: always_on
---

<!-- IDENTITY.md — The human's declaration of what matters.
     Fill this once. The agent reads it every session.
     This is the contract between you and your agent. -->

# [Project Name]

## What We're Building
<!-- One paragraph. What would you tell a smart friend who asks
     "what is this?" Not a spec — a human explanation. -->

## When It's Done
<!-- What does a person using this actually DO and SEE? -->
A user will:
1. [action → result]
2. [action → result]

## How It Should Feel
<!-- Not design jargon. How does it feel to use?
     Think of the best tool you've ever picked up. -->

## What Matters to Me
<!-- What do you consider high-risk? Non-negotiable? Trivial?
     This tells the agent where to be careful and where to move fast. -->
- High-risk: [e.g., "anything touching user data or auth"]
- Non-negotiable: [e.g., "accessibility on all interactive elements"]
- Move fast: [e.g., "internal admin pages, build tooling"]

## Where I Stay in the Loop
<!-- What decisions do you want to see before the agent acts? -->
- [e.g., "architecture choices", "third-party dependencies", "user-facing copy"]

## Where You Have Full Autonomy
<!-- What can the agent handle without asking? -->
- [e.g., "implementation within approved architecture", "test writing", "build config"]

## Tech Stack
- [framework, package manager, database, key dependencies]

## What We Don't Do
<!-- Project-specific anti-patterns. The agent checks here before adding anything. -->
- [e.g., "No client-side state management — server components only"]
- [e.g., "No custom date pickers — native HTML input"]
