# Current Task

**WHAT**: Implement the `checkout.session.completed` Stripe webhook handler.
**SCOPE**: Only `app/api/webhooks/stripe/route.ts` and Supabase DB helpers.
**NOT_TOUCHING**: 
- **NEVER** touch frontend checkout components (`app/checkout/page.tsx`).
- **NEVER** touch Stripe dashboard configuration.
**SUCCESS_CRITERIA**: 
1. Validates Stripe signature using the official SDK.
2. Updates `bookings` table status to `'paid'`.
3. Returns `200 OK`. 
4. Associated unit test passes.
