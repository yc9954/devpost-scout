---
slug: "lumina-s-trace-draw-the-laws-of-physics"
url: "https://devpost.com/software/lumina-s-trace-draw-the-laws-of-physics"
title: "Lumina's Trace: Draw the Laws of Physics"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 1374
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Lumina's Trace: Draw the Laws of Physics

> Guide light through ruins using the MX Ink stylus your hand pressure physically bends the laws of optics in Mixed Reality.

[Devpost](https://devpost.com/software/lumina-s-trace-draw-the-laws-of-physics) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]]

**stack** c#, logitech-mx-ink-sdk, meta, meta-xr-core-sdk, quest, unity-6, urp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lumina's trace: draw the laws of physics

## Body

Level 1 Level 2 Level 3 Level 4 Level 5 Level 6 Level 7 Level 8 Level 9 Level 10 Level 11 Level 12 Level 13 Level 14 Inspiration Every physics teacher has struggled to explain why light bends when it enters glass. Every student has seen the diagram — but never felt it. We wanted to build something that made the invisible laws of optics tangible, tactile, and magical. The Logitech MX Ink changed everything for us. When we realized that its pressure-sensitive tip could output an analog float from 0.0 to 1.0 — and that this value could be mapped directly to the Index of Refraction of a material — we knew we had something no one had ever built before. Not a drawing app. Not a painting tool. A physics engine controlled by the pressure of a human hand. The artistic inspiration came from three games we love: the impossible meditative geometry of Monument Valley , the voiceless emotional warmth of Journey , and the environmental puzzle language of Portal . We wanted to build something that lived at the intersection of all three — a puzzle game that feels like interactive art, set on your physical desk in Mixed Reality. What It Does Lumina's Trace is a Mixed Reality spatial puzzle game where you restore a ruined micro-civilization — The Lumenari — by rebuilding their shattered network of light conduits, one puzzle at a time. Using the Logitech MX Ink stylus , you forge three types of optical instruments directly onto your physical desk: Mirrors — Tap the desk to place a flat reflective plane. The pressure you apply sets its reflectivity: a light press creates a semi-transparent ghost mirror (letting 30% of light pass through), a hard press creates a perfect chrome reflector. Lenses — Press and hold to forge a glass sphere. The harder you press, the denser the material: light press = water glass (slight bend), hard press = diamond crystal (dramatic curve). The sphere visually shifts from pale blue to deep violet so you can see the physics before the beam touches it. Prisms — Double-tap to place a pyramid. Pressure controls dispersion: a light press produces a tight RGB split, a hard press fans the three colour beams wide across the desk. When the beam reaches its target, the dormant monument unfurls , flowers bloom at its base, and a star is added to a constellation that slowly assembles across the real ceiling of your room through MR passthrough. The game spans 20 levels across 4 acts , each introducing a new optical concept — from basic reflection, through refraction and total internal reflection, to dispersion and focal points — entirely through play, never through instruction. How We Built It Platform & Engine Unity 6.3 LTS with Universal Render Pipeline (URP) Meta Quest 2 / Quest 3 via Meta XR Core SDK v68+ Logitech MX Ink OpenXR Interaction Profile Core Systems MXInkInputBridge — Normalizes all raw stylus input into clean C# events: tip_value (float 0.0–1.0), cluster button states, inkingPose (6DoF tip position), and Inkwell dock detection. OpticsEngine — A recursive Physics.Raycast chain (max 12 bounces) that fires from the laser emitter each frame. Mirror hits use Vector3.Reflect . Lens hits use a simplified refraction approximation mapping tip_value to a bend angle multiplier. Prism hits split into three LineRenderer rays offset by the dispersion factor. No full Snell's Law vector math — the visual result is indistinguishable and runs comfortably on Quest 2. HapticsController — Maps game state to SendHapticImpulse . The most important mechanic: the stylus continuously purrs while the beam is live, and cuts to silence instantly when the beam breaks. This creates a direct tactile feedback loop between the player's hand and the light they are controlling. WorldStateManager — Puzzle tile system using ScriptableObject assets (30×30cm tiles placed on the desk via Meta Scene Understanding plane detection). Monument animations use DOTween scale tweens. Flora uses particle billboard systems with AI-generated textures. Art Pipeline (Solo Developer) 3D ruins: Free Unity Asset Store packs (low-poly modular stone) Optical instruments: Unity primitives (Sphere, Quad, Pyramid) + URP emission shaders VFX: Unity VFX Graph + free particle packs UI icons: AI-generated via Midjourney Audio: Freesound.org + free Unity Asset Store audio packs Color grading: URP Volume Override per act — one asset swap changes the entire world palette Challenges We Ran Into The 3D Refraction Math Trap — Real Snell's Law vector math in 3D ( n₁sinθ₁ = n₂sinθ₂ ) is deceptively complex when applied to arbitrary surface normals in world space. We spent time going down this path before realising a Vector3.Slerp approximation between the incoming direction and the surface normal, scaled by the refractive index, produced visually identical results at a fraction of the complexity. Done well, simplification is engineering. Continuous Haptics on Quest 2 — Driving SendHapticImpulse every frame for the "live beam purr" effect initially caused stutter. We solved this by batching haptic updates to every 3rd frame and clamping amplitude changes to avoid rapid oscillation. Desk Plane Detection Reliability — Meta Scene Understanding plane detection occasionally misidentifies the desk surface, placing the puzzle tile at the wrong height. We added a manual calibration fallback: holding the rear cluster button for 2 seconds lets the player tap the desk to set the surface anchor manually. Scope as a Solo Developer — 20 levels, 4 acts, a full optical engine, and MR integration is a significant scope for one developer. The puzzle tile ScriptableObject system was the key decision that made this achievable — levels are data, not scenes. Adding a new level takes minutes. Accomplishments That We're Proud Of The pressure-to-physics mapping — tip_value → refractiveIndex is, to our knowledge, the first time a stylus pressure input has been mapped to a fundamental optical property in a game. The moment a player first presses hard and watches the beam snap to the target is genuinely unlike anything in VR today. The haptic language — The continuous purr when light is flowing, and the instant silence when it breaks, creates an emotional connection between the hand and the beam that is hard to articulate and impossible to replicate with a standard controller. 20 levels teaching real physics — Every player who completes Lumina's Trace will have intuitively understood the Law of Reflection, Snell's Law, Total Internal Reflection, dispersion, focal points, and colour as wavelength — without reading a single formula. Zero art budget, maximum visual impact — The entire game is built from Unity primitives, free Asset Store packs, and AI-generated textures. URP bloom and HDR emission do the rest. The constraint became the aesthetic. What We Learned We learned that the most powerful input mechanic is one that maps directly to a physical intuition . Everyone knows that pressing harder should do more . Mapping that intuition to the refractive index of a material — something the player has never consciously thought about — creates an immediate, wordless understanding of a law of physics. The MX Ink's analog tip_value is the key that unlocks this entirely. We also learned that scope discipline wins hackathons . The puzzle tile ScriptableObject system, the refraction approximation, the AI-generated art pipeline — every decision was made to keep the core mechanic running perfectly rather than chasing completeness. A flawless one-mechanic demo beats a buggy full game every time. What's Next for Lumina's Trace: Draw the Laws of Physics Full 20-level campaign release on Meta App Store with the complete four-act story Level editor — publish the ScriptableObject puzzle tile format as a community tool so players can design and share puzzles Educational licensing — partner with science museums and secondary schools for a curriculum-aligned optics module. The game already covers the core optics syllabus for ages 12–16 without a single formula on screen. New instrument types — Diffraction gratings (splitting light into more than 3 channels), fibre optic cables (routing beams through flexible paths), and beam splitter cubes (50/50 splits without colour separation) Multiplayer co-op — two players, two MX Ink styli, one shared puzzle. Each player controls half the optical path. Quest 3 Scene Understanding upgrade — use full room mesh to place constellation patterns across actual walls and furniture, not just the desk surface <div