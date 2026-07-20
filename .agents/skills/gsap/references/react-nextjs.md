# GSAP in React & Next.js

Using GSAP in React requires understanding component lifecycles, re-renders, cleanup, and Server-Side Rendering (SSR).

## Installation

Ensure the required packages are installed via `npm` / `pnpm` / `yarn`:
```bash
npm install gsap @gsap/react
```

---

## Prefer the `useGSAP()` Hook

For React 18+ and Next.js (App Router or Pages Router), always use the `@gsap/react` hook `useGSAP()` instead of standard React `useEffect()` or `useLayoutEffect()`.

### Key Benefits:
1. **Automatic Revert/Cleanup**: Reverts all tweens, timelines, and ScrollTriggers created during execution automatically when the component unmounts.
2. **Context Scoping**: Restricts element selection to a specific container subtree.
3. **Safety for Event Handlers**: Exposes a `contextSafe()` wrapper to clean up event listeners/asymmetric callbacks.

### Basic Setup with Scope:
```javascript
import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";

// Register the useGSAP hook as a GSAP plugin once before running any animations.
gsap.registerPlugin(useGSAP);

export default function MyComponent() {
  const containerRef = useRef(null);

  useGSAP(() => {
    // Selector strings like ".box" will ONLY target elements inside containerRef
    gsap.to(".box", { x: 200, duration: 1 });
  }, { scope: containerRef });

  return (
    <div ref={containerRef}>
      <div className="box">Target Box</div>
      <div className="box">Another Target Box</div>
    </div>
  );
}
```

---

## Dependency Arrays, Scoping, and `revertOnUpdate`

The `useGSAP` hook takes a configuration object as its second argument:
```javascript
useGSAP(() => {
  gsap.to(".box", { x: endX });
}, {
  dependencies: [endX],      // Triggers re-synchronization when endX changes
  scope: containerRef,        // Limits selection queries
  revertOnUpdate: true        // Reverts existing animations before running the effect again
});
```

* **`dependencies`**: Analogous to `useEffect`'s dependency array. If empty, the hook runs once after mount.
* **`revertOnUpdate`**: Extremely important when dependencies update. Setting this to `true` ensures that old animations are reverted cleanly before generating the new tween, preventing overlapping animation conflicts.

---

## `gsap.context()` in `useEffect` (Failsafe)

If `@gsap/react` is not available, you MUST use `gsap.context()` inside a standard `useEffect` / `useLayoutEffect` to group all animations and kill/revert them on unmount. Failing to do this causes severe memory leaks.

```javascript
import { useEffect, useRef } from "react";
import gsap from "gsap";

export default function FailsafeComponent() {
  const containerRef = useRef(null);

  useEffect(() => {
    // Create a context scoped to containerRef
    const ctx = gsap.context(() => {
      gsap.to(".box", { y: 100 });
    }, containerRef);

    // Return the revert function as react cleanup
    return () => ctx.revert();
  }, []);

  return (
    <div ref={containerRef}>
      <div className="box">Box</div>
    </div>
  );
}
```

---

## Context-Safe Callbacks (`contextSafe`)

Animations created inside click handlers, mouse events, or other async callbacks that run AFTER the component mount are not automatically registered under the context. 

To ensure they are cleaned up on unmount, use the `contextSafe` wrapper:

```javascript
export default function InteractiveComponent() {
  const containerRef = useRef(null);

  // Extract contextSafe from the hook parameters or returned value
  const { contextSafe } = useGSAP({ scope: containerRef });

  // Wrap the event handler with contextSafe
  const handleMouseEnter = contextSafe((event) => {
    gsap.to(event.currentTarget, { scale: 1.1, duration: 0.2 });
  });

  return (
    <div ref={containerRef}>
      <div className="box" onMouseEnter={handleMouseEnter}>Hover Me</div>
    </div>
  );
}
```

---

## Server-Side Rendering (SSR) in Next.js

GSAP relies on DOM API availability (like `window` and document nodes). During SSR, these properties do not exist.

### 1. Run animations client-side only
Since `useGSAP` and `useEffect` only run in the browser, any animations placed inside them are inherently SSR-safe.
```javascript
// ✅ Safe: only runs on client mount
useGSAP(() => {
  gsap.to(".box", { opacity: 1 });
});
```

### 2. Guard Top-Level API calls
Do NOT call GSAP animations, register plugins, or execute gsap global controls directly in the module body if they require browser-only context.
```javascript
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

// ✅ Safe: Registering plugins top-level is safe
gsap.registerPlugin(ScrollTrigger);

// ❌ UNSAFE: Calling window/document based animations top-level will crash Next.js SSR build
gsap.to(window, { scrollTo: 0 }); 
```

### 3. Use `'use client'` Directive
Always include the `'use client'` directive at the top of Next.js App Router files where GSAP is imported and used, to indicate it is a Client Component.

### 4. Handling third-party libraries (Dynamic Import)
If a third-party slider or carousel imports GSAP at the top-level and causes SSR issues during the build, import it dynamically:
```javascript
import dynamic from "next/dynamic";

const AnimatedCarousel = dynamic(() => import("./AnimatedCarousel"), {
  ssr: false,
});
```
