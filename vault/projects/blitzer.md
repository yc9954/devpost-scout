---
slug: "blitzer"
url: "https://devpost.com/software/blitzer"
title: "Blitzer"
hackathon: "AWS Game Builder Challenge "
organization: "Amazon"
winner: true
words: 415
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/sensor_telemetry"
---

# Blitzer

> A shooter game made in 50 days using Amazon Q & Gen AI. Face an evil AI overlord through procedurally generated levels and an epic boss battle. Ready for the challenge?

[Devpost](https://devpost.com/software/blitzer) · hackathon [[AWS Game Builder Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[sensor_telemetry]]
  <sub>weak: geospatial</sub>

**stack** amazon-dynamodb, amazon-polly, amazon-q, amplify, bedrock, c#, cloudfront, cognito, nextjs, react, route-53, s3, typescript, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blitzer

## Body

Inspiration The spark for Blitzer came from our lifelong love of arcade shooters and roguelike games. We wanted to push the boundaries of what's possible when combining classic gaming elements with cutting-edge AI technology. The idea of an AI Overlord wasn't just a story element - it became the core of our innovative approach to procedural level generation. What it does Blitzer delivers an intense isometric shooter experience where every playthrough is unique. The game features AI-generated levels that continuously challenge players with new layouts, hazards, and enemy patterns. An AI Overlord taunts players with real-time generated voice lines as they navigate through these procedurally created environments, facing off against a challenging boss and competing on global leaderboards. How we built it We developed Blitzer using Unity for the core game mechanics, while leveraging React for the user interface and AWS services for the backend infrastructure. The game's unique AI-powered level generation system uses Amazon Bedrock with Claude 3.5 Sonnet, while Amazon Q significantly accelerated our development process. We integrated various AWS services including Amplify, DynamoDB, Polly, etc… to create a robust, scalable gaming solution. Challenges we ran into Our biggest hurdle was the compressed 50-day development timeline while managing our local business. Balancing game development with our day jobs required careful time management and late-night coding sessions. We also faced technical challenges in perfecting the AI level and voice line generation system to ensure consistently playable and engaging levels. Accomplishments that we're proud of Successfully creating a fully-functional game with AI-generated content in just 50 days stands as our greatest achievement. We're particularly proud of our innovative use of AWS services, especially the seamless integration of AI for both level generation and development assistance. The game's unique blend of procedural generation and classic shooter mechanics has created an experience that feels both familiar and fresh. What we learned This project taught us the transformative potential of AI in game development. We gained deep insights into AWS services and learned to effectively integrate multiple technologies into a cohesive gaming experience. Most importantly, we discovered that with modern tools and determination, a small team can create something truly innovative. What's next for Blitzer While we've enjoyed building Blitzer, its future development will depend entirely on player interest and feedback. If there's sufficient community enthusiasm to make the project sustainable, we'll consider keeping the servers running and adding new features. For now, we're eager to hear what players think about the game in its current form. <div