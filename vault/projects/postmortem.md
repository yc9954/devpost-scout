---
slug: "postmortem"
url: "https://devpost.com/software/postmortem"
title: "PostMortem"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 1168
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# PostMortem

> The real-time anonymous retrospective that lets product teams finally say what actually went wrong — then commit to fixing it, publicly, with their name attached.

[Devpost](https://devpost.com/software/postmortem) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[civic_government]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** anthropic-claude-api, d3.js, framer-motion, next.js, novus.ai, supabase, tailwind-css, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mortem

## Body

landing homepage Create Waiting room Confession phase Clustering phase Voting phase Truth Doc Novus Dashboard Inspiration Every team I've been around runs retrospectives. Almost none of them work. Someone opens a doc, asks "what went wrong?" and the room gives the polished version — the safe answer, the one that doesn't name names, doesn't implicate leadership, doesn't risk an awkward conversation next week. The real reasons things failed sit in everyone's heads, unsaid. because saying it out loud in front of your manager has a cost and Staying quiet doesn't. So the same root causes get rediscovered every quarter. Nobody's lying — they're just protecting themselves in a format that was never built for honesty. That one constraint — nobody has to be the person who said it — became the entire product thesis. What it does PostMortem is a real-time anonymous retrospective tool for product teams. A facilitator starts a session and shares one link. No accounts, no signup — anyone with the link joins anonymously in seconds. ① Confess — Everyone types what actually went wrong. Completely anonymous. Nothing is attributed at the data layer — there's nothing to leak even if someone tried. ② Cluster — The room watches live as a force-directed visualization groups every confession into themes. Claude reads the raw text cold and labels each cluster ("leadership overreach" and "ignored user research"). Nobody curates it. The AI does it in real time. ③ Vote — One vote each, no debates. The room is not the loudest person in it — decides which cluster is the real root cause. ④ Commit — This is the part that makes it work. Commitments are not anonymous. Once the room has agreed on the truth, you put your name on what you'll do about it. Truth without consequence is just venting. This is the consequence. ⑤ Truth Doc — An AI-generated narrative ties the confessions, the root cause, and the commitments into a shareable document — exportable as PDF, shareable to LinkedIn, with a public read-only link for anyone who wasn't in the room. The facilitator isn't a neutral observer — they confess, vote, and commit, exactly like everyone else. The only extra thing they have is a button to advance the phase. If commitments are about accountability, The facilitator can't be exempt from making one. How we built it Frontend — Next.js 14 with App Router and TypeScript. Framer Motion handles the phase transitions as the room moves from confessing → clustering → voting → committing → complete. D3.js powers the force-directed clustering visualization with collision, centering, and positional forces — not a static chart. Real-time — Supabase Realtime ( postgres_changes subscriptions) So every participant sees the room update live without refreshing. Confessions, votes, and commitments sync instantly across every open tab. AI — Anthropic Claude — does two things: clusters raw confessions into labelled themes during the clustering phase, and writes the closing Truth Doc narrative from scratch at the end of each session. Analytics — Novus.ai is wired into every meaningful moment across the session lifecycle. Twelve distinct events tracked: session_created · participant_joined · confession_submitted · ai_clustering_completed · phase_advanced · vote_cast · commitment_submitted · truth_doc_generated · share_link_copied · shared_to_linkedin · truth_doc_downloaded · session_completed Deployment — Vercel. Deployed, public, working right now. Challenges we ran into Realtime was the hard 20%. Getting confessions, votes, and commitments to sync instantly across every open tab via Supabase Realtime took significantly longer than building the entire voting UI. But it's the difference between "a form" and "a room". Without it the product's entire premise collapses. Anonymity has to be structural, not just promised. It's not enough to say "this is anonymous" in copy. Confessions are stored with zero attribution at the data layer — participant IDs are randomly generated animal names with no link to any real identity. There's nothing to leak even if someone tried. The facilitator role took three redesigns. I initially built the facilitator as a pure observer with a control panel. It took a clear-eyed look at the actual user journey to realize that broke the product's own thesis — if commitments are about accountability, the A facilitator can't opt out of making one. Rebuilding them as a full Equal participation was the right call but it meant rethinking the entire session data model. The D3 clustering visualization needed to feel alive, not just Correct. Getting the force simulation to feel organic — nodes drifting toward their cluster, labels appearing at the right moment, mobile falling back gracefully to cards took more iteration than any other single feature. Accomplishments that we're proud of A complete five-phase product that actually works end-to-end in real time across multiple users simultaneously The confession → clustering transition — watching anonymous text organize itself into themes live on screen is genuinely unlike anything else in the retro tool space Anonymity that is structural, not cosmetic — built into the data model, not just the copy The deliberate shift from anonymous (confession) to public (commitment) within a single session — that design decision is the whole product in one interaction Twelve Novus.ai events that answer real product questions, not just pageview tracking Shipped in 30 days, solo, from idea to deployed product What we learned The product thesis has to survive contact with the data model. If anonymity is your core promise, it can't just be a UI affordance — it has to be structurally impossible to break at the database level. Designing for that constraint early saved a much harder retrofit later. Realtime changes everything about how you think about state. Building for multiple simultaneous users who all need to see the same thing at the same moment is a fundamentally different problem from building a standard CRUD app. Supabase Realtime solved it — but only after I understood the problem properly. Novus answers the question a demo can't. Does anyone actually Finish the flow? The drop-off between `confession_submitted " and '0' is the single most useful number in this product. No amount of demo video replaces seeing that in a real dashboard. Ship the thing that makes you slightly nervous. The commitment phase — where anonymity ends and your name goes on something — was the feature I was least sure about. It turned out to be the feature that makes the whole product mean something. What's next for Mortem Session templates — pre-built post-mortem formats for common failure modes (missed deadline, feature flop, team misalignment) Async mode — let teams confess over 48 hours instead of a live session, for distributed teams across time zones Commitment tracking — follow up 30 days later: did the commitments actually stick? Team history — a private dashboard showing your team's recurring root causes across multiple sessions over time Slack integration — kick off a PostMortem directly from a Slack channel when something ships badly The core insight is that honesty needs anonymity but accountability needs names — doesn't change. Everything else is about getting that into more rooms. <div