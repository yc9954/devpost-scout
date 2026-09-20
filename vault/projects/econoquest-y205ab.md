---
slug: "econoquest-y205ab"
url: "https://devpost.com/software/econoquest-y205ab"
title: "EconoQuest"
hackathon: "Hackonomics 2026"
organization: "hackonomics"
winner: true
words: 1049
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# EconoQuest

> Govern a nation. Live with the consequences.

[Devpost](https://devpost.com/software/econoquest-y205ab) · hackathon [[Hackonomics 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[civic_government]] [[education]] [[finance_payments]] [[housing_homeless]] [[labor_employment]]
**user** [[educator_student]] [[general_public]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** authentication, fastify, groq, huggingface-spaces, javascript, jwt, langchain, llama-3.3-70b, node.js, pgvector, python, react, supabase, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for econoquest

## Body

Landing page Nation Selection Playground Report (final Summary of your changes) Hall of Fame Login page Register Page EconoQuest — Hackonomics Submission Inspiration Economics education has a fundamental problem: it teaches consequences by description rather than by experience . You can read that printing money causes inflation. You can memorize the Weimar Republic. But you don't feel it until you've made the choice yourself — and watched your currency collapse two rounds later. EconoQuest exists because the best way to understand compound causality — where early decisions constrain your options for years — is to live with it . No lecture captures what it feels like to face a 24% inflation rate and realize that your money-printing policy from three rounds ago is the reason salaries can no longer keep up. What It Does EconoQuest is a browser-based economics simulation where players govern a nation across 7–8 fiscal years , making real policy decisions and living with the consequences. Each Round Adjust 8 policy levers : Tax rates Interest rates Government spending R&D investment Tariffs Money supply Foreign lending Wealth fund risk The simulation engine then calculates 10 outcome metrics : GDP growth, inflation, unemployment, debt-to-GDP, currency strength, trade balance, innovation index, real salaries, citizen mood, and sovereign fund growth. The AI Advisor Players receive Socratic hints , powered by a full RAG pipeline. Each hint is retrieved against your actual game state from 99 knowledge chunks spanning 5 layers: Game mechanics Dangerous policy combinations Crisis playbooks Round strategy Historical analogies — Weimar, Volcker, Singapore, Zimbabwe The advisor asks pointed questions using your real numbers. It never gives answers. Game End Every run concludes with: An archetype (one of 7 possible) A wisdom score An AI-narrated mandate timeline reviewing every policy choice you made across the entire game How We Built It The entire architecture runs on free infrastructure . Fastify Gateway Handles authentication (same-domain cookie proxying, cross-domain WebSocket JWT), load balancing across two HuggingFace Spaces per service, LRU caching keyed by state hash and prompt version, and request queuing. RAG Pipeline Game state is embedded → pgvector in Supabase retrieves the most relevant knowledge chunks → a prompt is constructed with the retrieved context → Llama 3.3 70B via Groq streams the response over WebSocket. Conflict Detector Pure Python. Runs before the model, flagging dangerous policy pairs — money printing into high inflation, rate cuts with a weak currency — without burning a single token. Domain expertise as logic, not inference. React Frontend Fixed a batching bug where tokens arriving within the same millisecond collapsed the stream buffer. Solved by accumulating tokens directly into the messages array using an index ref, bypassing React's batching entirely. Archetype System 7 archetypes determined by pure logic — checks extreme conditions in priority order, at zero inference cost. Why streaming is 5 seconds, not 35: KV caching. Challenges We Ran Into The WebSocket streaming bug was the most subtle. Tokens from Groq arrived in bursts within the same millisecond — React's batching collapsed them, making the stream appear to not render at all. The fix: accumulate tokens directly into the messages array using an index ref, bypassing React's batching entirely. Cross-domain auth between the browser, WebSocket connection, and Fastify gateway required careful cookie proxying to avoid credential issues. The solution: same-domain proxying for the browser session, with a JWT passed in the WebSocket URL for the streaming connection. Writing 99 game-aware RAG chunks rather than generic economic ones. The advisor needed to know what printing money does at round 4 in EconoQuest specifically — not in a macroeconomics textbook. This required rethinking each chunk as a game-situated assertion rather than a standalone fact. Accomplishments We're Proud Of Situated RAG retrieval. The advisor mentions Weimar Germany because your inflation figure and money supply settings specifically matched that chunk — not because it was a random example. That quality comes entirely from how the 99 chunks were written, not from the model. The conflict detector. It runs in pure Python before any LLM call, catching dangerous policy pairs using domain logic rather than inference. It's faster, cheaper, and more reliable than asking the model to notice the same thing. Production-grade streaming on free infrastructure. Same-domain cookie proxying, cross-domain WebSocket JWT, LRU cache keyed by state hash, request queuing across two HuggingFace Spaces per service — zero cloud spend at demo scale, with an architecture that scales horizontally without changing a line of code. What We Learned RAG chunk design is everything. Writing chunks as game-aware assertions — "printing money at round 4 with inflation above 15% compresses real salaries within two rounds" — rather than general economic facts completely changed the character of the hints. The model doesn't know what EconoQuest is. The retrieved context tells it. The situated quality of the advisor comes from the knowledge base, not the model's training. The Socratic constraint was harder to enforce than expected. A capable model like Llama 3.3 70B wants to be helpful — and helpful usually means giving the answer. Getting it to ask a question that makes the player think harder , using their actual numbers, required more prompt engineering than anything else in the project. What's Next for EconoQuest Richer historical knowledge. The 99 knowledge chunks are a foundation, not a ceiling. Brazil's 1994 Plano Real, Japan's lost decade, the 2008 financial crisis, the post-COVID inflation wave — each historical period adds a new retrieval layer. A deeper simulation engine. More variables: housing markets, inequality indices, political capital as a resource that fiscal choices gradually deplete. Global leaderboard & competitive play. Every mandate is ranked against the global community using a weighted scoring formula — raw economic performance multiplied by nation difficulty. To climb the rankings, you can't just play it safe: you have to stabilize the world's most volatile economies. This turns a solo learning tool into a competitive platform with built-in replay motivation. Classroom integration. The highest-impact near-term addition — weekly simulations where students compare mandate timelines, debate each other's policy choices, and build economic intuition collaboratively rather than alone. A full debrief mode. The end-game advisor review could become a longer session drawing on the complete mandate timeline to generate personalized insight into how the player thinks about risk, growth, and stability tradeoffs. Not a score. A mirror. <div