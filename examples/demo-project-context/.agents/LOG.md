# Log

<!-- Append only. Never edit past entries. Compress to archive when >50 lines.
     Each entry: timestamp, task, what changed, approach, outcome, lessons. -->

## 2026-08-07T14:20:00Z - Initial DB Schema Setup
- **What changed**: Created migration for `profiles`, `classes`, and `bookings` tables in Supabase.
- **Approach**: Used standard Supabase migration workflows. Added RLS policies ensuring users can only see their own bookings.
- **Outcome**: Schema successfully deployed locally. RLS tests pass.
- **Lessons**: Supabase local development requires Docker running; noted to ensure it's up before running DB commands.

## 2026-08-08T09:15:00Z - Stripe Checkout Session Endpoint
- **What changed**: Implemented `POST /api/checkout` to create a Stripe Checkout Session.
- **Approach**: Used Stripe Node SDK. Mapped `class_id` to Stripe Price ID and passed user email to pre-fill the form.
- **Outcome**: Endpoint returns a valid session URL.
- **Lessons**: Needed to include `metadata.booking_id` in the session so the webhook can identify which booking to update later.
