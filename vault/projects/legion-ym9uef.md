---
slug: "legion-ym9uef"
url: "https://devpost.com/software/legion-ym9uef"
title: "Legion"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 230
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/mental_health"
  - "substrate/code_repository"
---

# Legion

> Because men aren’t meant to fight alone.

[Devpost](https://devpost.com/software/legion-ym9uef) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[mental_health]]
**substrate** [[code_repository]]

**stack** bolt.new, openai, stripe, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Legion - Because men aren’t meant to fight alone Inspiration I hit a dark stretch two years ago. The only things that pulled me out were Hitting gym and Honest conversations with my boys who refused to quit on me. Therapy is great but progress actually came from momentum + brotherhood. I wanted that mix on demand, so I built Legion What it does Missions : 7/21/30-day commitments with daily check-ins and streak tracking. Small wins stack fast. Mission Feed : other men follow, cheer, or call you out. Zero progress happens in silence. Meeting Pods : weekly video huddles focused on real issues: Spiritual Growth, Addiction Recovery, Fatherhood, and more. Aurel (AI Guide) : a grounded, masculine chat mentor. Not a therapist, not a hype-man just clear next steps, 24/7. Weekly Challenges + Cash Rewards : beat the leaderboard, take home actual money for levelling up. How we built it Bolt.new for rapid front-end scaffolding and real-time component syncing. Supabase (Postgres + Row Level Security) for auth, missions, logs, and pod data. OpenAI GPT-4o for Aurel’s conversation engine, streamed via Edge Functions for near-zero-latency replies. Stripe for payouts to weekly-challenge winners and future subscription tiers. Challenges we ran into Tone-fine-tuning Aurel : we iterated prompts until the voice felt firm but never preachy. Real-time feed lag : solved with Supabase Realtime and a simple optimistic-UI pattern in Bolt. <div