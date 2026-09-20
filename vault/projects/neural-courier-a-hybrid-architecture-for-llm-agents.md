---
slug: "neural-courier-a-hybrid-architecture-for-llm-agents"
url: "https://devpost.com/software/neural-courier-a-hybrid-architecture-for-llm-agents"
title: "Neural Courier: A Hybrid Architecture for LLM Agents"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 697
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/supply_logistics"
  - "substrate/geospatial"
---

# Neural Courier: A Hybrid Architecture for LLM Agents

> Neural Courier: A sim where a Groq LLM is the real-time brain for an autonomous drone. It makes strategic choices in <400ms, proving a new hybrid architecture for real-world AI agents.

[Devpost](https://devpost.com/software/neural-courier-a-hybrid-architecture-for-llm-agents) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[supply_logistics]]
**substrate** [[geospatial]]

**stack** gdscript, groq, javascript, llama-3, llm, nitrode-(godot), node.js, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neural courier: a hybrid architecture for llm agents

## Body

The Neural Courier drone navigating its environment. A full 3D world and AI agent built solo from scratch in 48 hours. The real-time command HUD, showing the AI's strategic thought and the sub-400ms decision latency delivered by the Groq API. The full-stack hybrid architecture: the Nitrode (Godot) game client on the left, and the Node.js WebSocket server logs on the right. Inspiration I've always been fascinated by autonomous systems, from warehouse robots to planetary rovers. Their biggest challenge isn't just moving; it's making smart, strategic decisions in real-time in complex environments. I wanted to see if modern, high-speed LLMs like the ones served by Groq could serve as the 'strategic brain' for such an agent, moving beyond simple commands to genuine tactical reasoning. What it does Neural Courier is a real-time strategy simulation where you don't directly control the agent; you command it. The user gives a final objective to an autonomous drone. The drone, powered by a Groq LLM brain, analyzes the hostile environment and chooses the best tactical waypoint to approach the goal. Its strategic thoughts, and the incredible sub-400ms latency of its decisions, are displayed on a live command HUD, demonstrating a new way to interact with and observe AI decision-making. How we built it Neural Courier is a full-stack application built solo in 48 hours. The 3D world and agent physics were built using Nitrode (a custom Godot engine), with game logic written in GDScript. This client communicates in real-time with a Node.js backend via a WebSocket server. When the agent needs a decision, the server packages the game state into a JSON object and sends it to the Groq API, which runs the Llama 3 8b model. The AI's JSON response, containing its strategic choice, is sent back to the client, which uses Nitrode's built-in Navigation Engine to reliably execute the high-level plan. This creates a complete, closed-loop, hybrid AI system. Challenges we ran into My initial approach was to use the LLM for direct, low-level navigation commands ("move left," "move forward"). I quickly hit a wall. I discovered that while the Groq API was incredibly fast, LLMs are not inherently reliable for the kind of stateful, precise spatial reasoning required for moment-to-moment navigation. This led to the agent getting stuck in infinite loops. This failure was the project's biggest breakthrough. It forced me to pivot from a naive architecture to a more sophisticated one. The insight was: the LLM shouldn't be the puppet; it should be the puppet master. Refactoring the system to use the AI for high-level strategic choice instead of low-level control was the main challenge, but it resulted in a far more robust and intelligent agent. Accomplishments that we're proud of Building a Full End-to-End System Solo in 48 Hours: From the 3D game client to the backend server to the AI integration, this entire complex project was designed, built, and debugged by a single person. Achieving True Real-Time AI: The sub-400ms latency from the Groq API allowed me to create a truly responsive agent, proving the viability of LLMs for time-sensitive strategic tasks. Designing a Novel Hybrid Architecture: The final architecture, which uses the LLM for high-level strategy and the game engine for low-level execution, is a robust and scalable pattern for future AI agents. What we learned The future of effective AI agents isn't just about bigger models; it's about smarter system design. I learned that the most powerful solutions combine the strengths of different technologies—using LLMs for what they're best at (high-level reasoning and choice-making) and leveraging deterministic engines for what they're best at (flawless execution). This hybrid approach is the key to creating reliable, real-world autonomous systems. What's next for Neural Courier: A Hybrid Architecture for LLM Agents The hybrid architecture of Neural Courier is incredibly scalable. The next step is to expand it into a multi-agent simulation platform. This would involve introducing multiple AI drones that need to communicate and collaborate to solve more complex objectives, like coordinating a delivery or mapping a larger area. This would allow for benchmarking different LLMs not just on speed, but on their ability to perform cooperative strategic reasoning, a key step towards real-world autonomous fleets. <div