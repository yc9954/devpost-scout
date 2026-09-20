---
slug: "rift-analyser"
url: "https://devpost.com/software/rift-analyser"
title: "Rift Analyzer"
hackathon: "Rift Rewind Hackathon"
organization: "Amazon"
winner: true
words: 1021
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Rift Analyzer

> Your AI coach that turns match data into mastery.

[Devpost](https://devpost.com/software/rift-analyser) · hackathon [[Rift Rewind Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]]
  <sub>weak: financial_record</sub>

**stack** amazon-dynamodb, amazon-web-services, amplify, apprunner, bedrock, boto3, claude3, ecr, mongodb, python, react

## How they structured the write-up

- 1. problem statement & opportunity
- 2. how it works
- 3. core features & innovation
- 4. going beyond op.gg
- 5. technical approach
- 7. key learnings
- 8. impact & production
- 9. hackathon alignment
- 10. conclusion
- aws ai services & data sources
- technology stack

## Body

Match analysis Page Year Recap Page Performance Analytics Page Rift Analyzer is an AI-powered League of Legends coaching platform that transforms a full year of match data into personalized, actionable retrospectives. By combining the Riot Games Developer API with Amazon Bedrock's Claude 3 Sonnet, the application delivers insights that go far beyond traditional stat trackers—offering narrative storytelling, conversational coaching, and shareable social moments that help players reflect, learn, and improve. Key Innovation: A multi-step reasoning AI agent that doesn't just report statistics but interprets trends, diagnoses persistent habits, and prescribes tailored practice plans through natural conversation. 1. Problem Statement & Opportunity League of Legends players generate massive amounts of match data throughout a season, but existing tools (e.g., op.gg) focus on raw statistics without context or actionable guidance. Players struggle to answer questions like: "Why am I stuck at this rank?" "What patterns are holding me back?" "How do I improve my late-game decision-making?" Rift Analyzer addresses this gap by using generative AI to interpret data, surface hidden patterns, and deliver personalized coaching that feels like a conversation with an expert analyst. 2. How It Works The platform follows a five-stage pipeline: Match Ingestion: Fetches a full year of match data from the Riot API and caches it locally to ensure fast subsequent loads. Feature Engineering: Computes advanced metrics like objective conversion rates, damage share trends, vision control patterns, and gold swing analysis across 20+ dimensions. Pattern Detection: Applies statistical analysis to identify persistent strengths, weaknesses, and standout performances using z-score outlier detection and rolling window aggregations. AI Synthesis: Feeds structured insights to Claude 3 Sonnet through Amazon Bedrock, using context-aware prompts and validation guardrails to generate grounded coaching responses. User Experience: Delivers instant headline stats from cache while AI narratives stream in progressively, keeping the interface responsive throughout. 3. Core Features & Innovation 3.1 AI Coaching Agent (Primary Innovation) What makes it special: Multi-Step Reasoning: Uses Claude 3 Sonnet's tool-calling capabilities to fetch analytics mid-conversation, compare performance to target ranks, and assemble practice roadmaps. Conversational Context: Maintains dialogue history so players can ask follow-ups like "What changed after I swapped to jungle?" Grounded Recommendations: Every suggestion is validated against actual match data using context hashes and validation checkpoints. Example Interaction: Player: "How can I improve to reach the next rank?" Agent executes multiple tools in sequence: 1. analyze_recent_performance() → Identifies win rate trends and game length patterns 2. detect_patterns() → Finds vision control drops in late game 3. compare_to_rank() → Shows gaps vs target rank benchmarks 4. generate_practice_plan() → Creates 3-week structured improvement plan Final response synthesizes findings with specific metrics and actionable next steps. 3.2 Year-End Recap & Analytics AI-generated narrative summarizing season journey with milestone achievements Interactive charts for win-rate trends, KDA, and objective control Champion mastery breakdown and role proficiency analysis Shareable summary cards for social platforms 3.3 Performance Optimization LocalStorage caching reduces page loads from 16s to <0.5s (97% improvement) Lazy loading and progressive rendering keep UI responsive Per-player, per-endpoint caching with manual refresh controls 4. Going Beyond op.gg Feature op.gg Rift Analyzer Raw Statistics ✓ ✓ Win Rate Tracking ✓ ✓ AI Narrative Storytelling ✗ ✓ Conversational Coaching ✗ ✓ Pattern Diagnosis ✗ ✓ Practice Plan Generation ✗ ✓ Context-Aware Insights ✗ ✓ Shareable Social Moments Limited ✓ Highlight Match Selection ✗ ✓ Key Differentiator: Rift Analyzer doesn't just show what happened—it explains why, predicts what's next, and prescribes how to improve. 5. Technical Approach Data Processing: Fetch match data via Riot API, compute advanced metrics (objective conversion, damage share, vision trends), apply z-score analysis for pattern detection AI Orchestration: Claude 3 Sonnet with structured JSON context, tool-calling functions, temperature tuning (0.3 for stats, 0.7 for narratives), validation pipeline to prevent hallucination 7. Key Learnings Caching Breakthrough: LocalStorage + lazy loading reduced page loads from 16s to <0.5s (97% improvement). AI Grounding: Context hashes and validation checkpoints eliminated hallucination issues in early prototypes. Insight Discovery: Late-game vision score emerged as strongest rank predictor (r=0.67), now anchors practice recommendations. 8. Impact & Production Value: AI-generated narratives for reflection, pattern analysis for learning, personalized coaching for improvement, shareable moments for social engagement Performance: <200ms cached responses, <2s AI generation, 85% cache hit rate, deployable on AWS Lambda + API Gateway 9. Hackathon Alignment ✓ All requirements met: AI agent, full-year data, insights, visualizations, sharing, AWS integration ✓ Key Innovations: First conversational coaching agent, context-aware AI, 97% performance improvement, validated responses, playstyle-driven recommendations 10. Conclusion Rift Analyzer transforms match data into personalized coaching through AWS Bedrock's Claude 3 Sonnet—interpreting trends, diagnosing habits, and prescribing improvement plans. Beyond a dashboard, it's a conversation partner for player development. Future: Multi-player recaps, real-time coaching, support for other Riot titles. AWS AI Services & Data Sources AWS AI Services: Amazon Bedrock (Claude 3 Sonnet): Primary AI service for generating personalized coaching responses and year-end narratives. Uses tool-calling capabilities to execute multiple analytics functions in sequence with temperature tuning (0.3 for stats, 0.7 for storytelling) AWS IAM: Provides secure, scoped credentials for Bedrock API access with least-privilege patterns Boto3 SDK: Handles authentication, request batching, and retry logic with exponential backoff for Bedrock calls Data Sources: Riot Games Developer API: Focused on player's complete season using two endpoints: GET /lol/match/v5/matches/{matchId} - Match summaries (KDA, damage, gold, vision, objectives) GET /lol/match/v5/matches/{matchId}/timeline - Minute-by-minute timeline data (positions, events, vision control) GET /tft/summoner/v1/summoners/by-puuid/{encryptedPUUID} - Details of the summoner by their ID GET /riot/account/v1/accounts/by-puuid/{puuid} - Account Details by ID Data Processing: Fetch full-year match list and individual match details Process timeline data for early/mid/late game performance patterns Compute advanced metrics: objective conversion rates, vision trends, damage share deltas Apply z-score and rolling window analysis for strength/weakness detection Structure findings as JSON context for AI agent consumption Technology Stack Backend: Python 3.11+ with FastAPI Riot Games Developer API integration LocalStorage API for caching Frontend: React 18 with Vite Tailwind CSS for styling Framer Motion for animations Recharts for data visualization AWS Cloud Services: Amazon API Gateway (routing) Amazon DynamoDB (analytics caching) Amazon S3 (asset storage) Amazon CloudWatch (monitoring) AWS ECR AWS AppRunner AWS Amplify Built with precision, powered by AWS, designed for players who want to level up. <div