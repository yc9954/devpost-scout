---
slug: "oceanguard-u19z4g"
url: "https://devpost.com/software/oceanguard-u19z4g"
title: "OceanGuard"
hackathon: "NextGenHacks"
organization: "NextGenHacks"
winner: true
words: 582
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# OceanGuard

> OceanGuard is an AI-powered website that transforms ocean health monitoring. We combine smart AI analysis and real-time global tracking to detect, predict, and coordinate marine conservation at scale.

[Devpost](https://devpost.com/software/oceanguard-u19z4g) · hackathon [[NextGenHacks]]

## Facets

**mechanism** [[human_in_the_loop]] [[on_device_local]] [[realtime_stream]]
**domain** [[transportation]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** css, elevenlabs, html5, mongodb, react.js, snowflake, solana, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oceanguard

## Body

Front-page Dashboard Global tracking Inspiration Our oceans are in crisis. Over 8 million tons of plastic enter the ocean every year, marine ecosystems are collapsing, and coastal communities lack the tools to respond effectively. Current monitoring is fragmented, slow, and reactive — by the time we detect a problem, the damage is done. We built OceanGuard to change that. What it does OceanGuard is an AI-powered ocean health intelligence platform that transforms marine conservation from reactive to proactive. It combines autonomous drone surveillance, a real-time 3D global tracking globe monitoring 20 major coastal cities, and AI-powered cleanup coordination. Operators get a live dashboard refreshing every 30 seconds with voice narration, 6 to 48-hour debris and kelp forest movement predictions, and an intelligent cleanup pipeline that goes from AI detection all the way to fleet dispatch and reporting. The public can directly fund specific cleanup operations through GoFundMe-style goals backed by transparent Solana blockchain donations. Before any team is deployed, an AI phone verification system — powered by Snowflake Cortex AI, ElevenLabs, and Twilio — calls the site to confirm conditions in a natural, multi-turn conversation streamed live to the dashboard. How we built it We built OceanGuard on a React, TypeScript, and Tailwind CSS frontend with Three.js and react-globe.gl powering the interactive 3D globe, and Framer Motion for animations. The backend runs on Node.js/Express with PostgreSQL via Drizzle ORM as the primary database, mirrored to MongoDB Atlas and piped into Snowflake for analytics. We integrated five AI systems: OpenAI GPT-4o-mini, Google Gemini 2.0 Flash for streaming environmental reports, Snowflake Cortex AI for deep ocean data analysis and as the phone agent brain, ElevenLabs for human-quality voice synthesis, and ExecuTorch for on-device edge AI inference on drone hardware. Twilio handles the voice calls with live speech recognition. Donations are processed on the Solana devnet with on-chain transaction signatures. Challenges we ran into Orchestrating five different AI systems together reliably was a core challenge — each with its own latency, API behavior, and failure modes. Streaming live call transcripts in real-time via SSE while simultaneously running background data engines updating every 30 to 60 seconds required careful architecture to keep everything in sync without bottlenecks. Accomplishments that we're proud of We’re proud of building a fully end-to-end pipeline — from AI detection to analysis, route planning, fleet dispatch, collection, and reporting — that actually closes the loop on ocean cleanup coordination. The AI phone verification system is a standout: a conversational agent that carries on up to 6 turns of natural dialogue, detects site availability, and streams a live transcript to the dashboard in real-time. We also successfully integrated blockchain-transparent donations tied directly to specific cleanup operations with live progress tracking. What we learned We learned how to orchestrate multiple AI systems — OpenAI, Gemini, Snowflake Cortex, ElevenLabs, and ExecuTorch — within a single cohesive platform, and how to design human-in-the-loop workflows where AI handles detection and analysis but humans retain final decision-making authority. We also deepened our understanding of real-time data architecture, edge AI deployment, and on-chain transparency for public trust in environmental funding. What's next for OceanGuard OceanGuard currently monitors 20 major coastal cities — the next step is scaling that global coverage further, expanding the autonomous drone network, and moving the Solana integration from devnet to mainnet for real-world fundraising. We also want to grow the ExecuTorch edge AI capabilities so more of the intelligence runs directly on drone hardware without cloud dependency, enabling faster response in remote ocean zones.​​​​​​​​​​​​​​​​ <div