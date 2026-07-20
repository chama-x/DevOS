# GSAP Plugins Guide

Plugins extend GSAP's core functionality to handle specific animating needs (SVG morphing, smooth layouts, dragging, text splitting, etc.).

---

## Club GSAP Update (Free & Standard Packages)

Following Webflow's acquisition of GSAP, **all premium GSAP plugins are now free, even for commercial use**. 
- ❌ Do NOT generate a `.npmrc` file with an auth token or configure `npm.greensock.com`.
- ❌ Do NOT tell developers to purchase a license key or sign up for Club GSAP.
- ✅ Simply import all plugins directly from the standard public `gsap` package (e.g. `import { SplitText } from "gsap/SplitText";`).

---

## Registration

Every plugin must be registered once before use, typically at the top level of the component or app entrypoint:
```javascript
import gsap from "gsap";
import { SplitText } from "gsap/SplitText";
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";

gsap.registerPlugin(SplitText, MorphSVGPlugin);
```

---

## SplitText (Text Animations)

`SplitText` breaks text blocks into characters, words, and/or lines, enclosing each in standard DOM nodes to enable staggered entrance animations.

```javascript
useGSAP(() => {
  // 1. Create the split instance
  const split = SplitText.create(".title", {
    type: "words,chars",
    autoSplit: true, // Automatically re-splits text if font finishes loading or container resizes
    onSplit(self) {
      // 2. Animate the split characters
      return gsap.from(self.chars, {
        opacity: 0,
        y: 20,
        stagger: 0.02,
        duration: 0.4
      });
    }
  });

  // SplitText instances are automatically reverted on unmount when inside useGSAP
}, { scope: containerRef });
```

---

## Flip (Layout & DOM transitions)

Flip captures layout states (size, position, rotation) of elements and animates them smoothly when their styling or DOM order changes (FLIP: First, Last, Invert, Play).

```javascript
import { Flip } from "gsap/Flip";
gsap.registerPlugin(Flip);

const toggleLayout = () => {
  // 1. Capture the initial state
  const state = Flip.getState(".item");

  // 2. Modify the DOM (e.g., change grid layout classes or append to a new parent)
  document.querySelector(".container").classList.toggle("active-layout");

  // 3. Animate between First and Last states
  Flip.from(state, {
    duration: 0.6,
    ease: "power2.inOut",
    stagger: 0.05,
    absolute: true // Uses position: absolute during transition to avoid layout breaking
  });
};
```

---

## Draggable & Inertia

Enables touch/mouse dragging, throwing, and momentum scrolling on DOM nodes.

```javascript
import { Draggable } from "gsap/Draggable";
import { InertiaPlugin } from "gsap/InertiaPlugin";
gsap.registerPlugin(Draggable, InertiaPlugin);

Draggable.create(".knob", {
  type: "rotation",
  bounds: { minRotation: 0, maxRotation: 360 },
  inertia: true // Enables smooth glide throw momentum
});
```

---

## SVG Plugins

### 1. DrawSVG (Stroke outline drawing)
Reveals or hides SVG strokes by animating `stroke-dashoffset`.
```javascript
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
gsap.registerPlugin(DrawSVGPlugin);

// Draw outline stroke from start (0%) to end (100%)
gsap.fromTo("#path-id", { drawSVG: "0% 0%" }, { drawSVG: "0% 100%", duration: 1.5 });
```

### 2. MorphSVG (Shape Morphing)
Morphs one SVG path into another, even if the paths have different point counts.
```javascript
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";
gsap.registerPlugin(MorphSVGPlugin);

// Convert primitives (circles, rects) to paths first if necessary
MorphSVGPlugin.convertToPath("circle, rect");

gsap.to("#circle-path", {
  morphSVG: "#star-path",
  duration: 1
});
```

### 3. MotionPath (Follow Curve)
Animates elements along an SVG path coordinates.
```javascript
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
gsap.registerPlugin(MotionPathPlugin);

gsap.to(".dot", {
  motionPath: {
    path: "#path-id",
    align: "#path-id",
    alignOrigin: [0.5, 0.5],
    autoRotate: true
  },
  duration: 2
});
```

---

## ScrollToPlugin (Scroll coordinates/elements)

Animates the scroll position of the window or a scrollable element container.

```javascript
import { ScrollToPlugin } from "gsap/ScrollToPlugin";
gsap.registerPlugin(ScrollToPlugin);

// Scroll the browser window to #section-id
gsap.to(window, {
  duration: 1,
  scrollTo: { y: "#section-id", offsetY: 50 },
  ease: "power2.inOut"
});
```
