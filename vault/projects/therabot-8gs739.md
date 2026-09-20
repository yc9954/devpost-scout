---
slug: "therabot-8gs739"
url: "https://devpost.com/software/therabot-8gs739"
title: "TheraBot"
hackathon: "LaunchHacks IV"
organization: "LaunchHacks"
winner: true
words: 503
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
---

# TheraBot

> TheraBot - your personal AI therapist and wellness companion.

[Devpost](https://devpost.com/software/therabot-8gs739) · hackathon [[LaunchHacks IV]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[mental_health]]
  <sub>weak: web_dom</sub>

**stack** css, framer-motion, gemini, html, postgresssql, react, supabase, tailwind, typescript, vite, web-speech-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for therabot

## Body

Inspiration Many people generally struggle with mental health issues, such as stress. In fact, about 1 in every 5 men struggles with a mental health illness every year. It's also men’s mental health awareness month and our friends struggle with mental health issues, such as from school and losing loved ones. Sometimes, due to a lack of therapists or the costs associated with them, many find themselves alone in their journey. This is why we decided to create TheraBot and why we chose to build our solution for the company, TheraBot AI Therapy. What it does Therabot is an AI-powered web app that helps people manage their mental health through different tools, such as real-time voice conversations with AI, text chats with AI (just like ChatGPT), daily AI-powered journaling, soothing breathing exercises, and by providing resources such as the Suicide Hotline. The AI then tracks your conversations and journal entries to track your mood and display it with our smart dashboard. How we built it In our frontend, we utilized TypeScript, Vite, Shadcn/ui, Tailwind CSS, and Framer Motion. The backend consisted of Supabase with PostgreSQL, and we also used Google Gemini 2.5 Flash as our LLM. We also used it as an AI tool. Challenges we ran into One main challenge we faced was to get the Web Speech API and the text to speech as well as the speech to text working. It was our first time using these APIs and we had trouble connecting all of the different components together. Another issue we had was to get the AI-powered mood analyzer for the whole app. Our app has a real-time live mood analyzer that gets updated every time the user adds something (a new voice/text chat, a new journal, etc). It was hard to connect the Gemini API to all the different components in our app and actually get it to work. Accomplishments that we're proud of The accomplishments that we are proud of are that we successfully overcame the challenges that we faced. After hours of debugging and development, we finally got the Voice Session feature to work with a voice that responded almost immediately. Also, getting the AI-powered features to work throughout the whole app was very rewarding. What we learned We learned a lot throughout this 3-day journey. We all learned so many more things about programming, many new APIs, but I think most importantly we learned about how to work as a team and manage changes with Git. What's next for TheraBot We plan to make Therabot usable internationally with multiple language support in both the Voice Session feature as well as the Text Chat conversations. Moreover, we want to make sure Therabot is personal to everyone so we plan to make the AI therapist’s voice more human-like so it helps people on a more personal level. We also want to give Therabot the ability to have multiple people be able to talk into the AI Therapist so it can help as many people as possible <div