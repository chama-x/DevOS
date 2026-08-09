# Log

<!-- Append only. Compress when >50 lines. Format: [Date] Feature: Outcome. (Decision/Lesson) -->

- **2026-08-07** Schema Migration: `profiles`, `classes`, `bookings` deployed locally. *(Lesson: Ensure local Docker daemon is running before Supabase CLI commands).*
- **2026-08-07** Database Security: RLS policies enforced for user-isolated reads. *(Decision: Users can only select bookings where `user_id == auth.uid()`).*
- **2026-08-08** Stripe Checkout: `POST /api/checkout` returns valid session URL. *(Decision: Injected `metadata.booking_id` into the session so the webhook can map it back to Postgres later).*
