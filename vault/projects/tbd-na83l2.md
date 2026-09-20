---
slug: "tbd-na83l2"
url: "https://devpost.com/software/tbd-na83l2"
title: "Rift Wrapped"
hackathon: "Rift Rewind Hackathon"
organization: "Amazon"
winner: true
words: 806
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Rift Wrapped

> Your League of Legends year rift-wrapped with AI : epic highlights, player head to heads, and an interactive chatbot to explore your stats.

[Devpost](https://devpost.com/software/tbd-na83l2) · hackathon [[Rift Rewind Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** amazon-dynamodb, amazon-ec2, aws-bedrock, claude, docker, nginx, python, react, replicate, riot-api, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rift wrapped

## Body

Chatbot Screen Example Chatbot Response Example Head to Head Overview Screen Analysis and Insights Screen Head to Head Verdict Screen Share Wrapped Screen Player Quirks Screen Highlights Screen Head to Head Stats Comparison Your Top Matches Screen Player Overview Screen Your Top Champions Screen Rift Wrappen Solo Screen Landing Page Rift Wrapped Head to Head Screen Inspiration We've all seen Spotify Wrapped take social media by storm every year, and we thought - why don't we gamers have something equally shareable and fun? Gaming is deeply personal, filled with epic victories, devastating defeats, and countless memorable moments. We wanted to create an experience that transforms raw gaming data into a story worth sharing, celebrating the highs and laughing at the lows. Rift Wrapped was born from the desire to give players their own personalized gaming year-in-review that's as entertaining as it is insightful. What it does Rift Wrapped transforms your gaming history into an interactive, shareable experience that's equal parts celebration and entertainment. Users can: Generate personalized wrapped summaries showcasing their best performances, top champions, and season highlights Go head-to-head with friends to see who truly dominated the rift Explore a timeline of their best matches with detailed breakdowns Get coached by an AI companion that analyzes your entire gaming history and provides personalized improvement tips, answers questions like "How can I improve my Ezreal Winrate?" or "Which champion should I play more?", and helps identify patterns in your gameplay Enjoy fun facts and roasts - because sometimes you need an AI to tell you that your 2 AM ranked games are statistically your worst idea Share everything on social media - every insight, roast, and accomplishment is designed to be social media ready How we built it We leveraged a modern tech stack to bring Rift Wrapped to life: AWS Bedrock powers our AI capabilities, generating personalized insights, witty roasts, coaching advice, and handling natural language queries about player history Python backend processes and analyzes gaming data, calculating statistics, identifying patterns, and feeding our AI models AWS DynamoDB serves as our NoSQL database, caching player wrapped data and comparison results to optimize performance and reduce redundant API calls React frontend delivers a smooth, interactive experience with shareable graphics and dynamic visualizations The architecture connects player data to AWS Bedrock's language models, enabling the chatbot to have contextual conversations about specific matches, trends, and performance metrics while providing actionable coaching Challenges we ran into The technical challenges were substantial and multifaceted: Riot API rate limits - working within strict rate limits while fetching comprehensive match histories for users required intelligent caching and request batching strategies Data volume - processing the sheer amount of match data (dozens to hundreds of games per player) and transforming it into meaningful insights without overwhelming our systems Prompt engineering and optimization - crafting effective prompts to extract meaningful insights from raw statistics while maintaining consistency, accuracy, and personality across different AI-generated content types (roasts, coaching, personality analysis) AI model selection trade-offs - finding the sweet spot between model quality, response time, and AWS Bedrock credit costs. More powerful models gave better coaching insights but took longer and cost more per query Accomplishments that we're proud of We created something that makes people actually want to look at their stats! Our AI-powered coaching chatbot provides genuinely useful insights that help players improve, while the roasts and fun facts strike the perfect balance between savage and supportive. The comparison feature sparked competitive banter during testing, and the timeline visualization helped players genuinely understand their improvement over time. Most importantly, we built a full-stack application integrating cutting-edge AI and working around real-world API constraints in ashort timeline - from data processing to shareable social cards to intelligent coaching. What we learned This project taught us that AI's real power isn't just in processing data - it's in making that data meaningful and human . We learned how to craft prompts that generate consistently entertaining yet personalized content, how to structure conversations with context-aware coaching chatbots, and how gaming communities crave both validation and actionable advice. On the technical side, we deepened our understanding of AWS Bedrock's capabilities, learned to navigate API rate limits creatively, and discovered the art of balancing model performance with cost efficiency. We also learned that building experiences people genuinely want to share requires thinking beyond just features - it's about emotional impact. What's next for Rift Wrapped We're just getting started! Future plans include: Squad wrapped - team-based analytics showing how friend groups perform together AI-based advanced coaching - deeper performance analysis with personalized improvement plans and matchup-specific advice Achievement system - unlock badges and milestones based on your wrapped insights Mobile app - making it even easier to generate and share on the go The ultimate goal? Make Rift Wrapped the must-have tradition for every gamer's year-end celebration. <div