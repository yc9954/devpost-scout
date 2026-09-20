---
slug: "massive-data-center"
url: "https://devpost.com/software/massive-data-center"
title: "HypeMarket"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 707
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# HypeMarket

> Live esports prediction arena with telemetry-synced stakes and crowd-driven odds.

[Devpost](https://devpost.com/software/massive-data-center) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[transportation]]
  <sub>weak: developer_tools</sub>
**user** [[frontline_worker]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-aurora-dsql, amazon-cognito, amazon-dynamodb, aws-iot-core, aws-lambda, aws-sdk, k6, mqtt, next.js, node.js, react, tailwind-css, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i'm proud of
- what i learned
- what's next

## Body

Load Test Result k6-cloud (Dublin) Local Load Test Result Architecture Diagram v0 Usage AWS DynamoDB AWS DSQL Query Deployment Lambda Fanout Lambda Aggregator Inspiration I watch a lot of esports finals on Twitch. The best moments are those unexpected and fast crucial decisions or actions that players make. Twitch has polls and channel points for that, but someone still has to start a poll. The current process is too slow, they feel like something extra glued on top of a well-done project (Channel Points Predictions helped, but on most streams someone still has to fire /prediction while the round is already decided). Polls should not be a secondary part of platform, it should be one of the main drivers of hype in a stream. I wanted a second screen where the map, the event feed, and a stake panel stay in sync. When a kill hits, momentum shifts. You stake play-money Hype Credits before the round ends. Pool sizes set the odds, not a house line. That is HypeMarket . What it does HypeMarket is a live esports prediction arena for H0: Hack the Zero Stack (Track 3: Million-scale Global App). Viewers stake free, non-redeemable Hype Credits on parimutuel markets (demo: "Who wins Map 3?"). Odds come from pooled stakes. Live match telemetry (kills, objectives, positions) arrives over MQTT next to the market UI. The momentum strip reads recent telemetry while the odds bar reads the crowd. Live demo: https://hypemarket-v0-aws.vercel.app Demo video: https://youtu.be/7oMf9jGEBME Build write-up: https://dev.to/emiliano_xy/building-hypemarket-a-million-scale-esports-prediction-market-with-dynamodb-iot-core-and-vercel-2g3k Play money only. Hype Credits do not cash out. This is a prediction simulation, not real-money gambling. How I built it Game telemetry and stakes have different requirements. I split them into two pipelines. Telemetry. telemetry_mock_data/producer.js writes to Amazon DynamoDB ( MatchTelemetry , 24h TTL) every 500ms. DynamoDB Streams trigger EsportsTelemetryFanout , which publishes to AWS IoT Core on esports/telemetry/M-1001 . Browsers subscribe over MQTT WebSocket with Cognito Identity Pool guest credentials. No IAM keys in the frontend. Markets. Stakes go through a Next.js Server Action ( placeStake ) on Vercel into Amazon Aurora DSQL : wallet debit, random shard increment (32 shards per outcome), wallet_ledger insert. UgePollTotalsAggregator sums shards into poll_totals . GET /api/markets serves implied odds from the edge cache. Resolve runs inline parimutuel settlement and credits winners. The UI came from two Vercel v0 passes (market panel, then second-screen layout). Challenges I ran into Early on I tried one database for kills and stakes. Telemetry is append-only and identical for every viewer. A stake debits your wallet and bumps a shared pool row other people hit in the same second. Those needs fought each other, so I split my idea into DynamoDB and Aurora DSQL. During testing I found a bug where event feed wasn't refreshed correctly with intermittent networks. MQTT only delivers messages published after you subscribe, meaning that after a dropped connection, the feed was stale until I added a hydrate API call to properly refresh the event panel. For scale, combined k6 runs were too much for free tier architecture. I separated scenarios instead: smoke at 100%, sustained ~45 stakes/sec at 99.9% success, write-only stress past 13k real DSQL transactions, and a 50-subscriber MQTT soak. What I'm proud of The demo loop I cared about actually works: kill on the map, momentum moves, stake 250 credits, odds shift, lock, resolve, payout hits the wallet with a ledger row behind it. The AWS pieces are real, not mocked: DynamoDB, IoT Core, Cognito, two Lambdas, Aurora DSQL. Load tests hit the production stake path. What I learned For live global events, I would split firehose broadcast from transactional state again. IoT Core beat rolling my own WebSocket fan-out for one-to-many telemetry. And for hype moments, latency matters as much as the feature. If the UI lags the match, engagement dies even when the backend is fine. What's next Markets that open and resolve from telemetry rules, so nobody clicks a button mid-fight. Run multiple matches in parallel to stress the DynamoDB → IoT ingest path before the next finals-scale demo. More things to spend Hype Credits on: flair, event entry, and side markets so credits matter beyond one map stake. AWS databases used: Amazon DynamoDB (telemetry) and Amazon Aurora DSQL (wallets, sharded pools, ledger, settlement). #H0Hackathon <div