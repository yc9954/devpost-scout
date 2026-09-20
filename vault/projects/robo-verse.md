---
slug: "robo-verse"
url: "https://devpost.com/software/robo-verse"
title: "Robo-verse"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 642
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Robo-verse

> hands-on, game-like environment to practice algorithmic thinking

[Devpost](https://devpost.com/software/robo-verse) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** express.js, node.js, react, typescript, vite

## How they structured the write-up

- inspiration
- purpose
- game modes
- key features
- tech stack
- getting started
- bot api reference
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for robo-verse

## Body

Inspiration AI-Coded Robot Arena A hackathon project where you program robots using JavaScript to compete in combat battles and navigation challenges. Write a tick() function, deploy your bot, and watch the simulation play out. Purpose The arena gives programmers a hands-on, game-like environment to practice algorithmic thinking. Instead of writing tests or staring at a console, you write bot AI that controls a robot in real time — and immediately see whether your logic holds up under fire. Game Modes Robot Fight Two robots enter, one leaves. You program your combat robot's AI by writing a tick(state) function that runs every simulation frame. Your bot reads sensor data — nearby enemies, incoming projectiles, ammo pickups, obstacles — and returns commands to move, aim, and fire. Before each match you pick your loadout: chassis (HP pool), weapon (damage type and ammo), and movement system (speed vs. terrain handling). The match runs server-side up to 2,700 ticks (~45 seconds at 60Hz) against a built-in baseline opponent, then the full replay is streamed back to the viewer so you can scrub through every frame and see exactly what happened and why. Robot Platform No enemies — just you, your code, and a minefield of circular obstacles between your robot and a distant goal. Write a tick(state) function that steers the robot to the target coordinates using only imprecise sensor readings. The goal's position is fuzzy (approximate), short-range obstacles give you exact data, and long-range ones only hint at where danger might be. Three difficulty levels scale from 5 obstacles (Level 1) up to 35 (Level 3). It's a focused test of pathfinding and obstacle-avoidance logic before you throw a weapon into the mix. Key Features In-browser code editor — Monaco Editor (same engine as VS Code) with syntax highlighting and a starter template to get you going fast. Modular robot builder — Choose from 3 chassis types (Light / Medium / Heavy), 3 weapons (Laser / Cannon / Missile), and 3 movement systems (Wheels / Legs / Tracks), each with distinct stat trade-offs. Dual sensor system — Bots see the world through two layers: short-range (precise coordinates, ~60px radius) and long-range (fuzzy approximate positions, 250px cone in front of turret), rewarding smarter sensing logic. Line-of-sight & fog of war — Obstacles block detection; you only see what your sensors can reach, not the full game state. Sandboxed bot execution — User-submitted JavaScript runs in a secure server-side sandbox so arbitrary code can't break the simulation. Full replay viewer — After each run the battle is replayed frame-by-frame so you can diagnose exactly where your strategy succeeded or failed. Ammo & reload mechanics — Weapons have clip sizes and magazine counts; bots must track ammo state and issue reload commands or they'll run dry mid-fight. Tech Stack Layer Tech Frontend React 19, TypeScript, Vite, Monaco Editor Backend Node.js, Express 5, TypeScript Simulation Shared TypeScript physics engine (npm workspace) Getting Started # Install all workspace dependencies npm install # Run frontend + backend concurrently npm run dev Backend runs on http://localhost:3001 , frontend on Vite's default port ( http://localhost:5173 ). Bot API Reference Your tick(state) function is called every simulation frame. Return an action object: function tick(state) { return { moveTarget: { x: 400, y: 300 }, // world coordinate to move toward aimTarget: { x: 700, y: 300 }, // world coordinate to aim turret at fire: true, // shoot this tick reload: true, // manually trigger reload }; } state object shape (battle mode): state.self — your robot's position, heading, HP, ammo, speed state.shortRange.enemies / ammoOrbs / obstacles / projectiles — precise nearby objects state.longRange.enemies / ammoOrbs / obstacles / projectiles — fuzzy far objects (cone in front of turret) ## What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for Robo-verse <div