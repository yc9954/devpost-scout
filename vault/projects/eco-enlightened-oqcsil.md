---
slug: "eco-enlightened-oqcsil"
url: "https://devpost.com/software/eco-enlightened-oqcsil"
title: "Eco Enlightened"
hackathon: "EduHacks ($300,000+ in-prizes)"
organization: "EduHacks"
winner: true
words: 294
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/mental_health"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Eco Enlightened

> Where sustainability meets your thoughts

[Devpost](https://devpost.com/software/eco-enlightened-oqcsil) · hackathon [[EduHacks -300-000- in-prizes-]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[mental_health]]
**substrate** [[structured_db]] [[video_visual]]

**stack** api, docker, fastapi, langchain, llms, openai, plasmo, postgresql, python, redis, svelte, tailwindcss, typescript, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of & what we learned
- what's next for eco enlightened

## Body

logo Inspiration Our lives are filled with habits and lifestyles that cause negative consequences without us even being aware of it, one major consequence is the impact on our environment. For that reason, we wented to create an extension for your digital life that would help you become more aware of how your actions affect the environment and how you can change them for the better. What it does An extension for your digital life that makes it easy for you to learn about sustainability in the context of your life How we built it The browser extension follows you everywhere and tracks what you write. It then uses Algorithms and an LLM to determine the context of what you are writing about. If the context is related to sustainability, it will show you a popup with information about the topic and personalized actions you can take to improve your impact on the environment. Challenges we ran into Who woulda thought setting up a local database postgres and redis database with docker and docker compose for the first time in a hackathon was going to be a good idea... Prompting the LLM to only send a response when the user is talking about sustainability. unfortunately, LLMs care about you so when you talk about how tragic your day was, it will empathize with you instead of just not responding. Websockets just decided to not work for us... so we just went for REST instead Accomplishments that we're proud of & What we learned Getting the LLM to work with a vector database of knowledge on sustainability Finally understanding how Docker works What's next for Eco Enlightened Even better LLM Other forms of input (voice, images, etc) Other topics (physical health, mental health, etc) <div