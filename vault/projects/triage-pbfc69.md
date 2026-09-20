---
slug: "triage-pbfc69"
url: "https://devpost.com/software/triage-pbfc69"
title: "Triage"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 917
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Triage

> Slack-native AI issue triage that classifies, drafts, and duplicates — but never ships without you.

[Devpost](https://devpost.com/software/triage-pbfc69) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[health_clinical]] [[housing_homeless]] [[supply_logistics]]
**user** [[developer]] [[government_staff]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** gemini, github-api, github-webhooks, model-context-protocol, next.js, node.js, pgvector, postgresql, react, slack-api, slack-bolt-sdk, supabase, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next

## Body

Inspiration Every open-source project I love runs on borrowed time. Someone spends their nights and weekends triaging issues, closing duplicates, and drafting responses — usually while apologizing for slow reply times. The tools that exist for maintainers either bury them in dashboards or automate away the human judgment that makes open-source trustworthy. That felt wrong to me. The problem isn't that maintainers need more automation. It's that they need a way to move faster without losing control . Triage is my attempt to build that. What it does Triage is a Slack-native AI agent for open-source maintainer inboxes. When a GitHub issue or pull request opens, Triage classifies it with Gemini, embeds it into a pgvector store, checks it against every open issue for semantic duplicates, and posts a card to the maintainer's Slack channel with a drafted response and three buttons — Approve, Edit, Skip . Nothing ever ships without a human clicking a button. Around that core loop, there's a full dashboard showing metrics, LLM-clustered patterns across issues, latest digest, and the full backlog with filters. A slash command /triage-digest posts on-demand summaries to Slack. And a Model Context Protocol (MCP) server exposes the same data to any AI client — Claude Desktop, Cursor, MCP Inspector, or anything spec-compliant. One agent. Same data. Every surface a maintainer already works from. How I built it The stack is deliberately boring where possible and sharp where necessary. Slack Bolt SDK handles bot events, slash commands, and interactive buttons GitHub webhooks stream issue and PR events into a Next.js API route on Vercel Gemini handles classification ( bug / feature / question / docs / spam ), severity assessment, and response drafting pgvector on Supabase Postgres stores text embeddings for semantic duplicate detection using cosine similarity A decision engine routes each classified issue through an 8-rule cascade — spam gets flagged, duplicates get linked, critical bugs get urgent-attention treatment, and everything else gets a drafted response for maintainer review Pattern detection runs an LLM clustering pass over recent issues to surface themes across the backlog The MCP server implements JSON-RPC 2.0 over Streamable HTTP with Bearer token authentication, exposing three tools: list_patterns , search_similar_issues , and get_digest The dashboard is a Next.js server-component app with a route-group split between public marketing pages and authenticated dashboard surfaces The design system is monospace, near-black, emerald accent, sharp corners — consciously not trying to look like every other AI product Everything runs on Vercel with a Supabase Postgres backend. Zero-config deploys, cold-start times under 500ms. Challenges I ran into Two challenges I want to name honestly. The first was the human-in-the-loop constraint itself. It would have been faster to build a fully autonomous system that just closes duplicates and posts responses. But I kept coming back to a simple test: would I trust this bot to speak for me to my own contributors? The answer was no unless I could review every draft first. So the decision engine gained a rule specifically for "generate a draft but wait for human approval" — and the whole product changed shape around that constraint. Slower to build, but the right shape. The second was composability. Every surface — Slack cards, dashboard, digest, MCP — reads from the same store. That sounds obvious until you build it and realize how many places you can accidentally drift into surface-specific data models. I refactored the shared query layer three times before the shape held. Also, real transparency: I hit Gemini rate limits, wrestled with Slack sandbox provisioning at the eleventh hour, and rebuilt duplicate persistence when I realized the initial version only flagged in Slack but never wrote to the database. All of those got fixed. All of them made the product sharper. Accomplishments I'm proud of Shipped a full-stack product end-to-end — Slack bot, GitHub webhook pipeline, dashboard, MCP server, landing page — all working, all deployed, all tested Built a real MCP server that any spec-compliant AI client can query — not a toy, an actual JSON-RPC 2.0 endpoint with auth Held the line on the human-in-the-loop constraint even when it was easier to skip Made every surface pull from the same source of truth — one query layer, three delivery channels Designed something that doesn't look like every other AI product — monospace, technical, quiet What I learned That trust is a technical property, not just a design one. Building Triage taught me that the shape of AI agents matters as much as their capabilities — where they sit, when they wait, who they defer to. The same underlying model can feel like a partner or an intruder depending on how you structure the interaction. I also learned how much systems design is really about inventory — knowing where every piece of data lives, who owns it, and which surface reads it. The MCP server was easy to add once the store was clean. The store was hard to clean. What's next Multi-tenant support — OAuth 2.0 install flow so any maintainer can install Triage on their own repos and Slack More MCP tools — draft generation, approval submission, pattern manipulation, all exposed as callable tools for AI agents Rich digest customization — configurable cadence, per-channel routing, digest templates Deeper GitHub Actions integration — closing duplicates, applying labels, tagging maintainers automatically (still human-gated) Real user testing — take this to actual open-source maintainers and see what breaks Triage is version 1.0. The scaffolding is real. The next version is about scale, not proof. <div