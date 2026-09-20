---
slug: "tell-me-more-texpik"
url: "https://devpost.com/software/tell-me-more-texpik"
title: "Tell me more!"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 370
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Tell me more!

> You listen to your favorite podcasts and all the sudden, you think... Tell me more! Lets show you AI magic through: Diarization, Transcribing, Sentiment analysis, Extraction of persons, organizations.

[Devpost](https://devpost.com/software/tell-me-more-texpik) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** c#, dbrx, docker, node.js, particle, python, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tell me more

## Body

Inspiration My own daily podcast usage and how often I wish I could mark a segment for re-listen. But even better, to follow an inspirational speaker through other podcasts. What it does Through the workspaces and notebooks, it shows most of the different pieces to turn this into a functioning web app. It can do a DB vector search as it was the only endpoint I managed to make available outside Databrix. How we built it I used Databricks server-less clusters to run Python processing scripts and experiment with the different AI analysis functions. To save remote processing resources, I enlisted my local computer and GPU for the processing. Challenges we ran into Amount of data! Once you transcribe and segment episodes, you get thousands of new elements. They quickly turned out to be small and it will need further optimization to find the optimal length. The diarization libraries were often imprecise, which caused speaker biometric profiling invalid. This is still a work in progress and needs much more finetuning. Fully understanding where Databricks clusters run. I managed to run a small AWS bill inside the Databricks trial. There are many different pieces that still needs to be put together. How do you verify the AI learnings. This is another matter to be studied and I saw this very interesting blog post about using AI to verify AI. Accomplishments that we're proud of Starting with a wild idea and then learn, that it is now possible. The technologies are here and they are improving fast. What we learned A lot about Generational AI. All the building blocks that are now available to piece together an impressive solution. And... what is Databricks and their goals. What's next for Tell me more MVP! Make use of all the knowledge gained and turn it functional product. There will need to be players for mobile platforms. Find a strategy for start processing as many podcasts as possible and build up the speaker database. I spend a lot of time on experiments, Databricks Youtube videos and learning of what is even possible. I will continue to work on it and add the missing features, like speaker biometrics, social graphs. And make it fully functional. <div