---
slug: "checkr-esikfo"
url: "https://devpost.com/software/checkr-esikfo"
title: "Checkr"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 647
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/patient_family"
---

# Checkr

> The future of mental health.

[Devpost](https://devpost.com/software/checkr-esikfo) · hackathon [[NexHacks]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
**domain** [[education]] [[health_clinical]] [[mental_health]]
**user** [[educator_student]] [[patient_family]]

**stack** braveapi, elevenlabs, google, leanmcp, livekit, photon, thetokencompany, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for checkr

## Body

Inspiration Today, 40% of college students struggle with depression, and 80% face harmful levels of stress. As first year college students tackling extra classes, project teams, and startups, we often push mental health aside, telling ourselves, “I’ll be fine, I just need to push through and it’ll all be better eventually.” But therapy access is inadequate. Between the struggle to find providers, schedule appointments, or even ask for help, most students never reach out. That’s why we built Checkr, a super-intuitive AI companion that checks in on you, listens, and connects you to real support before it’s too late. Additionally, having built multiple award winning mental health applications, we noticed that therapists face the issue of not having any context about their patients due to the lack of out-of-clinic info. Checkr solves both problems at once, removing barriers to support and enabling therapists to better serve their patients. What it does Checkr uses an Agentic infrastructure via Livekit across text and call Performs empathetic onboarding Hyper-realistic onboarding Performs background search to get a better understanding through LeanMCP Aggregates student context (calendar) to figure out future therapist scheduling plans Finds therapists and resources over phone The first tool to be able to use both phone and text with shared context and agentic integrations Uses LeanMCP to perform websearch using BraveAPI Uses Google API to determine open blocks for therapists appointments Schedules appointments automatically and creates a Google Calendar invite Directly connects with therapists near you Provides a short background of the user and their needs The user is then redirected to a tunneled call with the therapist Implements Elevenlabs to provide a seamless voice agent experience How we built it We built five specialized AI agents orchestrated by Livekit : Onboarding agent: proactive iMessage-based experience powered by photon.codes Therapist and Resource Agent: LeanMCP for fast lookups + BraveAPI + BrowserUse Scheduling Agent: automated calendar sync, booking, and patient context sharing with therapist profiles Voice agent: Uses the context from onboarding to ask more about the concerns of the user, connects to the Resource Agent if necessary Text agent: works alongside the voice agent, making this the first context-shared voice + text based platform. Challenges we ran into Perfecting the onboarding process with hyper-realistic agents and tooling (LeanMCP). Orchestrating fifteen steps into five complex agents (LiveKit). Calendar api and setting up the voice agent to properly negotiate times. Keeping context and empathy across agents (LiveKit). Accomplishments that we're proud of Multi-source context aggregation (Text + Video, Calendar, LiveKit). Voice empathy engine via ElevenLabs. Web scraping and data enrichment using The Token Company + BraveAPI. Orchestration and automation via LiveKit, chaining all agents seamlessly. Real-time resource discovery via LeanMCP. What we learned Working with cutting-edge sponsor technologies transformed our development process. Integrating LiveKit's agent orchestration enabled seamless multi-agent coordination and real-time voice workflows that would have taken weeks to build from scratch. It was our first time working with LiveKit. We discovered its powerful AgentSession and Workflow systems for orchestrating complex voice AI pipelines with dynamic handoffs between specialized agents perfect for production-grade conversational systems. It was our first time working with Mastra, and we were blown away by how powerful it can be, as a TypeScript-native workflow orchestration engine. ElevenLabs’s voice agents engine delivered emotionally intelligent TTS that elevated our user experience far beyond standard text-to-speech. The Token Company + BraveAPI allowed for web scraping and became effortless with reliable, scalable data enrichment across multiple sources without infrastructure headaches. LeanMCP: Real-time resource discovery opened new possibilities for dynamic data retrieval during live conversations. What's next for Checkr Checkr is set up to make a significant impact by lowering barriers to care and building trust through proactive support: For students: Stigma-free, quick access to therapy. For therapists: Clients arriving fully prepared, less time spent on menial tasks. For universities & insurers: Mental health care that lowers costs and risk <div