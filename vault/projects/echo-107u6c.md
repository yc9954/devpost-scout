---
slug: "echo-107u6c"
url: "https://devpost.com/software/echo-107u6c"
title: "Echo"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 1092
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Echo

> I often feel overwhelmed by life's changes, but this app reminds me: You're not alone, proven with data, private by design. It's safe to share today!

[Devpost](https://devpost.com/software/echo-107u6c) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** docker, elasticsearch, fastapi, nanogpt-api, next.js, ollama, postgresql, python, qwen3.5-0.8b, sentence-transformers, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for echo

## Body

Inspiration Has anyone here had a thought they were too ashamed to say out loud? Most of us have. And most of us believe we're the only one who's ever had it. Intrusive negative thoughts are near-universal — but they feel uniquely isolating. Existing mental health apps don't solve this. Therapy has a waitlist. Talking to friends feels like a burden. Generic affirmation apps feel hollow. AI chatbots feel clinical and impersonal. There's no app that just shows you, with evidence, that other people have felt exactly what you're feeling right now — and what actually helped them. That's what Echo is. What it does You open Echo, tap the logo, and type what's on your mind. A few seconds later: "847 people have felt something like this." You scroll through their experiences — humanised, anonymised, real. Some of them found a way through, and left a note for you. No chatbot. No social feed. No clinical questionnaire. Just ambient proof that you're not alone. Core features: Thought submission — type or dictate a thought, submit it, and receive a count of how many others have felt the same, along with their humanised experiences as scrollable cards "What helped" — when users resolve a thought, they can optionally leave a note for others in the same situation. Shown verbatim, never paraphrased by AI — because misconstrued mental health advice is a real harm Breathing With Others — the home screen breathing animation responds to how many people shared thoughts in the same emotional space this week, creating a subtle sense of ambient co-presence Future You letters — after resolving a thought, users can write a short note to their future self, stored locally and resurfaced automatically if the same theme reappears Guardrails of Care — for risk-related themes (crisis, self-harm, etc.), a static safety resource block surfaces crisis helplines, rendered entirely client-side with zero logging How we built it Echo runs on a three-stage AI pipeline designed around a strict privacy constraint: raw thought text must never persist on any server, in any form. Stage 1 — Anonymisation The user's raw thought is sent over HTTPS to our FastAPI backend, where a self-hosted Qwen3.5-0.8B model (served via Ollama) strips personally identifiable information while preserving emotional specificity. "My boss FirstName at CompanyName undermines me" becomes "My [male name] at [tech company] undermines me." The raw text is discarded immediately — never written to disk, never logged. Stage 2 — Humanisation The anonymised text is passed to the NanoGPT API (qwen3.5-122b-a10b), which rewrites it as a natural, empathetic 50–60 word expression and classifies it into one of 30+ theme categories. This is the only form of the thought that ever leaves our server. Stage 3 — Semantic search The humanised text is embedded using sentence-transformers ( all-MiniLM-L6-v2 ) into a 384-dimensional vector and indexed in Elasticsearch. Cosine similarity search returns the closest matching thoughts from other users, paginated with search_after for efficient infinite scroll. The frontend is built in Next.js 16 with TypeScript and Tailwind CSS, mobile-first at 375px. Authentication is email and bcrypt only — no names, no DOB, nothing else. Personal history and raw thought text are stored exclusively in localStorage , client-side encrypted with AES-GCM, and never uploaded. Challenges we ran into The hardest architectural decision was holding the privacy line at every step. It's easy to accidentally log a request body for debugging, or pass the wrong variable to an external API. We had to build middleware that explicitly blocks request body logging in all environments, enforce that the anonymiser is always the first service called, and verify that Elasticsearch documents contain zero user-identifying fields. Getting the breathing animation right was also harder than expected. The animation needed to feel emotionally meaningful — not just a spinner — and respond subtly to co-presence data without being distracting. We ended up with 9 layered SVG paths using Catmull-Rom interpolation, driven by requestAnimationFrame , with 5 distinct presence levels mapped from Elasticsearch weekly aggregate counts. The "what helped" verbatim storage decision created a constraint on the UX: we couldn't let AI touch resolution text after anonymisation. That meant designing a submission flow that felt natural while making it clear the user's words would be shown exactly as written. Accomplishments that we're proud of The privacy architecture is something we're genuinely proud of. We designed for the worst case: assume the entire infrastructure is breached. Even then — an attacker gets email addresses linked to emotional theme categories, and a dataset of humanised anonymous thoughts with zero user linkage. They cannot read what any individual wrote. They cannot link thoughts to people. That constraint shaped every decision we made. The count reveal moment works. Watching the number tick up to "847 people have felt this" — even in testing — lands differently than we expected. That's the thesis statement of the whole product made visible. The "what helped" flow is the feature we believe in most. The dataset grows every time someone gets better and decides to share it. The advice is specific, human, and unfiltered by AI. That specificity is the whole point. What we learned Building under a strict privacy constraint is a design superpower, not just a limitation. Every feature we couldn't build because of the privacy model forced us toward a better alternative. We couldn't store personal history on the server — so we built it client-side, which means it's actually private. We couldn't log sentiment trends per user — so we built aggregate counts per theme, which turned into the co-presence breathing feature. We also learned that the emotional design of a waiting state matters. The 2–3 second breathing animation during processing isn't wasted time — it's the moment users feel the weight of what they just shared. Shortening it or replacing it with a spinner would have been the wrong call. What's next for Echo We want to grow the dataset. The more people use Echo, the more useful it becomes — and the more resolution notes accumulate, the more powerful the "what helped" feed gets. Seeding it with real anonymised experiences, and building the delayed opt-in prompt that nudges users to share what helped after 3 weeks of silence, are the next priorities. On the technical side, we're exploring fine-tuned embeddings trained specifically on emotional language, which we believe would improve match quality significantly over a general-purpose sentence encoder. Longer term: a native mobile app, push notifications for the delayed resolution prompts, and expanding the Guardrails of Care feature with localised crisis resources by country. <div