# Current Task

**WHAT**: Implement the `checkout.session.completed` Stripe webhook handler.
**SCOPE**: `app/api/webhooks/stripe/route.ts`, Supabase client helpers to update the `bookings` table status to 'paid'.
**NOT_TOUCHING**: Frontend checkout page logic or the actual Stripe product configuration.
**DONE_WHEN**: The webhook successfully verifies the Stripe signature, updates the booking status in Postgres, and returns a 200 OK. We have written a unit test simulating a valid payload.
