---
slug: "walter-wego"
url: "https://devpost.com/software/walter-wego"
title: "Walter Wego"
hackathon: "Perplexity Hackathon"
organization: "Perplexity"
winner: true
words: 788
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/runtime_tool_creation"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/geospatial"
---

# Walter Wego

> A 21st century intelligence dashboard built for deep dives & bold minds

[Devpost](https://devpost.com/software/walter-wego) · hackathon [[Perplexity Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]] [[runtime_tool_creation]]
**domain** [[media_journalism]]
**user** [[researcher]]
**substrate** [[geospatial]]

**stack** mcp, miro, nextjs, perplexity, shadcn, supabase, tailwindcss

## How they structured the write-up

- 🚀 what it does
- ⚙️ how we built it
- ⚠️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for walter wego

## Body

Architecture Evidence board with all sources Detail View for Events on Custom react-flow Canvas Internal tool calls from server logs Custom Deep Research implementation using sonar-reasoning APIs 🔍 Inspiration Every investigator needs a control room — a space where scattered information becomes structured insight. While Perplexity is great for quick lookups, deeper investigation needs more than just linear answers. You need a bird’s eye view — a place to collect facts, spot patterns, and connect dots with clarity. That’s why we built Walter Wego — a digital, intelligent, and incognito dashboard that feels like a tactical boardroom for your brain. It maps evidence visually, links ideas intelligently, and helps you form theories with real-time AI research — all without breaking your flow or revealing your hand. Think Figma meets Cursor meets Miro! 🚀 What it does Walter Wego is a private intelligence dashboard that: Investigates queries using real-time web search with citations (powered by Perplexity Sonar) Organizes information spatially on a dynamic board powered by Miro via Model Context Protocol Connect private data sources for enhanced investigations & Deep Research Allows you to explore and visualize theories with interconnected evidence Embeds everything into a single clean UI with collaboration baked in In short: it's your alter ego for digging deep, connecting dots, and keeping it all off the record. ⚙️ How we built it We used a modern, full Typescript stack with modular intelligence orchestration: Next.js for full-stack rendering and API handling TailwindCSS & Shadcn for UI clarity and rapid design iteration Perplexity Sonar API (especially sonar-reasoning-pro ) for real-time, structured intelligence Custom RAG Pipeline that integrates with the Sonar model family to retrieve and process relevant chunks before reasoning Custom Deep Research Algorithm tailored for Visual Intelligence — a 3-phase protocol (Intelligence Gathering → Pattern Analysis → Synthesis) that structures reasoning and outputs data in a format optimized for mind maps and investigative visuals Miro MCP ( via smithery.ai ) for live diagramming, letting us push sticky notes, connectors, and visuals on the fly 🔥 The most technically ambitious part? We built a live-rendering integration between our app and Miro boards, turning AI research output into visual, spatial maps on a collaborative canvas — without reinventing the wheel. Here's how: We implemented our own tool calling layer over Perplexity’s API which would then interface with our MCP client hosted on smithery.ai , allowing for native tool calling using Sonar Reasoning Models. We created a custom connector between our Perplexity LLM and MCP logic, which dynamically generates sticky notes, connectors, and structures based on research data. Perplexity-style nested queries were parsed and enriched through Sonar and passed as rich JSON to our renderer, and we also used Sonar models to ascertain the relationship between nodes (to add connectors). This allowed us to: Avoid building a custom canvas system from scratch Tap into Miro's robust real-time collaboration features Keep everything instantly shareable, linkable, and transparent while also referencing the citations provided ⚠️ Challenges we ran into Dynamic rendering on Miro via API was complex — especially handling placement, z-index, collisions, and connections between sticky notes, all under AI control Structuring real-time data from Sonar into meaningful, visual representations without overwhelming the board Maintaining AI instruction determinism so that sticky note positions and logic were predictable and traceable Embedding and syncing Miro seamlessly into our app via iframe while keeping it responsive and intuitive Balancing live search speed with citation completeness in a multi-threaded query architecture 🏆 Accomplishments that we're proud of Integrated a real-time, source-grounded AI search experience directly into a live Miro canvas Created a fully working prototype where AI generates research and visualizes findings without user intervention Built a context-persistent investigation stack with MCP — which can scale to journalism, OSINT, research, and more Designed a system that feels light but does heavy lifting behind the scenes 📚 What we learned Building on powerful tools like Miro lets you focus on differentiation, not duplication Research becomes exponentially more useful when it's visual, persistent, and grounded in real-time sources Getting AI to control a structured canvas isn't trivial — instruction clarity and failure recovery were key Embedding trust (via citations) and clarity (via visual graphs) is a must when dealing with AI outputs 🚀 What's next for Walter Wego [ ] Create new boards & manage boards on Miro Better [ ] Introduce hypothesis nodes and AI-generated insight links [ ] Improve the placement of cards and items on the board, with enough spacing [ ] Improve the custom-canvas for interactivity (maybe a custom MCP too!) [ ] Add voice-driven querying and dictation-to-investigation mode [ ] Expand to plugin-based research enrichers (e.g., Notion, Google Scholar, News APIs) [ ] Launch alpha with investigative journalists and academic researchers <div