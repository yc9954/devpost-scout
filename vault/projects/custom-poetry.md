---
slug: "custom-poetry"
url: "https://devpost.com/software/custom-poetry"
title: "Custom Poetry"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 214
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
---

# Custom Poetry

> Given any topic supplied by the user, this skill composes a new, custom poem about the topic.

[Devpost](https://devpost.com/software/custom-poetry) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]

**stack** amazon-web-services, c++, cuda, flask, javascript, machine-learning, python

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for custom poetry

## Body

Inspiration GARTNER, INC. :“By 2018, 20% of business content will be authored by machines.” We: “So is poetry!” What it does Given any topic supplied by the user, this skill composes a new, custom poem about the topic. How it was built Our backend system is based on the paper “Generating Topical Poetry; Marjan Ghazvininejad, Xing Shi, Yejin Choi, and Kevin Knight; EMNLP 2016”. We implement an API that accepts any topic phrase and returns a new poem composed by computer in real time. Challenges we ran into Designing the utterance user interface for Alexa. Accelerating our backend so that it can generate a four-line poem within 1 seconds. Tune the hyper parameters with human in the loop. Coming up with a skill name which is easily recognizable for Alexa. Accomplishments that we are proud of Speed up the whole pipeline using GPU (30s to 1s for generating a 4-line poetry - alexa motivated this speedup) Find a better hyper parameter by collecting a large amount of feedback from Amazon Mechanical Turk. What we learned Build a closed pipeline using : Amazon Web Services + Amazon Mechanical Turk + Amazon Alexa Skill. CUDA GPU acceleration technicals. What's next for Custom Poetry Maybe short stories on topics Maybe poems for other languages like Spanish. <div