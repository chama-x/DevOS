# GSAP Core Tween API

Tweens are the building blocks of GSAP. A Tween does all the animation work: animating property values of targets (elements or objects) over time.

## Core Methods

* **`gsap.to(targets, vars)`**: Animates elements from their current state to the values defined in `vars`. (Most commonly used).
* **`gsap.from(targets, vars)`**: Animates elements from the values in `vars` to their current state (ideal for entrance animations).
* **`gsap.fromTo(targets, fromVars, toVars)`**: Explicitly defines both the start values (`fromVars`) and end values (`toVars`).
* **`gsap.set(targets, vars)`**: Instantly sets properties to target values (duration 0).

---

## Transform Aliases (Prefer over raw CSS transforms)

Always use GSAP's transform aliases instead of writing raw CSS `transform` strings. They are faster, cross-browser compatible, and apply in a stable order (translation → scale → rotation → skew).

| GSAP Property | CSS Equivalent / Notes |
| :--- | :--- |
| `x` / `y` / `z` | `translateX` / `translateY` / `translateZ` (Default unit: `px`) |
| `xPercent` / `yPercent` | `translateX` / `translateY` in percentage (e.g. `xPercent: -50`) |
| `scale` | Animates both `scaleX` and `scaleY` |
| `scaleX` / `scaleY` | Scale along X or Y axis |
| `rotation` | `rotate` (Default unit: degrees; e.g. `360` or rad strings like `"1.5rad"`) |
| `rotationX` / `rotationY` | 3D rotations |
| `skewX` / `skewY` | Skew angle |
| `transformOrigin` | origin of transforms (e.g., `"50% 50%"` or `"left top"`) |

*Relative values*: You can animate relative to the current value using string prefixes:
`x: "+=100"` (moves 100px right), `rotation: "-=45"` (rotates 45deg counter-clockwise).

---

## AutoAlpha (Opacity + Visibility)

Always prefer **`autoAlpha`** over `opacity` when fading elements out completely.
- At `0`, `autoAlpha` sets `opacity: 0` AND `visibility: hidden`.
- At any value greater than `0`, it sets `visibility: inherit`.
This prevents invisible elements from blocking user mouse events or links.

```javascript
// ✅ Correct
gsap.to(".overlay", { autoAlpha: 0, duration: 0.5 });
```

---

## Easing

GSAP offers a rich set of built-in easing curves. Use string identifiers:
* **`"power1.out"`** (default: gradual slow down)
* **`"power3.inOut"`** (strong accelerate, strong decelerate)
* **`"back.out(1.7)"`** (overshoot and settle)
* **`"elastic.out(1, 0.3)"`** (springy bounce)
* **`"none"`** (linear speed)

### Custom Easing:
For custom curves, use `CustomEase` (requires registering the plugin):
```javascript
import { CustomEase } from "gsap/CustomEase";
gsap.registerPlugin(CustomEase);

const custom = CustomEase.create("hop", "M0,0 C0.1,0.5 0.3,1 1,1");
gsap.to(".box", { ease: custom });
```

---

## Staggering

Stagger offsets the start times of animations across an array of targets:
```javascript
// Simplest form: start each animation 0.1s after the previous one
gsap.to(".item", { y: -50, stagger: 0.1 });

// Advanced object form:
gsap.to(".item", {
  opacity: 1,
  stagger: {
    amount: 0.5,        // Total time distributed among all targets
    from: "center",     // Animation starts from the center outward ("start", "end", "edges", "random")
    grid: "auto"        // For 2D grids (auto-detects rows and columns)
  }
});
```

---

## Pitfall: Multiple `from()` or `fromTo()` Tweens (`immediateRender`)

By default, `.from()` and `.fromTo()` tweens render their starting values **immediately** when created. 

If you stack multiple `.from()` or `.fromTo()` animations targeting the same element and property in sequence, the second animation will capture the "immediate" start state of the first animation as its final destination, causing unexpected visual jumps.

### Solution:
Set **`immediateRender: false`** on any subsequent tweens targeting the same property.
```javascript
const tl = gsap.timeline();
tl.from(".box", { x: -100, duration: 1 })
  // Since this is the second 'from' tween on the same property, prevent immediate render
  .from(".box", { opacity: 0, immediateRender: false }, "+=0.5");
```

---

## Responsive & Accessibility with `gsap.matchMedia()`

To make animations responsive or disable them for users who prefer reduced motion, always use **`gsap.matchMedia()`**.

It automatically cleans up and reverts animations when the viewport changes breakpoints.

```javascript
useGSAP(() => {
  let mm = gsap.matchMedia();

  mm.add({
    isDesktop: "(min-width: 800px)",
    isMobile: "(max-width: 799px)",
    reduceMotion: "(prefers-reduced-motion: reduce)"
  }, (context) => {
    const { isDesktop, reduceMotion } = context.conditions;

    if (reduceMotion) {
      // Disable movement for accessibility
      gsap.set(".box", { opacity: 1 });
      return;
    }

    gsap.to(".box", {
      x: isDesktop ? 300 : 100,
      rotation: 360,
      duration: 1
    });
  }, containerRef); // Scoped to ref

  // mm.revert() is automatically handled if inside useGSAP!
}, { scope: containerRef });
```
