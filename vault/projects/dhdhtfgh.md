---
slug: "dhdhtfgh"
url: "https://devpost.com/software/dhdhtfgh"
title: "CivitasX"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 694
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# CivitasX

> CivitasX turns cities into autonomous digital ecosystems—AI agents that understand intent, trigger complex civic workflows, and log every verified action immutably on the XRP Ledger.

[Devpost](https://devpost.com/software/dhdhtfgh) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[civic_government]] [[finance_payments]] [[transportation]]
**user** [[frontline_worker]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[video_visual]]

**stack** creao, creaofileupload-mcp, creaosearch-mcp, docker, docker-compose, fastmcp, fishaudio, livekit, python, railway, render, typescript, vapi, x-mcp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for civitasx

## Body

civitasx Inspiration CivitasX began from a simple but powerful observation: governments still run on paper logic in a digital world. One of our teammates has close family members working in the public sector and has seen firsthand how outdated systems create endless friction—forms that must be retyped, portals that don’t talk to each other, and decisions that vanish into untraceable bureaucracy. We asked ourselves: “What if citizens could talk to their city like they talk to a person?” “And what if every government action was provably transparent?” That vision—of turning bureaucracy into conversation and governance into an intelligent, verifiable system —sparked CivitasX: the operating system for an AI-powered city. What it does CivitasX transforms a city into a living, conversational intelligence. Citizens can simply talk, type, or send an image —and the system instantly understands intent, executes complex workflows, and records the resulting civic action on the XRP Ledger for immutable accountability. Example: A citizen says, “I need to renew my driver’s license.” CivitasX detects the intent through semantic parsing, triggers the “license renewal” workflow , retrieves profile and document data, and performs all necessary steps autonomously—while logging a proof-of-action hash on XRPL. It integrates text, voice, and image reasoning, creating an entirely new paradigm where civic processes become intelligent, self-orchestrating conversations. How we built it CivitasX was built entirely on the Creao agentic platform , which allows AI systems to design and deploy other AI systems. We used Creao’s compositional model to build a multi-agent ecosystem combining official MCPs (Model Context Protocols) with custom integrations for blockchain and voice. Official Creao MCPs Used: 🧠 CreaoSearch MCP — semantic ES|QL civic data search 🗂️ CreaoFileUpload MCP — secure upload for documents, images, and audio 👁️ OpenAIGPTVision MCP — interprets real-world images (e.g., road damage, public works) 💬 OpenAIGPTChat MCP — core reasoning for citizen dialogue 📰 X (Social Media) MCP — retrieves real-time civic sentiment Custom MCP Integrations Built: 🔊 Vapi MCP — enables real-time voice call interactions with citizens 🔗 XRPLedger MCP — records all verified civic actions on the XRP Ledger for tamper-proof transparency Supporting APIs: 🎙️ LiveKit — real-time two-way voice streaming 🗣️ Fish Audio — speech-to-text and text-to-speech for natural voice conversations Every workflow, from conversation parsing to ledger logging, is autonomously orchestrated inside Creao’s Render, Biz, and Data layers —demonstrating AI not just as an assistant, but as an autonomous system builder . Challenges we ran into Interoperability: Getting multiple MCPs—official and custom—to align schemas and reasoning contexts dynamically. Latency: Achieving natural, sub-second voice interactions while integrating XRPL validation. Blockchain integration: Designing asynchronous confirmation flows so the system could continue reasoning while XRPL transactions finalized. Workflow inference: Creating semantic triggers (e.g., “renew driver’s license”) that reliably launched complex multi-agent processes. Accomplishments that we're proud of 🚀 Built the first AI-powered civic operating system , completely inside an AI builder (Creao) — no manual code. 🤖 Integrated 9 autonomous MCPs that collaborate across text, voice, and image modalities. 🔗 Linked AI reasoning directly to blockchain accountability , bridging cognition with verifiable trust. 🏗️ Implemented intent-triggered workflows that autonomously complete real government-style procedures. ⚡ Delivered a fully functional prototype in under 5 hours — a complete AI-governance simulation that truly works . What we learned How agentic build systems like Creao can generate and orchestrate full applications autonomously. How to use the XRP Ledger for civic trust infrastructure—beyond finance—to verify decisions, feedback, and citizen participation. How AI multimodality (voice, text, image) can make civic systems inclusive, accessible, and human again. How to design autonomous workflows that blend natural language understanding with blockchain verification. What's next for CivitasX 🏛️ Pilot Programs: Partner with municipalities to test participatory budgeting, public feedback verification, and form automation. 🛰️ IoT & GIS Integration: Real-time infrastructure monitoring (traffic, waste, utilities) feeding directly into AI civic analytics. 💰 XRPL Rewards: Incentivize verified citizen engagement through micropayments or civic token rewards. 🌐 Multilingual Expansion: Deploy voice models for major global languages via Fish Audio. 🤝 Open Protocol Vision: Turn CivitasX into an open civic operating standard—where any government can deploy an AI city OS in minutes. Tagline CivitasX — Where the City Thinks, Listens, and Evolves with You. <div