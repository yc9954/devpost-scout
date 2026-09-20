---
slug: "sonar-onjtvd"
url: "https://devpost.com/software/sonar-onjtvd"
title: "Sonar"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 695
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Sonar

> Sonar is a live radar of what's happening around you right now — ephemeral, crowd-curated, conversational. Built on DynamoDB for speed, Aurora DSQL for record.

[Devpost](https://devpost.com/software/sonar-onjtvd) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-aurora-dsql, amazon-bedrock-(claude-haiku), amazon-cloudfront, amazon-dynamodb, amazon-web-services, api-gateway-websockets, aws-cdk, aws-lambda, iam, mapbox, next.js-16, react, stripe, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it — the data model is the product
- what's next for sonar

## Body

Inspiration Every social product forces a single time horizon. Snapchat is all-ephemeral — it forgets everything. Instagram is all-permanent — nothing ever fades. But a place isn't either. A festival stage, a campus quad, a conference floor has a living, recent memory : what's happening now and over the last day, not forever. We wanted the layer in between — where a place remembers just long enough to be useful, and the crowd decides what's worth keeping. The deeper bet: this is fundamentally a database-shaped problem , not a feature problem. "What's worth going over to, right now, near me?" is a question about a high-write stream of geo-tagged, time-decaying events — and a separate question about durable accounts, money, and analytics. Those are two different data shapes. We chose two different AWS databases on purpose. What it does Open Sonar and you see a live radar of your surroundings. People drop waypoints — a note, photo, or video — onto colored channels (Events, Food, Music, Social, Safety). Waypoints: - stream in live over WebSockets and are ranked by proximity + freshness ; live as long as you choose — the author picks a lifespan (default 15 minutes , up to 24 hours ), and life trades against size: the longer a drop lives, the smaller it may be — a byte-hour budget (50 MB at 15m → 3 MB at 24h). Sonar stays ephemeral by design; - gain life from likes — every like adds +5 minutes to a drop's countdown, uncapped, so the crowd keeps the good stuff alive minute by minute. Two things make it more than a map: Ask the place — AI summarizes and answers questions over a location's last 24 hours ("What's the vibe at the north stage?" "Where's the shortest food line?"). Likes buy time; sponsors buy permanence — nothing user-posted lasts forever. The only permanent pins are sponsored ones: a paid waypoint that never expires and carries the sponsor's name. Permanence isn't earned by love; it's purchased. How we built it — the data model is the product We deployed a polyglot, all-serverless AWS data layer, choosing each database for its access pattern rather than defaulting to one store. Amazon DynamoDB — the live radar (hot path). Every waypoint is a single-digit-millisecond item write keyed for geo + time. Ephemerality is native : each drop carries a TTL derived from the author's chosen lifespan, so DynamoDB expires dead waypoints itself — no cleanup job, no cron. A like is one conditional UpdateItem that extends expiresAt by +5 minutes (uncapped), so the crowd keeps content alive at write time . The byte-hour budget (50 MB @ 15m → 3 MB @ 24h) is enforced on the write path — lifespan and size trade against each other before an item is accepted. Proximity + freshness ranking runs off those same hot items, pushed to clients over API Gateway WebSockets + Lambda so the radar updates the instant something drops nearby. Amazon Aurora DSQL — the system of record. Everything durable lives here, off the hot path: accounts, the sponsorship ledger, and the only permanent objects in the system — sponsored pins bought through Stripe . DSQL's serverless scale-to-zero means the record side costs nothing between bursts while staying strongly consistent for money and analytics. Ephemeral geo-writes in DynamoDB, durable state in DSQL — that's the "two databases on purpose" bet: two data shapes, two engines, one clean seam. Amazon Bedrock (Claude Haiku) — "ask the place." A Lambda pulls a location's last-24h waypoints from DynamoDB and hands them to Claude Haiku to summarize and answer questions over the recent activity. Haiku keeps it cheap and fast enough to feel live. Delivery & infra. Media served via CloudFront , radar UI on Mapbox , the backend defined in AWS CDK with least-privilege IAM , and the frontend built in Next.js 16 / React on Vercel . What's next for Sonar Sonar for Work (B2B): the same engine as an office/building coordination layer with an operator analytics dashboard. Sponsorship marketplace for venues and organizers; richer "ask the place" with multi-place trends. Push notifications for channels you subscribe to; offline-tolerant drops. <div