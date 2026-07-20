# GSAP React/Next.js Animation Templates

This reference guide provides production-ready, fully choreographed React component templates and curated resources for building high-end interactive websites.

---

## Curated Official Starters (StackBlitz)

Use these official StackBlitz starter projects to inspect real, working environments with GSAP configuration and routing:

*   **[GSAP Next.js Starters Collection](https://stackblitz.com/@gsap-dev/collections/gsap-nextjs-starters)**: The definitive collection of Next.js App Router and Pages Router boilerplate templates.
*   **[GSAP React Starter Kit](https://stackblitz.com/edit/react-gsap-starter)**: standard React Vite project pre-configured with GSAP and the `@gsap/react` package.
*   **[Next.js Page Transitions Boilerplate](https://stackblitz.com/edit/nextjs-gsap-page-transitions)**: Standard code structure illustrating route transition animations.

---

## 1. Choreographed Hero Entry (`AnimatedHero.jsx`)

An award-winning hero entrance choreography pattern. It stages elements sequentially (Background scale/fade first, title reveal next, subtitle entry, and staggered feature cards).

```jsx
'use client';

import { useRef } from 'react';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';

export default function AnimatedHero() {
  const heroRef = useRef(null);

  useGSAP(() => {
    // Create a choreographed timeline
    const tl = gsap.timeline({
      defaults: { ease: 'power4.out', duration: 1.2 }
    });

    // Sequence of animations using relative timing parameters
    tl.from('.hero-bg', { scale: 1.2, opacity: 0, duration: 1.8 })
      .from('.hero-title', { y: 100, autoAlpha: 0, skewY: 5 }, '<0.4') // starts 0.4s after background starts
      .from('.hero-desc', { y: 30, autoAlpha: 0 }, '<0.3')            // starts 0.3s after title starts
      .from('.hero-cta', { y: 20, autoAlpha: 0 }, '<0.2')
      .from('.hero-card', { 
        y: 50, 
        autoAlpha: 0, 
        stagger: 0.15,
        ease: 'back.out(1.4)' 
      }, '<0.3'); // staggered cards slide up with elastic back ease
  }, { scope: heroRef });

  return (
    <section ref={heroRef} className="relative min-h-screen overflow-hidden flex flex-col justify-center bg-black text-white px-8">
      {/* Background Graphic */}
      <div className="hero-bg absolute inset-0 bg-gradient-to-tr from-gray-900 to-black opacity-80" />

      <div className="relative z-10 max-w-4xl mx-auto space-y-6">
        <h1 className="hero-title text-6xl md:text-8xl font-extrabold tracking-tight">
          Crafting Antigravity.
        </h1>
        <p className="hero-desc text-xl text-gray-400 max-w-2xl">
          Beautifully choreographed motion systems for web applications that demand peak visual elegance and composability.
        </p>
        <div className="hero-cta">
          <button className="bg-white text-black px-8 py-4 rounded-full font-bold hover:bg-gray-200 transition-colors">
            Get Started
          </button>
        </div>
      </div>

      {/* Feature cards below */}
      <div className="relative z-10 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto mt-16 w-full">
        {[1, 2, 3].map((num) => (
          <div key={num} className="hero-card bg-gray-900/50 backdrop-blur border border-gray-800 p-6 rounded-2xl">
            <h3 className="text-xl font-bold mb-2">Feature {num}</h3>
            <p className="text-gray-400 text-sm">Synchronized entrances using fine-grained timeline choreography.</p>
          </div>
        ))}
      </div>
    </section>
  );
}
```

---

## 2. ScrollTrigger Panel Reveal (`ScrollRevealSection.jsx`)

A pinned section reveal template. It pins the container, scrubs content changes relative to scroll progress, and uses batching for child cards.

```jsx
'use client';

import { useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useGSAP } from '@gsap/react';

gsap.registerPlugin(ScrollTrigger);

export default function ScrollRevealSection() {
  const sectionRef = useRef(null);

  useGSAP(() => {
    // 1. Pinned header with scroll-scale
    gsap.to('.reveal-header', {
      scale: 0.8,
      opacity: 0.2,
      scrollTrigger: {
        trigger: sectionRef.current,
        start: 'top top',
        end: '+=400',
        scrub: true,
        pin: '.reveal-header-wrap'
      }
    });

    // 2. Batched entrance for content cards as they enter viewport
    ScrollTrigger.batch('.reveal-card', {
      start: 'top 85%',
      onEnter: (batch) => gsap.to(batch, { 
        autoAlpha: 1, 
        y: 0, 
        stagger: 0.1, 
        duration: 0.8, 
        ease: 'power3.out' 
      }),
      onLeaveBack: (batch) => gsap.set(batch, { autoAlpha: 0, y: 50 })
    });
  }, { scope: sectionRef });

  return (
    <section ref={sectionRef} className="bg-gray-950 py-32 px-6">
      <div className="reveal-header-wrap h-64 flex items-center justify-center mb-24">
        <h2 className="reveal-header text-4xl md:text-6xl font-black text-center text-white">
          Scroll Down to Discover
        </h2>
      </div>

      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        {[1, 2, 3, 4].map((id) => (
          <div 
            key={id} 
            className="reveal-card opacity-0 translate-y-[50px] bg-gray-900 border border-gray-800 p-8 rounded-3xl"
          >
            <span className="text-purple-500 font-mono text-sm font-bold">STEP 0{id}</span>
            <h3 className="text-2xl font-bold text-white mt-2 mb-4">Batched Reveal Block</h3>
            <p className="text-gray-400">
              This card is triggered using ScrollTrigger.batch() which groups elements that enter the viewport together and staggers them.
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
```

---

## 3. Premium Line-by-Line Reveal (`TextReveal.jsx`)

An award-winning typography reveal animation that masks text within hidden bounding boxes (`overflow-hidden`) and slides lines/words up. 

If `SplitText` is registered, it uses it; otherwise, it degrades gracefully to a CSS-wrapped line structure.

```jsx
'use client';

import { useRef } from 'react';
import gsap from 'gsap';
import { SplitText } from 'gsap/SplitText';
import { useGSAP } from '@gsap/react';

gsap.registerPlugin(SplitText);

export default function TextReveal() {
  const containerRef = useRef(null);

  useGSAP(() => {
    // Check if SplitText is loaded
    if (gsap.plugins.splitText) {
      const split = SplitText.create('.mask-text', {
        type: 'lines,words',
        linesClass: 'overflow-hidden line-parent',
        wordsClass: 'inline-block'
      });

      gsap.from(split.words, {
        yPercent: 100,
        rotateX: 10,
        stagger: 0.05,
        duration: 1,
        ease: 'power4.out'
      });
    } else {
      // Graceful fallback for environments where SplitText did not load
      gsap.from('.fallback-line span', {
        yPercent: 100,
        stagger: 0.1,
        duration: 1,
        ease: 'power4.out'
      });
    }
  }, { scope: containerRef });

  return (
    <div ref={containerRef} className="py-24 bg-zinc-950 flex flex-col items-center justify-center text-center">
      {/* Premium SplitText Target */}
      <h2 className="mask-text text-3xl md:text-5xl font-semibold leading-tight text-white max-w-3xl px-6">
        Great designs are not just visually pleasing; they are Choreographed.
      </h2>

      {/* Fallback Markups (Hidden if SplitText runs) */}
      {!gsap.plugins.splitText && (
        <div className="text-2xl md:text-4xl text-gray-500 max-w-xl mt-8">
          <div className="fallback-line overflow-hidden h-[1.3em]">
            <span className="inline-block">This is fallback reveal line 1</span>
          </div>
          <div className="fallback-line overflow-hidden h-[1.3em]">
            <span className="inline-block">This is fallback reveal line 2</span>
          </div>
        </div>
      )}
    </div>
  );
}
```

---

## Essential Learning & Resource Directory

- **[Official GSAP + React Integration Docs](https://gsap.com/resources/React)**: Covers advanced routing guides, context, and optimization tips.
- **[GSAP GreenSock Forums](https://gsap.com/community/)**: Active community support forum for troubleshooting complex animation bugs.
- **[ScrollTrigger Showcase](https://gsap.com/showcase/)**: Curated production-level scrolling site showcase for inspiration.
