---
slug: "oceanguard-nvc5sf"
url: "https://devpost.com/software/oceanguard-nvc5sf"
title: "Oceanguard"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 506
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Oceanguard

> A simple web app that helps communities track ocean pollution and plan cleanups.

[Devpost](https://devpost.com/software/oceanguard-nvc5sf) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** css, elevenlabs, mongodb, react, snowflake, solana, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oceanguard

## Body

Front-page Dashboard Global tracking Inspiration Ocean pollution is something we constantly hear about, but most people don’t know what’s happening in real time or how they can help. Over 8 million tons of plastic enter the ocean every year, yet monitoring systems are often slow and reactive. We wanted to build a simple and practical web application that makes ocean health data easier to understand and helps communities take action instead of waiting for problems to get worse. What it does OceanGuard is a web application that tracks ocean pollution levels and helps coordinate cleanup efforts. Users can: View a live dashboard showing pollution and kelp health data See ocean health scores for major coastal cities View short-term predictions of debris movement Identify which areas need urgent cleanup Support specific cleanup operations through transparent donations The platform makes complex environmental data simple and easy to understand so communities can respond faster. How we built it We built OceanGuard using: Frontend: React, TypeScript, and Tailwind CSS for a clean and responsive interface 3D Visualization: Three.js and react-globe.gl to display an interactive global map Backend: Node.js and Express Database: PostgreSQL with data mirrored to MongoDB AI Tools: OpenAI and Gemini for generating environmental insights and reports Analytics: Snowflake Cortex for deeper data analysis Voice System: Twilio and ElevenLabs for AI-based site verification calls Blockchain: Solana devnet for transparent donation tracking We focused on keeping the user interface clean and beginner-friendly while integrating multiple technologies behind the scenes. Challenges we ran into One of the biggest challenges was coordinating multiple AI systems together. Each tool had different response times and behaviors, so making everything update smoothly in real time required careful debugging. Another challenge was managing live updates every 30–60 seconds without slowing down the user interface. We had to optimize how data streamed to the dashboard to prevent bottlenecks. Accomplishments that we're proud of We are proud that we built a complete end-to-end system that connects detection, prediction, cleanup coordination, and funding into one platform. Our AI phone verification system is a major highlight. It can carry out a natural conversation to confirm cleanup site conditions before dispatching teams, and it streams a live transcript to the dashboard. We also successfully implemented blockchain-based donations tied directly to specific cleanup operations, increasing transparency and trust. What we learned We learned how to integrate multiple AI systems into one cohesive application and manage real-time data pipelines. We also learned the importance of designing systems where AI assists humans rather than replacing them. Building human-in-the-loop workflows made the platform more practical and realistic. This project deepened our understanding of full-stack development, real-time architecture, and responsible AI integration. What's next for Oceanguard Next, we plan to: Expand monitoring beyond 20 cities Move blockchain donations from devnet to mainnet Improve edge AI capabilities so more analysis runs directly on drone hardware Add more community engagement tools to help volunteers organize local cleanups Our long-term goal is to make OceanGuard a scalable and transparent platform that empowers communities worldwide to protect their oceans. <div