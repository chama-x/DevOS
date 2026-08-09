---
trigger: always_on
---

# Project Identity

## What We're Building
We are building "AcmeBook", a Next.js B2B SaaS platform where fitness instructors can manage their class schedules and clients can book slots. It focuses on a frictionless mobile booking experience and a powerful desktop calendar view for instructors.

## Tech Stack
- Frontend: Next.js 14 (App Router), React, Tailwind CSS
- Backend: Supabase (Postgres, Auth, Edge Functions)
- Payments: Stripe
- UI Components: shadcn/ui

## Test Command
`npm run test`

## What We Don't Do
- Never use raw SQL queries. Always use Supabase JS client or Prisma ORM.
- No custom date pickers — rely on native HTML `<input type="date">` or shadcn's standard calendar component.
- Do not add external state management libraries (no Redux, no Zustand). Stick to React Context and Server Components.

## What Matters to Me
- High-risk: Anything touching user data, Stripe payment logic, or Row Level Security (RLS) policies. Double-check before modifying.
- Non-negotiable: Accessibility. All interactive elements must be keyboard navigable and screen-reader friendly.
- Move fast: Internal admin dashboards and basic CRUD UI.

## Where I Stay in the Loop
- Architecture choices and database schema migrations.
- Adding any new third-party dependencies.
- User-facing copy (marketing pages).

## Where You Have Full Autonomy
- Implementation of features within the approved architecture.
- Writing unit tests and resolving test failures.
- Styling components to match the existing Tailwind design system.
