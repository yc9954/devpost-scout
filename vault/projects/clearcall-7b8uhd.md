---
slug: "clearcall-7b8uhd"
url: "https://devpost.com/software/clearcall-7b8uhd"
title: "ClearCall"
hackathon: "United Hacks V7"
organization: "Hack United"
winner: true
words: 1110
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/revocation_withdrawal"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ClearCall

> A public referee knowledge network where users share real game incidents, make structured calls, compare similar plays, and learn from expert rule-backed discussion.

[Devpost](https://devpost.com/software/clearcall-7b8uhd) · hackathon [[United Hacks V7]]

## Facets

**mechanism** [[provenance_signing]] [[revocation_withdrawal]] [[simulation_digital_twin]]
**domain** [[accessibility]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** css, eslint, html5, intersection-observer, javascript, next.js, node.js, playwright, postgresql, react, supabase, tailwind-css, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clearcall

## Body

Homepage Inspiration Every soccer match is filled with split-second decisions, and one whistle can change the outcome of a game. But referees have almost no way to practice those high-pressure moments outside of live matches. Players get thousands of repetitions in training. Officials get their reps in front of crowds, coaches, and real consequences. The existing options are all passive: watching VAR breakdowns, reading the Laws of the Game, or scrolling debate threads where nobody actually has to commit to anything. We wanted to build the opposite. A place where you have to make the call first, and only then see how the community, verified referees, and the actual rules judged the same play. What it does ClearCall is a social-style case network for officiating decisions. Incident feed : a continuous feed of real game incidents as video, image, or text scenarios, filterable across ten foul categories (handball, serious foul play, DOGSO, offside interference, advantage, simulation, and more). Each case carries a status badge ( Verified Ruling , Expert Consensus , or Open Discussion ) so you know how settled a call actually is. Structured decisions : instead of a hot take, you submit a structured call: the decision itself, a 0 to 100 confidence rating, and the specific rule factors that drove it (point of contact, ball position, denial of an obvious opportunity, etc.). Reveal after commit : only after submitting do you see three vote distributions side by side: the full community, verified referees only, and fellow learners. The gap between them is the lesson. Immutable first attempts : you can revise a call after reading the discussion, but your initial answer is preserved forever. Calibration is measured against what you believed under pressure, not your edited history. Teaching contrasts : a similarity engine surfaces near-identical plays with different correct outcomes and highlights the exact factors that flipped the decision. This targets where officials actually fail, which is the edges between rules, not the rules themselves. Expert discussion : threaded responses anchored to rule citations, with pinned verified explanations and factor-level agree/disagree reactions. Learner profiles and personalization : accuracy by category and difficulty, a calibration score that detects overconfidence (high-confidence errors are tracked explicitly), streaks, and a personalized feed weighted toward your weakest categories and highest-disagreement cases. Case publishing : a full authoring flow for submitting new incidents with structured factors, rule paths, media provenance, and explicit permission status. New cases enter a pending expert review state. Trust by design : every seeded distribution and demo comment is explicitly disclosed in the UI as demonstration material, never presented as official rulings or live community data. How we built it Stack: Next.js 16 (App Router) · React 19 · strict TypeScript · Tailwind CSS 4 · Supabase (Postgres, Auth, Storage, RLS) · Vitest · Playwright · Vercel Frontend. Next.js 16 App Router with React 19, fully strict TypeScript, and a discriminated text | image | video media model. The feed uses cursor-style progressive loading with an IntersectionObserver sentinel plus a manual load-more fallback. The design system is a custom paper/ink/field-green/signal-yellow token set with an editorial serif for case prompts. We built it against WCAG 2.2 AA: keyboard-complete filters and forms, visible focus, reserved media dimensions, reduced-motion support, and no nested interactive link traps. Backend. Supabase Postgres with row-level security across profiles, answers, votes, and discussion. Live vote distributions are computed server-side in a get_case_vote_distribution Postgres function and split into community vs. verified-referee breakdowns. That means real aggregation, not client-side math, with a clean fallback to disclosed demo distributions when there are zero votes. Six migrations cover the relational schema, backfill, function hardening (revoked trigger execution, secured search paths), media storage policies, and immutable preservation of initial answer attempts at the database layer. Algorithms (all unit-tested in Vitest): Similarity scoring uses a weighted Jaccard across case attributes: $$S = 0.35\,J_{factors} + 0.20\,J_{rulepath} + 0.15\,C_{context} + 0.15\,P_{difficulty} + 0.15\,D_{disagreement}$$ Teaching contrast selection takes the similarity score and adds a $+20$ bonus when the recommended outcomes differ, then extracts the top three factor differences with the critical factor ranked first. Calibration is a Brier-loss-based score computed against locked first attempts, mapped to labels from "Well calibrated" to "Overconfident." Reputation is a 0 to 100 score: $$R = 0.40\,(\text{verified agreement}) + 0.25\,(\text{reasoning quality}) + 0.20\,(\text{helpful votes}) + 0.15\,(\text{calibration})$$ Feed personalization weights weakness at 0.35, interest at 0.20, disagreement at 0.20, difficulty fit at 0.15, and freshness at 0.10. Quality gates. Typecheck, ESLint, the full Vitest suite, a production build, and Playwright checks across desktop and mobile viewports. Challenges we ran into Making commitment feel fair. Locking a first attempt while still allowing revision took careful schema design. We ended up preserving the initial attempt immutably in Postgres with a revision counter, so learning metrics stay honest without punishing people for changing their minds. Live vs. demo data honesty. A hackathon demo has seeded content, and we refused to fake liveness. Every distribution carries a basis and isSynthetic flag that surfaces as a disclaimer in the UI, and live Postgres aggregation transparently takes over as real votes come in. Teaching contrast quality. Naive similarity returned "related" cases that taught nothing. Restricting eligibility to same-category cases, weighting factor overlap heaviest, and bonusing outcome flips finally produced comparisons that explain why two near-identical plays get different calls. A social feed that isn't a doomscroll. Split evidence/discussion cards, honest end-of-catalog states instead of fabricated infinite content, and focus-preserving filters keep ClearCall a study tool that just happens to feel like a feed. Accomplishments that we're proud of A complete commit → reveal → compare → calibrate learning loop, not just another quiz app. Server-side vote aggregation with role-split distributions behind RLS. Database-enforced immutability of first attempts. You can't rewrite your own history. An explainable similarity engine that shows its reasoning to the user ("Selected because both cases cover handball but differ in point of contact and ball position"). Being radically honest about demo content in a category (sports rulings) where faking authority would have been easy. What we learned Structured disagreement teaches better than consensus. The most valuable screen in the app isn't the expert answer. It's the moment you see verified referees split 60/40 on a call you were 95% confident about. Designing for that moment shaped everything else: locked first attempts, reveal after commit, and contrast-first comparison. What's next for ClearCall Expert reviewer onboarding and a verification pipeline for real officiating educators Permissioned video uploads with moderation and provenance workflows More sports, since basketball, football, and hockey share the same case/factor model Spaced-repetition resurfacing of your high-confidence errors League and referee-association cohorts with private case libraries Don't just watch the game. Make the call. <div