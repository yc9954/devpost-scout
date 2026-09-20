---
slug: "necromaniac"
url: "https://devpost.com/software/necromaniac"
title: "necromaniac"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1172
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# necromaniac

> 🧟 NECROMANIAC - A haunting 3D model viewer built for Kiroween 2024 for Costume Contest category showcasing Kiro's vibe coding.

[Devpost](https://devpost.com/software/necromaniac) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[civic_government]] [[developer_tools]] [[scientific_research]]
**user** [[developer]] [[legal_professional]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** css, framer-motion, javascript, kiro, react, tailwind, three.js, vite, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for necromaniac

## Body

Necromaniac - Devpost Submission Inspiration The inspiration for Necromaniac came from my fascination with how modern horror games create atmosphere through lighting and visual effects. I wanted to explore whether AI-assisted development could help a solo developer build something that typically requires a full team - 3D graphics, complex animations, and cinematic effects. Halloween has always been about pushing boundaries and embracing the unsettling, so I challenged myself: Could I use Kiro to build a truly haunting experience? The "Costume Contest" category was perfect - it let me focus on creating a polished, memorable UI that would make judges feel like they'd stepped into a horror game. I was also inspired by the potential of AI-powered development tools to democratize game development. Not everyone has access to 3D artists or shader programmers, but with Kiro's spec-driven approach, I could implement complex systems and create professional-grade effects as a solo developer. What it does Necromaniac is an immersive 3D horror model viewer that brings your nightmares to life in the browser. It features: 4 Terrifying 3D Models : Halloween creatures, monsters, and a cursed pumpkin with unique backstories Cinematic Horror Effects : Screen glitches with RGB split, flashing lights, blood splatter particles, film grain overlay, and pulsing vignette Interactive Audio : Scary ambient sounds during intro, jump scare laughs, and spatial audio support Smooth 3D Controls : Orbit camera with mouse/touch, zoom, pan, and keyboard shortcuts Story-Driven Experience : Each model has its own dark narrative revealed through atmospheric overlays Jump Scares : Random scary moments with visual and audio effects to keep users on edge The app starts with a dramatic warning screen and story sequence, then drops users into an interactive 3D environment where they can explore horror models while experiencing randomized scares and atmospheric effects. How we built it Tech Stack: React + Vite : Fast development and hot module replacement React Three Fiber : Declarative 3D rendering with Three.js Tailwind CSS v4 : Modern styling with custom horror theme Framer Motion : Smooth animations and transitions Vitest + fast-check : Property-based testing for correctness Development Process: Spec-Driven Development : Used Kiro's spec workflow to create comprehensive requirements (12 requirements, 60+ acceptance criteria), design document (27 correctness properties), and implementation tasks (70+ tasks) AI-Assisted Coding : Leveraged Kiro to generate components following strict code style guidelines and horror theme standards 3D Model Integration : Implemented GLTF/GLB loader with progress tracking, error handling, and fallback models Horror Effects System : Built modular effect components (glitch, blood splatter, film grain, vignette) with performance optimization Audio Management : Created singleton audio manager respecting browser autoplay policies Testing : Wrote property-based tests for camera controls, model loading, and horror effects Key Features Implemented: Custom horror theme with blood-red, toxic-green, and ghost-purple color palette Glitch effect with SVG filters and RGB chromatic aberration Physics-based blood splatter particle system (20-40 particles per click) Animated background with floating particles Story overlay system with model-specific narratives Jump scare system with random timing (30-60 second intervals) Challenges we ran into 1. Intro Screen State Management The intro story sequence kept getting stuck on the first line. The issue was complex useEffect dependencies causing re-renders. Solution: Simplified state management with a storyStarted flag and removed problematic dependencies. 2. Model Scaling Issues Different 3D models had wildly different scales - the pumpkin was microscopic while others were huge. Solution: Implemented dynamic scaling based on model ID (pumpkin at 3x, creature at 2x, others at 1x). 3. Model Positioning The pumpkin model's pivot point was off-center, making it appear on the left side. Solution: Added position offsets per model to center them properly in the viewport. 4. Browser Autoplay Policies Audio wouldn't play automatically due to browser restrictions. Solution: Implemented proper audio manager that enables audio only after user interaction (clicking "I DARE TO ENTER"). 5. Memory Management Three.js objects were causing memory leaks. Solution: Implemented proper cleanup in useEffect with geometry and material disposal on unmount. 6. Animation Controls UI Black rectangle appearing for models without animations. Solution: Added strict conditional rendering checking both modelInfo.hasAnimations and availableAnimations.length . Accomplishments that we're proud of Built in Record Time : Created a fully functional 3D horror experience with complex effects in under 24 hours using Kiro's AI assistance Professional Polish : Achieved AAA-game-quality visual effects (glitches, particles, post-processing) typically requiring specialized graphics programmers Spec-Driven Quality : Followed formal software engineering practices with 27 correctness properties and property-based testing Performance : Maintains 60 FPS with multiple simultaneous effects (particles, film grain, vignette, glitches) Accessibility : Despite horror theme, maintained WCAG AA contrast ratios and keyboard navigation Mobile Support : Touch controls work smoothly (one-finger rotate, two-finger zoom/pan) Audio Integration : Seamless scary sounds that enhance the horror atmosphere without being annoying What we learned Technical Skills: React Three Fiber : Learned declarative 3D programming and the differences between imperative Three.js and R3F patterns Property-Based Testing : Discovered how to write universal correctness properties instead of just example-based tests Audio APIs : Mastered Web Audio API constraints and browser autoplay policies 3D Math : Gained deeper understanding of quaternions, euler angles, and camera transformations Performance Optimization : Learned to profile and optimize particle systems and shader effects AI-Assisted Development: Spec Workflow : Discovered the power of formal requirements and design documents for guiding AI code generation Steering Files : Learned how to create reusable guidelines that ensure consistent code style across an entire project Iterative Refinement : Found that AI works best with clear, specific instructions and immediate feedback loops Testing First : Realized that property-based tests catch bugs AI-generated code might miss Game Development: Horror Design : Learned principles of creating tension through timing, randomness, and atmosphere User Experience : Discovered the importance of warning screens and skip buttons for intense content Audio Design : Understood how sound design amplifies visual horror effects What's next for Necromaniac Short-term Enhancements: More Models : Add 10+ additional horror creatures with unique animations Custom Animations : Implement idle, attack, and death animations for each model Spatial Audio : Make sounds louder/quieter based on camera distance from model VR Support : Add WebXR integration for immersive VR horror experience Model Customization : Let users adjust lighting, fog, and effects in real-time Long-term Vision: User-Generated Content : Allow users to upload their own 3D horror models Multiplayer Gallery : Create shared horror galleries where users can explore together Horror Game Engine : Expand into a full game engine for creating browser-based horror games AI Model Generation : Integrate AI 3D model generation to create unique creatures on demand Story Mode : Add a narrative campaign where users uncover the laboratory's dark secrets Community Features: Model Voting : Let community vote on scariest models Effect Customization : Allow users to create and share custom horror effects Leaderboard : Track who can handle the most jump scares without skipping Social Sharing : Generate shareable horror screenshots with custom filters Built with Kiro AI - Demonstrating the future of AI-assisted game development. 🎃 Where Your 3D Nightmares Come to Life 🎃 <div