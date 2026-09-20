---
slug: "memact"
url: "https://devpost.com/software/memact"
title: "Memact"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 903
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/web_dom"
---

# Memact

> Let your identity live in one place.

[Devpost](https://devpost.com/software/memact) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** access, context, contracts, github, javascript, memory, node.js, react, sdk, supabase, vite, wiki

## How they structured the write-up

- inspiration
- what it does
- how it works
- what exists now
- why this matters
- challenges
- what i learned
- what's next

## Body

Inspiration I started Memact because apps know things about us, but we usually do not get a clear place to see it. A shopping app may guess what you like. A fitness app may ask the same setup questions again. A music app may build a taste profile quietly. An AI assistant may keep asking for the same background. Every app builds its own little version of you, and most of that version is hidden, hard to correct, and stuck inside that app. Memact is my attempt to make that visible. The idea is simple: see what apps know about you and control it. Apps should adapt to people. People should not rebuild themselves inside every app. What it does Memact gives users a place to review the memory apps want to use or add. An app can ask for consent. After access is approved, the app can suggest memory such as a food restriction, a reading preference, a preferred username, a fitness goal, or a style preference. The user can accept it, edit it, reject it, delete it, or change who can use it. Apps do not get the full user memory page. They only get the memory categories the user allowed. Memact also supports app input that is not already clean memory. For example, an app may send specific app activity or evidence. Memact Context can shape that into a user-readable memory suggestion. The user still decides whether it becomes accepted memory. Activity is not identity. A click, a skipped song, a workout, or a one-time purchase should not become a permanent claim about someone. How it works The current product loop is: an app asks first Access checks the app, user connection, scopes, categories, and revocation the app suggests memory or sends specific app details Context shapes messy app input into readable memory suggestions Yourself shows the user what apps know or want to remember the user accepts, edits, rejects, deletes, or changes visibility Memory stores what survives SDK lets apps read only allowed memory The Website is the portal for users and developers. Users see Yourself, posts, settings, app access, and help. Developers register apps, create API keys, read setup instructions, and use the SDK. What exists now Memact has working repos for Website, Access, Context, Wiki, Memory, Contracts, and SDK. Access handles API keys, consent, scopes, categories, app connections, memory suggestions, allowed memory reads, credits, and audit-style records. Context is the open-source category layer. Contributors are adding categories such as news articles, productivity, food delivery, creator tools, and AI assistants. A fitness category is now needed for NutriPlan Lite. Memory supports CRUD and RAG-style retrieval for accepted memory. I also added a future-ready task context packet system so Memact workers can help with small tasks without seeing a full profile. Contracts defines shared shapes such as app context proposals, Wiki entries, category schemas, memory summaries, SDK responses, and task context packets. SDK gives apps server-side helpers to suggest memory, send app activity, verify access, and read allowed memory. Why this matters This is not about making another chatbot or another AI wrapper. Memact is about giving apps better memory while giving users a place to see and fix what apps know. For a fitness app, this can reduce onboarding friction. If the user already approved fitness memory, the app can skip questions it already knows and ask only what is missing. If the user denies Memact access, the app still works normally. For AI agents, this solves a common problem: they often lack user background. Memact can provide only the small approved memory packet needed for a task, instead of dumping a full profile into a model. Challenges The hardest part was not code. It was staying honest about the idea. It is very easy to describe this with vague words like infrastructure, AI, context layer, or personalization platform. Those words make the product sound bigger, but they also make it harder to understand. The clearer version is this: Memact is where users see what apps know about them and control it. Another challenge was designing the permission boundary. Apps should not browse a full user Wiki. They should request a category, get only what is allowed, and leave a trail the user can understand. What I learned I learned that product clarity can change the whole architecture. Earlier versions had too many moving parts. Capture, Inference, Intent, and Playground made sense for experiments, but they did not match the simplest useful product. The current spine is cleaner: Access -> Wiki -> Context -> Memory -> SDK -> Apps. More accurately: App suggests memory or sends app details -> Access checks permission -> Context shapes it -> Yourself shows it -> user controls it -> Memory stores accepted memory -> SDK lets apps read allowed memory. What's next The next big test is making a real customer integration work. NutriPlan Lite is the first one. The goal is practical: if a user connects Memact, NutriPlan can reuse approved fitness memory like goals, diet preference, and restrictions. If enough memory exists, onboarding gets shorter. If memory is missing, NutriPlan asks only the missing questions and can propose those answers back to Memact for user review. The next technical step is a proper fitness Context category. After that, I want Memact to become the place people associate with one thing: See what apps know about you, and change it. <div