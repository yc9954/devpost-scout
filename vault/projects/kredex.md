---
slug: "kredex"
url: "https://devpost.com/software/kredex"
title: "Kredex"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1371
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Kredex

> AI Agents for Small-Scale Businesses

[Devpost](https://devpost.com/software/kredex) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]]
  <sub>weak: vision_ocr</sub>
**domain** [[finance_payments]] [[health_clinical]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** caddy, docker, docker-compose, express.js, jwt, mongodb, mongoose, nginx, node.js, qwen, qwen-cloud, react, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for kredex

## Body

Landing page Dashboard Chat low stock alert Credit sale Chat - who owes me Chat - daily summary Chat - receipt-OCR Chat - Cross-session memory Memory Tiers Opportunity Scout Profit & Loss Screen Inspiration This project didn't start in 2026. It started in 2020, just before COVID , at a kitchen table — with my father. We watched the small traders around us — the provisions shops, the foodstuff sellers, the market women — run entire businesses out of their heads and a worn exercise book. They were brilliant at it, but the moment they forgot who owed what, or which item was quietly bleeding money, it cost them. My dad and I believed we could help. So we did what you're supposed to do: we ran a survey, we talked to real shop owners, and the answer came back loud and clear — people genuinely needed this. Back then, our plan was to do it manually — spreadsheets, forms, human data entry. It was heavy, it didn't scale, and life happened. Then COVID happened. And then, some time later, my father passed away. The idea stayed with me. What changed is what's now possible: I no longer need armies of manual data entry, because AI can be the bookkeeper. A shop owner can simply talk , and the system understands, records, and — most importantly — remembers . When I saw what Qwen's models could do, I realized the dream my dad and I sketched at that table was finally buildable, by one person, the right way. So I built Kredex — picking up an idea we started together and carrying it across the line. What it does Kredex is an AI bookkeeper for African micro-businesses that you run entirely by talking to it — in plain English or Nigerian Pidgin. No forms, no columns, no training. You: Amaka took 3 bags of rice on credit, she'll pay next Friday. Kredex: Recorded — Amaka owes ₦102,000, due next Friday. Your rice stock is now 13 bags. Bookkeeping by conversation — log stock (with reorder levels), cash and credit sales, payments, and running-cost expenses in a sentence. Ask it anything — "what's low?" , "who owes me?" , "am I making money this month?" Beyond typing — snap a supplier receipt and it reads the items into stock; log with your voice and it talks back. Get paid & stay on top — numbered PDF invoices, reminders, and automatic low-stock alerts. A memory that spans every conversation — start a brand-new chat with zero history and it still knows your prices, customers, and rules, because memory belongs to the business , not the thread. Look outward — an Opportunity Scout that finds grants and loans your shop can actually apply for. Reusable — its whole memory engine is exposed over MCP, so any agent can use Kredex as a backend. How we built it Kredex is a full-stack product powered end-to-end by Qwen Cloud . The stack: React + Vite + TypeScript on the front end; Node.js + Express + MongoDB on the back end; seven Qwen models behind a single OpenAI-compatible client. The models, each for a job: qwen3.5-flash — fast tool-calling, fact extraction, and web-grounded opportunity search (speed matters when one message triggers several model round-trips). qwen3.7-max — deep profit-and-loss reasoning. qwen-vl-max — reads crumpled supplier receipts into structured items. text-embedding-v4 — powers semantic memory. qwen3-asr-flash + qwen3-tts-flash — voice logging and talk-back. The agent loop: a 0ms local classifier guesses intent, then Qwen sees the message plus tool schemas and calls the right one of 11 bookkeeping tools against MongoDB, then streams a warm, plain-language reply token by token. The two-tier memory engine — the core innovation. A shop's knowledge is two different things, so I store it two ways: Tier 1 — a canonical-key trie for exact, correctable facts (prices, phone numbers, reorder levels). Writes overwrite in place with history kept; reads are deterministic — no model call, no hallucination surface. Tier 2 — a vector store for fuzzy, associative knowledge (habits, standing rules), where recall is scored, diversified with MMR, and reinforced on use: $$\text{score} = \cos(\theta) \times \text{importance} \times \text{recency}$$ The exact stuff is instant and always current; the fuzzy stuff is recalled by meaning. That's how a brand-new chat with zero history still knows the whole business. Reusable over MCP. I exposed the entire memory engine and all bookkeeping tools over the Model Context Protocol , reusing the same tool registry that powers the Qwen agent (an OpenAI function schema and an MCP inputSchema are both just JSON Schema). Any MCP client — Claude Desktop, an IDE agent — can use Kredex as a memory backend. 17 tools, one source of truth, two front-ends. Deployed on Alibaba Cloud. Kredex is a no-GPU, API-wrapper agent, which makes Simple Application Server (SAS) the right fit over ECS. It runs as a four-service Docker Compose stack (MongoDB, Express, nginx, Caddy), with Caddy handling automatic HTTPS and routing the server's public IP to my domain, kredex.xyz . Challenges I ran into Model exhaustion → smart routing. Free-tier quotas empty at different rates, and I learned Qwen's Token Plan keys are for interactive dev tools, not backends — a backend must use the pay-as-you-go endpoint. I wrapped every model call in a quota-aware fallback ( qwen3.5-flash → qwen3.7-max ) so the app degrades gracefully instead of dying on a 403 . The model that "reasoned its way to lying." In thinking mode, flash sometimes claimed it recorded a sale without calling the tool — silent book corruption. Fix: disable thinking on the agent path and force a tool call for action intents, so it must act before it can speak. Fact laundering. My canonicalizer originally read the AI's own reply, so a hallucination once got saved as a fact. The fix was one line with a big principle: extract facts from the owner's words only — never the AI's. A 50-second web search that kept "failing." The Opportunity Scout timed out under a global 30s cap. A per-request 90s timeout plus 10-minute caching fixed it. (Bonus: an MCP server that hung because a console.log was polluting the JSON-RPC stdout stream — diagnostics now go to stderr.) Accomplishments that we're proud of Shipped a real, live product solo — kredex.xyz , deployed on Alibaba Cloud, not a prototype. A memory engine that's both fast and truthful — the two-tier design means exact facts never drift and are never guessed, while fuzzy knowledge is still recalled by meaning. One tool registry, two front-ends — the same tools power the in-app Qwen agent and a standards-based MCP server, so Kredex is a reusable memory backend, not a walled garden. Genuinely inclusive — it works in English and Nigerian Pidgin, and across text, receipt photos, and voice. Turned a six-year-old idea into something you can use today. What we learned The engineering is the glue, not the model. The intelligence is a handful of Qwen API calls; the product is everything around them — routing, memory design, tool orchestration, and resilience. Memory is an architecture decision, not a database. Splitting exact facts from fuzzy narrative made the app both faster and more truthful than any single store could be. Qwen lowered the barrier dramatically. Being OpenAI- and Anthropic-compatible meant I brought my existing skills; the generous free tier meant I could experiment without fear. It made a solo build of this scope genuinely feasible. What's next for Kredex WhatsApp as the front door — most owners already live there; the agent loop is channel-agnostic, so it's a connector, not a rewrite. Proactive nudges — "you're low on garri, and Alhaji Musa delivers Tuesdays — want me to draft the order?" Voice-first mode , end-to-end, for owners who'd rather talk than type. Shared memory for cooperatives — many shops, one knowledge base. Every feature in Kredex traces back to a conversation my dad and I had six years ago about the traders in our community and the dignity of tools that actually fit their lives. He didn't get to see it built. I did — with Qwen's help — and I intend to bring it fully alive. Dad, this one's for you. 🧡 <div