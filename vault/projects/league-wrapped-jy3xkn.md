---
slug: "league-wrapped-jy3xkn"
url: "https://devpost.com/software/league-wrapped-jy3xkn"
title: "League Wrapped"
hackathon: "Rift Rewind Hackathon"
organization: "Amazon"
winner: true
words: 733
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# League Wrapped

> An AI-powered coaching agent that analyzes League of Legends player performance data to provide personalized insights, trend analysis, and actionable feedback.

[Devpost](https://devpost.com/software/league-wrapped-jy3xkn) · hackathon [[Rift Rewind Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[sensor_telemetry]]
  <sub>weak: genomic_bio</sub>

**stack** amazon-web-services, awsbedrock, fastapi, next.js, pandas, python, riot-games, shadcn, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for league wrapped

## Body

Landing page with search form Player Dashboard Hidden gems, Head-to-head comparison with another player Achievements, Stats, Champion performance, role distribution, playstyle DNA Top 5 moments of 2025, Performance charts Squad Synergy analysis AI insights Loding player data Shareable cards Inspiration League of Legends has 150 million players who play hundreds of ranked games each season. Stat sites like OP.GG show KDA and win rates, but don't explain what makes each player's style different or how they've improved. I built League Wrapped to surface those insights: playstyle patterns, performance evolution, and standout games. What it does League Wrapped analyzes 100+ ranked matches and uses Amazon Bedrock to generate personalized AI insights. The platform combines data visualization (performance trends, champion analysis, role distribution) with 8 types of AI-generated content: season story, coaching feedback, playstyle personality, top moments commentary, and squad synergy analysis. It also detects 7 non-obvious patterns like time-of-day performance, tilt behavior, and comeback wins that stats sites miss. The AI coaching is direct and honest. Instead of "good job, keep practicing," it says things like "Your vision score averages 18 per game—35% below your rank's median. Place 3-4 control wards near objectives" or "32% win rate on this champion over 25 games. Practice in normals first." Every insight includes specific numbers and rank-appropriate benchmarks. Everything is shareable: downloadable cards for social media, one-click X posts, player-vs-player comparison mode. How I built it I'm using Amazon Bedrock's Nova Micro model ($0.00245 per user) for all AI insights. The tech stack is Next.js 15 + React 19 on the frontend, FastAPI + Pandas on the backend, deployed on AWS EC2 with Nginx and PM2. Data comes from Riot Games API; I fetch 100+ matches per player, process them into aggregate statistics with Pandas, then send that to Bedrock to generate 8 parallel insights in 3-4 seconds. I also tried Amazon Polly for AI-narrated videos, but testing showed they just repeated UI content without adding value, so I removed the feature but kept the code. Three optimizations keep costs low: Nova Micro saves 70-90% vs alternatives, pre-computing stats cuts token usage by 95%, and 24-hour caching reduces costs by 80% on repeat visits. At 1M users, total cost is $505/month. With 1% premium conversion at $4.99/month, that's $50K revenue = 99x ROI. Challenges I ran into Riot migrated from summoner names to Riot IDs (Name#TAG), breaking player lookups. I built automatic fallback that tries all common region tags if none is specified. AI costs could spiral fast at scale. I solved this with Nova Micro (70-90% cheaper), pre-computation (95% token reduction), and 24-hour caching (80% cost savings). The Polly video feature taught me that multi-modal formats need unique value. Videos just repeated UI content, so I removed the feature after testing. Shareable cards work because they enable social distribution; videos didn't offer that. What I learned Bedrock is production-ready. Nova Micro delivers quality at $0.00245 per analysis. Pre-computation cuts token usage by 90%, and 24-hour caching achieves 80% hit rates. Parallel processing (8 concurrent Bedrock calls) finishes in 3-4 seconds vs 20+ sequential. The Polly experiment taught me that technical success doesn't guarantee UX value. Multi-modal features need to provide something unique, not duplicate what's already visible. Players prefer honest, data-driven feedback over generic encouragement. Specific metrics with rank comparisons work better than vague advice. What's next for League Wrapped Immediate Priorities (Next 2 Months) 1. Video Export Feature (Reimagined) Target : Social media sharing, premium monetization Status : Initial Polly implementation removed after testing revealed UX issues Next Iteration : Redesign to provide unique value beyond UI duplication Amazon Polly : Text-to-speech narration with personalized insights not visible on screen Video Generation : 30-60 second animated recap with exclusive content Export Formats : MP4 optimized for Instagram Reels, TikTok, Twitter AWS Stack : Lambda for video rendering, S3 for storage 2. Multi-Season Comparison Target : Year-over-year user retention Historical Tracking : 2023 → 2024 → 2025 progression Evolution Narrative : AI-generated "Your League Evolution" story Visual Timeline : Interactive rank progression chart Storage : DynamoDB for historical player data Business Value : Keep users engaged year-round 3. Mobile App (React Native) Target : Mobile user engagement Platform : iOS + Android with shared codebase Features : All web features + push notifications Offline Mode : View cached analyses without internet Share Integration : Native iOS/Android share sheets Downloads : App Store + Google Play <div