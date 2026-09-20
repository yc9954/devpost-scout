---
slug: "clatri-ved84t"
url: "https://devpost.com/software/clatri-ved84t"
title: "Clatri - Your AI agent for everything"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 1487
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Clatri - Your AI agent for everything

> Control and unify your finances with the speed of a message

[Devpost](https://devpost.com/software/clatri-ved84t) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: transportation</sub>
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** flutter, railway, revenuecat, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clatri

## Body

Inspiration The idea for Clatri came up when my girlfriend told me she wanted to start saving money. She began by recording her expenses in her WhatsApp chat and exporting them as CSV files to ChatGPT so it could do the math for her. I told her I could build an app that solved that problem in a month. She laughed and said I was exaggerating, since I had already spent over a year and a half building Gurwi, the app that I built with my partner Jonnier. From that moment, the idea of Clatri lived in me. I knew that with the current state of agentic frameworks and large language models it would be possible to build something like this, but at the time I was building Gurwi and couldn't abandon my main project halfway for a new idea. Everything changed when I saw that RevenueCat announced their new Shipyard hackathon. I saw it as the perfect opportunity to finally build Clatri. What It Does Clatri is a personal AI assistant you can chat with to organize your life. You send it a message or voice note and it takes care of recording, calculating, and showing you everything in a visual dashboard. For finances, you can tell it things like "I have 500 dollars in cash and a Bank of America account with 2,300" and it creates the accounts. If you later say "I spent 12 dollars on lunch", it automatically deducts it. It supports multiple currencies, so it works the same whether you're in Colombia, Brazil, Germany, or Japan. It also handles credit cards with their billing cycles, recurring subscriptions like Netflix or Spotify, debts you owe or are owed with interest calculations, savings goals, and even investments like CDs, stocks, or crypto. One thing I'm pretty proud of is document processing. You can upload a bank statement in PDF or a CSV with 120 transactions and in less than a minute it processes them all and updates your dashboard. For health, you can register chronic conditions like diabetes or allergies, medications with their schedules, temporary episodes like a flu, and metrics like weight or blood pressure. The idea is that you never lose a medical authorization again or forget which medication helped you last time. For personal growth it has tasks, habits with Duolingo-style streaks, a unified calendar where you see your events alongside your debt payment dates, bookmarks to save URLs, and a journal for reflections. What sets Clatri apart from other apps is that everything works through conversation. You don't have to navigate menus or fill out forms. You just talk to it like a friend who helps you organize your life, and it executes actions and shows you visualizations in real time as it responds. How We Built It The frontend is in Flutter so it works on iOS, Android, and Web with the same codebase. I use BLoC to manage state and GoRouter for navigation. The most complex part was implementing chat streaming: the backend sends events in real time (Server-Sent Events) and the frontend renders them as they arrive, with a 50ms throttle so the UI doesn't stutter. The backend is in Python with FastAPI. The heart of it is a multi-agent system using the OpenAI Agents SDK. It works like this: there's a main orchestrator agent that receives the user's message and decides which specialist agent to delegate it to. I have a MoneyAgent with over 190 tools for everything financial, a HealthAgent for health, a MyselfAgent for personal stuff, and a WebSearchAgent that can search the internet when it needs updated information. Each agent has its own tools that interact directly with the database. For example, the MoneyAgent has tools like create_account, register_transaction, create_credit_card, calculate_debt_interest, and so on. When the user says "I spent 50 on a taxi", the orchestrator detects it's financial, delegates to MoneyAgent, and it executes register_transaction with the right parameters. For LLMs, I implemented a fallback chain that supports OpenAI, Anthropic, Google, DeepSeek, and Qwen. If the primary model fails due to rate limit or error, it automatically tries the next one. The user doesn't even notice. The database is on Supabase with PostgreSQL. I have 6 separate schemas with over 50 tables. Everything uses Row Level Security so each user can only see their own data. Monetization is integrated with RevenueCat. I have three subscription plans that give monthly credits, plus credit packs to buy separately. Every time the agent responds, I calculate how many tokens it used, convert it to cost in dollars, and deduct the corresponding credits. Challenges We Ran Into The biggest challenge was understanding how finances actually work. It sounds simple: "track income and expenses". But when you start implementing, you realize credit cards aren't simple accounts—they're debt instruments with billing cycles, cutoff dates, interest rates that are calculated in weird ways. I had to research how compound interest works, the difference between accrued income and cash flow, how to handle multi-currency accounts like Wise where a single account has pockets in different currencies. Another challenge was token economics. Each model has different costs, and when you use a fallback chain, you have to track exactly how many tokens each one consumed. Plus, I had to balance the generosity of the free trial with business viability. I ended up building a system that tracks tokens in real time during streaming and deducts credits from the right source (first from subscription, then from purchased credits, then from trial). LLMs also gave me headaches. Sometimes they hallucinate and say they executed an action when they didn't. I implemented a detection system where a secondary model verifies write actions against the actual database state. If it detects inconsistency, it retries with a corrective prompt. Streaming was harder than I expected. I had to implement throttling in Flutter so it wouldn't stutter with so many updates, handle clean cancellations without memory leaks, and show tools executing in real time without overwhelming the user. Accomplishments That We're Proud Of I'm proud of the credits system because it works exactly as I imagined: tracks every token, calculates costs per model, deducts in real time, and it's all transparent to the user. Also of having tested practically every accessible LLM to find the right balance between intelligence, speed, and cost. The 80+ financial tools took me weeks but they were worth it. The agent can handle multi-currency accounts, calculate credit card interest, track debt amortization, savings with compound interest, investment portfolios, and process bank statements with OCR. Launching with 8 languages from day one also makes me proud. English, Spanish, Portuguese, German, Japanese, Korean, and Chinese. Including translations of all database enums. And the dashboard that updates in real time as you chat. There are 14 different widget types: KPI cards, charts, bank accounts, credit cards, GitHub-style habit calendars. All dynamically rendered based on what the agent responds. What We Learned I learned that personal finances are way more complex than they seem. "Balance" means different things depending on context. Multi-currency requires careful decimal precision. Interest calculation has a thousand variations. I learned that agentic systems need guardrails. LLMs are powerful but they hallucinate, so you need to verify their actions. Tool execution order matters for data integrity. And users need to see what the agent is doing to trust it. I learned that streaming UX is hard. Partial responses need graceful rendering. Cancellation has to be clean. Errors need clear communication. RevenueCat simplified monetization a lot for me. Subscription logic is complex (trials, grace periods, billing retries) and they handle all of that. I only had to implement the webhook and credit deduction. And I learned that building with entity separation from the start pays dividends. Personal and business finances are completely separate. Sharing entities between users is possible. RLS secures everything at the database level. What's Next for Clatri In the short term, I'm going to launch an anticipation campaign on social media to drive pre-registrations in the app stores. Launch is planned for April. I'll create YouTube tutorials showing how to use each feature and complement Gurwi's financial education with Clatri's practical tracking. After launch, I want to position the app in the Hispanic and English-speaking markets, run ads based on initial user feedback, and keep iterating based on what users ask for. Long term, the goal is to integrate Open Banking. I want to start with the most popular banks in the countries where Clatri has the most users, so transactions sync automatically and users don't have to log everything manually. I also want to build integrations with external tools like Google Calendar, to strengthen the agent's capabilities and fulfill its purpose of being the AI agent for everything. The name Clatri comes from our philosophy: " Cla rity Tri ples Results". When people have clarity about their finances, health, and personal growth, they make better decisions. That's the vision. <div