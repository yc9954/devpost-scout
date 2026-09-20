---
slug: "speech-companion"
url: "https://devpost.com/software/speech-companion"
title: "Speech companion"
hackathon: "Civo Hackathon 2021"
organization: "Civo"
winner: true
words: 259
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/transcript_audio"
---

# Speech companion

> Want a clerk who prints whatever you say? Or you need someone to read a big passage for u?

[Devpost](https://devpost.com/software/speech-companion) · hackathon [[Civo Hackathon 2021]]

## Facets

**domain** [[education]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[transcript_audio]]

**stack** civo, css3, docker, html5, kubernetes, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for speech companion

## Body

speech companion UI Inspiration We as students always struggle with assignments and projects. Most of this work requires reading a big amount of text. We always wished there was a technology that can read the given text for us and also write the given text. So we built a project named Speech Companion. What it does Speech Companion can convert your given speech into text for convenience. It can also read the given text for you making your work a lot easier. How we built it We built it using a react hook that converts speech from the microphone to text and makes it available to React components. useSpeechRecognition is a React hook that gives component access to a transcript of speech picked up from the user's microphone. Challenges we ran into Using the in-built JavaScript speech recognition method. After making the project we realized that the text recognition was having trouble with blank spaces. So we replaced all the blank spaces to make it easier for npm to read. Accomplishments that we're proud of We were successfully able to deploy our application using the Civo platform. What we learned We learned a lot about text and speech recognition libraries. We also learned more about Kubernetes and managing containerized workloads and services. What's next for Speech companion Speech Companion has a lot of improvements to make yet. We can design it such that it can also be used in different languages, also we can give users the best experiences by changing the accent and speed for the better. <div