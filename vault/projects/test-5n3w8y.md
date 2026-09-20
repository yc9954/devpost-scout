---
slug: "test-5n3w8y"
url: "https://devpost.com/software/test-5n3w8y"
title: "SkyGuard"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 369
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
---

# SkyGuard

> When air traffic control is overloaded, one mistake can be fatal. SkyGuard’s AI agent augments controllers and guides pilots with real-time decision making and radio communication.

[Devpost](https://devpost.com/software/test-5n3w8y) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
  <sub>weak: developer_tools, disaster_emergency</sub>
  <sub>weak: code_repository, web_dom</sub>

**stack** css, html, javascript, livekit, mcp, node.js, python, react, typescript

## Body

Our UI, with the AI agent operating The components of our solution What our AI can handle as an air traffic controller The need for AI-assisted air traffic controllers Introducing Skyguard On average, over three aircraft crash a day around the world. Of these crashes, nearly 80% of these disasters are caused by human error. Current airspace safety relies solely on human coordination, but the framework is a safety liability. At towered airports, air traffic controllers are swamped, juggling a high volume of data as they make critical decisions to direct planes safely in real time. At untowered airports, pilots have to sort out their positions and landing order among themselves. Pilots talking over each other leads to confusion, and fatigue leads to mistakes. That’s why our team is building SkyGuard to keep the skies of Turing City and the whole world safe. SkyGuard is an AI agent that reads the same data as human air traffic controllers to intelligently support, augment, and (in careful cases) automate air traffic coordination. It maintains an internal model of aircraft positions and intentions, and listens to and responds to live radio traffic, following FAA-certified procedures. SkyGuard reduces the cognitive load and acts as a second line of defense for air traffic controllers, and as a situationally aware guide for pilots when controllers aren’t there. In the process, we learned about various technical difficulties that ATCs and pilots face. As we worked through the project, one of our biggest challenges was clarity. As much as we were fascinated by the various APIs and tools we could utilize, our codebase quickly grew large and messy. Parallel development without a structured central branch resulted in significant time being spent solving merge conflicts. After multiple failed attempts at merging and pruning of ideas, we went back to defining and implementing the core features that truly mattered, allowing us to learn about both the importance of communication and concentration. Currently, SkyGuard will primarily be used to assist agents and pilots, while being used to automate in a limited number of cases. As we improve SkyGuard, safety remains our priority, and we hope to relieve the stressful burden of air traffic controllers by fully automating the process. <div