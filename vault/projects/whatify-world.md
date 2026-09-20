---
slug: "whatify-world"
url: "https://devpost.com/software/whatify-world"
title: "Future Scenarios"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 440
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# Future Scenarios

> Explore plausible future developments through real-time, narrated simulations.

[Devpost](https://devpost.com/software/whatify-world) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
  <sub>weak: climate_energy</sub>
**substrate** [[geospatial]]

**stack** actions, bolt, d3.js, docker, elevenlabs-api, github, gsap, kiro, kiro-(spec-to-code, next.js, node.js, openai, openai-api, openai-api-(gpt-4)

## Body

Inspiration The project grew out of an interest in systems thinking — how technology, society, climate, and geopolitics interact over time. Instead of presenting static predictions, the goal was to build an experience that simulates change: one where the future unfolds gradually, reacts to events, and can be followed as a coherent story rather than a block of text. I wanted the future to feel experienced, not just described. What it does Users enter a short description of a possible future development. The system then: constructs a step-by-step future progression, delivers the narrative through continuous voice narration, visualizes global consequences on an interactive world map that updates in real time. The experience is designed to feel closer to a live briefing or documentary playback than a typical AI response. How it was built Interface & Layout: Built with Next.js, React, and Tailwind. The UI is mobile-first, with a full-screen map, persistent playback controls, and expandable contextual panels for deeper reading. Scenario Engine: Input prompts are processed into a streamed sequence of events rather than a single response, allowing content to appear progressively. Audio Layer: Speech starts immediately using a browser-based solution, with optional higher-quality synthesis handled server-side. Playback is optimized to avoid pauses or overlap. Flow Control: Each run is fully resettable, allowing multiple simulations in one session without reloading or stale state issues. Using Kiro Rapid layout generation: Kiro was used to translate high-level UX constraints into working React components, especially for mobile navigation and layered UI. Iteration speed: Animation timing, visual rhythm, and accessibility options were refined through quick back-and-forth iterations. Streaming logic: Kiro assisted in shaping a resilient streaming pipeline and audio queue system that can interrupt, restart, and synchronize narration without noticeable delay. Challenges encountered Mobile audio restrictions: Some platforms block sound until direct interaction. This was solved by implementing an explicit audio-unlock flow and pre-initialization logic. State consistency: Early versions suffered from lingering listeners and unfinished streams. A strict lifecycle model with enforced teardown resolved this. Visual purity: Unintended overlays and filters interfered with contrast. The rendering stack was simplified to ensure clarity and consistent visual tone. Highlights Narration begins almost instantly, creating a strong sense of responsiveness. The interface remains readable and usable even during dense event sequences. A film-like aesthetic was achieved without sacrificing performance or accessibility. Key takeaways Users perceive speed through early signals, not completion time. Audio-driven experiences require platform-aware design from the start. Streaming content feels more natural than waiting for a “final answer.” Future directions Persistent links for replaying and sharing simulations. Multiple narrative voices representing different viewpoints. Deeper environmental, economic, and political data layers with branching outcomes. <div