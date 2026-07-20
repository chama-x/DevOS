# GSAP Performance Optimizations

To ensure smooth 60fps (or 120fps) animations and eliminate layout jank, follow these optimization guidelines.

---

## 1. Prefer Composited Properties (GPU Acceleration)

Always animate properties that do not trigger page layout or repaint, as they are handled by the compositor thread on the GPU.

- **✅ DO Animate (Compositor Only)**:
  - Translations: `x`, `y`, `z`
  - Scale: `scale`, `scaleX`, `scaleY`
  - Rotation: `rotation`, `rotationX`, `rotationY`
  - Skew: `skewX`, `skewY`
  - Opacity: `opacity`, `autoAlpha`

- **❌ AVOID Animating (Triggers Layout Thrashing)**:
  - Layout offsets: `top`, `left`, `bottom`, `right`
  - Box dimensions: `width`, `height`, `margin`, `padding`
  - Typography: `font-size`, `letter-spacing`

```javascript
// ❌ Poor Performance (triggers layout recalculation on every frame)
gsap.to(".box", { left: 200, width: 300 });

// ✅ High Performance (only handles transform layers on the GPU compositor)
gsap.to(".box", { x: 200, scale: 1.5 });
```

---

## 2. Using `will-change` (CSS)

Add the `will-change: transform` or `will-change: transform, opacity` CSS property to elements that will animate. This advises the browser to promote the element to its own GPU layer beforehand.

```css
.animating-element {
  will-change: transform, opacity;
}
```

> [!CAUTION]
> Do NOT set `will-change` on all elements. Over-promoting elements to GPU layers wastes system memory and can actually decrease performance. Apply it selectively only to primary animating items.

---

## 3. High-Frequency Animations (`gsap.quickTo()`)

If you are updating values at a high frequency (like mouse trackers, scrolling coordinates, parallax multipliers, or custom drag handlers), do NOT instantiate a new tween on every frame. Instead, use **`gsap.quickTo()`**, which returns a function that dynamically updates a single cached tween instance.

```javascript
import { useRef } from "react";
import gsap from "gsap";
import { useGSAP } from "@gsap/react";

export default function MouseFollower() {
  const followerRef = useRef(null);

  useGSAP(() => {
    // Cache the target tweens
    const xTo = gsap.quickTo(followerRef.current, "x", { duration: 0.3, ease: "power3" });
    const yTo = gsap.quickTo(followerRef.current, "y", { duration: 0.3, ease: "power3" });

    const handleMouseMove = (e) => {
      xTo(e.clientX);
      yTo(e.clientY);
    };

    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, { scope: followerRef });

  return <div ref={followerRef} className="follower" style={{ position: "fixed" }} />;
}
```

---

## 4. ScrollTrigger Performance

ScrollTrigger evaluates layout positions on scroll. Keep performance optimal by:
- **`scrub` smoothness**: Avoid heavy calculations or layouts during scrub. Scrubbing with a lag factor (e.g. `scrub: 1`) is often easier on the browser than `scrub: true`.
- **Debounced Refresh**: Call `ScrollTrigger.refresh()` only when the DOM structure changes (e.g., loaded image assets, client-side pagination). Avoid call-frequency spikes.
- **Pin Sparingly**: Pinning wraps elements in spacers and modifies style offsets. Keep the pinned elements as lightweight as possible.

---

## 5. Prevent Layout Thrashing

Layout thrashing occurs when your code repeatedly reads layout properties (e.g., `offsetHeight`, `getBoundingClientRect()`) and then writes style updates (causing layout reflow).
- Let GSAP handle style writes; it batches updates internally.
- If you must read layout properties during an animation, read them ahead of time outside the animation timeline loop, or batch all reads together before starting the animations.
