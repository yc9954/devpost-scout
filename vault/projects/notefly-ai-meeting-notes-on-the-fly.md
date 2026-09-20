---
slug: "notefly-ai-meeting-notes-on-the-fly"
url: "https://devpost.com/software/notefly-ai-meeting-notes-on-the-fly"
title: "Notefly - AI Meeting Notes on the Fly"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 389
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Notefly - AI Meeting Notes on the Fly

> Notefly is your real time online meeting note taker. See meeting transcript and AI summary while on the call. Always stay on point with short notes from your personal typist for meetings.

[Devpost](https://devpost.com/software/notefly-ai-meeting-notes-on-the-fly) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** agora, fetch.ai, gemini, mongodb, next.js, react, tailwid, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for notefly - ai meeting notes on the fly

## Body

landing_page app us Inspiration We are students at Minerva University which uses innovative curriculum and learning methods. Online forum classes is how we learn, they require active participation. While on the classes, we might doze off or forget about something discussed, which diminishes our grades. We always wanted a live, automatic AI note taker so we won't need to take notes all the time. What it does Our product, Notefly, turns the talks in the meetings into live transcript text. Then it turns the transcripts into short note blocks, a 40 words speech becomes 10 words. The short note blocks turn into bullet points and bullet points turn into main idea summary notes. All these summaries can be seen while in the meeting so everyone knows what we are discussing and important details, like a customers mail address. How we built it Started by using agora's SDK to create a basic web conferencing software using next.js for the frontend. Then used agoras transcription features and figured out how we retrieve, store and process that data using fetch.ai agents. Used gemini for processing and mongo.db for storing data Challenges we ran into Our tech stack didn't exactly matched with the project. Storing transcripts was a BIG bugger, we thought agora had place to store data but they didn't. we tried to send to singlestore but that didn't worked properly as well. Making fetch.ai agents work and make them retrieve and send data, and communicate with each other was also a problem. Making the app live update was also a challenge. Accomplishments that we're proud of IT FUC'IN WORRKKS!!! What we learned How to create a video calling app, something that we have 0 knowledge about, using tools that we have 0 knowledge about. Also deciding on the idea took much longer than it should, we will focus on not the perfect but the most applicable and team friendly idea next time. What's next for Notefly - AI Meeting Notes on the Fly After an all-nighter, the app is far from done, there could be more improvements in the summary logic. We can turn this into a more scalable product that allows people to host their own meetings in the cloud, its on a local host that lives in agoras serves now, we sadly can't send try us links rn. <div