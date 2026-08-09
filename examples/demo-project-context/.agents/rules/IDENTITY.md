---
trigger: always_on
---
# AcmeBook — Project Identity

## Boundaries & Core Stack
- **Stack:** Next.js 14 App Router, Supabase, Tailwind, shadcn/ui.
- **Mission:** B2B SaaS for fitness instructors to manage classes and clients to book slots.

## Constraints (What We Don't Do)
- **NEVER** use raw SQL. **ALWAYS** use the Supabase JS client.
- **NEVER** use inline styles. **ALWAYS** use Tailwind utility classes (e.g., `<div className="flex gap-4">`).
- **NEVER** add state management libraries like Redux or Zustand. Rely strictly on React Server Components and native Context.
- **NEVER** implement custom date pickers. **ALWAYS** use native HTML `<input type="date">` or the canonical shadcn calendar component.

## Priorities
- **High-Risk:** Row Level Security (RLS) policies and Stripe payment Webhooks. Stop and verify before changing.
- **Non-Negotiable:** Keyboard accessibility on all interactive elements.

## Autonomy vs. Approval
- **Full Autonomy:** Feature implementation within boundaries, unit tests, matching Tailwind designs.
- **Requires Approval:** DB schema migrations, adding third-party `npm` dependencies, modifying Stripe products.
