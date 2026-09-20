---
slug: "haven-dn65lq"
url: "https://devpost.com/software/haven-dn65lq"
title: "HAVEN"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 910
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/simulation_digital_twin"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/general_public"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# HAVEN

> Facing eviction in England? HAVEN checks if your notice is even legal, shows how much time you have, and tells you exactly what to do next — based on the most recent law as of 1st May 2026.

[Devpost](https://devpost.com/software/haven-dn65lq) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[simulation_digital_twin]]
**domain** [[housing_homeless]] [[labor_employment]] [[legal_justice]]
**user** [[general_public]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** api, claude, concurrently, css, express.js, git, github, groq, javascript, json, llama-3.3-70b, node.js, npm, outfit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for haven

## Body

Same question, two answers. ChatGPT treats the S21 as valid. HAVEN flags it as illegal — abolished 1 May 2026. A stressed renter types in plain English. HAVEN extracts the facts, asks only what it needs, then confirms before any verdict. Maps the eviction process, counts down to the 56-day council window, and gives 3 steps ordered by your specific urgency. Won't draft until all 5 facts are supplied. Produces a letter asserting the duty owed now — you review, edit, and send it. Options ladder, CRF eligibility check, jargon decoder, landlord message, phone script, packet — all built around your case. HAVEN maps your options and the law. It won't tell you whether to stay or leave — that choice is always yours to make. Inspiration In May 2026, England's Renters' Rights Act abolished Section 21 "no-fault" evictions overnight — and almost no renter understands the new rules. The people who lose their homes usually aren't the weakest cases; they're the ones who wait too long, never knowing their council legally owes them help 56 days before homelessness. Here's the part that got us into building this: today's AI models still confidently describe the old, abolished law as current. LLMs are trained on years of past internet text, so they default to what used to be true. Ask a general chatbot "I got a Section 21 notice, do I have to leave?" and it may say yes — when that notice is now invalid. For someone facing eviction, that single outdated answer can mean packing up a home they had every right to stay in. A new law, frightened people, and an AI that defaults to the wrong answer — that's the gap HAVEN closes. What it does HAVEN is a calm, plain-English navigator for renters in England facing eviction. Tell it what's happening and it: Checks your notice against current law — after you confirm the key facts. Maps your timeline with a live countdown to the 56-day council-help window. Gives a tailored 48-hour plan , ordered by your urgency. Builds a council-duty letter toolkit: the letter, document packet, phone script, talking points, and a "what happens next" simulator. Prepares a briefing for a human adviser , then hands the decision back to you — it never decides, and never contacts anyone for you. A persistent handoff bar always routes you to the right human — Shelter, Citizens Advice, your council, or the Domestic Abuse Helpline. How we built it React + Vite frontend, a minimal Express proxy to Groq's Llama-3.3-70B. One principle: don't trust the model with what it's bad at. Grounding: an era-override prompt tells the model its training is outdated, and a verbatim knowledge base of the new law is the source of truth. Determinism: the 56-day clock is computed in code, never by the LLM. Reliability: one focused JSON call per output, with defensive parsing so a bad response never breaks the screen. Human-in-the-loop by design: verify-before-verdict, a gate that refuses to draft without your facts, and a final decision-handback. A self-test harness proves the model never reverts to old law. Challenges we ran into The model "knew" the old law too well — it kept slipping into Section 21 language. We fixed it with the era-override, the ground-truth knowledge base, and tests that fail if old law leaks through. Hallucinated dates — so we moved all date math into code. Tone under stress — every line had to stay calm and never overstep into legal advice. Free-tier reliability — rate limits and bad JSON could break the demo, so we added retry fallback and defensive parsing. Accomplishments that we're proud of An AI that stays correct about a law it was never trained on — and proves it with tests. Responsible-AI by design: it flags assumptions, frames everything in confidence terms, refuses to guess, and hands the decision back. The council-duty letter toolkit — turning a vague legal right into a letter, a script, and a plan to push back if you're wrongly turned away. It's calm — the hardest and most important thing to get right for a tool about eviction. What we learned Grounding beats cleverness — constrain the model to a source of truth and do the deterministic parts in code. The responsible move is often less automation — the best features are where HAVEN deliberately doesn't act. Trust is a UX problem — confidence framing and visible assumptions did more than any single answer. What's next for HAVEN Stronger model — swap in a paid-tier model for higher reliability, then deploy a publicly hosted version anyone can reach without setup. Document upload — photograph or upload a notice and have HAVEN read the dates, notice type, and grounds directly, removing the need to type them. Save & resume — lightweight login so users can return to their case as it develops, with session memory and an updatable letter toolkit. Deliberately absent from v1 to avoid storing sensitive data without proper consent flows. More nations and tenures — extend coverage to Wales, Scotland, and social housing, each with their own legal frameworks and notice rules. Printable toolkit — export the full council-duty letter, document checklist, and phone script as a single PDF the user can take to an appointment. Adviser partnerships — direct handoff into Shelter or council intake systems, so HAVEN's output becomes the starting point for a real case rather than something the user has to re-explain. <div