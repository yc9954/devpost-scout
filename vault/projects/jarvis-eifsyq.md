---
slug: "jarvis-eifsyq"
url: "https://devpost.com/software/jarvis-eifsyq"
title: "Jarvis"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 717
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Jarvis

> Your proactive AI copilot — lives in your browser, reads your world, acts before you ask.

[Devpost](https://devpost.com/software/jarvis-eifsyq) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]]
**domain** [[labor_employment]]
**substrate** [[geospatial]] [[web_dom]]

**stack** 2.0, agent, agentverse, api, asi:one, bridge, calendar, chrome.alarms, chrome.identity), chrome.storage, css-chrome-extensions-api-(shadow-dom, fastapi, fetch.ai, gmail

## How they structured the write-up

- inspiration
- what we built
- how we built it

## Body

Inspiration Most AI tools wait for you to come to them. You open a chat, type a question, get an answer. That's not an assistant — that's a search engine with better grammar. I wanted something different. An AI that already knows you — your schedule, your inbox, your habits, your preferences — and acts on your behalf before you even think to ask. Something that lives in the background of your digital life and shapes itself around you , not the other way around. JARVIS is that assistant. What We Built JARVIS is an AI-native proactive browser extension that sits quietly in the corner of every webpage and runs your life. It's not a chatbot you open. It's not a tab you switch to. It's ambient intelligence — always on, always watching, always a step ahead. It learns your personality , your habits , and your lifestyle to act as a true personal agent: Proactive inbox briefings — the moment you open Gmail, JARVIS reads your emails and gives you a casual, friend-style rundown. Not a summary. A briefing . Meeting detection & action — it spots meeting requests buried in emails, surfaces accept/decline buttons inline, writes to your Google Calendar, and sends polite decline emails automatically — all without you touching a thing. Lifestyle-aware restaurant recommendations — powered by a dedicated Agentverse agent that learns your taste profile, dietary habits, and preferences over time to recommend places you'll actually want to go. Proactive alerts — new emails and upcoming meetings surface on whatever tab you're on, not just in your inbox. Natural chat — ask anything about your day, your schedule, what's in your inbox. Everything runs through ASI:One ( asi1-mini ) and is agent-deployed on Agentverse , making JARVIS a true member of the Fetch.ai agent ecosystem — not just a wrapper around an LLM. How We Built It The system has two tightly integrated layers: Browser layer — A Chrome MV3 extension with a Shadow DOM overlay (immune to page styles and CSP on any site). A background service worker handles all intelligence: Google OAuth, Gmail and Calendar API calls, ASI:One inference, and routing decisions. Agent layer — A Python orchestrator on Agentverse coordinates a network of specialized agents. The restaurant agent maintains per-user lifestyle profiles and scores recommendations using a weighted preference model. The bridge server connects the extension to the agent network in real time. For meeting detection, we run a single combined inference call that returns structured JSON: { "briefing": "hey aryan, sanjith wants to meet at 11pm...", "meetings": [...] } We also built a deterministic regex fallback that independently scans email text for time patterns, so meeting detection never depends entirely on model consistency: $$P(\text{meeting detected}) = 1 - P(\text{AI fails}) \cdot P(\text{regex fails})$$ Restaurant preference scoring uses a weighted lifestyle match across cuisine, distance, price, and dietary constraints — shaped entirely by the user's profile, not generic recommendations. Challenges Making it truly proactive, not reactive — The hard part isn't the AI. It's deciding when to fire, what to surface, and how to avoid being annoying. We built deduplication keyed on Gmail message IDs so the same email never surfaces twice, with a daily auto-reset so each morning starts fresh. MV3 service worker lifecycle — Chrome kills the service worker constantly. Any in-memory state evaporates between restarts. All agent state lives in chrome.storage.local, making JARVIS resilient to the MV3 lifecycle without needing a persistent background page. Timezone correctness — toISOString() returns UTC, which means at 11pm local time you're already asking to create tomorrow's calendar event. Fixed with a local-date function: function localDateISO() { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`; } Personality grounding — Getting the AI to speak to you, not at you, required careful prompt engineering. The system prompt treats ASI:One not as a chatbot but as a friend who already knows your context — casual, direct, zero corporate fluff. What We Learned A proactive assistant changes the relationship between a person and their AI entirely. You stop using the tool and start trusting it. That shift — from reactive to proactive, from generic to personal — is what makes JARVIS feel less like software and more like having someone in your corner. The intelligence is cheap. Knowing when to use it is everything. <div