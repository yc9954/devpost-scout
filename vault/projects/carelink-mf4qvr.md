---
slug: "carelink-mf4qvr"
url: "https://devpost.com/software/carelink-mf4qvr"
title: "CareLink"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 687
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# CareLink

> AI-powered discharge coordination connecting hospitals, shelters, and social workers to ensure safe patient transitions

[Devpost](https://devpost.com/software/carelink-mf4qvr) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[agriculture_food]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[labor_employment]]
**user** [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** brightdata, fetchai, gemini, python, react, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carelink

## Body

Inspiration Every day across America, hospitals discharge unhoused patients with nowhere safe to go. We were shocked to learn that over 50-70% of homeless patients in U.S. hospitals are discharged to unsafe or unstable environments without a clear care plan. The current process is slow, fragmented, and relies on phone tag between hospitals, shelters, transport providers, and social workers. Case coordinators spend 4-5 hours per case , making dozens of phone calls, often only to find shelters are full or transportation isn't available. We built CareLink to solve this critical problem by creating an intelligent, voice-enabled coordination system that ensures every unhoused patient leaving a hospital has a verified shelter placement, coordinated transport, and connected social worker for continuity of care. What it does CareLink is a decentralized, multi-agent AI system that automates the entire discharge planning workflow for unhoused patients: 9 Specialized AI Agents (Powered by Fetch.ai) Coordinator Agent : Orchestrates the entire workflow https://agentverse.ai/agents/details/agent1qf5tefy3dd9jwtwl8s0ht0aq6yn4du7ntvwdhhcfxqwwjas7fwcpsme6g35/profile Parser Agent : Extracts structured data from discharge documents using LlamaParse + Gemini AI https://agentverse.ai/agents/details/agent1qthwalvx5c757u0gsdrx6xfu9lf0y9cc6jce8ddvx87cy2w9a7mgv0rthgr/profile Shelter Agent : Matches patients with available shelter beds using real-time data https://agentverse.ai/agents/details/agent1qd4kn4syvtlypa20aq8pct4d6wa6fke77su5tjqsj2ymgr2n0klew447j3s/profile Transport Agent : Schedules accessible transport (Paratransit, Lyft Access, Uber WAV)\ https://agentverse.ai/agents/details/agent1q0vm9tl5d5tjpj3d7qqk692jz0y9f486twxmjzfv8eng288gqf0pgjt83nd/profile Social Worker Agent : Assigns case workers and schedules follow-ups https://agentverse.ai/agents/details/agent1qfxx6ry60e9clra6vgyp76q0uvfrkc6n0kga4cln3f7c6fnl44wgujvphnd/profile Resource Agent : Coordinates food, hygiene kits, and clothing https://agentverse.ai/agents/details/agent1qfz242vsc6hr3ck48kmef73hlj39538ksgt2w4v3fpawyjp8q2yrwr2hdfp/profile Pharmacy Agent : Ensures medication continuity post-discharge https://agentverse.ai/agents/details/agent1qdaq0qhnsgt3f3p0sk0f5642fyceqfh44739prhv0x9x828ay0a6vh4dgen/profile Eligibility Agent : Verifies benefits (Medi-Cal, GA, SNAP) https://agentverse.ai/agents/details/agent1qf0phyg2dqm4q5nee9jx8ukzlry5k3x388rqzdp24kksujmc2nzysa398tf/profile Analytics Agent : Tracks system performance and outcomes https://agentverse.ai/agents/details/agent1qg0g6fm790qu6rcl6tqulk5gvvvq0ma5a4tzcwzkdzp3dr8tneqdjldgltj/profile Voice-First Communication (Powered by Vapi) Automated shelter availability verification calls Social worker outreach and coordination Transport provider scheduling Post-discharge patient check-ins Accessible for low-tech organizations Real-Time Intelligence (Powered by Bright Data) Live shelter capacity data from San Francisco HSH and community sources Up-to-date resource listings (food banks, medical respite, outreach centers) Transport provider schedules Continuously refreshed community resource database Intelligent Document Processing AI-powered PDF parsing with LlamaParse Automatic form autofill from discharge documents Gemini AI for data extraction and structuring Confidence scoring with manual review flagging How we built it Frontend: Framework : Next.js 14 with TypeScript UI/UX : Tailwind CSS + Framer Motion for smooth animations Maps : Mapbox GL JS + react-map-gl for interactive shelter mapping Components : React 18 with modern hooks and state management Icons : Lucide React for consistent iconography Backend: API Framework : FastAPI (Python) Agent Framework : Fetch.ai uAgents for decentralized coordination Database : Supabase (PostgreSQL) for persistent case storage Voice AI : Vapi for automated phone communications Document Processing : LlamaParse for PDF parsing AI Intelligence : Google Gemini 1.5 Pro for data extraction Web Intelligence : Bright Data for real-time shelter/resource data DevOps & Integration: HTTP Client : httpx for async API calls Tunneling : ngrok for webhook handling during development Testing : pytest for backend testing Code Quality : black, ruff, mypy for Python; ESLint for TypeScript Challenges we ran into Agent Communication Complexity Challenge : Coordinating 9 independent Fetch.ai agents without message loss or race conditions Solution : Implemented a robust coordinator pattern with: Message queuing and retry logic State synchronization via Supabase Unique message IDs to prevent duplicates Timeout handling for unresponsive agents Timeline Visualization Challenge : Displaying complex multi-agent workflows in an intuitive timeline Solution : Used Framer Motion for smooth animations Built hierarchical status tracking (agent → task → subtask) Implemented collapsible sections for detailed logs Accomplishments that we're proud of 9 Production-Ready Fetch.ai Agents - Fully functional multi-agent system with real coordination Vapi Voice Integration - Successfully automated shelter verification and social worker outreach calls Bright Data Intelligence - Live web scraping provides up-to-date shelter availability What we learned Multi-Agent Systems Are Powerful But Complex Agent coordination requires careful message handling State synchronization is critical for distributed systems Fallback strategies are essential for production readiness Document Intelligence Needs Multiple Layers Single-tool solutions aren't robust enough Combining specialized tools (LlamaParse + Gemini) improves accuracy Confidence scoring enables manual review workflows What's next for CareLink Mobile App Native iOS/Android apps for social workers Push notifications for case assignments Offline mode for areas with poor connectivity SMS Integration Text updates for patients without smartphones Bilingual support (English/Spanish) Two-way communication for confirmations <div