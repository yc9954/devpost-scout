---
slug: "voice-teller-dial-adk-mcp"
url: "https://devpost.com/software/voice-teller-dial-adk-mcp"
title: "Voice Teller - Dial ADK + MCP"
hackathon: "GKE Turns 10 Hackathon"
organization: "Google"
winner: true
words: 389
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Voice Teller - Dial ADK + MCP

> Changing how we call. Intelligent phone bots instead of clunky IVR.

[Devpost](https://devpost.com/software/voice-teller-dial-adk-mcp) · hackathon [[GKE Turns 10 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[financial_record]] [[web_dom]]

**stack** docker, fastapi, fastmcp, google-adk, google-cloud, kubernetes, python, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what’s next for voice teller — dial adk + mcp

## Body

Architecture Diagram Inspiration We’ve all been there: you call a business and get trapped in an antiquated IVR—“Press 1 for this, press 2 for that.” If you speak at the wrong moment, it breaks. I wanted to replace that menu maze with a real-time intelligent phone experience using Google’s Agent Development Kit (ADK) and Gemini’s live streaming so the system actually understands you. What it does Voice Teller is an AI phone agent that handles core banking actions via MCP tools derived from the Bank of Anthos server. Call in and: Log in by voice Check your balance Create a transaction Beyond Anthos, the same MCP approach can connect to tools from any system, turning Voice Teller into a general voice interface. How we built it Platform: All components (Bank of Anthos, MCP server, VoiceBridge) run on a GKE Autopilot cluster (containers built with Docker). Agent: Google ADK powers the conversational loop and tool orchestration. VoiceBridge (FastAPI): Receives Twilio webhooks/media streams, turns audio events into agent turns, and returns TTS audio. MCP server (FastMCP): Exposes typed tools (e.g., get_balance, add_transaction) and calls Anthos HTTP APIs securely. Telephony: Twilio for the phone call + bidirectional media stream. Challenges we ran into Live streaming gaps in ADK docs: Bi-directional media setup with Twilio required experimentation (e.g., getting audio encoding right). Learning Kubernetes under time pressure: I picked up deployments, probes, requests/limits, and GKE Autopilot basics in a weekend. Authentication for MCP: Current prototype passes a username/password from the model—not acceptable for production. We need a safer way for the agent to authenticate on behalf of the user. Accomplishments that we’re proud of A real-time AI voice agent that understands and responds smoothly. Built my first MCP server and got it talking to the agent over the network. Learned Kubernetes quickly enough to ship on GKE Autopilot. What’s next for Voice Teller — Dial ADK + MCP Secure auth flow for MCP: Replace creds-in-model with an SMS login link to a web page that issues a token to the MCP server; store short-lived tokens on behalf of the user and never expose credentials to the model. Business customization: Make agents configurable per business (prompts, tools, branding) to become a turnkey solution. Feature growth: Add more tools, leverage Resources and Prompts from MCP Hardening: Rate limits, better auditing, protection against prompt injection. <div