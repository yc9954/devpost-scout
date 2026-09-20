---
slug: "coffee-copilot"
url: "https://devpost.com/software/coffee-copilot"
title: "Coffee Copilot"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 321
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# Coffee Copilot

> Streamline your post-coffee chat routine with Coffee Copilot! We transcribe, summarize, and suggest talking points. Maximize your networking efficiency.

[Devpost](https://devpost.com/software/coffee-copilot) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]]

**stack** assemblyai, cockroachdb, cohere, fastapi, next.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coffee copilot

## Body

app app gene Inspiration In the fast-paced world of networking and professional growth, connecting with students, peers, mentors, and like-minded individuals is essential. However, the need to manually jot down notes in Excel or the risk of missing out on valuable follow-up opportunities can be a real hindrance. What it does Coffee Copilot transcribes, summarizes, and suggests talking points for your conversations, eliminating manual note-taking and maximizing networking efficiency. Also able to take forms with genesys. How we built it Backend : Python + FastAPI was used to serve CRUD requests Cohere was used for both text summarization and text generation using their latest Coral model CockroachDB was used to store user and conversation data AssemblyAI was used for speech-to-text transcription and speaker diarization (i.e. identifying who is talking) Frontend : We used Next.js for its frontend capabilities Challenges we ran into We ran into a few of the classic problems - going in circles about what idea we wanted to implement, biting off more than we can chew with scope creep and some technical challenges that seem like they should be simple (such as sending an audio file as a blob to our backend 😒). Accomplishments that we're proud of A huge last minute push to get us over the finish line. What we learned We learned some new technologies like working with LLMs at the API level, navigating heavily asynchronous tasks and using event-driven patterns like webhooks. Aside of technologies, we learned how to disagree but move forwards, when to cut our losses and how to leverage each others strengths! What's next for Coffee Copilot There's quite a few things on the horizon to look forwards to: Adding sentiment analysis Allow the user to augment the summary and the prompts that get generated Fleshing out the user structure and platform (adding authentication, onboarding more users) Using smart glasses to take pictures and recognize previous people you've met before <div