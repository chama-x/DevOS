---
name: gsap
description: Configuration profile for GSAP animations in React/Next.js. Enforces architectural constraints and performance standards.
---

# GSAP Architecture Configuration

This is a configuration profile, not a textbook. You already know the GSAP API. Apply these constraints strictly when writing GSAP code for this project:

## React Integration
1. **Hook:** ALWAYS use the `@gsap/react` `useGSAP` hook. Never use raw `useEffect` or `useLayoutEffect` for GSAP.
2. **Scope:** Always pass the container ref to the `useGSAP` scope `{ scope: containerRef }`.
3. **Cleanup:** Rely on `useGSAP`'s automatic cleanup. Do not manually kill tweens unless dynamically created outside the initial render cycle.

## ScrollTrigger Rules
1. **Pinning:** Pin to a specific local DOM node ref, never to `document.body` or `window`.
2. **Markers:** Disable markers in production.
3. **Refresh:** If layout changes dynamically (images loading, accordions), ensure `ScrollTrigger.refresh()` is called, but debounce it.

## Performance Constraints
1. **Properties:** Animate ONLY composited properties: `transform` (x, y, scale, rotation) and `opacity`.
2. **Layout Thrashing:** NEVER animate width, height, top, left, margin, or padding. If you must scale a layout element, use `transform: scale()`.
3. **Will-Change:** Use `will-change: transform` cautiously, only on elements currently animating or about to animate.
