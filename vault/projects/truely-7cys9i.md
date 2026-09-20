---
slug: "truely-7cys9i"
url: "https://devpost.com/software/truely-7cys9i"
title: "Truely"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 453
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Truely

> Never be lied to again.

[Devpost](https://devpost.com/software/truely-7cys9i) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[labor_employment]] [[media_journalism]] [[supply_logistics]] [[transportation]]
  <sub>weak: civic_government</sub>
**substrate** [[video_visual]] [[web_dom]]

**stack** anthropic, letta, svelte, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- architecture
- accomplishments we’re proud of
- learnings & challenges
- what’s next

## Body

truely debunking a conspiracy theory with timeline analysis truely citing the census to verify that there aren't 21 trillion people truely debunking the lie we planted in this devpost :-) Never Be Lied to Again. Meet Truely 🔎 Inspiration “When we abandon facts, we abandon freedom.” — Timothy Snyder. Misinformation is lethal: 232 000 Americans died in 15 months after vaccine-hoax posts deterred them from a free COVID shot. 330 000 South Africans lost their lives—and 35 000 babies were needlessly infected—because one speech denied the HIV-AIDS link. The viral Cluely “cheat-on-everything” AI now pumps out polished essays, deepfakes, even fake lab data, eroding trust in all AI. Every new pandemic and every election is a bigger target. That’s the blaze— Truely is our fire-extinguisher. What It Does Truely is a plug-and-play browser extension that unleashes a fleet of AI agents the instant a page loads: Pain Truely’s Cure Hidden half-truths & outright lies Live highlights & corrections with primary-source citations AI-generated stealth content Deep-scan detector flags synthetic text, images, audio, or video Missing context Additional statistics and neutral summaries right where you need them How We Built It Frontend: WXT (Web Extension Toolkit) for modern Chrome extension development with TypeScript Svelte 5 for reactive, component-based UI with excellent performance TailwindCSS for utility-first styling and responsive design Backend: Chrome Extension Manifest V3 for secure background service workers and content scripts LETTA AI API for intelligent fact-checking and misinformation detection Anthropic Claude API as a secondary AI agent for robust analysis Custom DOM parsing engine to extract and clean webpage content for AI analysis WebExtension Messaging API for secure communication between extension components UUID-based action tracking for managing multiple fact-checking annotations Architecture Accomplishments We’re Proud Of Built a real-time AI fact-checker that flags misinformation directly in the browser Designed interactive annotations with clear, cited corrections that don’t interrupt reading Engineered a smart DOM pipeline that filters only essential user-visible content Shipped a performant and secure Manifest V3 Chrome Extension with advanced background capabilities Learnings & Challenges Parsing complex, inconsistent DOM structures across the web Compressing large webpage text into limited AI context windows without losing key facts Building a seamless system to highlight and annotate dynamic content without breaking page layout Coordinating responses across multiple AI agents with different output formats What’s Next Cross-page memory: Agents remember what you’ve seen and flag contradictions or recurring misinformation across sites. Custom AI agents, made by users: Anyone can deploy browser-native agents using just a prompt Monetization through agent marketplaces: Users can create, share, and even monetize their own agents via blockchain-powered rewards Truth has a new home address: your browser. We’re not just fighting misinformation—we’re making honesty the default experience on the internet. Join us. <div