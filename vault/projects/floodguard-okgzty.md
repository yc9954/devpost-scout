---
slug: "floodguard-okgzty"
url: "https://devpost.com/software/floodguard-okgzty"
title: "FloodGuard"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 472
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
---

# FloodGuard

> FloodGuard turns rising tides into early alerts—an AI-powered system that predicts, detects, and coordinates responses to floods, protecting lives, property, and cities in real time.

[Devpost](https://devpost.com/software/floodguard-okgzty) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[disaster_emergency]]
  <sub>weak: climate_energy</sub>
  <sub>weak: frontline_worker, general_public</sub>
**substrate** [[geospatial]]
  <sub>weak: structured_db</sub>

**stack** a2a, adk, gemini, github, google-cloud, neon, node.js, postgresql, postman, prisma, react, typescript

## Body

Console Agents activity AgentsStatus 🌊 Inspiration We were inspired by the ever-changing climate and the real disasters happening around us—Miami’s rising waters, San Antonio’s recent devastating floods, and Florida’s hurricanes and cyclones. Watching how unprepared cities often are, we wanted to build something that could actually help communities get ahead of these crises, not just react to them. ⚡ What it does FloodGuard is a real-time AI agent system that predicts, detects, and responds to urban flooding. It monitors weather forecasts, drainage status, and local emergency signals, then turns them into actionable early alerts for citizens, first responders, and city officials. Simply put: it helps people prepare before the flood hits. 🛠️ How we built it We went through a lot of trial and error—tried different approaches, failed many times, but failed fast and recovered faster. Eventually, we landed on a local database solution with Prisma + Neon powering the backend, Postman for testing, and Google ADK + A2A for the multi-agent setup. Each agent has its own “job”: One keeps an eye on weather data, Another watches drainage and infrastructure, Another handles alerts and emergency communication. They run in parallel and communicate using Google’s agent frameworks, giving us a looping system that never stops scanning for risks. We also hosted and deployed pieces of our system using Google Cloud, structured our data flows with modern APIs, and built a clean frontend demo (with help from Wix) to make the solution accessible. 🚧 Challenges we ran into Juggling multiple sponsor requirements while staying true to solving a real-world problem. Handling data inconsistencies and building a risk model that didn’t break under edge cases. Getting the agents to communicate smoothly without overloading the system. Explaining all of this in a clear and simple way within hackathon time constraints! 🏆 Accomplishments that we’re proud of We actually got the multi-agent loop working—agents talk to each other, split tasks, and hand off responsibilities in real time. We aligned our solution with Google ADK/A2A (autonomous agents), Base44 & Wix’s “solve a real-world problem”, and Microsoft’s “innovative problem” challenges. Built something that feels like more than just a hackathon project—it feels like a foundation for a real deployment. 📚 What we learned How to use Google’s ADK/A2A to build agent-based systems that are more than just theoretical. The value of resilience in the process—every time something broke, we learned why and came back stronger. How to balance sponsor asks with our own vision and keep the project coherent. 🚀 What’s next for FloodGuard We see FloodGuard as much more than a hackathon demo. Next, we want to: Connect directly with city emergency systems and public dashboards. Expand alerts through SMS and mobile push notifications. Train models on diverse flood data to improve predictive accuracy. Extend the multi-agent architecture to other crises—like wildfires, earthquakes, or infrastructure outages. <div