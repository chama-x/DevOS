# GSAP ScrollTrigger

ScrollTrigger allows you to create scroll-driven animations, pin elements, scrub animations to the scroll progress, and trigger custom callbacks on scroll milestones.

---

## Registration

Always register the plugin before using it:
```javascript
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
```

---

## Basic Trigger Configuration

You can attach a `scrollTrigger` object directly inside a tween's `vars`:

```javascript
gsap.to(".box", {
  x: 500,
  scrollTrigger: {
    trigger: ".box",        // Element that triggers the animation
    start: "top center",     // "triggerElementPosition viewportPosition" -> when top of box hits center of viewport
    end: "bottom 20%",       // when bottom of box hits 20% from the top of viewport
    toggleActions: "play reverse play reverse", // onEnter, onLeave, onEnterBack, onLeaveBack
    markers: true            // Show start/end lines for debugging (remove in production)
  }
});
```

### Start & End Positions:
* Can be keywords: `top`, `center`, `bottom`, `left`, `right`.
* Can be percentages or pixels: `80%`, `100px`.
* Can be relative strings: `"+=300"` (ends 300px after start).
* Can be wrapped in `clamp()` (v3.12+) to respect scroller boundaries: `start: "clamp(top bottom)"`.
* Can be a function: `start: () => "top " + myDynamicOffset`.

### ToggleActions:
Defines behavior at four scroll states: `onEnter`, `onLeave`, `onEnterBack`, `onLeaveBack`.
Options: `"play"`, `"pause"`, `"resume"`, `"reset"`, `"restart"`, `"complete"`, `"reverse"`, `"none"`.

---

## Scrubbing (Scroll-Linked Playhead)

Scrubbing links the animation playhead directly to the scrollbar progress.

```javascript
gsap.to(".progress-bar", {
  scaleX: 1,
  scrollTrigger: {
    trigger: ".container",
    start: "top top",
    end: "bottom bottom",
    scrub: true // Can be a number in seconds (e.g. 1) for a smooth catch-up delay
  }
});
```

---

## Pinning

Pinning locks an element in place during scroll while another range of scrolling takes place.

```javascript
gsap.to(".panel", {
  scrollTrigger: {
    trigger: ".panel",
    start: "top top",
    end: "+=1000",   // Pin for 1000px of scrolling
    pin: true,        // Pin the trigger element
    pinSpacing: true  // Adds padding to push down content below so it doesn't overlap
  }
});
```

> [!WARNING]
> Do NOT animate the pinned element itself (like `scale` or `y`) as it will fight with the pinning container transforms. Instead, animate a child element inside the pinned container.

---

## ScrollTrigger with Timelines

When using ScrollTrigger with a timeline, **always** put the `scrollTrigger` config in the `timeline()` constructor, **never** on individual tweens inside the timeline.

```javascript
// ✅ Correct
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".container",
    start: "top top",
    end: "+=1000",
    scrub: 1,
    pin: true
  }
});

tl.to(".box1", { x: 100 })
  .to(".box2", { y: 100 }); // Sequenced relative to the scrollbar progress
```

---

## Fake Horizontal Scroll (`containerAnimation`)

To trigger vertical animations while a panel scrolls horizontally (usually pinned vertical scroll translating a wrapper left):

1. Animate the horizontal wrapper using `ease: "none"`.
2. Reference that tween/timeline as the `containerAnimation` in other ScrollTriggers.

```javascript
// 1. Setup the horizontal panel scroll
const horizontalTween = gsap.to(".horizontal-wrapper", {
  x: () => -(document.querySelector(".horizontal-wrapper").scrollWidth - window.innerWidth),
  ease: "none", // MUST BE NONE
  scrollTrigger: {
    trigger: ".container",
    pin: true,
    scrub: 1,
    start: "top top",
    end: "+=3000"
  }
});

// 2. Trigger individual actions based on horizontal progress
gsap.from(".nested-box", {
  scale: 0,
  scrollTrigger: {
    trigger: ".nested-box",
    containerAnimation: horizontalTween, // Reference the horizontal scroll
    start: "left center", // Triggered when left of nested-box hits center of viewport horizontally
    toggleActions: "play none none reset"
  }
});
```

---

## Batched Triggers (`ScrollTrigger.batch()`)

Useful for staggering entrance animations on long lists as they scroll into view.

```javascript
ScrollTrigger.batch(".card", {
  interval: 0.1, // Wait 0.1s to capture multiple cards scrolling in
  batchMax: 4,   // Max size of a single batch
  onEnter: (batch) => gsap.to(batch, { opacity: 1, y: 0, stagger: 0.1, overwrite: true }),
  onLeaveBack: (batch) => gsap.set(batch, { opacity: 0, y: 50, overwrite: true })
});
```

---

## Cleanup in React

ScrollTriggers must be unregistered and killed on page transitions or component unmount to prevent severe performance decay.

If using `useGSAP`, this is handled automatically. If you must do it manually:
```javascript
useEffect(() => {
  const trigger = ScrollTrigger.create({
    trigger: ".box",
    start: "top center"
  });

  return () => {
    trigger.kill();
  };
}, []);
```
To kill all active ScrollTriggers (useful during SPA page transitions):
```javascript
ScrollTrigger.getAll().forEach(trigger => trigger.kill());
```
