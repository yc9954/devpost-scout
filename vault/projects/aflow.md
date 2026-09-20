---
slug: "aflow"
url: "https://devpost.com/software/aflow"
title: "voki"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 361
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# voki

> audio messaging revisited.

[Devpost](https://devpost.com/software/aflow) · hackathon [[HackZurich 2021]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** azure, firebase, hugging-face, javascript, python, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voki

## Body

logo GIF login and register GIF recording a new message GIF sentiment analysis and transcript Inspiration Complex communication and social interaction is one of the major characteristics that define us as humans. We believe that even with today's amazing technologies, communication is one of the bottlenecks in human interaction. We wanted to explore and enable new ways of communication, only available now because of recent developments in computation and artificial intelligence. What it does voki is an audio messaging app that reimagines chat messaging. Using sentiment analysis, voki gives visual feedback of the other person's emotions in an audio message. By using topic detection, we give summarized information to the user of the audio message's content. Tapping at any of the keywords one can navigate quickly to the related audio timestamp. Long pressing on the summary keywords, provides a full transcript of each message! How we built it To build voki , we used React-native as a front-end framework, coupled with Firebase for our database functioning. Our various NLP tasks are facilitated through a custom back-end API in Python and Microsoft Azure's speech-to-text functionality. Challenges we ran into Many steps were challenging like always during an Hackhaton. One on the most challenging one was to patiently debug the cloud functions which we had no experience with. Also, since none of us was a UI developer, we faced particular challenges in styling the app the way we envisioned. Accomplishments that we're proud of The overall design of the app and the features all work smoothly which we are very excited about. We are happy that we managed to build a fully working app and look forward to developing it even further. What we learned We learned a LOT, it was the first real mobile app that any of our team members developed. What's next for voki We will be thrilled to receive feedback from HackZurich and our friends and families and then decide what direction we should take. From the technical side, we have loads of features and UI improvements we want to make. We really believe voki has a potential to bring a new paradigm in the digital communication world. <div