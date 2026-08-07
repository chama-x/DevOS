---
name: awwwards-animations
description: Configuration profile for premium/award-level motion design. Enforces specific easing, scrolling, and interaction constraints.
---

# Premium Motion Configuration

This is a configuration profile, not a textbook. You already know how to write animations. When the user requests Awwwards-level quality, enforce these specific constraints:

## Easing & Timing
1. **Never use defaults:** `linear`, `ease-in`, `ease-out` are forbidden.
2. **Custom curves:** Default to `power3.out`, `power4.out`, or custom cubic-bezier curves `(0.76, 0, 0.24, 1)` for premium tension.
3. **Duration:** Entrances should be snappier (0.6s - 1.2s). Exits should be faster (0.3s - 0.5s).

## Scroll & Parallax
1. **Smooth Scroll:** If full-page scroll effects are requested, mandate a virtual scroll hijacking library like Lenis. Native scroll is not sufficient for premium parallax.
2. **Parallax depth:** Use subtle transform-y offsets (e.g., `-10%` to `10%`). Avoid extreme parallax that induces motion sickness.

## Interactions
1. **Latency:** Micro-interactions (hover, click) must trigger visual feedback within 100ms.
2. **Magnetic effects:** If implementing magnetic buttons, calculate distance from center using `getBoundingClientRect()` and apply spring physics, not linear lerping.

## Transitions
1. **Overlap:** Page transitions must overlap. The outgoing page should start animating out *before* the incoming page finishes animating in.
