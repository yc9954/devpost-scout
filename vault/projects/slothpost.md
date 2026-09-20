---
slug: "slothpost"
url: "https://devpost.com/software/slothpost"
title: "SlothPost"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 984
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# SlothPost

> SlothPost watches your GitHub commits, Vercel deploys, and Rants, then drafts X and Threads posts for you to approve. Build in public without the writer's block

[Devpost](https://devpost.com/software/slothpost) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[labor_employment]]
  <sub>weak: government_staff</sub>
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** amazon-dynamodb, anthropic-claude-haiku-4.5, aws-kms, clerk, cloudflare-waf-&-dns, cloudflare-workers, github-app-api, groq-llama-3.3-70b, groq-whisper-v3, next.js-16, react, resend, tailwind-css, threads-api

## How they structured the write-up

- what's the problem
- what it does
- the database design
- the 3-tier memory pipeline
- what broke me in the process
- what i learned
- the voice feature

## Body

What's the problem Building in public is supposed to be a growth strategy. Tweet about your progress, get followers, build an audience, and by the time you launch you already have customers. Everyone says it works. And honestly, I think it does. The problem is that it's one more thing to do. When I'm deep in a debugging session at midnight, the last thing I want to do is craft a Twitter thread about what I just fixed. So I just don't post. The commit goes unannounced. The build-in-public strategy quietly fails. SlothPost is the tool I built to solve this for myself, and for every other indie dev who's tried and failed to stay consistent. What it does SlothPost connects to your GitHub, your Vercel account, and optionally App Store Connect. Whenever something interesting happens like a commit, a deployment or a release — it captures that event. You can also open the app and do a quick or detailed rant about what you're working on. Once you have events, the AI generation engine kicks in on a schedule. It reads your recent activity, your weekly summary, your writing style profile (built from your speaking style over time), and drafts posts for X and Threads. You review them, edit if you want, and approve. That's it. You never start from a blank page. The database design This project uses Amazon DynamoDB as the primary database, and the schema design was the most deliberate architectural decision I made. Everything is split across 9 tables: slothpost-events — raw events (commits, PRs, deployments, voice transcripts), TTL 7 days slothpost-users — user accounts, preferences slothpost-products — the indie products a user tracks slothpost-posts — draft and published posts, TTL 30 days after publish slothpost-integrations — KMS-encrypted OAuth tokens per platform slothpost-rants — voice recordings and transcripts, TTL 60 days slothpost-daily-summaries — AI-generated daily rollups, TTL 30 days slothpost-weekly-summaries — weekly rollups for longer-term context slothpost-brand-learnings — extracted voice profile and writing style per product The access patterns are almost entirely primary-key lookups or narrow range queries, which is exactly what DynamoDB is designed for. I resisted single-table design — it looks elegant in blog posts, but debugging it at 3am when access patterns evolve is not fun. I added 4 Global Secondary Indexes: scheduleStatus-nextRunAt-index — used by the scheduling cron. Only products with scheduleStatus='active' appear in this index (a sparse index). The cron runs every minute and does a targeted range query to find products due for post generation. Zero table scans anywhere in the codebase. installationId-index — GitHub App webhooks carry an installationId , not a userId . This GSI routes incoming webhook payloads to the right product instantly. vercelProjectId-index (sparse) — same pattern for Vercel deployment webhooks. Only products with a connected Vercel project have this attribute, so the index stays small. When a deployment event arrives, one query finds the right product. userId-createdAt-index — used for analytics queries where I need a user's post history sorted by date. Every table runs PAY_PER_REQUEST billing with PITR enabled. All OAuth tokens are encrypted with AWS KMS using a customer-managed key ( alias/slothpost-oauth-tokens ) before being written to DynamoDB. There is no plaintext credential anywhere in the database. The 3-tier memory pipeline This is the part I'm most proud of architecturally. A Cloudflare Worker runs 3 cron jobs against the Next.js API: Every minute: checks the schedule index and triggers post generation for products that are due Every night at midnight UTC: reads all raw events from the past 24 hours and writes a daily summary Every Monday at 1am UTC: reads the past 7 daily summaries and writes a weekly rollup When the AI generates a post, it has access to your latest events, your daily summaries, your weekly rollup, and your brand-learnings profile — all pulled from DynamoDB. The result is posts that reflect what you've actually been working on, not just your last commit message. What broke me in the process The Vercel Marketplace integration. I discovered mid-build that OAuth marketplace integrations cannot create webhooks via the Vercel REST API — you get a hard 403. The documentation for this is basically nonexistent. I had to pivot to a global webhook configured in the Integration Console and route events internally using the sparse vercelProjectId-index GSI. It ended up being a cleaner architecture, but it cost me a full day. The scheduling system also went through 3 complete rewrites. The first version scanned the products table. The second added a GSI but checked a field called daySchedule.enabled that didn't exist — the enabled state is actually represented by time !== null . The third version is the one that shipped. What I learned DynamoDB rewards you for designing around access patterns first. Every time I wrote application code before thinking about the DynamoDB query, I ended up backfilling data or adding a GSI later. The removeUndefinedValues: true option on DocumentClient is also not optional when you're writing TypeScript — I spent two hours on that. On the infrastructure side: Cloudflare's Bot Fight Mode will silently block GitHub and Vercel webhooks. Never turn it on. The voice feature Tap the sloth logo in the sidebar. Record a rant. Talk about what you shipped today, what's frustrating you, what you figured out. That audio goes to Groq Whisper for transcription, then to Claude Haiku to extract personality markers, preferred vocabulary, and writing style. That profile updates over time and influences every post the system generates. It's the difference between a post that says "Released v1.2 with bug fixes" and one that sounds like the person who actually stayed up until 2am fixing it. This project was built for the H0: Hack the Zero Stack with Vercel v0 and AWS Databases hackathon. The DynamoDB data model and Vercel deployment aren't bolted on — they're the foundation the product runs on. The app is live at slothpost.app . <div