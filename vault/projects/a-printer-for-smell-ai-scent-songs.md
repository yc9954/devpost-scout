---
slug: "a-printer-for-smell-ai-scent-songs"
url: "https://devpost.com/software/a-printer-for-smell-ai-scent-songs"
title: "A Printer… for Smell — (AI “Scent Songs”)"
hackathon: "OpenAI Open Model Hackathon"
organization: "OpenAI"
winner: true
words: 757
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# A Printer… for Smell — (AI “Scent Songs”)

> An AI “scent compiler” turns prompts into a JSON plan (recipe + timeline). A syringe gantry doses ±2 µL-accurate drops, then two diffusers crossfade fresh and deep blends into time-synced scent songs.

[Devpost](https://devpost.com/software/a-printer-for-smell-ai-scent-songs) · hackathon [[OpenAI Open Model Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]] [[scientific_research]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** chatgpt-oss, fast-api, javascript, nextjs, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a printer… for smell — (ai “scent songs”)

## Body

2 diffusers and ~100 essential oil selection Precision dosing 3 Axis Motion control system Inspiration Most diffusers are “one-note”: add drops by hand, turn on, hope for the best. We wanted an instrument—a printer for smell—that performs a scent like music: build, crossfade, end cleanly, repeat on command. At the same time, LLMs now turn words into code, images, even audio. But what about smell? If a model can compile text into structured plans, could it compile a scent? That question set our north star: treat air like a medium you can program. The printer metaphor gave us a concrete playbook (test page, recipe, duty cycle), and the “duet” idea—two coordinated atomizers—unlocked layered, evolving scents instead of a flat room smell. What it does Prompt-to-Scent Printer turns natural language into a single plan file and then performs it with hardware. Prompt → plan.json (gpt-oss-120b): The model compiles your intent (preferences, duration, strength, sensitivities) into one JSON: Recipe: which essential oils, volumes (µL), and which atomizer (A = fresh/bright, B = warm/grounded). Timeline: minute-by-minute power for A/B (duty cycles) and stage labels (intro → crossfade → finish). Precision dispensing: A syringe array doses essential oils with microliter precision into each atomizer—no manual mixing. Duet playback: Two water-based atomizers crossfade and layer according to the timeline, creating “scent songs.” Clean cutoffs: Automatic purge cycle between blends to prevent carry-over. Safety by default: Allergy/avoid list in the compiler, intensity caps, ventilation reminder, and a physical EMERGENCY STOP. Use cases: focus, sleep, yoga, gaming ambience, wake-up alarm; plus business installs (wellness, galleries, retail demos, R&D labs). How we built it Software Model: gpt-oss-120b (open weights), served on our hosted GPU. We designed a strict JSON schema so the model emits a single plan.json that drives both dosing and playback. Compiler UX: Web app with presets and a two-track timeline (A/B). “Generate” shows the JSON + the graph. Runtime: A controller daemon parses plan.json and orchestrates pumps, gantry moves, and A/B duty cycles in real time (1 s tick), with a state machine for Start / Pause / Stop / Purge. Hardware Syringe array (~100 slots): pre-loaded 2.5 ml syringes on micro linear actuators / syringe pumps; gravity-safe 5 mm input ports; ~5 cm drop height. 3-axis motion: shared linear rail/gantry positions each atomizer under assigned syringes, then returns to center for diffusion. Dual atomizers: large water tanks, independent duty cycles, LED status; run in parallel for crossfades. Water management: shared pump to base-fill and execute purge cycles (pre/post-flush volumes in the plan). Controls & IO: stepper drivers, endstops, flow timing, physical E-STOP wired to cut motors and pumps. Key design choice: one plan file. It simplifies reproducibility, debugging, and testing: if you can render the JSON and the timeline, you can reason about the performance. Challenges we ran into Drop repeatability: Oil viscosity and temperature made early dosing inconsistent. We switched to microliter units, shortened tubing, tuned actuator speeds, and added pre/post-flush in the plan. Cross-contamination: Even tiny residue ruins the next blend. We added a purge-then-diffuse cycle and guarded it in the state machine. Time sync: Keeping A/B in lockstep required a centralized scheduler with drift checks and a ±1 s correction window. Explaining A vs B: People don’t intuit “two atomizers.” The timeline visualization (A=blue, B=amber) and short stage labels fixed comprehension. Accomplishments that we're proud of A working duet rig that reads a prompt and performs a 20–60 min scent with clean start and finish. The single-file compiler (plan.json) that covers both recipe and playback. Precision microliter dosing and reliable purge → fresh blend. A safety-first UX (allergy filter, intensity cap, E-STOP) baked into both software and hardware. What we learned Smell is slow but powerful—designing evolutions (intro → build → finish) matters more than raw intensity. Mechanical tolerances dominate user experience; 1–2 µL errors are noticeable over time. LLMs shine when you give them tight schemas and constraints; “one plan” beats multiple partial outputs. Visualizing the plan (the A/B timeline) is the fastest path to user trust. What's next for A Printer… for Smell — (AI “Scent Songs”) Local/offline path: package the compiler for edge devices once memory is available (Ollama/LM Studio configs in the repo). Closed-loop control: add VOC/airflow sensing to auto-adjust duty cycles for room size and ventilation. More voices: quartet mode (A/B/C/D) and spatial choreography across multiple atomizers. Creators’ API: OSC/MIDI/WebSocket so musicians and game engines can “play the air.” Cartridges & maintenance: quick-swap oil trays and automated cleaning reports. Mini user studies: comfort, alertness, and preference scores across presets (focus, calm, sleep). <div