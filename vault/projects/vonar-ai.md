---
slug: "vonar-ai"
url: "https://devpost.com/software/vonar-ai"
title: "Vonar.ai"
hackathon: "Perplexity Hackathon"
organization: "Perplexity"
winner: true
words: 583
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Vonar.ai

> Vonar.ai is an AI-powered voice agent that answers inbound calls, handles support requests, and instantly finds answers using real-time search — all without a human.

[Devpost](https://devpost.com/software/vonar-ai) · hackathon [[Perplexity Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
  <sub>weak: health_clinical</sub>
  <sub>weak: developer</sub>
  <sub>weak: structured_db</sub>

**stack** ai, css, html5, javascript, llama4, perplexity, redis, sonar

## Body

🚀 Inspiration We were frustrated by how bad most inbound call experiences are — long wait times, robotic phone trees, and irrelevant answers. At the same time, most businesses don’t have the resources to build a full AI voice stack. Vonar.ai was born from that gap: we wanted to create a voice agent that actually understands callers, acts fast, and gets smarter with real-time knowledge — without needing a team of engineers to set it up. ⸻ 🤖 What it does Vonar.ai is a voice-based AI assistant that answers inbound calls, triages requests, and responds using real-time, search-powered intelligence. It can: • Answer questions about policies, outages, or product info using Perplexity’s Sonar API • Handle account, tech, or service-related queries in a guided, secure way • Mock advanced flows like authentication and ticket creation to simulate integrations • Escalate to human agents or inform users when they need a custom production setup All while speaking naturally and keeping the experience smooth and on-brand. ⸻ 🛠 How we built it • Voice pipeline: Built using Vapi.ai to power voice input/output with real-time LLM processing • LLM: We used Llama 4 via Groq for blazing-fast inference and plugged in Perplexity’s Sonar Pro as a real-time search tool • Tool integration: Designed custom tool calls that silently inject Sonar results into the LLM’s context mid-call • Frontend/Infra: Serverless backend with Netlify Functions, live audio/webhook streaming, and optional Redis caching for performance • Demo optimization: Built a system prompt + dynamic persona system for customized flows per org or use case ⸻ ⚔️ Challenges we ran into • LLM prompt management: Keeping the system prompt concise while packing in real logic and disclaimers for mock/demo flows • Tool call timing: Ensuring that tool responses came back fast enough to avoid Vapi auto-ending the call due to silence • Auth & ticketing mocks: Simulating secure flows in a realistic way without violating trust or misleading the user • Silent lookups: Preventing the AI from “breaking character” when fetching from Sonar — had to tune the tone and behavior closely ⸻ 🏆 Accomplishments that we’re proud of • Built a fully working inbound AI voice agent that can actually hold useful conversations, not just reroute calls • Seamlessly connected real-time search (Sonar) into a voice workflow — almost no one does this live and cleanly • Delivered a usable demo that businesses could test with their own call flow in minutes • Optimized latency with Groq + Netlify + Redis to make everything feel snappy as hell ⸻ 📚 What we learned • Fast voice UX needs ruthless simplicity and aggressive caching — even 500ms of lag ruins the experience • People will forgive a lot if the voice is confident, clear, and useful — tone matters more than people think • Vapi’s infrastructure is powerful but fragile if you miss even one config (like toolIds) • Real-time search + voice agents is a killer combo, especially for gov and compliance-heavy orgs ⸻ 🚧 What’s next for Vonar.ai • Pilot with gov-aligned orgs and service-heavy businesses like MSPs, SaaS platforms, or utilities • Production integrations with Jira Service Management and Salesforce for live ticketing + user auth • Deploy self-serve onboarding so any org can spin up a branded Vonar voice agent with their own FAQ link • Expand tool library to include weather, outage detection, gov databases, or internal knowledge base sync • Go-to-market: targeting Carahsoft channels, AI hackathons, and defense tech conferences for early traction <div