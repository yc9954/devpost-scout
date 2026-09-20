---
slug: "project-lend"
url: "https://devpost.com/software/project-lend"
title: "Project Lend"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 572
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "user/social_worker"
  - "substrate/structured_db"
---

# Project Lend

> An autonomous food bank run entirely by AI + robotics, sourcing and distributing over 50lbs of food during TreeHacks to Palo Alto shelters in 1 weekend!

[Devpost](https://devpost.com/software/project-lend) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[disaster_emergency]] [[finance_payments]] [[housing_homeless]] [[supply_logistics]]
**user** [[social_worker]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** claude-agent-sdk, claude-code, claude-vision-api-(haiku-3.5), computer-vision, fetch.ai, html/css, poke-by-interaction-company, python, react, warp-ide

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments
- what we learned
- what's next

## Body

Project Lend AI-powered autonomous food rescue, because giving should be as smart as taking Inspiration We've spent years volunteering at food banks and shelters, experiencing firsthand the challenges of both front-office admin and back-breaking logistics. When Anthropic released Project Vend showing Claude could run a business autonomously, we wondered- what if we applied that same capability to helping people give instead of take? With agents now able to reason, communicate, and operate in the physical world, Project Lend was born at the intersection of technical possibility and human need. What it does Project Lend is an autonomous food bank run entirely by AI. Over TreeHacks weekend, our agent system sorted donations from fellow builders using a robotic arm with computer vision, coordinated with 3+ shelters in Palo Alto, and delivered over 100 lbs of food in one weekend . The system handles everything—intake, sorting, inventory, shelter coordination, scheduling, and delivery logistics—completely autonomously. Donors text to contribute, the robotic arm sorts items into shelter-specific boxes, and our agents coordinate pickup times with actual shelters. No human intervention required. How we built it We basically replicated the entire front and back office of a traditional food rescue operation using the Claude Agent SDK as the brain: Physical Operations: Robotic arm sorted donations using Claude Vision API (lightning fast on Haiku 3.5!), reasoning over resource allocation from our inventory database Computer vision pipeline identified and categorized food in real-time Data streamed to our frontend dashboard for live visibility Coordination Layer: Orchestrator agent (inspired by Project Vend's "boss" architecture) coordinated with local shelters using Fetch.ai email agents Multi-agent system with specialized sub-agents for sorting, scheduling, donor engagement, and allocation Donor Engagement: Text-based agent powered by Interaction Company's Poke sent personalized messages to TreeHacks participants, raising over $100 for our GoFundMe Development Stack: Claude Code and Warp IDE agents for rapid iteration React frontend with real-time database syncing Python hardware integration with custom MCP tools Challenges Network outage at 3 AM forced a complete hardware stack pivot. Robot calibration needed constant fine-tuning. Agent concurrency issues when multiple sub-agents accessed shared resources. Real-world shelter schedules (nonprofits don't always respond to AI emails immediately!). Computer vision reliability under hackathon lighting. The usual chaos. Accomplishments Sourced over 100 lbs of food organically through the hackathon community Autonomous coordination with actual shelters—REAL coordination, not mocked, resulting in scheduled Monday deliveries Working computer vision/robotic sorting pipeline $100 raised through AI agent interactions Full multi-agent orchestration handling intake through delivery Proved AI agents can run real-world service operations, not just digital workflows What we learned AI in the real world is messy, but it's real . We learned how to handle 5 AM networking disasters, make agents resilient to unpredictability, and ship something that genuinely helps people in 36 hours. When you build something that actually matters, the energy to push through just appears. Most importantly—the gap between "AI demo" and "AI doing real work in the physical world" is closable right now with today's tools. It's not science fiction anymore. What's next We're delivering to 2 shelters Monday morning! Next steps: scaling robotic sorting for higher volumes, integrating more Bay Area shelters, building partnerships with grocery stores and restaurants for regular donations, creating a network of autonomous food banks that share resources, and potentially open-sourcing our orchestration framework so other communities can deploy their own AI-powered food rescue. The future where AI helps humans give, not just take, starts here. 🌲❤️ <div