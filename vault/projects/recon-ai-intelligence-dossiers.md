---
slug: "recon-ai-intelligence-dossiers"
url: "https://devpost.com/software/recon-ai-intelligence-dossiers"
title: "Recon : AI - Intelligence Dossiers."
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 855
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Recon : AI - Intelligence Dossiers.

> Name a target. Get the file. An AI agent reads the live web and files a cited intelligence dossier on any company in seconds, with a numbered exhibit behind every claim.

[Devpost](https://devpost.com/software/recon-ai-intelligence-dossiers) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[legal_justice]] [[media_journalism]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** groq, python, react, render, tavily

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recon

## Body

Landing Page. Why this wins over a chatbot. The architecture of how it works. A Sample Dossier. More info on a dossier Inspiration AI research tools have a trust problem. Ask one about a company and you get a confident wall of text with no way to check a single claim. Real analysts in finance, journalism and due diligence don't work from vibes. They work from sources . We wanted a tool that researches like an analyst, not a chatbot: it goes and reads the open web, and every claim it makes is tagged to the exact source it came from. What it does You name a target, a company or product or ticker, and Recon dispatches an AI agent that searches the live web, reads primary sources, and assembles a structured intelligence dossier in front of you in seconds: Key Facts: CEO, HQ, founded, employees, sector, ticker, and market cap / valuation. Seven sourced sections: What They Do, Leadership, Traction & Funding, Financials & Stock, Competitive Landscape, Risks & Red Flags, and Recent Developments. An Analyst Assessment: a bottom-line verdict stamped with a confidence score. Citations on every bullet , with all sources listed as numbered exhibits. A run fires seven searches in parallel, dedupes ~34 sources into numbered exhibits, and files the dossier in under a minute. It runs out of the box in a scripted Sample mode, and flips to live research with two free API keys. Live demo: https://recon-ckfe.onrender.com/ How we built it Frontend: Vite + React. The agent's progress and each finished section stream into the UI over Server-Sent Events, so you watch the dossier assemble. Loading sections appear as redaction bars that "declassify" into text. Backend: A Node/Express server runs the agent loop: identify the target, run seven web searches in parallel, extract structured key facts, synthesize each section constrained to its own retrieved sources (citing source IDs), then weigh everything into a verdict and confidence score. Models & data: Groq (GPT-OSS 120B, with automatic fallback to 20B) for fast, free inference; Tavily for web search that returns page content , which is what makes grounding possible. Zero paid APIs, no database, deployed free on Render. Design: We deliberately rejected the generic "dark dashboard + neon accent" AI look and built a declassified case-file aesthetic: warm near-black paper, a single amber accent, and three typefaces with strict roles. Archivo for headings and data, Courier Prime for file numbers and labels, Newsreader for the dossier prose. Self-hosted, so no font CDN at runtime. Challenges we ran into A model that knew too much. Our prompts told the model to use only retrieved sources and cite what it used, and we assumed that worked. When we measured, only 17% of bullets carried a citation , and the failure wasn't random: five of seven sections cited nothing while two cited perfectly. For a well-known company the model already knew the answer from pretraining, so it wrote fluent, accurate, completely unsourced prose with nothing to attribute. Fixed by naming the exact legal source IDs per section, forbidding prior knowledge, requiring a citation per bullet, and validating returned IDs against the ones actually shown. Citation rate went from 17% to 97-100% . A dependency that vanished. Mid-competition, Groq retired the model we ran on. Every call started returning 404. Search still worked, so the app kept filing completely empty dossiers. We migrated and added a fallback chain, so the next retirement degrades the dossier instead of emptying it. Latency. Reasoning models spend hidden tokens thinking before answering. This work is extraction and grounded summary, not deduction, so that thinking mostly cost time. Turning reasoning effort down took a full dossier from 145s to ~45s . Free-tier rate limits. Nine LLM calls per run bumps against Groq's tokens-per-minute cap, so calls retry with backoff. A truncation bug hiding facts. The key-facts extractor capped its digest at 5,000 characters across all sources, so it never saw past ~source 14 of 34 and silently missed CEO and HQ. Raising the cap took filled fields from 2 to 6. Accomplishments that we're proud of A research tool where the sourcing claim is measured, not asserted . On a live run against Figma: 7 sections, 29 findings with 28 cited, 37 citations across 34 exhibits, confidence 78. It runs on $0 of infrastructure and looks like nothing else in the pool. What we learned Streaming the agent's reasoning is what makes AI feel trustworthy : showing the work matters as much as the answer. The deeper lesson was about grounding. A model that already knows your subject is more dangerous than one that doesn't, because it produces confident, correct-sounding, unsourced prose, and no amount of politely asking it to cite will stop that. You have to constrain what it's allowed to say, validate the citations it returns, and actually measure the rate. We only found our own grounding gap because we measured it. What's next for Recon Export dossiers to PDF and shareable links. People and market/sector targets, not just companies. Live pricing and financials via a markets API. Surfacing disagreement between sources instead of reconciling it silently. <div