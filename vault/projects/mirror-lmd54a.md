---
slug: "mirror-lmd54a"
url: "https://devpost.com/software/mirror-lmd54a"
title: "Mirror"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 490
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# Mirror

> Reflecting on your past work, relationships, and learning has never been easier. Mirror turns your minute-to-minute into a comprehensive and indexable knowledge base in the form of a journal.

[Devpost](https://devpost.com/software/mirror-lmd54a) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[transcript_audio]]

**stack** augmentos, elasticsearch, java, mistral, nextjs, react, typescript, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for mirror

## Body

Inspiration Remembering things is hard – and staying on top of your self improvement and reflection while juggling a busy schedule is even harder. As a team of busy students, one of whom recently started working a full time job, we decided to build Mirror as a tool to leverage unique smart glasses technology to revolutionize the way people handle self-improvement and reflection. What it does Mirror is an AI-powered app compatible on all AugmentOS -enabled smart glasses which transcribes your conversations and generates actionable insights and summaries tuned for reflection in real time. Our processing agents will automatically update on the Mirror web interface as you speak, intelligently picking out the most appropriate points to give a well-rounded overview of your day, extracting todos, a general snapshot of your day, and important reflection questions. Just as important as understanding the specific details of your day is being able to look back in time at past memories and see how they fit into the context of the rest of your memories. Mirror offers full-text semantic search through all memory content to allow for quick and easy retrieval and recall of specific details even if you only have a small idea of what you’re looking for. Furthermore, visualizing the relationships between memories is made easy and beautiful via Mirror’s 3-Dimensional memory map which displays latent connections between memories. Each edge and connected component tells a story and provides insights into the relationships between your experiences. The best part – all of this is generated via our processing pipeline in real time as you talk! Throughout the entire day, Mirror will always be up to date with your latest memory insights. How we built it Mirror is built in 3 parts: The AugmentOS Smart Glasses Client is an Android application written in Java which handles the interface with the smart glasses – handling both the voice transcription and relaying text back to the user via the display. Shoutout to the Mentra team for providing mentorship and lending us the Even Realities G1 Glasses that we built Mirror to work with. The backend is written in TypeScript via NextJS and handles interactions with both the smart glasses client and the web interface. Using ElasticSearch, Mistral AI, Vercel’s NextJS, and Codeium’s Windsurf, we created an intuitive interface to interact with your thoughts throughout the day. What we learned We learned that working with experimental hardware is hard – and persistence is key. We are the R&D for the software for these glasses, testing the limits of what’s possible with them and trying to push the field forward. What's next for Mirror We would love to continue expanding Mirror’s interaction with our users, especially in terms of active reflection throughout the day. We envision a world where our agents can prompt you during conversations about related past conversations, remind you of your past reflections, and help guide you towards a more productive, social future. <div