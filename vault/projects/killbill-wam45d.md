---
slug: "killbill-wam45d"
url: "https://devpost.com/software/killbill-wam45d"
title: "Killbill"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 827
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Killbill

> An agent that finds every recurring charge, judges which ones you actually use, and hands you the cancellation emails ready to send. You keep 100% of what you save.

[Devpost](https://devpost.com/software/killbill-wam45d) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[legal_professional]] [[small_business]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** jac

## How they structured the write-up

- inspiration

## Body

Inspiration Two months ago I noticed a $14.99 charge from a streaming service I hadn't opened in almost a year. That's $180 gone to a thing I forgot existed. When I checked the rest of my statement I found two more. The average American spends about $273 a month on subscriptions but estimates they spend $111. That $162 gap is just stuff you forgot to cancel. The kicker: the tools that already exist to fix this charge you a fee to cancel things. Rocket Money takes 30 to 40 percent of whatever they negotiate down for you. That felt backwards, so I built killBill: an agent that does the audit once, for free, and goes away. ##What it does You drop a year of bank statement CSV onto the page. killBill clusters the recurring charges, hands each one to an agent that decides whether to keep it, downgrade it, or cancel it, and for every cancel it drafts the actual email you'd send to the merchant. Subject line, body, where to send it. Copy, paste, done. The agent does not just flag charges. It reasons across the portfolio. When it told me to cancel Hulu the reason it gave was "you already pay for Netflix Premium." It had read my entire subscription list, not just that one line. When it told me to downgrade Adobe Creative Cloud it suggested the specific cheaper plan and the monthly delta. On the bundled 12-month sample (331 transactions, 12 recurring subs) it surfaces about $1,800 a year in savings end to end in under 90 seconds. ##How we built it The whole stack is Jac. The agentic core is one function: def analyze_one_subscription(...) -> str by llm(tools=[ enrich_merchant, judge_value, find_cheaper_alternative, draft_cancellation_email ]) Four typed tools are registered, the model picks the order itself for each subscription. There is no hand-written if-elif pipeline anywhere. Graph state (BankStatement, Subscription, KillRecommendation, CancellationEmail nodes) auto-persists on Jac's root graph across runs. The AuditStatement walker becomes a REST endpoint automatically the moment you run jac start audit.jac. No FastAPI, no route decorators. Inference runs on Featherless.AI (Qwen 2.5 14B Instruct) over LiteLLM's OpenAI-compatible route. The recurrence detection that feeds the agent is deterministic Python clustering. I wanted the LLM's job to be judgment, not pattern matching. The frontend is a single static HTML file that POSTs to the walker. Drag, drop, watch the savings counter animate up. ##Challenges we ran into The biggest one was a stack quirk. byLLM emits a response_format: {"type":"json_schema"} envelope for typed object returns, and Featherless's vLLM backend rejects it as malformed. The first three runs hung silently. The fix was to switch every typed-object tool return to a JSON-encoded string and reconstruct the object in Python. Same outcome, sturdier path. The probe script I wrote to detect this early is now committed to the sibling project. Second one: the 14B model occasionally rules Planet Fitness as "essential under $5" when it should be cancelled. The 72B model gets it right but takes three times longer and gets rate-limited under Featherless free tier. I shipped on 14B and accepted that the demo's most reliable cancel candidates are the duplicate streaming overlaps, not the dormant gym. Third: the agent's first drafts of cancellation emails were too apologetic. Took a few prompt iterations to get something that reads like a confident user, not a guilty one. ##Accomplishments that we're proud of Real money saved on a real-shaped statement, on free-tier inference, in under a minute and a half. The reasoning per subscription is specific enough to be trusted. When killBill says cancel Hulu, it shows you the Netflix line it noticed. The walker becoming a REST API with zero glue code is the kind of thing that makes you want to use Jac for the next project. The whole stack from CSV upload to drafted email to graph persistence works on a laptop with one env var set. ## What we learned Agentic loops want narrow tools. Four tools per agent invocation, called per subscription, is the sweet spot. Wide loops with five-plus tools and nested LLM calls inside each tool tend to hang on inference providers that don't fully support tool calling. The recurrence math doesn't need an LLM. Clustering by merchant and cadence is a 200-line Python function. Save the model for judgment. And: users trust a cancel recommendation about as much as they trust the reason behind it. The verdict alone is noise. The verdict plus "you already pay for X" is a decision. ##What's next for killBill Plaid connection so users don't have to download CSVs. A voice agent that actually places the cancellation call when the merchant doesn't accept email. A monthly recurring scan that runs in the background and pings you when a new sub appears. And eventually a flat $8 a month tier that beats Rocket Money's 30 to 40 percent take, because the math only works if we charge for the audit, not the savings. <div