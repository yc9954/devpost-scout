---
slug: "explainit-512obp"
url: "https://devpost.com/software/explainit-512obp"
title: "ExplainIt"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 345
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# ExplainIt

> ExplainIt is an AI-power app made in next.js that gives students a way to understand complex school topics by breaking it down by key concepts, with a quiz after each explanation

[Devpost](https://devpost.com/software/explainit-512obp) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** firebase, next.js, ollama-ai-provider, shadcn, typescript, vercel-ai-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for explainit

## Body

ExplainIt chatbot Inspiration Often times, students in class have a hard time understanding what their teachers are saying because their teaching style is not complementary to the students. The goal of ExplainIt is to meet the student where they are by providing a clear breakdown of a topic What it does ExplainIt is powered by the ollama 3 model, and when it is given a subject and topic as input, it breaks down the topic by discussing what it is, key topics within the main topic, key equations if necessary, and provides a quiz at the end for understanding How we built it This entire app was built within Next.js , a react framework. On the frontend, tailwind was used as a substitute for CSS, and shadcn was used to create components. On the backend, firebase was used for authenticating users, and the AI SDK by vercel was used to create a link between the frontend and the AI. Challenges we ran into Specializing the AI for the aim of the project was hard because it could just end up looking and preforming like any AI chatbot, which was not the goal. Also, setting up a real-time database proved to be challenging because as the conversation between the user and AI developed, storing all of it became more difficult Accomplishments that we're proud of I'm proud of the AI implementation into the app, since this was our first time doing this. Also, I was able to specialize the AI for breaking down topics by passing a system parameter to the streamText function which allowed us to tell the AI what it was supposed to do and how to do it What we learned Building an AI-powered app is by no means easy, but approachable if you have an approachable goal. Also, the best apps are the ones built because of past-experiences What's next for ExplainIt I want to integrate a realtime database to store the conversations between the user and AI, as well as use the AI to generate study plans for the user. <div