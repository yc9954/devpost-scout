---
slug: "mr-blueprint-draw-physics-into-reality"
url: "https://devpost.com/software/mr-blueprint-draw-physics-into-reality"
title: "MR Blueprint: Draw Physics Into Reality"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 484
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/simulation_digital_twin"
  - "domain/scientific_research"
  - "substrate/geospatial"
---

# MR Blueprint: Draw Physics Into Reality

> Turn any room into an interactive simulation space by drawing constraints with the MX Ink.

[Devpost](https://devpost.com/software/mr-blueprint-draw-physics-into-reality) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[runtime_tool_creation]] [[simulation_digital_twin]]
**domain** [[scientific_research]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]]

**stack** c#, logitech-mx-ink-sdk, meta-quest-3, mixed-reality-passthrough, physics, unity, xr-interaction-toolkit

## How they structured the write-up

- inspiration
- what it does
- how to build it
- challenges we ran into
- what we learned
- future directions

## Body

Inspiration We were inspired by the idea that spatial computing should not just visualize the world — it should let you author behavior inside it. Most XR creation tools focus on drawing geometry or sculpting models. We wanted to explore a different paradigm: drawing physics itself . The Logitech MX Ink stylus introduces a level of precision (pressure, tilt, tip contact) that makes it possible to map physical meaning directly to gestures. This opened the door to a new interaction model where users draw forces, constraints, and systems instead of menus or UI panels. Our goal became simple: What if anyone could turn their room into a physics laboratory in seconds? What it does MR Blueprint is an augmented reality physics simulator running on the Meta Quest 3. Users can place virtual objects into their real environment using passthrough mixed reality and then draw interactions between them using the MX Ink stylus. Instead of configuring physics through menus, users sketch behaviors directly: Draw a line between objects → spring constraint Press harder → increased stiffness Draw a circle → hinge joint Draw a boundary → collision wall Flick objects → impulse forces The real room becomes part of the simulation space. How to build it The project is built using Unity with XR and physics systems. Key systems included: Mixed Reality room setup using Quest spatial anchors Real-time constraint generation from stylus strokes Mapping stylus pressure to physical parameters Unity rigidbody physics for simulation Gesture interpretation pipeline for converting strokes into constraints Runtime visualization tools for forces and boundaries The project implements a simplified spring system based on Hooke’s Law: $$ F = -k(x - x_0) $$ Where: $$k$$ is derived from stylus pressure $$x_0$$ is determined by stroke length Direction comes from stylus orientation This allowed users to “feel” the physics while drawing. Challenges we ran into One of the biggest challenges was translating freeform drawing into deterministic physics behaviors. Human strokes are noisy, so we had to design interpretation rules that felt intuitive while remaining stable. Other challenges included: Mapping stylus input meaningfully to simulation parameters Maintaining simulation stability with dynamically created constraints Aligning virtual objects convincingly with real-world geometry Designing interactions that were understandable within seconds We also had to balance realism with responsiveness to keep the experience playful and educational. What we learned We learned that precision input dramatically changes how users think about spatial computing. Instead of navigating menus, users naturally experimented — almost like playing with real objects. We also discovered that drawing behavior instead of geometry is a powerful mental model that could extend beyond physics into robotics, game design, and engineering education. Future directions Future versions could include: Collaborative multi-user simulations Advanced material properties Data visualization overlays and graphs Educational lesson modes Importing scanned real-world objects Robotics and engineering prototyping tools We believe this approach could evolve into a new category of spatial productivity software. <div