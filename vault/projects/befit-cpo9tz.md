---
slug: "befit-cpo9tz"
url: "https://devpost.com/software/befit-cpo9tz"
title: "BeFit"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 378
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# BeFit

> Intelligent AI-powered workout Coach

[Devpost](https://devpost.com/software/befit-cpo9tz) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[structured_db]]

**stack** mediapipe, openai, opik, postgresql, prisma, qdrant, sveltekit, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration I was inspired to build BeFit because I saw how many people struggle to stay consistent with their workouts. I wanted to make a fitness app that doesn’t just show static workout plans, but creates personalized workouts and helps users improve their form using real-time AI feedback. I also love AI tools and wanted to bring them into fitness in a meaningful way. What it does BeFit is an intelligent AI-powered workout assistant that combines Agentic AI, RAG-enhanced knowledge, and MediaPipe pose detection to create personalized workout routines and provide real-time form correction. it is designed for fitness enthusiasts at every level. How we built it I built BeFit with these main ideas: SvelteKit & Tailwind CSS for a clean, responsive frontend UI. AI tools & LLMs to generate workout routines based on goals, experience, and equipment. Pose detection to analyze form and give real-time feedback during workouts. Database & storage so workout routines and exercise configs are saved and reusable. Users can tell BeFit what their goals are, and the AI will give them custom workout plans tailored just for them, not the same generic plans everyone sees in other apps. The app also analyzes movement through the webcam and gives real-time feedback to help improve exercise form. Challenges we ran into There were a few big challenges along the way: Integrating AI with real-time feedback: Getting the AI to generate accurate workouts and usable pose configs took experimentation. Learning new tools: I had to learn how to work with pose detection tech and connect it to AI responses. Balancing features with usability: I wanted the app to be powerful but also simple to use. That meant spending extra time refining UI and interactions. But overcoming these challenges taught me a lot and made the project much stronger. What we learned While building this project, I learned a lot about: AI-powered apps - how to use Large Language Models (LLMs) to generate workouts and respond to users. Real-time pose analysis - integrating pose detection (using MediaPipe) to give users feedback on their exercise form. Full-stack development - connecting frontend UI with backend services, databases, and AI tools. User-centric design - making features that feel helpful and easy to use for anyone at any fitness level. <div