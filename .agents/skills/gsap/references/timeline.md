# GSAP Timelines

A Timeline is a powerful container for sequencing and choreographing multiple tweens. It coordinates timing, controls playback for groups of animations, and supports nesting.

---

## Creating a Timeline

By default, child animations in a timeline are appended chronologically:
```javascript
const tl = gsap.timeline();

tl.to(".box1", { x: 100, duration: 1 })
  .to(".box2", { y: 50, duration: 0.5 })  // starts after box1 finishes
  .to(".box3", { opacity: 0, duration: 0.3 }); // starts after box2 finishes
```

---

## Timeline Defaults

Pass a `defaults` object into the timeline constructor to avoid repeating options in child tweens. Any children will inherit these defaults unless explicitly overridden.

```javascript
// ✅ Clean and DRY code
const tl = gsap.timeline({
  defaults: {
    duration: 0.5,
    ease: "power2.out"
  }
});

tl.to(".box1", { x: 100 }) // Uses duration 0.5, power2.out
  .to(".box2", { y: 50, ease: "bounce.out" }); // Overrides ease with bounce.out
```

---

## The Position Parameter (Choreographing)

The position parameter is the **third argument** of the timeline tween methods. It controls *when* the animation starts relative to other elements in the timeline.

| Position Syntax | Description | Example |
| :--- | :--- | :--- |
| **Absolute Time** | Start at a specific pixel/second mark | `tl.to(".box", {x: 100}, 2)` *(starts exactly at the 2s mark)* |
| **Relative Offset** | Offset from the end of the timeline | `tl.to(".box", {x: 100}, "+=0.5")` *(0.5s gap)* / `"-=0.2"` *(0.2s overlap)* |
| **Labels** | Start at a named marker | `tl.to(".box", {x: 100}, "myLabel")` |
| **Label Offset** | Offset relative to a label | `tl.to(".box", {x: 100}, "myLabel+=0.5")` |
| **Start of Previous** | `<` matches start of most recently added tween | `tl.to(".box2", {y: 50}, "<")` *(starts at the same time as .box1)* |
| **End of Previous** | `>` matches end of most recently added tween | `tl.to(".box2", {y: 50}, ">")` *(equivalent to default behavior)* |
| **Start Offset** | Offset relative to previous start | `tl.to(".box2", {y: 50}, "<0.2")` *(starts 0.2s after .box1 starts)* |

```javascript
const tl = gsap.timeline();

tl.to(".a", { x: 100, duration: 1 })
  .to(".b", { y: 100, duration: 1 }, "<")    // starts at same time as .a
  .to(".c", { scale: 2, duration: 0.5 }, "+=0.2") // starts 0.2s after .b finishes
  .to(".d", { rotation: 90 }, "<0.1");        // starts 0.1s after .c starts
```

---

## Labels

Labels are named markers along the timeline. They are great for organizing complex sequences and controlling playback.

```javascript
const tl = gsap.timeline();

tl.addLabel("intro", 0)
  .to(".title", { opacity: 1 }, "intro")
  .to(".subtitle", { y: 0 }, "intro+=0.2")
  .addLabel("mainContent", "+=0.5")
  .to(".grid", { scale: 1 }, "mainContent");

// Playback control using labels:
tl.play("mainContent"); // Seeks to the label and starts playing
tl.reverse("mainContent"); // Plays backward from the label
```

---

## Playback Controls

You can control the entire timeline as a single entity:
```javascript
const tl = gsap.timeline({ paused: true });

tl.to(".box", { x: 200, duration: 10 });

// Trigger these from React buttons:
tl.play();       // Plays forward
tl.pause();      // Pauses execution
tl.reverse();    // Plays backward from current position
tl.restart();    // Restarts from the beginning
tl.progress(0.5); // Jump directly to 50% progress
tl.time(2);      // Seek to the 2-second mark
```

---

## Nesting Timelines

You can nest timelines inside a master timeline for complex orchestrations:
```javascript
const master = gsap.timeline();

const buildIntro = () => {
  const tl = gsap.timeline();
  tl.from(".logo", { scale: 0 }).to(".title", { opacity: 1 });
  return tl;
};

const buildContent = () => {
  const tl = gsap.timeline();
  tl.from(".cards", { y: 50, stagger: 0.1 });
  return tl;
};

// Add nested timelines
master.add(buildIntro())
      .add(buildContent(), "+=0.3"); // Starts 0.3s after intro finishes
```
