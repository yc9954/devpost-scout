---
slug: "idle-lumber"
url: "https://devpost.com/software/idle-lumber"
title: "Idle Lumber"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 583
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/supply_logistics"
  - "domain/transportation"
---

# Idle Lumber

> every tree becomes a paycheck!

[Devpost](https://devpost.com/software/idle-lumber) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[supply_logistics]] [[transportation]]

**stack** ai, skybox, typescript, ui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for idle lumber

## Body

Inspiration We love cozy job sims and the satisfying rhythm of factory/tycoon games. Lumber is a tactile, visual process with real‑world steps cut, prep, square, slice, stack, ship that translate cleanly into short, mobile‑friendly tasks. We wanted to capture that feeling of useful work while making it social, safe, and approachable. Also: forklifts. Forklifts are fun. What it does Idle Lumber is a mobile‑first tycoon where players keep a sawmill humming by running a real production line: Tree Area → Station 1 (Log Prep) → Station 2 (Square Mill) → Station 3 (4×4 Boards) Cut trees, debark logs, mill beams, slice boards, then stack pallets for shipment. Play solo or co‑op. Teamwork accelerates throughput and unlocks bonus payouts. Role variety. Chop, move materials, drive forklifts, stack pallets, or load box trucks. Economy loop. Completing pallet shipments earns diamonds for upgrades and cosmetics. Vibe & clarity. Realistic safety signage, clear task prompts, and an industrial‑cartoon art style make the yard readable on small screens. AI flavor. A GenAI foreman gives randomized work tips and motivational voice lines; AI‑generated ambient sound (birds, saws, forklift engines) sells the lumberyard atmosphere. How we built it We focused on a tight, mobile‑optimized production pipeline and cooperative flow: Systems & gameplay Modular “Station” architecture with well‑defined inputs/outputs to model each step (logs → beams → boards → pallets). Lightweight state machines for station logic (Idle, Working, Jammed, Output Full). Physics‑assisted forklift controls tuned for touch: steer, lift, tilt, and pallet snapping to reduce frustration. Queue & capacity rules to keep lines flowing and create meaningful bottlenecks. Performance & UX Object pooling for logs/boards/pallets, LODs for props, and simplified colliders for smooth 60fps on mid‑range phones. Big‑thumb touch UI: contextual buttons, progress rings, and guided arrows to the next task. Clear, color‑safe signage and pictograms to explain stations at a glance. Co‑op Room‑based sessions with authority on shared interactables (pallet jacks, forklifts, station switches). Anti‑griefing rules (auto‑unstick, pallet reset, soft ownership of loads). Audio & AI AI‑generated ambient loops layered by zone (Tree Area vs. Milling Floor) and machine state (on/off). Foreman assistant: prompt‑driven tips, safety reminders, and randomized “good job!” stingers delivered via on‑device TTS. Balancing Data‑driven economy tables (throughput per station, bonus thresholds, shipment rewards) so we can tune without code changes. Challenges we ran into A tiny tweak at one station could stall the entire line; we added buffers and smart queueing. Mobile performance. Dozens of moving parts (logs, boards, forklifts) required aggressive pooling and careful physics layers. Co‑op sync & griefing. We needed friendly rules to prevent “pallet stealing,” forklift flips, and jammed conveyors. Readable safety & signage. Making real‑world signage legible and helpful on small screens without clutter. Accomplishments that we're proud of End‑to‑end lumber lifecycle that feels authentic yet approachable. Forklift controls that are satisfying, forgiving, and mobile‑friendly. Co‑op bonuses that truly reward teamwork (not just parallel soloing). AI foreman + ambient sound that add personality and place without getting in the way. What we learned The sweet spot for mobile job‑sims is short, stackable tasks with visible progress every 10–30 seconds. Bottlenecks are content. With the right buffers and roles, a “problem” becomes a fun team puzzle. AI works best as flavor and guidance, not a gameplay crutch. Investing early in data‑driven tuning saves huge time once playtesting starts. What's next for Idle Lumber Live ops: Seasonal leaderboards and rotating contract themes to keep the yard lively. Progression: Tool/vehicle upgrades, yard expansions, vanity skins, and title cards for specialists (e.g., “Master Loader”). <div