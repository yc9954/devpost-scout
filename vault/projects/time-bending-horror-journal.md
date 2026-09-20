---
slug: "time-bending-horror-journal"
url: "https://devpost.com/software/time-bending-horror-journal"
title: "Time Bending horror Journal"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 910
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/accessibility"
  - "domain/labor_employment"
  - "substrate/document_pdf"
---

# Time Bending horror Journal

> **“A haunted digital journal where time fractures. Entries appear from the future, the past rewrites itself, and the interface becomes part of the horror.”**

[Devpost](https://devpost.com/software/time-bending-horror-journal) · hackathon [[Kiroween]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[accessibility]] [[labor_employment]]
**substrate** [[document_pdf]]

**stack** css3, github, html5, javascript, react, tailwind, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for time-bending horror journal

## Body

Welcome to the Time bending Horror Journal This is not A normal Diary (Future echoes , past Echoes and branch Tagline) A ghost is hiding behind this diary Experience The Ambient glitches and Ghost mode Inspiration The idea came from a simple question: What if your journal didn't obey time? I wanted to create something that felt genuinely unsettling—not through jump scares, but through the slow realization that the interface itself is unreliable. Entries appearing from the future, past words rewriting themselves, timelines branching into parallel realities. The horror comes from losing control over your own narrative. For the Kiroween Costume Contest, I saw an opportunity to push the boundaries of what a "haunted UI" could be—where the interface becomes an active participant in the horror experience. What it does Time-Bending Horror Journal is a web application that transforms journaling into a temporal horror experience: Write journal entries that persist across sessions Trigger time anomalies that break causality: Future Echo ⚡ - Entries appear from hours in the future with corrupted text Alter Past ⚠ - Existing entries rewrite themselves with ominous phrases Branch Timeline ⑂ - Reality splits into parallel timeline branches Visualize the chaos with an interactive timeline showing temporal distortions Experience the horror through glitch effects, ghost text, and a cursed UI aesthetic Control the intensity with ritual settings (visual effects, glitch overlays, ambient mode) The app maintains full usability while creating an atmosphere of temporal dread. Your words are never safe. How we built it Built entirely in Kiro IDE using a spec-driven development workflow: 1. Specification Phase Created formal requirements (9 requirements, 45 acceptance criteria) Designed architecture with 11 core components Defined data models and correctness properties Generated 33 sequential implementation tasks 2. Tech Stack React + TypeScript for type-safe components Vite for lightning-fast development Tailwind CSS with custom horror theme Framer Motion for cinematic animations Zustand for state management localStorage for persistence 3. Key Features Implemented Temporal logic engine ( lib/temporal.ts ) with text distortion algorithms Timeline visualization with branch rendering Glitch overlay system with 5 distinct effects Settings panel for customizable horror intensity Temporal cursor trail and animated backgrounds 4. Kiro's Role Kiro's vibe coding generated entire components from natural language prompts. The spec documents ensured consistency across 30+ files, maintaining type safety and architectural coherence throughout. Challenges we ran into 1. Balancing Horror with Usability The biggest challenge was making the interface feel broken and unsettling while remaining fully functional. Too many glitches and it becomes unusable; too few and it's just a dark theme. Solution: Layered effects with user-controlled intensity. 2. Timeline Visualization Representing branching timelines without complex SVG was tricky. I used CSS transforms and absolute positioning to create the "fork" effect, with horizontal offsets for branches and connector lines. 3. Text Distortion Algorithms Creating text corruption that felt ominous but remained readable required iteration. The final approach uses 15-20% corruption rates with strategic placement of glitch characters and reversed words. 4. Performance Multiple animations, glitch effects, and cursor trails could tank performance. Solution: Debounced updates, limited trail points (8 max), and pointer-events: none on overlays. 5. Temporal Logic Managing apparentTime vs createdAt required careful state management. Entries needed to "claim" they're from different times while tracking their real creation time for proper sorting and decay effects. Accomplishments that we're proud of Complete spec-driven workflow : Requirements → Design → Tasks → Implementation, all documented in .kiro/specs/ 33 tasks completed systematically, each building on the previous Zero TypeScript errors thanks to spec-defined types Cinematic polish : Glitch effects, temporal cursor trail, animated backgrounds, ghost text Fully functional : CRUD operations, persistence, timeline visualization, settings panel Genuinely unsettling : The UI creates real unease through subtle wrongness Built in a single session : Kiro's assistance enabled rapid development without sacrificing quality The timeline visualization with color-coded anomalies and branch rendering turned out better than I imagined. Watching entries rewrite themselves is genuinely creepy. What we learned About Kiro: Spec-driven development maintains consistency across complex projects Vibe coding accelerates implementation without losing architectural coherence Type safety from specs prevents entire classes of bugs Clear task breakdown makes large projects manageable About Horror UX: Subtle effects are more unsettling than obvious ones Users need control (settings panel) to avoid overwhelming them Temporal distortion is deeply unsettling—our brains expect time to work Animation timing matters: too fast feels buggy, too slow loses impact Technical Insights: Framer Motion's layoutId creates seamless selection animations Zustand with persistence middleware is perfect for this use case Feature-based architecture scales well (journal, timeline, effects, settings) localStorage serialization requires careful date handling What's next for Time-Bending Horror Journal Immediate Enhancements: AI-powered rewrites : Integrate GPT-4 via MCP for genuinely creative text alterations Sound design : Ambient horror soundscapes with reversed clock ticking Landing page : Proper intro experience with glitch animation More anomaly types : Time loops, entry merging, causality violations Advanced Features: Timeline branch merging : Parallel realities collapsing back together Entry relationships : Visual connections between parent/child entries Export/Import : Share your temporal chaos Collaborative mode : Multiplayer horror where users affect each other's timelines Polish: Accessibility : Screen reader support, reduced motion mode Mobile optimization : Touch-friendly timeline interaction Performance : Web Workers for heavy text processing Analytics : Track which anomalies users find most unsettling The core concept has so much potential. Imagine entries that predict your future actions, or a timeline that loops back on itself. The horror of unreliable time is just beginning. <div