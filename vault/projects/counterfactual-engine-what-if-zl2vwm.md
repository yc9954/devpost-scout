---
slug: "counterfactual-engine-what-if-zl2vwm"
url: "https://devpost.com/software/counterfactual-engine-what-if-zl2vwm"
title: "Counterfactual Engine - What if?"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 510
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Counterfactual Engine - What if?

> See the consequences of your choices—before they become reality.

[Devpost](https://devpost.com/software/counterfactual-engine-what-if-zl2vwm) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[measured_ablation]] [[realtime_stream]] [[runtime_tool_creation]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** css, hosted-on-vercel, html, node.js, python, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what we learned & what's next for counterfactual engine - what if?

## Body

Inspiration Some of the most important decisions in life come down to uncertainty. I’ve personally spent a lot of time thinking through major choices—trying to predict outcomes, imagining scenarios, weighing risks—only to realize that it’s still largely guesswork. That disconnect stood out to me. We simulate weather, traffic, even financial markets, yet we don’t have a way to simulate our own decisions. I wanted to build something that treats decisions as systems under uncertainty—something that allows you to explore possibilities before committing to them. That idea became Counterfactual Engine – What If? What it does Counterfactual Engine is a decision simulation platform that allows users to input a choice and explore multiple possible futures. For any decision, the system generates: -A best-case scenario -A worst-case scenario -A most likely outcome Each scenario includes: -Structured reasoning -Key influencing variables -Risk factors and trade-offs -A comparative probability estimate Instead of giving a single “answer,” the platform presents branching pathways, helping users understand uncertainty rather than eliminate it. How I built it I built the frontend using TypeScript and JavaScript with frameworks like React and Next.js, implementing component-based UI architecture, dynamic rendering, state management, animations, and responsive UX design. For the visualization layer, I used libraries such as D3.js and Three.js to construct interactive causal graphs and simulation interfaces. On the backend, I worked with API design, asynchronous processing, database management, and server-side routing using technologies like Node.js and Java-based frameworks. I designed the simulation engine using algorithmic logic and custom data structures to model causal dependencies, event propagation, and efficient scenario recomputation. The project also required systems design at a broader level — structuring scalable architectures, optimizing performance bottlenecks, managing client-server communication, and designing interfaces that remained intuitive despite the computational complexity underneath. Challenges I ran into The main challenges involved maintaining low-latency performance during real-time scenario recomputation, designing scalable state management for dynamically changing causal graphs, and preventing frontend rendering bottlenecks caused by high-frequency updates. On the backend, I handled asynchronous event processing, optimized API throughput, and structured efficient dependency-resolution algorithms for multi-variable simulations. Another major challenge was synchronizing complex client-server data flow while preserving responsiveness, consistency, and computational efficiency across the entire system. Accomplishments that I am proud of Key accomplishments included engineering a responsive full-stack architecture capable of real-time causal simulation, implementing efficient state synchronization across complex interactive workflows, and optimizing rendering performance for dynamically generated visualizations. I also designed scalable event-processing pipelines, reduced computational overhead through optimized data-flow management, and created an intuitive UI/UX layer that made technically dense simulations feel fluid and accessible to users. What we learned & What's next for Counterfactual Engine - What if? Through building the project, I gained practical experience in full-stack architecture, asynchronous systems, frontend performance optimization, and scalable state management for data-intensive applications. I also developed a deeper understanding of system orchestration, event-driven processing, and interactive visualization design. The next stage of the project involves improving computational efficiency, implementing more advanced simulation algorithms, expanding backend scalability, and refining the visualization engine to support larger and more complex dependency networks. <div