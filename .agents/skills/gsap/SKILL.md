---
name: gsap
description: Official GSAP skill for React and Next.js. Use when implementing, refactoring, or optimizing GSAP animations in React components or Next.js pages. This covers the useGSAP hook, ScrollTrigger, timelines, performance, and plugins (Flip, Draggable, SplitText, MorphSVG, etc.).
---

# GSAP with React & Next.js

This skill defines the best practices for using the GreenSock Animation Platform (GSAP) inside React and Next.js applications.

## Quick Reference Guides

For deep-dives into specific GSAP features, consult the modular reference guides:
1. **[React & Next.js Lifecycle & useGSAP](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/react-nextjs.md)**: Details `useGSAP` hook, scoping refs, `contextSafe`, and SSR safety.
2. **[Core Tween API](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/core.md)**: Covers `gsap.to()`, `from()`, `fromTo()`, transform aliases, and easing.
3. **[Timeline Sequencing](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/timeline.md)**: Explains `gsap.timeline()`, position parameter, and labels.
4. **[ScrollTrigger](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/scrolltrigger.md)**: Scroll-linked animation, pinning, scrub, and `containerAnimation`.
5. **[GSAP Plugins](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/plugins.md)**: Guide to registering and using SplitText, Flip, Draggable, MorphSVG, etc.
6. **[Performance & Optimizations](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/performance.md)**: Best practices for smooth 60fps, `quickTo()`, and avoiding layout thrashing.
7. **[Templates & Choreography](file:///Users/chamaththiwanka/Desktop/0/Projects/chx.cortana.lk/.agents/skills/gsap/references/templates-choreography.md)**: Reusable React component templates (AnimatedHero, ScrollRevealSection, TextReveal) and curated boilerplate starter links.

---

## 3 Core Rules for React Animating

### 1. ALWAYS use the `useGSAP` hook
Never use standard React `useEffect` or `useLayoutEffect` for GSAP setup unless `@gsap/react` is unavailable. The `useGSAP` hook handles automatic cleanup (killing running tweens/ScrollTriggers and reverting inline styles) on unmount.
```javascript
import { useGSAP } from "@gsap/react";
import gsap from "gsap";

useGSAP(() => {
  gsap.to(".box", { x: 100 });
}, { scope: containerRef });
```

### 2. ALWAYS scope your selectors
Always pass a `scope` container `ref` in the `useGSAP` options. This ensures that GSAP selector strings (like `".box"`) are strictly query-selected within that container, preventing selector collision across different components.

### 3. ALWAYS use `contextSafe` for asynchronous callbacks
If you create animations inside event handlers or callbacks that execute AFTER the main component render, they will not be registered in the GSAP context and won't clean up automatically. Wrap them in `contextSafe`.
```javascript
const { contextSafe } = useGSAP({ scope: containerRef });

const onMouseEnter = contextSafe(() => {
  gsap.to(".box", { scale: 1.2 });
});
```

---

## Next.js (SSR) Guidelines
GSAP requires access to the DOM window object.
- **Client Components**: Mark files containing GSAP animation logic with `'use client'` at the very top.
- **Client-Side Only**: Ensure all animation execution resides inside `useGSAP` or client-only handlers.
- **Dynamic Imports**: If importing third-party libraries that bundle GSAP and run code at load time, load them dynamically in React with `{ ssr: false }`.
