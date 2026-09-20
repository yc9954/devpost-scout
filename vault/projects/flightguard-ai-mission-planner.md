---
slug: "flightguard-ai-mission-planner"
url: "https://devpost.com/software/flightguard-ai-mission-planner"
title: "FlightGuard: AI Mission Planner"
hackathon: "Airia AI Agents Hackathon"
organization: "airia"
winner: true
words: 677
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# FlightGuard: AI Mission Planner

> Enterprise AI orchestrator for drone missions. Uses Airia MCPs for live weather & airspace intel, enforcing Human-in-the-Loop (HITL) Commander approval for secure, compliant flight deployments.

[Devpost](https://devpost.com/software/flightguard-ai-mission-planner) · hackathon [[Airia AI Agents Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]]
**domain** [[labor_employment]] [[legal_justice]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** airia, anthropic, anybrowse, claude, mcp, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flightguard: ai mission planner

## Body

Agent location Backend part for the agent User UI with AI agent connection and backend Inspiration Commercial and defense drone operations are incredibly complex. Before a drone can launch, operators must manually cross-reference weather conditions (METOC), terrain elevations, airspace compliance (NOTAMs, No-Fly Zones), and drone specifications (like calculating fixed-wing takeoff vectors against the wind). A single oversight can lead to a crashed drone or a severe compliance violation. We realized that an Enterprise AI Agent could orchestrate this entire pre-flight checklist in seconds, saving hours of manual labor and significantly reducing risk. What it does FlightGuard is an AI-powered Mission Planner and Enterprise Orchestrator. The system operates as a smart aviation assistant: Data Collection: It asks the human operator for their Drone Specs (e.g., Fixed-wing, 2kg, wingspan) and desired Map Waypoints. Agentic Intel Gathering: It automatically fetches real-time wind speeds, weather conditions, and active NOTAMs (Notice to Air Missions) for those specific coordinates. Structured Flight Engineering: It uses advanced step-by-step reasoning to calculate the exact catapult launch heading required to launch into the current wind based on the drone's specific weight and class. Human-in-the-Loop (HITL): FlightGuard acts strictly as an advisor. It compiles a "Pre-Flight Risk Briefing" and strictly halts execution. It requires the human Commander to explicitly review the data and type "APPROVED" before it finalizes the mission. How we built it We built FlightGuard natively on the Airia Platform to leverage its enterprise-grade routing and Model Context Protocol (MCP) capabilities. The Orchestrator: We configured an Airia Agent to act as the central brain. To ensure strict, factual, and deterministic outputs—crucial for defense and aviation—we turned the model's temperature down to 0.1. Airia MCP Integrations: This is where the magic happens. We integrated two critical MCP deployments to give our agent enterprise capabilities: FlightGuard_Sequential_Reasoner (Anthropic Sequential Thinking): We deployed the Sequentialthinking tool to force the agent into structured mission risk reasoning. Instead of guessing flight vectors, it mathematically and logically calculates the mission parameters step-by-step, ensuring no safety checks are skipped. FlightGuard_Web_Intel (AnyBrowse): We deployed AnyBrowse with Search , Crawl , Scrape , and Extract tools enabled. This grants our agent live web access to scrape up-to-the-minute METOC (weather/wind) data and extract live FAA/Military airspace restrictions directly from aviation databases. Challenges we ran into A major challenge in aviation AI is preventing "hallucinations" of weather or airspace data. We initially struggled with the AI trying to guess the weather. By strictly defining the AnyBrowse MCP in the system prompt, we forced it to rely entirely on real-time external extraction for NOTAMs and wind data. Furthermore, calculating launch vectors requires precision; getting the AI to slow down and show its work was tough until we integrated Anthropic Sequential Thinking , which beautifully solved our logic-skipping issues. Finally, getting the AI to stop and wait for HITL approval required careful prompt constraint engineering. Accomplishments that we're proud of We are incredibly proud of how seamlessly the Airia MCP ecosystem handled complex tool routing. The agent successfully acts as an intelligent bridge—taking raw map coordinates, using AnyBrowse to scrape live wind vectors, and then feeding that data into the Sequential Reasoner to return a highly accurate, math-backed takeoff vector. We are also proud of implementing a true, enterprise-grade HITL safeguard that mirrors real military Command & Control (C2) flows. What we learned We learned the immense power of Model Context Protocols (MCPs) combined with structured reasoning. Instead of hardcoding fragile, custom API connections for weather and maps, Airia's MCP catalog allowed us to plug our AI directly into the live web in minutes. We also learned how to properly engineer prompts for high-stakes, low-temperature environments where safety, sequential logic, and compliance are paramount. What's next for FlightGuard: AI Mission Planner For the next iteration, we plan to implement a true Multi-Agent Swarm architecture within Airia, where different sub-agents handle specific compliance layers (e.g., a dedicated Legal Agent, a dedicated Metoc Agent). We also plan to output the final approved flight plan as a dynamic .KML file that can be ingested directly into military and commercial drone flight controllers. <div