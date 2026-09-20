---
slug: "faxi-16iecy"
url: "https://devpost.com/software/faxi-16iecy"
title: "Faxi"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1254
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Faxi

> Faxi resurrects fax for seniors left behind digitally. Handwrite a request, fax it, and our AI turns it into two-way email, bookings, or online orders. No devices or technical skills required.

[Devpost](https://devpost.com/software/faxi-16iecy) · hackathon [[Kiroween]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**domain** [[civic_government]] [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[retail_commerce]] [[security_privacy]]
**user** [[general_public]]
  <sub>weak: legal_professional</sub>
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** amazon-web-services, bullmq, docker, ecs, gemini, mcp, node.js, playwright, postgresql, redis, s3, ses, stripe, telnyx

## How they structured the write-up

- summary (for judges)
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for faxi

## Body

Summary (for Judges) Faxi is an AI-powered fax-to-internet bridge that lets offline seniors in Japan access email, shopping, and online services using nothing but a fax machine. During this hackathon, I built a complete end-to-end system : incoming fax → multimodal AI interpretation → MCP service execution → outbound fax generation → automated email bridge. Kiro made this possible by driving the entire build through a spec-driven workflow : If you’d like to try it yourself, feel free to resurrect your fax machine and send a fax to +1-302-400-8899 or +81-50-5050-8899 — Faxi will happily fax you back. Inspiration Japan has the oldest population in the world, and millions of seniors have never used the internet. As daily life moves online, they’re being left behind. But almost every household still has a fax machine - a device they know and trust. The question: What if modern AI let seniors access the digital world without learning anything new? Faxi is that experiment, built rapidly from concept to a working multi-service prototype during this hackathon. What it does Faxi turns handwritten fax instructions into real digital actions performed by agents. How it works: The user writes a message by hand and faxes it. Gemini Vision reads and interprets the handwriting—even messy notes or multi-line instructions. Faxi identifies the intent (email, shopping, weather, messages, appointments, etc.). MCP agents perform the actions online. Faxi sends a clean, formatted fax back with the results. Each user also receives a personal email address tied to their fax number (e.g., fax-number@me.faxi.jp ). Family emails → senior receives a fax. Senior replies by fax → Faxi converts it back to email. No apps. No accounts. No learning curve. How we built it Core Stack Telnyx for fax-over-IP Express + TypeScript for fax ingestion via webhook + routing Gemini 2.0 Flash for fax interpretation (handwriting, layout, circles) BullMQ for async workflows MCP servers for Email (SES) Amazon.jp search (Playwright) Payments (Stripe) General AI chat/Q&A S3 for storage & artifacts Custom context engine for multi-fax conversation continuity Next.js 14 dashboard for live pipeline + job visibility It is a full production-style pipeline with retries, monitoring, and a replayable test-fax harness. Kiro-Powered Development Workflow This project was only feasible during the hackathon because Kiro handled the architectural coherence and multi-service complexity. Kiro helped create: 16+ specifications in .kiro/specs/ defining system behavior, workflows, and tool contracts 4 agent hooks including: Auto-translate localization files for automatic internationalization maintenance TypeScript error detection Update the help and FAQ pages when functionality changes Auto update documentation and spec files when code changes Steering documents capturing product intent, architecture, and constraints Custom IDE MCP servers extended Kiro further. Spec Validator MCP Checked generated code against specs Flagged missing implementations Generated test scaffolds Auto-Docs MCP (Playwright) Navigated the UI Captured screenshots Generated and refreshed Markdown guides Kiro didn’t just generate code—it maintained the entire environment. How Kiro shaped the system Kiro’s spec-driven workflow was central to the project. Instead of building features reactively, we wrote explicit behavioral specs describing how seniors should experience the product. This surfaced constraints we would never have identified early on—such as one-shot interpretation, no clarifying questions, no sessions, and circle-based confirmations. One small spec line ended up shaping the entire architecture: “WHEN a user circles an option on a fax THEN the system SHALL complete the action with no additional steps, no accounts, and no digital UI.” This simple statement forced us to unify search, email, purchasing, confirmations, and AI interpretation into a single-page fax interface. It became the north star for all MCP integrations, agent workflows, and fallback logic. Kiro kept the architecture coherent, prevented drift, and enabled extremely rapid iteration across all specs. Challenges we ran into 1. Making digital services feel intuitive for seniors Our users should never need to understand technical processes. They should just write a message and send a fax. → Kiro helped designing a UX without exposing any technical concepts, lingo, or workflows. 2. One-shot interpretation Seniors shouldn’t receive multiple faxes. AI must get intent right on the first attempt. → Kiro helped create stable prompts, fallback paths, and error policies. 3. No sessions or cookies Context must be inferred from fax metadata and semantic history. → Kiro helped design and refine the context engine spec. 4. Multi-intent orchestration One handwritten page often contains multiple commands. → Kiro generated sequencing logic and response synthesis patterns. 5. Reliable Amazon.co.jp scraping Must succeed on first load; no “refresh.” → Kiro produced robust Playwright flows and retry strategies. 6. Safety for vulnerable users Fraud-resistant purchasing, trusted inbox rules, and hallucination safeguards. → Specifications ensured safety logic remained consistent across features. Accomplishments that we're proud of A complete end-to-end fax-to-digital system Achieving consistent round-trips across multiple services was a major milestone. A fully functional, invisible email client for seniors Faxi implements a complete email system—send, receive, reply, manage contacts—while hiding all digital concepts. Seniors use email naturally without ever touching an inbox or device. Multi-intent execution and one-shot interpretation Our multi-intent parser decomposes, sequences, and executes tasks, then synthesizes everything into a single coherent response fax. Reliable e-commerce search under real-world constraints Our Playwright-based Amazon.co.jp integration searches and deliver product results that are immediately useful. Seniors cannot “refresh,” so we engineered the search flow to succeed on the first try. Built-in protections tailored for seniors Because our users are elderly and often vulnerable, we designed Faxi’s digital interactions to be inherently safe: Fraud-proof payments using Japan’s furikomi bank transfer flow , ensuring seniors approve every purchase manually and cannot be charged unexpectedly. Human-in-the-loop review for orders, allowing operators to catch unusual or dementia-related purchase patterns before money is ever moved. No automated purchases. A protected email inbox that only accepts messages from trusted contacts, shielding seniors from spam, phishing, and unknown senders. These protections make Faxi not just functional, but safe , culturally aligned, and senior-friendly. Real-time admin dashboard with deep visibility The dashboard provides operators with live job streams, AI interpretation visibility, cost metrics, and safety monitoring. Built end-to-end using Kiro’s spec-driven development workflow Kiro enabled us to manage and ship a complex multi-service system within the hackathon timeframe. Kiro kept the architecture coherent, the requirements explicit, and the development velocity high. What we learned Technology must adapt to people, not the other way around Seniors don’t need simpler smartphones; they need systems that respect the tools and habits they already trust. Modern AI makes legacy interfaces powerful again Today, multimodal AI can unlock use cases that were previously impractical. Abstraction is a feature The more invisible the technology feels, the more empowering it becomes for the end user. Spec-driven development scales complexity With 16+ specs, 4 hooks, and multiple MCP servers, Kiro’s structure prevented us from losing track of requirements and architecture like other vibe coding platforms do. Japan's context shapes the solution Aging demographics, cultural comfort with fax, and the government’s push for digital transformation combine into a unique environment. What's next for Faxi Pilot programs with real users We plan to partner with elder-care facilities, municipal governments, community centers, and local clinics in Japan to test Faxi with seniors and their families in real daily workflows. Improving reliability across edge cases We plan to enhance handwriting robustness, add more context-recovery patterns for multi-step tasks, and build a deeper library of intent templates tailored to senior communication styles. Partnerships with businesses and local governments Healthcare providers, e-commerce platforms, and municipal offices are all eager to reach elderly populations. Faxi can serve as a bridge between digital-first services and analog-first citizens. <div