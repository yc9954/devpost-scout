---
slug: "maxangle"
url: "https://devpost.com/software/maxangle"
title: "MaXangle"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 377
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/geospatial"
---

# MaXangle

> Master trigonometry and 3D geometry in mixed reality. Use the MX Ink stylus to construct spatial structures and calculate trajectories with sub-millimeter precision.

[Devpost](https://devpost.com/software/maxangle) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** 5, blueprints, c++, component, ink, kit, logitech, mathematics, mesh, meta, mixed, mx, physics, procedural

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maxangle xr

## Body

MaXangle XR: Precision STEM Engineering in Mixed Reality Inspiration Traditional STEM education is stuck in 2D. We learn 3D concepts like trigonometry and spatial geometry on flat whiteboards. With the launch of the Logitech MX Ink, we saw an opportunity to turn the physical world into a mathematically precise laboratory. We wanted to make math tactile, interactive, and high-stakes. What it does MaXangle XR is a Mixed Reality platform where players solve complex math and physics challenges using the Logitech MX Ink as a precision scientific instrument. Core Modules: Angle Sniper: Calculate and draw projectile trajectories in your room using real-world trigonometry. Geometry Builder: Construct 3D shapes in mid-air with a strict $Tolerance \leq \pm 1^\circ$ system that validates your spatial accuracy. Equation Portal: Solve algebraic functions (like $y = x^2$) by physically graphing them in 3D space to unlock spatial portals. Precision Engineering Mode: Repair virtual structures or perform "surgery" on mechanical parts with sub-2mm error margins. How we built it Developed using Unreal Engine 5 , MaXangle XR leverages the Meta XR SDK and the Logitech MX Ink SDK. We built a custom C++ spatial validation engine that tracks the 6DOF input of the stylus and compares it against mathematical models in real-time. We focused on high-performance procedural mesh updates to ensure a smooth, lag-free carving and drawing experience. Challenges we ran into The biggest challenge was "Hand-Jitter Compensation." Since human hands naturally shake, we developed a mathematical smoothing algorithm that maintains the raw precision of the MX Ink while ensuring the virtual geometry remains mathematically "perfect" without losing the sub-millimeter tracking data. Accomplishments that we're proud of We successfully transformed intimidating 3D math into a fun, gamified experience that feels like a professional engineering tool. Integrating the pressure sensitivity of the MX Ink to control the "depth" of 3D mathematical cuts was a major breakthrough for us. What we learned We gained deep insights into spatial computing mathematics—specifically how to map 2D algebraic concepts into a 6DOF interactive environment while maintaining strict industrial tolerances. What's next for MaXangle XR We plan to introduce Multiplayer Co-Op Workshops , allowing students from across the globe to collaborate on the same 3D blueprint in a shared Mixed Reality space, turning MaXangle into a global STEM league. <div