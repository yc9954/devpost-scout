---
slug: "pendantic"
url: "https://devpost.com/software/pendantic"
title: "Hippo"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 401
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/social_worker"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Hippo

> Computing conversational quality and identifying logical fallacies for productive communication.

[Devpost](https://devpost.com/software/pendantic) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[social_worker]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** elevanlabs, fal, lovable, make, python, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hippo

## Body

Inspiration Inspired by the HIPPO effect—where the Highest Paid Person’s Opinion often dominates discussions—we set out to build a tool that ensures meetings are driven by logic, fairness, and data, rather than hierarchy and bias. Our AI-powered application sits in on meetings, analyzing logical fallacies, sentiment dynamics, and speaker balance to foster more productive and inclusive conversations. By surfacing objective insights in real-time, we help teams move beyond the HIPPO and toward truly collaborative decision-making. What it does Intakes both real-time and bulk audio from a meeting and analyzes the sentiment, lexical density, information density, contributions, and logical fallacies. How we built it Our solution involved directly integrating with microphone audio and establishing a WebSocket connection to an Automatic Speech Recognition (ASR) provider, which provided diarized ASR outputs. These outputs were stored in a backend database. The transcript was displayed on the frontend, which was developed using Lovable and Cursor, updating in real-time as it was generated. This real-time transcript was then transmitted to a set of low-latency agents powered by SambaNova, utilizing the Llama 3.3 70B model. These agents performed various analyses, including information density assessment, semantic analysis, entropy measurement, logical fallacy detection, and controversy analysis. Challenges we ran into The diarization of real-time audio feeds posed significant challenges, particularly due to the limited availability of providers offering both streaming and event-based outputs. Converting the WebSocket stream into batch processing and ensuring seamless integration across the entire pipeline, from microphone input to frontend output, presented another major challenge. Additionally, the high volume of calls to the LLMs resulted in rapid rate limiting. Achieving and maintaining ultra-low latency throughout the entire pipeline was another significant hurdle. Accomplishments that we're proud of Real time pipeline that can diarize multiple speakers in one microphone and advanced language analytics that can be used to create comprehensive analysis of users. What we learned We learned a lot about current challenges in diarization of speakers, and how many companies just rely on the fact that meetings use multiple microphones to create high quality seperation in speaker numbering. What's next for Hippo Clustering of speaker types based on the different qualities they have such as "engaging" for a person who frequently speaks before a person that rarely speaks does. Set triggers for AI interaction such as when a speaker dominates the interaction. Integration into meetings directly (google meet, zoom, teams) More agent connectors. Bug fixes! 🐛🐛🐛 <div