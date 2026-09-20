---
slug: "flowpilot-zoom-agent-that-automates-your-workflows"
url: "https://devpost.com/software/flowpilot-zoom-agent-that-automates-your-workflows"
title: "FlowPilot: Your Agentic Co-Pilot"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 816
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# FlowPilot: Your Agentic Co-Pilot

> FlowPilot listens, understands, and executes, transforming Zoom meetings into Slide decks and Notion workflows. No more lost action items - just approve and watch it execute.

[Devpost](https://devpost.com/software/flowpilot-zoom-agent-that-automates-your-workflows) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[transcript_audio]]

**stack** dain, docker, express.js, node.js, rtms, websockets, zoom

## How they structured the write-up

- inspiration
- what it does
- technical architecture
- implementation challenges solved
- future technical roadmap

## Body

Inspiration FlowPilot listens, understands, and executes, transforming Zoom meetings into Slide decks and Notion workflows. No more lost action items - just approve and watch it execute. FlowPilot provides amazing collaboration opportunities for sales, engineering, and product teams alike. Having been apart of workflows at fast-growing startups and large corporations, our team grew increasingly frustrated with the significant friction caused by meetings. This includes the amount of action items discussed in meetings that often get forgotten, tediously written, or executed. We noticed that while tools like Notion excel at documentation and Google Workspace handles scheduling, there wasn't a seamless way to transform meeting conversations into automated workflows. FlowPilot bridges this gap by creating an intelligent layer that turns verbal commitments into automated actions. What it does FlowPilot transforms Zoom meetings into an autonomous productivity engine. By leveraging DAIN's advanced agent framework, our system: Creates comprehensive Notion documentation including meeting notes, workflow templates, and task assignments Automatically generates follow-up slide decks for educational sessions and team presentations Handles calendar scheduling and email communications through Google Workspace Maintains contextual awareness across multiple meetings to track long-term projects and commitments Technical Architecture 1. Meeting Intelligence Layer Zoom RTMS Integration : Implements WebSocket connections for real-time audio stream processing Verifies local server client for the Zoom application via Ngrok 2. DAIN Agent Framework Implementation Agent Orchestration : Custom-built context router that manages state between multiple specialized agents Implements DAIN's memory system for maintaining conversation context and user preferences Uses structured JSON formats for inter-agent communication and task delegation Specialized Agents : Documentation Agent: Handles Notion to add tasks and todo Calendar Agent: Manages Google Calendar scheduling and reminders Communication Agent: Handles Gmail operations and meeting follow-ups, and supports audio email attachments via Eleven Labs text-to-speech Presentation Agent: Automates slide deck creation and updates using a custom renderer from v0.dev Outbound Phone calls: Make outbound phone calls via DAIN client 3. Custom Agent Integration through Orchestrator Data Processing Pipeline : Orchestrator agent built using Magic Loops' schema system Real-time event processing for immediate action execution 4. Execution Framework with DAIN Tunneling Service Architecture : Secure WebSocket tunneling for real-time bi-directional communication Load-balanced request routing for scalable action execution OAuth token management for secure service authentication Service Integration Layer : Notion API integration for document/task creation and updates Google Workspace API integration for calendar and email management Custom templating engine for slide deck generation with v0.dev interface Send email with audio transcript generated with ElevenLabs Implementation Challenges Solved Our journey in building FlowPilot presented several complex technical hurdles that required innovative solutions. The first major challenge was optimizing real-time processing of audio streams. We solved this by implementing a sophisticated buffering system that uses chunked transfer encoding, allowing us to process meeting data with minimal latency while maintaining data integrity. Context management proved to be another significant challenge, particularly when handling multiple concurrent meetings and maintaining conversation state. By leveraging DAIN's memory system, we developed a robust solution that maintains contextual awareness across sessions while efficiently managing system resources. Action reliability was perhaps our most critical challenge, given the importance of executing tasks accurately. We addressed this by building a resilient tunneling service with intelligent retry mechanisms and transaction management, ensuring that every action - from creating Notion pages to scheduling calendar events - completes successfully or fails gracefully with proper error handling. The final hurdle was integrating multiple third-party services seamlessly. We overcame this by developing a unified authentication layer that efficiently manages various OAuth flows while maintaining secure token storage and rotation. Another major hurdle was building out a custom presentation renderer. Developing it took a long time and was difficult to get running properly. With v0.dev, however, we were able to quickly build a custom frontend that reliably renders our presentations. Finally, integrating multiple third-party services seamlessly was challenging, so we developed a unified authentication layer that efficiently manages various OAuth flows while maintaining secure token storage and rotation. Future Technical Roadmap Our vision for FlowPilot's technical evolution focuses on two key areas: advancing our agent intelligence and scaling the platform infrastructure. We're working on implementing DAIN's advanced memory models to significantly enhance our agents' context retention capabilities, allowing for more nuanced understanding of long-term projects and recurring meetings. This will enable our agents to make more intelligent decisions about task creation and workflow automation while maintaining context across multiple sessions. On the infrastructure side, we're architecting a distributed processing system that will handle concurrent meetings more efficiently, implementing an enhanced caching layer for improved performance, and moving towards a microservices architecture for our agent components. This architectural evolution will allow us to scale horizontally while maintaining the reliability and speed our users expect. We're particularly excited about the potential to expand our agent ecosystem, creating specialized agents that cater to specific industries and use cases while maintaining our core focus on seamless automation and intelligent workflow management. <div