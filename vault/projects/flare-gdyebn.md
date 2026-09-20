---
slug: "flare-gdyebn"
url: "https://devpost.com/software/flare-gdyebn"
title: "flare"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 866
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# flare

> Flare detects AWS anomalies with AI, calls the on-call engineer with a root cause analysis, and stays on the line as a voice triage assistant to pull live infrastructure data on demand.

[Devpost](https://devpost.com/software/flare-gdyebn) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]]
**user** [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** amazon-bedrock, amazon-cloudwatch, amazon-connect, amazon-dynamodb, amazon-ec2, amazon-ecr, amazon-ecs-fargate, amazon-eventbridge, amazon-lex-v2, amazon-nova-lite, amazon-nova-multimodal-embeddings, amazon-nova-sonic, amazon-rds-postgresql, amazon-sns

## How they structured the write-up

- about the project

## Body

About the Project Inspiration As an engineer who has been on call, I know we are not glued to our laptops 24/7. Often when an alert comes through, I am driving or busy doing something and it might take me a few minutes to get to my laptop. After I finally get there, I have to spend 15 minutes just getting caught up to speed. I built Flare to help me debug the problem while I am getting to my laptop. It is an AI system that doesn't just detect the problem, but calls you on the phone and walks you through it. Flare will answer questions and gather information for you, so by the time you open your laptop you already have a game-plan. The core insight was that incident response is actually three distinct problems stitched together: finding the signal in noisy logs , reasoning about root cause , and communicating the answer to a human under pressure . Each maps naturally to a different modality of foundation model — embeddings, text reasoning, and speech — which made Amazon Nova's model family a perfect fit. How I Built It Flare is a fully serverless pipeline on AWS, orchestrated by Lambda functions (deployed as a container image) and triggered by CloudWatch Alarms, EventBridge schedules, or log subscription filters. Pipeline 1 — Log Analysis. When triggered, Flare fetches logs from CloudWatch and runs them through a token budget planner. If the logs fit the model's context window, they go straight to Nova 2 Lite. If they don't, Flare uses Cordon , a semantic anomaly detection library I built. Cordon slides a window across the log text, embeds each window via Bedrock, and scores anomalies using k-nearest-neighbor density estimation. The anomaly percentile threshold is computed dynamically so the reduced output hits the token budget. For n log groups, budget is allocated via greedy fair-share: small groups that fit keep full logs, and remaining budget is split proportionally among larger groups. The reduced (or raw) logs are then sent to Nova 2 Lite, which produces a structured root cause analysis with severity, affected components, evidence, and next steps. Pipeline 2 — Predictive Pre-Fetch. Before the engineer even picks up the phone, Flare asks Nova 2 Lite: "Given this RCA, what CloudWatch metrics, logs, and resource statuses would the engineer investigate next?" The model returns a structured JSON plan of 5–8 queries. These are executed in parallel against CloudWatch and cached in DynamoDB. The pre-fetch and outbound phone call run concurrently, and by the time the engineer answers, the investigation data is already cached and ready. Pipeline 3 — Voice Conversation. Amazon Connect places the outbound call. When the engineer answers, a contact flow hands off to a Lex V2 bot powered by Nova 2 Sonic speech-to-speech. Nova Sonic delivers the RCA briefing and then listens for follow-up questions. The fulfillment Lambda implements a retrieve-then-reason pattern: it pulls relevant data from the DynamoDB cache (or falls back to a live CloudWatch query on cache miss), then passes the engineer's question, the data, and the full RCA context to Nova 2 Lite. This means questions like "Does it look like the database is overwhelmed?" get intelligent, correlated answers. The entire system is deployed via CloudFormation — no manual console setup required — and the end-to-end latency from alarm to first answered question is approximately 45 seconds. What I Learned Log reduction is a token economics problem. Naively truncating logs throws away the most important parts. Framing it as "keep the top p% most semantically anomalous windows to hit a token budget" turned out to be far more effective than keyword filtering, and the percentile p can be derived directly from the ratio of available tokens to total tokens. Pre-fetching is the key to voice UX. A 2-second CloudWatch API call is invisible in a text interface but devastating in a voice conversation. By predicting the engineer's questions and caching answers during the time the phone is ringing, I made follow-up responses near-instantaneous (~100ms cache read vs. ~2s live query). Retrieve-then-reason beats retrieval-augmented generation for structured data. Rather than embedding CloudWatch metrics into a vector store, I let the LLM plan the queries, execute them directly via AWS APIs, and then reason over the raw results. This gives the model precise, real-time data rather than approximate vector matches. Challenges Token budget allocation across multiple log groups. A single log group is straightforward — compute the anomaly percentile as the ratio of budget to total tokens. But with k log groups of varying sizes, I needed a fair-share algorithm that doesn't starve small groups or waste budget on groups that don't need reduction. The greedy approach (sort by size, give small groups their full logs, split the remainder) was simple but required careful handling of edge cases. Parallel timing of pre-fetch vs. phone ringing. The pre-fetch must complete before the engineer starts asking questions, but we can't block the outbound call on it. Running both in a ThreadPoolExecutor and relying on the natural ~15–30 second ring time as a buffer worked, but I had to add graceful degradation (fall back to live queries) for cases where pre-fetch is slow or fails. <div