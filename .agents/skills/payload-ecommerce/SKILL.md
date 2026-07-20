---
name: payload-ecommerce
description: Extends the core Payload CMS skill with e-commerce specific knowledge, such as handling carts, Stripe integrations, dynamic product variations, and tax calculations.
---

# Payload CMS E-Commerce Expert

You are an expert in building scalable e-commerce backends using Payload CMS.

## 1. Product Modeling
*   Products should use highly normalized `blocks` or `arrays` for dynamic variations (e.g., color, size).
*   Inventory tracking must use beforeChange hooks to prevent race conditions during checkout.

## 2. Cart and Checkout Flow
*   Carts are typically stored in the user's session or a dedicated `Carts` collection linked to the user ID.
*   Never trust client-side price calculations. Always re-calculate totals in a Payload webhook/endpoint before passing them to Stripe.

## 3. Stripe Integration
*   Use Payload hooks to sync Products and Prices with Stripe's API.
*   Implement a dedicated `stripe-webhooks` endpoint in Payload to listen for `checkout.session.completed` and automatically update order status.

## 4. Media Management
*   E-commerce requires optimized images. Ensure `formatOptions` are used in Payload's upload collections (e.g., WebP conversion, multiple sizes).
