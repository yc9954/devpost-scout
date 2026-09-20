---
slug: "agent-shell"
url: "https://devpost.com/software/agent-shell"
title: "AgentShell: From Model Context to Control"
hackathon: "AWS AI Agent Global Hackathon"
organization: "AWS"
winner: true
words: 983
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/scientific_research"
  - "user/general_public"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# AgentShell: From Model Context to Control

> AgentShell redefines the Model Context Protocol (MCP) from "information retrieval" to "body control," enabling a cloud-based AI agent to inhabit cameras as its physical embodiment.

[Devpost](https://devpost.com/software/agent-shell) · hackathon [[AWS AI Agent Global Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]] [[scientific_research]]
**user** [[general_public]] [[small_business]]
**substrate** [[geospatial]] [[video_visual]]

**stack** agentcore, alexa, amazon-web-services, camera, kiro, mcp, python, rstp, strands

## How they structured the write-up

- redefining mcp from data access to physical body control
- the problem
- the solution: one mind, many bodies
- architecture & tech stack
- 📊 impact & value
- technical execution
- innovation highlights
- challenges solved
- scalability & future vision

## Body

Architecture Diagram AgentShell: From Model Context to Control Redefining MCP from Data Access to Physical Body Control The Problem Traditional AI agents are confined to screens, limited to information retrieval and text responses. When it comes to physical spaces—monitoring babies, assisting visually impaired individuals, or providing on-demand guidance—we face a dilemma: constant surveillance (privacy invasion + high cost) or no monitoring at all (safety risk). The Solution: One Mind, Many Bodies AgentShell redefines the Model Context Protocol (MCP) from "information retrieval" to "body control," enabling a cloud-based AI agent to inhabit multiple PTZ cameras as physical bodies . Core Innovation: MCP as a Body Interface MCP is traditionally for data access. We've transformed it into a physical control interface that gives AI: Vision : Snapshot capture & multimodal analysis (Amazon Bedrock Nova) Voice : Natural speech synthesis & recognition (AWS Polly/Transcribe) Movement : PTZ control, nods, shakes for emotional expression (ONVIF) Autonomy : Self-selects cameras and tools via agentic loop (Strands Agents) Key Paradigm : A single cloud consciousness (Amazon Bedrock AgentCore) inhabits multiple camera bodies only when needed, executing see → think → speak → listen cycles autonomously. Architecture & Tech Stack ┌─────────────────────────────────────────────────────────┐ │ Cloud Layer (AWS) │ │ • Amazon Bedrock AgentCore (Agentic Loop) │ │ • Strands Agents SDK (MCP Tool Orchestration) │ │ • Amazon Bedrock Nova (Multimodal Image Analysis) │ │ • AWS Polly/Transcribe (Voice I/O) │ │ • Amazon S3 (Snapshot Storage) │ └────────────────────┬────────────────────────────────────┘ │ Authorized Remote MCP │ (ngrok/cloudflared tunnel) ┌────────────────────┴────────────────────────────────────┐ │ Local MCP Servers (FastMCP Framework) │ │ • camera1_* tools (7 tools per camera) │ │ • camera2_* tools │ │ - analyze_camera_image, speak_on_camera │ │ - listen_on_camera, move_camera │ │ - nod_head, shake_head, reset_position │ │ • go2rtc (RTSP Stream & Audio Management) │ └────────────────────┬────────────────────────────────────┘ │ ONVIF/RTSP (Local Network Only) ┌────────────────────┴────────────────────────────────────┐ │ Physical Devices │ │ • PTZ Cameras × 2 │ └─────────────────────────────────────────────────────────┘ Security by Design ✅ No camera port exposure (RTSP/management API remain local) ✅ One-way tunnel connection via ngrok/cloudflared ✅ Authorized MCP only - all control flows through authenticated endpoints 📊 Impact & Value Unified Security & Scale Control exclusively via authorized remote MCP Horizontal scaling: Adding MCP = Adding a body (no workflow changes) Centralized operations and auditing Extreme Cost-Effectiveness Hardware : $20-40 consumer cameras vs $500-2000+ AI cameras Up to 50x cost reduction while gaining more intelligence & flexibility Cloud pay-per-use : No expensive on-premise AI servers Democratization : Makes AI agent technology accessible to homes, small businesses, and developing regions Universal Support & Applications Baby/elderly care : On-demand intervention, not constant surveillance Visual impairment support : AI becomes surrogate eyes, delivers info via voice Ghost concierge : Unmanned reception during off-hours Exhibition guide : Provides explanations from optimal viewpoints Entertainment : Physical gestures create character-driven AI performers Measurable Impact Privacy-preserving : Appears only when called (vs 24/7 surveillance) Cost savings : 5-camera home setup = $100-200 vs $2,500+ traditional AI cameras Accessibility : Supports people with physical constraints in daily life Technical Execution AWS Services Integration ✅ Amazon Bedrock AgentCore : Core agentic loop for autonomous decision-making ✅ Strands Agents SDK : Automates MCP tool selection and execution ✅ Amazon Bedrock Nova (Micro/Pro) : On-demand multimodal image analysis ✅ AWS Polly (Neural TTS) : Multiple voices for character expression (Matthew, Joanna, etc.) ✅ AWS Transcribe : Real-time speech recognition from camera microphones MCP Tool Implementation (FastMCP) Each camera provides 7 MCP tools: analyze_camera_image : Snapshot + Nova multimodal analysis speak_on_camera : TTS playback via go2rtc listen_on_camera : RTSP audio → AWS Transcribe move_camera : PTZ control (pan/tilt) nod_head / shake_head : Emotional gestures reset_camera_position : Return to home Autonomous Agent Behavior Agent autonomously selects which camera to use Strict execution rules via system prompt (1 tool/response per camera) Strands Agents orchestrates MCP tool calls without manual routing Reproducibility ✅ Open standards: MCP, ONVIF, RTSP, FastMCP ✅ Complete documentation with setup scripts ✅ Minimum requirements: AgentCore + Strands + PTZ cameras + MCP servers ✅ Easy horizontal scaling: Add MCP server = Add location/camera Innovation Highlights 1. MCP Paradigm Shift First project to demonstrate MCP as a "body interface" rather than just data access. Proves AI can control physical devices through standard protocols. 2. Embodied AI with Agentic Loop True "One Mind, Many Bodies" implementation: Single consciousness inhabits multiple physical forms Autonomous camera and tool selection (no manual routing) Seamless possession transitions between bodies 3. Physical Body Language PTZ movements (nods, shakes, gaze) create emotional presence Voice selection (multiple AWS Polly voices) expresses personality Visual + audio feedback builds trust 4. On-Demand Intervention Model New paradigm: Not constant surveillance, but appears when called Balances privacy and peace of mind Cost-efficient (cloud compute only when active) Trust-building experience 5. Cost Democratization Transforms affordable consumer hardware into intelligent agents, making enterprise-grade AI accessible to everyone. Challenges Solved Multi-Camera Synchronization Problem : Parallel tool calls caused conflicts Solution : Strict execution rules in system prompt + camera-prefixed MCP tools ( camera1_* , camera2_* ) Voice Output Timing Problem : TTS → playback → completion timing misalignment Solution : Synchronous processing with go2rtc API, waiting for playback completion Security & Scalability Problem : How to control cameras using AI agents without exposing camera ports? Solution : Authorized remote MCP via ngrok/cloudflared tunnel + access control headers Scalability & Future Vision Current Status ✅ End-to-end functionality verified (Alexa trigger → camera selection → conversation loop) ✅ Tested with 2 cameras (living room + entrance) ✅ Secure architecture with no port exposure ✅ Autonomous tool selection via Strands Agents Easy Scale-Out Add MCP server = Add body (no code changes) Same agent, same policy, infinite cameras Theoretically unlimited expansion Future Vision Real Alexa voice trigger in production Amazon S3 integration for snapshot and conversation history storage Dashboard for event timeline & snapshot history Multi-language support (global AWS Polly/Transcribe) Integration with smart home, robots, drones via MCP Edge AI for low latency & offline operation <div