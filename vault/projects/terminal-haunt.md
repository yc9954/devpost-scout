---
slug: "terminal-haunt"
url: "https://devpost.com/software/terminal-haunt"
title: "Haunted Portfolio"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 686
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
---

# Haunted Portfolio

> A spine-chilling developer portfolio that haunts visitors with interactive animations and eerie design — where code meets the supernatural.

[Devpost](https://devpost.com/software/terminal-haunt) · hackathon [[Kiroween]]

## Facets

**domain** [[accessibility]] [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** framer-motion, howler.js, react, tailwindcss, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for haunted portfolio

## Body

About Contact Projects Hero Section Inspiration Every Halloween, developers transform their portfolios into digital haunted houses. But most stop at slapping on a dark theme and calling it spooky. I wanted to create something that would make visitors genuinely question if their browser was possessed. Something that respected the craft of horror game design while showcasing technical skills. When I heard about Kiroween 2025's Costume Contest, I knew this was my chance to resurrect the dead art of memorable portfolio websites. What it does Haunted Portfolio is a fully functional developer portfolio that feels like stepping into a horror game. It features: The Summoning (Landing) : A parallax graveyard with floating spirits, atmospheric fog, and ghostly text reveals The Séance (About) : Your bio emerges from a mystical crystal ball while tarot cards showcase your skills The Graveyard (Projects) : Each project is a tombstone that rises from the grave on scroll. Click to open a haunted modal shrouded in cobwebs Contact the Spirit (Contact) : An interactive Ouija board contact form where a planchette follows your typing Global effects include a ghost cursor with trail, random lightning flashes, blood drips, crawling spiders, and decorative cobwebs—all while respecting prefers-reduced-motion for accessibility. How we built it The project was built using Kiro's spec-driven development workflow : Spec Phase : Created detailed requirements.md , design.md , and tasks.md documents Steering : Established coding standards for consistent TypeScript patterns and animation guidelines Implementation : Built 50+ React components with TypeScript, styled with Tailwind CSS, and animated with Framer Motion Key technical implementations: Custom particle system for fog/mist effects SVG-based ghost cursor with physics-based trailing Intersection Observer API for scroll-triggered "rise from grave" animations CSS transforms for 3D tombstone tilting Framer Motion orchestration for complex multi-stage animations The tech stack includes React 18, TypeScript, Vite, Tailwind CSS 4, and Framer Motion for buttery-smooth 60fps animations. Challenges we ran into Performance vs. Spectacle : The biggest challenge was balancing visual richness with performance. Running particle systems, parallax effects, and multiple simultaneous animations nearly melted older devices. Solution: Implemented IntersectionObserver to only animate visible elements and used CSS transforms + will-change hints for GPU acceleration. Accessibility Without Sacrificing Theme : Making a horror-themed site accessible seems contradictory—spooky effects can trigger motion sickness or seizures. I added comprehensive prefers-reduced-motion support, disabled all jump scares by default, and ensured high contrast ratios throughout. The site is fully keyboard navigable with proper ARIA labels. The Ouija Board Physics : Making the planchette movement feel natural while following text input was surprisingly complex. Had to implement custom easing functions and lerp interpolation to prevent jittery motion. Accomplishments that we're proud of Every animation is cancellable : No janky interrupted transitions Zero layout shift : All decorative elements are absolutely positioned Fully responsive : From 320px mobile to 4K displays WCAG AA compliant : Despite the dark theme and spooky effects Production-ready : Proper error boundaries, loading states, and fallbacks Kiro-powered workflow : The entire project was built using spec-driven development with custom steering documents What we learned Specs Save Time : Writing detailed specifications upfront prevented scope creep and kept features focused Animation Orchestration : Framer Motion's orchestration API is incredibly powerful for complex multi-step animations Performance Profiling : Learned to use React DevTools Profiler and Chrome's Performance tab to identify render bottlenecks Accessibility Testing : Tested with screen readers (NVDA, JAWS) and keyboard-only navigation CSS Transform Optimization : transform and opacity are the only properties you should animate for 60fps What's next for Haunted Portfolio Sound Effects System : Add toggleable atmospheric audio (howling wind, creaking doors) using Howler.js CMS Integration : Connect to Sanity.io so non-developers can update projects without touching code Easter Eggs : Hidden ARG-style secrets scattered throughout the site (maybe a Konami code?) Theme Variants : Additional seasonal themes (Christmas haunted manor, Valentine's vampire castle) Performance Mode : Ultra-low graphics mode that still looks great but runs on a potato 3D Elements : Experiment with Three.js for a 3D graveyard scene Built with 🖤 and dark magic for Kiroween 2025 "The code you write today haunts the developers of tomorrow" <div