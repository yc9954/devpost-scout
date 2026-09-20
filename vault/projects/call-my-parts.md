---
slug: "call-my-parts"
url: "https://devpost.com/software/call-my-parts"
title: "Call My Parts"
hackathon: "Gemini Live Agent Challenge"
organization: "Google"
winner: true
words: 422
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/social_worker"
---

# Call My Parts

> Sit back and relax while our agent help find the right fit

[Devpost](https://devpost.com/software/call-my-parts) · hackathon [[Gemini Live Agent Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[supply_logistics]] [[transportation]]
**user** [[social_worker]]

**stack** adk, browser-use, cloud-run, docker, fastapi, firebase, gcp, gemini, python, react, twilio, typescript, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for call my parts

## Body

Architecture Sequence Flow from User to Calling vendor Flow Diagram for how does user connect with vendors Flow Diagram for Architecture flow Inspiration Working at a used car dealership we came across a problem of how time consuming finding a used part can be. Especially when you work at a dealership which needs used parts for multiple vehicles on an every day basis. What it does Helps you save time where it can be utilized for other important things rather than phoning around for parts and negotiating with vendors. How we built it Built on FastAPI with Google's Agent Development Kit (ADK) orchestrating three agents: voice intake, browser search, and outbound calling Voice intake uses Gemini 2.5 Flash Native Audio streamed over WebSocket so the conversation feels natural and supports real-time interruptions Browser search uses BrowserUse with LLM-driven navigation plus Playwright fallbacks for sites like RockAuto and car-parts.com Outbound calling bridges Twilio's Programmable Voice with Gemini Live, dialing up to 3 vendors in parallel and extracting structured results Frontend built in React with a live pipeline tracker and real-time vendor call status, deployed to Firebase Hosting Challenges we ran into Building the Twilio to Gemini audio bridge required full codec conversion (8kHz μ-law in, 16kHz PCM out) with no room for latency Real phone calls meant navigating IVR menus, answering machines, and AI screeners so we built a 4-phase gatekeeper classifier Voice activity detection needed significant tuning to avoid triggering on background noise and cutting off the agent mid-sentence Keeping browser sessions alive across mid-conversation pauses and resuming them in the exact same state took multiple iterations Accomplishments that we're proud of The full loop works end-to-end: speak a request, the system searches vendors, calls them with AI, and returns a ranked results list without touching a phone Handling real-world call messiness like IVR trees and answering machines while still extracting clean structured pricing data A frontend that shows concurrent vendor calls resolving in real time, making the whole system transparent rather than a black box What we learned AI voice products are mostly infrastructure problems codec pipelines, connection drops, and session state management are harder than the model logic Starting from a real workplace problem kept every architectural decision grounded and prevented over-engineering What's next for Call My Parts Docker-based Chrome containers for multi-user browser concurrency A negotiation layer that pushes back on price and asks about condition and warranty Expanding beyond auto parts the architecture is domain-agnostic and any business sourcing inventory by phone is a potential use case <div