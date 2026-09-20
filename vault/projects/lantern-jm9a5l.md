---
slug: "lantern-jm9a5l"
url: "https://devpost.com/software/lantern-jm9a5l"
title: "Lantern"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 3146
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Lantern

> A language dies every two weeks. Lantern is Duolingo for dying languages: it turns the words a community still remembers into a real course, with AI that never invents a word.

[Devpost](https://devpost.com/software/lantern-jm9a5l) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[provenance_signing]] [[retrieval_grounding]] [[structural_withholding]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[finance_payments]] [[scientific_research]]
  <sub>weak: civic_government</sub>
**user** [[educator_student]] [[researcher]] [[social_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** anthropic-sdk, cobe, framer-motion, groq, llama-3.3-70b, mongodb, next.js, react, tailwindcss, typescript, vercel, web-speech-api, zod

## How they structured the write-up

- inspiration
- the proof (live — anyone can verify it right now)
- what it does
- how we built it
- accomplishments we're proud of — and we measured it
- why this is "ai that actually helps people"
- what we learned
- what's next
- 1. architecture at a glance
- 2. request lifecycle (a learner opening a language)
- 3. the anti-hallucination guardrail, in full
- 4. frontend
- 5. backend
- 6. data layer
- 7. authentication
- 8. infrastructure and hosting
- 9. reliability engineering
- 10. the build history (how we got here)
- 11. engineering challenges and how we solved them
- 12. ethics and community data sovereignty

## Body

Lantern: civic infrastructure for the city of tomorrow, keeping its languages alive. How it works: the AI amplifies a community's own words, and a code guardrail discards any word real speakers never said. Proof, not a promise. Live at /api/metrics: 0 hallucinated words, 48/48 vocab cited, 7/7 practice sentences pass. One TypeScript codebase, client, API, the induction engine and its guardrail, swappable AI providers, zero-config data. Inspiration Most "AI" you see is pointed at making something faster or flashier. We wanted to point it at one of the most human problems there is: a language goes silent somewhere on Earth about every two weeks, and the people losing theirs are overwhelmingly Indigenous and marginalized communities who already have the least support. We kept picturing one person — a grandparent who still dreams in a language their grandchild was never taught, one of the last in the family who can speak it. Her language has no app and no course, not because no one cares, but because writing a language down and teaching it has always taken trained experts years, and most languages will never get that time. We wanted to put that power in the hands of the person who actually holds the words — not a researcher, not a company. So we built Lantern: AI that actually helps a person keep their own language alive, and that a non-expert can use on their phone. The proof (live — anyone can verify it right now) Every number below is recomputed on each request at https://lantern-cyan.vercel.app/api/metrics . It is not a screenshot. Hallucinated words that ever reached a learner 0 zero. always. enforced in code by guardrail.check.ts |__________________________________________________ Vocabulary with a real, cited source 48 / 48 ############################## 100% Practice sentences passing the attestation gate 7 / 7 ############################## 100% How Lantern differs from a normal "AI tutor": +------------------------------+-------------+--------------------+ | | Generic AI | LANTERN | +------------------------------+-------------+--------------------+ | Invents words to fill gaps | yes | forbidden in code | | Cites a real source per word | no | 48/48 (100%) | | Works for ~50-speaker langs | barely | built for it | | Proves its honesty live | no | /api/metrics | | Demo locked behind sign-in | often | never -- fully open| +------------------------------+-------------+--------------------+ What it does Lantern is Duolingo for languages that are dying. Pick a language so endangered that no app, no textbook, and no online course exists for it. Lantern takes a handful of remembered phrases, works out the grammar hidden inside them, and builds a real course you can actually learn from: flashcards with the word, the meaning, and pronunciation you can hear out loud; the grammar it discovered, explained in plain language (for Māori, how a small word before the verb changes past, present, and future); a vocabulary bank where every word shows the phrase it came from; and a Contribute button: add one phrase you remember, like Ka pai ("good"), and the whole course rebuilds itself, richer, in seconds. It comes pre-loaded with eight endangered languages; two of them — Māori and Cherokee — are fully learnable right now. The whole thing works on a phone, and a stranger understands what it does in one sentence. Try it live at https://lantern-cyan.vercel.app — watch it learn Māori from 41 phrases, see the grammar it found, and take the course it built. The one rule it never breaks is the most important part: it only ever teaches words a real speaker actually said. An AI can't truly know a language with fifty speakers, so instead of letting it make things up, Lantern only reorganizes and teaches the community's own words — and a check built into the code throws away any sentence containing a word nobody actually used. How we built it The anti-hallucination pipeline, end to end: community corpus (only real, cited phrases) | v tokenize + normalize one canonical, case-folded pass | v induce grammar + vocab Llama 3.3 70B on Groq | v [ GUARDRAIL: CITE or REJECT ] is each candidate word attested? | | yes| no|-----> DISCARDED (never reaches a learner) v course: SRS flashcards + grammar notes + in-browser audio If the model is ever unreachable, the engine fails soft to a hand-verified fixture, so Contribute never throws and the demo stays honest and online. A web app in Next.js 16 + TypeScript, deployed on Vercel, so it runs on any phone or laptop with no install. An AI induction engine that reads only the phrases it's given, lines up each word with its meaning, and spots grammar by comparing similar phrases. We force the AI to return clean, structured data and double-check it with Zod before anything is shown. A no-hallucination guardrail written directly into the code: every sentence is split into words and each is checked against the real vocabulary; if even one word was never actually said, the sentence is deleted before any learner sees it. A flashcard course on the SM-2 spaced-repetition algorithm with in-browser text-to-speech so you can hear the words. Live AI runs an LLM — Llama 3.3 70B on Groq, driven through the Anthropic SDK — with a hand-verified backup so the demo always works. Accomplishments we're proud of — and we measured it We didn't just want to say it helps and that it's honest, so we measured it: FROM 41 MĀORI PHRASES, LANTERN BUILT ────────────────────────────────────────────── 34 words you can learn, each one real and cited 5 grammar patterns it discovered on its own 12 flashcards on a smart review schedule ────────────────────────────────────────────── 0 made-up words ever shown to a learner ✓ 48/48 words backed by a real source ✓ 7/7 practice sentences pass the honesty check ✓ Reproducible live at GET /api/metrics. So: zero made-up words ever reach a learner, enforced by the code, not just a promise; it's genuinely clear; the interface is warm and easy so you never feel lost; and it's real and live, not a slideshow — the AI runs on the actual website. And we built it to production quality, measured on the live site: Lighthouse (every page, production) Accessibility ########## 100 Best Practices ########## 100 SEO ########## 100 Performance ########## ~100 (LCP 241ms, CLS 0.00) Worked example -- the guardrail rejecting an invented word: a model asked about Maori water-spirits will gladly produce "taniwha" lessons. But if "taniwha" is not in THIS community's corpus, Lantern discards it on screen, live, in the induction demo. The learner only ever sees words a real speaker actually said. Why this is "AI that actually helps people" It solves a real, human problem for real people — not a demo, a tool a community can use today. It's usable by a non-expert: a grandparent, a kid, anyone who remembers a few words; no AI knowledge required. It's honest by design — the most respectful thing AI can do with someone's heritage is refuse to invent it. We made the AI do less, on purpose, and that's exactly what makes it trustworthy and genuinely helpful. What we learned That the most helpful AI is sometimes the one that does less. By refusing to invent, Lantern became something a whole community — and even a language expert — could trust, and trust is everything when you're handling someone's heritage. We also learned how much a clear, kind interface matters: the best technology does nothing if the person who needs it can't use it. What's next Real recordings from native speakers, a way for fluent speakers to review and approve lessons, printable booklets for communities without good internet, and controls so each community fully owns and governs its own words. The dream is a living library with a place for every endangered language, where anyone who still remembers can help bring theirs back — starting today. Technical deep dive — the whole system, end to end This is the complete engineering account of Lantern: every layer, every decision, every fail-safe, and the history of how it was built. The sections above are the "why." This is the "how," in full. 1. Architecture at a glance Lantern is one Next.js 16 application (App Router, React Server Components, Turbopack) written end to end in TypeScript. There is no separate backend service: server logic lives in Server Components and Route Handlers on Vercel's Node runtime, right next to the UI that consumes them. THE BROWSER (any phone or laptop) +-----------------------------------------------------------------+ | React Server Components (streamed HTML) + small client islands | | Hero . LiveInduction . Workspace . Flashcards . ContributeForm | +----------------+--------------------------------+---------------+ | server-rendered | fetch() /api/* v v +-------------------------+ +------------------------------+ | Next.js 16 (Vercel Node)| | Route Handlers (/api/*) | | RSC data loading | | contribute induce audio | | layout pages metadata | | metrics stats auth/[...] | +-----------+-------------+ +--------------+---------------+ | | v v +-----------------------------------------------------------------+ | THE INDUCTION ENGINE (src/lib/engine) | | tokenize -> normalize -> induce(LLM) -> GUARDRAIL(cite|reject) | | -> attestation gate -> lesson assembly | +----+-------------+-------------+----------------+---------------+ v v v v +-------+ +---------+ +----------+ +-------------+ | Groq | | MongoDB | | Firestore| | Vercel Blob | | LLM | | Atlas | | users / | | pronunciation| |3.3 70B| | corpus | | auth | | audio (CDN) | +-------+ +---------+ +----------+ +-------------+ | | | | v v v v fixture in-memory graceful 503 fail-soft fallback fallback auth gating (storage off) Every external dependency has a fail-soft path. Nothing here can take the demo down. 2. Request lifecycle (a learner opening a language) 1. GET /lang/mi (Server Component, Vercel Node, force-dynamic) 2. getLanguageMeta("mi") -> record; unknown id -> notFound() -> 404 3. getStore() -> MongoDB Atlas (or in-memory if no URI) 4. store.getPhrases("mi") -> the cited corpus for this language 5. <Workspace> hydrates; Learn tab calls the engine 6. runInduction(corpus): tokenize + normalize every phrase (canonical, case-folded) LLM induces vocab + grammar FROM THOSE PHRASES ONLY Zod validates the LLM JSON (reject malformed shapes) GUARDRAIL drops any word not attested in the corpus assemble SRS cards + practice (attestation-gated) 7. The learner sees only words a real speaker said. Always. /api/metrics runs this exact path, so the honesty numbers are computed by the same code that builds lessons, not a separate flattering report. 3. The anti-hallucination guardrail, in full A normal model on a tiny corpus invents plausible words to fill gaps. For a 50-speaker language that invented word can outlive the last elder. We made it structurally impossible. Canonical tokenization: one tokenizer, one normalizer, case-folded, no stale copy anywhere (a project invariant). Two strings are "the same word" only after both pass through it. Cite-or-reject: every candidate word the model proposes is checked against the tokens that actually appear in the community's phrases. for each candidate word w: if normalize(w) in corpusTokens: KEEP (record its citation) else: REJECT (never reaches a learner) No confidence threshold, no "probably fine." 100% citation coverage is not a metric we hope for; it is an invariant the code refuses to violate. Attestation gate on generated sentences: practice sentences are made by recombining known words; each is re-checked word by word, and if one token was never said, the whole sentence is deleted. That is why "practice sentences failing attestation" is always 0. Worked example -- rejecting "taniwha" corpus: 41 attested Maori phrases (no "taniwha") model wants to teach "taniwha" guardrail: normalize("taniwha") in corpusTokens? NO -> DISCARDED on screen learner sees only the 34 words the 41 phrases actually contain guardrail.check.ts runs the full induction over the shipped