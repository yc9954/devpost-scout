---
slug: "scaena-os"
url: "https://devpost.com/software/scaena-os"
title: "Scaena OS"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1188
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Scaena OS

> Scaena automates gig booking for entertainers. Four AI agents research venues, write pitches, follow up, and learn what works. They get smarter every round so you book more shows with less effort.

[Devpost](https://devpost.com/software/scaena-os) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[geospatial]] [[structured_db]]

**stack** agentverse, asi-1-mini, css, eventbrite, fastapi, figma, gemini, godaddy, google-gmail-oauth, mongodb, peerspace, python, react, recharts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scaena os
- company challenges

## Body

Home Page on Dashboard Market Research Agent Outreach Agent Analytics Agent Pipeline Agent Inspiration You just dropped your best track. It's getting streams, people are sharing it, the comments are calling you out for shows. So what do you do next? You open a spreadsheet. You spend three hours Googling venues. You write fifteen cold emails that get no reply. You follow up manually. You lose track of who said maybe. You do it all again next week, and the week after, on top of actually trying to make music. This is the reality for millions of up and coming artists. The ones who make it are not always the most talented. They are often just the ones with a team behind them. A booking agent. A manager. Someone working the phones while they work the studio. We built Scaena OS to be that team. An AI system that acts as your booking agent, handling research, outreach, follow-ups, and pipeline management so you can stay focused on the craft. Not just a tool. An agent working on your behalf. What it does Scaena OS is a four-agent AI system that automates the full booking pipeline for any artist type: rappers, musicians, DJs, comedians, speakers. An artist sets up a profile in under a minute. Four agents take over from there. Agent 1: Market Research Scans dozens of venues by artist type and location. Pulls market rates, scores each venue by fit, and streams results live through a terminal-style log. Powered by ASI-1 Mini with live data from Gemini Grounding, Google Search, Eventbrite, Peerspace, and social pages. Agent 2: Pitch Generator Writes a personalized outreach email for each venue, referencing the venue's vibe and why this specific artist fits. Sends directly from the artist's Gmail via OAuth2. Supports auto-send or manual review. Agent 3: Analytics and Learning Tracks response rates, identifies what's converting, and feeds insights back into Agents 1 and 2. Classifies venue replies automatically (interested, negotiating, booked, rejected) and proposes rate adjustments based on real data. Agent 4: Follow-Up Engine Schedules Day 3, 7, and 14 follow-ups for non-responders. Handles objections with counter-offers. Sends pre-show and post-show messages to confirmed bookings. Each round, the system gets smarter. Agent 3's learning feeds Agent 1's targeting and Agent 2's pitches. How we built it Backend: FastAPI, SQLite, MongoDB Atlas, ASI-1 Mini Agents: Four uAgents registered on Fetch.ai Agentverse with Chat Protocol. Typed Pydantic message models for inter-agent communication. WebSocket manager for real-time frontend events. LLM: ASI-1 Mini for reasoning and pitch generation. Gemini 2.5 Flash with Grounding for live venue discovery. Live research: Five data sources (Gemini Grounding, Google Search, Peerspace, Eventbrite, social pages) deduplicated and ranked in a single pipeline. Gmail: Full OAuth2 flow. Real emails sent from the artist's own address. Replies synced and classified automatically. Frontend: React 18, Vite, Tailwind CSS, Recharts. Neobrutalist dark design with neon accents, live agent status, terminal log, and typewriter pitch animation. Infrastructure: Vultr Cloud Compute at scaena.work. MongoDB Atlas on AWS us-east-1. Challenges we ran into Live venue data is messy. Five APIs return wildly different formats. Building a pipeline to fetch, normalize, deduplicate, and rank results with graceful fallbacks took most of our iteration time. Gmail OAuth under time pressure. Handling dry-run vs. live sends, per-entertainer token storage, and keeping frontend status in sync with real OAuth state required careful plumbing across multiple layers. Real-time agent communication. Each agent needed to broadcast live updates without blocking the API thread. We built a WebSocket event system so the frontend animates agent activity as it happens. Making the feedback loop real. Agent 3's insights had to actually change Agent 1's next scan, not just display on a chart. Getting that injection into prompt context on the next cycle was the core design challenge. Accomplishments that we're proud of End-to-end pipeline works. Zero to sent pitch emails in under 2 minutes. Not a prototype. Five live data sources. Agent 1 pulls from Gemini Grounding, Google Search, Peerspace, Eventbrite, and social pages in one scan. Nothing mocked. Real Gmail sending. Venues receive actual emails from the artist's own address via OAuth2. Feedback loop that compounds. Agent 3's insights genuinely update Agent 1 and Agent 2 on the next round. Live agent visibility. Users watch all four agents work in real time via a streaming terminal log. Agentverse with Chat Protocol. All four agents registered and reachable via ASI:One. Deployed and live. Running at scaena.work on Vultr with Atlas persisting data across sessions. What we learned Building Scaena taught us that the hardest part of a multi-agent system isn't the individual agents, but it's the interfaces between them. Typed message models, shared state, and a clean event broadcasting layer are what make the difference between agents that feel like a coordinated system and agents that feel like disconnected scripts. We also learned that real-world data integration is where most of the time goes. The actual LLM calls are fast to write. Wrangling five external APIs into a coherent, deduplicated, ranked result set (with graceful fallbacks) is where the engineering is. And we validated a real pain point. The pitch personalization that Agent 2 produces (referencing a venue's specific vibe, booking patterns, and why a particular artist fits) is qualitatively better than anything an artist would spend time writing at scale. That's the insight: agents don't just automate, they do certain things better. What's next for Scaena OS Spotify / streaming integration — Agent 1 pulls real streaming stats to strengthen pitches Rate negotiation — An Agent 5 that handles back-and-forth with venue bookers within a defined range Manager mode — One Scaena account managing multiple artists across the same pipeline Payment Protocol — Fetch.ai Payment Protocol so venues can deposit booking fees directly via ASI:One Mobile app — Artists approve pitches, get reply notifications, and manage deals from their phone The market is real: millions of independent artists worldwide can't afford booking agents. Scaena makes the agent available to everyone. Company Challenges Fetch.ai: Agentverse Search and Discovery All four agents are registered on Agentverse with Chat Protocol and are reachable via ASI:One. ASI-1 Mini powers the core reasoning. User intent ("get me booked in LA") produces real outcomes: venue lists, sent emails, tracked responses, scheduled follow-ups. Arista Networks: Connect the Dots Scaena is a data routing system. Profile data flows into Agent 1, venue data into Agent 2, pitch results into Agent 3, learning back into Agent 1. Five external APIs feed a single unified discovery pipeline. Gmail replies route through sentiment analysis back into the booking pipeline. MLH x MongoDB Atlas Atlas persists analytics events, pitch logs, and venue results across sessions, making Agent 3's learning loop durable. The /api/health endpoint confirms Atlas connection live during the demo. MLH x GoDaddy Registered scaena.work via GoDaddy Registry. Scaena is Latin for "stage." Live and pointing to Vultr. MLH x Vultr FastAPI backend and agent runtime deployed on Vultr Cloud Compute. Persistent public endpoint for real Gmail OAuth callbacks and live agent orchestration. Figma Make Used Figma Make to prototype the dashboard and neobrutalist design system before writing any frontend code. Chat log: https://www.figma.com/make/R88tbHbJht8MTnQk8GLIt3/Frontend-design-for-Lumen?p=f <div