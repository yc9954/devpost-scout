---
slug: "nova-creator-ai"
url: "https://devpost.com/software/nova-creator-ai"
title: "Nova Creator AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 336
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Nova Creator AI

> “Nova Creator AI generates viral captions for reels and cinematic edits using Amazon Nova in seconds.”

[Devpost](https://devpost.com/software/nova-creator-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, amazonaimodel, amazonbedrock, api, css, html, java, javascript, maven, novalite, springboot

## How they structured the write-up

- inspiration
- what it does
- how it works
- challenges we ran into
- what i learned
- future improvements

## Body

Thumbnail Home About Output Inspiration As a video editor and content creator, I often struggled to find engaging captions for my Instagram reels and cinematic edits. Writing captions manually takes time and sometimes limits creativity. This inspired me to build Nova Creator AI , a tool that automatically generates creative, cinematic captions using artificial intelligence. The goal was simple: Make caption creation fast, creative, and effortless for creators. What it does Nova Creator AI is a web application that generates viral captions for reels, edits, and cinematic videos . Users simply enter a short description of their video, and the system generates multiple creative captions instantly. The captions include: • Emojis • Cinematic phrases • Social media friendly formatting • Numbered captions ready for posting This helps creators save time and improve engagement on social media. How it works User enters a short description of their video. The request is sent to a Spring Boot backend API . The backend communicates with Amazon Bedrock . The Amazon Nova Lite AI model generates captions. The captions are returned to the website and displayed instantly. Challenges we ran into While building the project, I faced several technical challenges: • Integrating Amazon Bedrock API with Java • Handling AI response formatting properly • Fixing issues with JSON structure and model responses • Designing a clean UI/UX for creators These challenges helped me learn how to integrate real AI models into production applications. What I learned Through this project I learned: • AI integration using Amazon Bedrock • Backend development with Spring Boot • Building APIs and connecting them to a frontend • Prompt engineering for better AI results • UI/UX design for creator-focused tools Future Improvements Planned upgrades for Nova Creator AI: • Image → Caption generation • Video analysis for captions • Hashtag generator • Caption tone selection (Funny / Cinematic / Emotional) • Multi-language captions • Mobile-friendly creator dashboard The vision is to turn Nova Creator AI into a complete AI toolkit for social media creators. <div