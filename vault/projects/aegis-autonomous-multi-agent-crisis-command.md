---
slug: "aegis-autonomous-multi-agent-crisis-command"
url: "https://devpost.com/software/aegis-autonomous-multi-agent-crisis-command"
title: "Aegis: Autonomous Multi-Agent Crisis Command"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 744
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Aegis: Autonomous Multi-Agent Crisis Command

> An autonomous multi-agent command center that prevents 911 collapse by triaging thousands of distress signals instantly using Google Gemini 3.

[Devpost](https://devpost.com/software/aegis-autonomous-multi-agent-crisis-command) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: human_in_the_loop, on_device_local</sub>
**domain** [[disaster_emergency]] [[health_clinical]] [[supply_logistics]]
  <sub>weak: civic_government, legal_justice, media_journalism</sub>
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** antigravity, google-cloud, google-gemini, google-maps, next.js, tailwind-css, typescript

## Body

Report Generate using Gemini 3 Flash Dashboard Gemini tactical analysis Dashboard showing Protocol Zero Dashboard showing reasoning My Photo Inspiration In the first 60 minutes of a mass casualty event whether it's a flood, earthquake, or urban fire the 911 infrastructure doesn't fail because of technology. It fails because of volume. When 10,000 distress signals hit in ten minutes, human dispatchers collapse. Critical intelligence (tweets, SMS, drone feeds) becomes unstructured noise. Response times lag by hours, and the "Golden Hour" is lost. We built Aegis to answer one question: What if the 911 system didn't just log calls, but actually reasoned like a Commander? We wanted to move from "Data Visualization" to "Autonomous Triage." What it does Aegis is an autonomous "Civilian-to-Command" response grid. Instead of a static dashboard, it employs a Multi-Agent Swarm powered by Google Gemini 3 to act as a digital first responder: The Coordinator Agent: Intercepts thousands of raw signals (Audio, Text, Video, Images) and routes them instantly to specialized agents. The Triage Agent: Uses Deep Reasoning to understand physics and context. It knows that "trapped in basement" + "rising water" = High Priority Drowning Risk, upgrading the threat level automatically. The Surveillance Agent: Analyzes incoming images (e.g., from drones) and cross-references them with live Google Search data to validate threats (e.g., verifying a chemical plant's layout or checking live weather reports). The Logistics Agent: Calculates optimal paths for rescue assets. The Reporter Agent: Autonomously compiles every data point reasoning logs, timestamps, and locations into a legal Situation Report for post-mission audits. Protocol Zero: For high-stakes decisions (like deploying heavy assets), the AI flags uncertainty and requests "Voice of God" approval from the human commander, ensuring safety-by-design. How we built it The Brain (Gemini 3 Pro): We utilized Gemini's Deep Thinking capabilities to minimize hallucinations. The system doesn't just keyword match; it generates a "Reasoning Trace" (visible in the UI via a typewriter effect) to explain why it made a decision. The Eyes (Google Maps Platform): We implemented the Google Maps JavaScript API with a custom "Dark Mode" tactical style. We used Advanced Markers to create a clean, high-contrast command center interface that reduces eye strain during crisis monitoring. The Nervous System (Next.js 14): Built on the App Router with Server Actions to handle parallel agent streams without blocking the UI. The Architecture: We used a modular Agentic pattern where each agent (Triage, Surveillance, etc.) has a specific system prompt and tools, coordinated by a central logic hub. Challenges we ran into Cognitive Overload: Our first version showed too much reasoning text. The screen was unreadable. We built a "Spotlight Protocol" that processes incidents in the background but only visualizes the detailed "thought process" of the highest-priority threat to keep the UI clean. Hallucinations vs. Reality: Early tests had the AI inventing locations. We solved this by integrating Google Search, forcing the agent to verify locations, weathers and incidents against real-world data before dropping a pin. The "Black Box" Problem: Users didn't trust the AI's priority scoring. We solved this by forcing the model to output concise "Display Reasoning" bullet points, so the human commander can instantly audit the AI's logic. Accomplishments that we're proud of The "Spotlight" UX: We successfully visualized Gemini's "thinking process" in real-time without overwhelming the user. Multi-Agent Orchestration: Getting the Triage Agent to hand off data to the Surveillance Agent seamlessly was a complex challenge we solved. Real-time Verification: Building a system that doesn't just believe user reports but actively "fact-checks" them using Google Search. Protocol Zero: Successfully implementing a "Human-in-the-Loop" workflow that feels natural, not obstructive. What we learned Latency Matters: Parallel processing is essential. processing incidents sequentially is too slow for disaster scenarios. UX is Safety: In a crisis tool, a confusing UI isn't just annoying; it's dangerous. Dark mode and clear typography (using the Geist font) are critical for readability. AI Needs Boundaries: The most powerful AI is one that knows when to ask for human help (Protocol Zero). What's next for Aegis: Autonomous Multi-Agent Crisis Command IoT Integration: Direct connection to smart city sensors (flood gauges, thermal cameras) to feed the Surveillance Agent. Offline First: A mobile "Field Responder" mode that syncs data via mesh networks when the internet is down. Voice-to-Action: Implementing full voice control so commanders can verbally order "Sector 4 Evacuation" and the Logistics Agent handles the details. GovTech Pilot: We plan to pitch the prototype to local municipal disaster management teams as a "Force Multiplier" tool. <div