---
slug: "inklectric"
url: "https://devpost.com/software/inklectric"
title: "INKlectric"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 808
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/geospatial"
---

# INKlectric

> A mixed-reality circuit lab powered by MX Ink that turns sketching into instant simulation with a clear schematic-to-3D PCB preview workflow.

[Devpost](https://devpost.com/software/inklectric) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[mental_health]]
  <sub>weak: finance_payments</sub>
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** c#, logitechmxink, metaquest, metaxr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for inklectric

## Body

Inspiration When you’re working with electronics, the fastest way to explore is still sketching: a battery, a resistor, a LED, a quick wire. But sketches are static, and simulators are separated from the physical space where you’re actually thinking. With MX Ink on Quest, we can turn the desk into a circuit workspace - draw like on paper, and immediately see what the circuit does. What it does INKlectric is a Mixed Reality concept for Meta Quest + Logitech MX Ink that lets you draw electronic circuits naturally - on a desk surface or in the air - and turns those strokes into a clean schematic with live simulation feedback. The interaction is sketch-first: draw a battery, resistor, LED, switch, and wires; the app recognizes intent, snaps the sketch into readable symbols, and updates behavior in real time (for example, LED brightness and circuit state). On top of sketch + simulation, INKlectric adds a practical "maker bridge": a lightweight PCB preview mode in MR where the same circuit is visualized as a simple 3D board with basic footprints and “ratsnest” connection lines. It’s meant to be a fast visualization step - not full PCB CAD - with an optional export path for later toolchain integration. How we built it We treated Phase 1 as a focused design sprint and iterated until the scope was both differentiated and realistic: From "a freehand drawing demo" to "a constrained sketch language that always works." Instead of trying to recognize anything a user might draw, we narrowed the first version to a small, reliable vocabulary (battery, resistor, LED, switch, wire) and designed explicit fallbacks when recognition confidence is low so the user can confirm intent rather than getting stuck. From "pretty strokes" to "a real circuit model." We moved away from treating sketches as visuals and defined a circuit graph (components, pins, nodes, nets) as the source of truth. That makes simulation and PCB preview consistent, because both are driven by the same underlying representation. From "full simulation accuracy" - to "instant, understandable feedback." We prioritized a lightweight simulation loop that responds immediately with outputs users can interpret (LED behavior, switch state, basic measurements). The goal is fast learning and iteration, not perfect modeling. From "electronics sandbox" to "a maker bridge." We added a simple PCB preview mode mapping the same circuit graph to basic 3D footprints and ratsnest connectivity so users can see a clear next step without turning INKlectric into a full PCB CAD tool. This is how INKlectric became what it is: a sketch-first MR circuit experience where MX Ink input becomes structured intent, leading to snapped schematics, instant simulation, and a lightweight path toward physical realization. Challenges we ran into Even at concept stage, a few constraints shaped the direction: Recognition vs. reliability: freehand sketches can be ambiguous, so we constrained the first version and designed fallbacks to avoid “it didn’t recognize my drawing” dead-ends. Scope temptation: it’s easy to slide into full EDA territory (libraries, routing, DRC). We intentionally framed PCB preview and export as lightweight extensions, not core requirements. MR clarity: circuits must stay readable and stable in passthrough; that pushed us toward snapping, clean rendering, and minimal UI clutter. Simulation realism: we want believable behavior without building a full simulator, so we’re prioritizing responsive educational feedback and simple models that feel correct to users. Accomplishments that we're proud of We’re proud that we chose a concept where MX Ink is the core, not an afterthought: precision sketching becomes structured input, and the system responds immediately. We also structured the experience around a single satisfying loop - draw - snap - simulate- so the value is obvious within seconds. We’re also proud of the "maker bridge" decision: a simple 3D PCB preview keeps the experience grounded in real workflows and makes the output feel tangible, without turning the project into a full CAD tool. What we learned We learned that the success of an MR tool like this depends more on responsiveness and clarity than on piling on features. Fast feedback builds trust, and snapping to clean symbols makes the experience feel like a real tool, not a drawing demo. We also learned that constraints are a feature: limiting the first version to a small component set makes it more reliable, easier to teach, and much easier to expand later. What's next for INKlectric Next we’ll start building and validating the core loop on real hardware: stroke capture, recognition, snapping, and real-time feedback. We’ll iterate based on feel - pressure, buttons, erase/undo behavior, and recognition speed - until the experience is natural and repeatable. Once the core loop is stable, we’ll expand toward the strongest next-stage experiences: a short guided tutorial for first-time users, a controlled burnout/failure moment for learning realism, and a polished PCB preview that turns a sketch into a spatial, shareable artifact. <div