---
slug: "a-i-kaigo-a-i"
url: "https://devpost.com/software/a-i-kaigo-a-i"
title: "介護A.I. [KaiGō A.I.]"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 457
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
---

# 介護A.I. [KaiGō A.I.]

> An A.I. powered voice cloning utility optimized for caretakers of special needs individuals

[Devpost](https://devpost.com/software/a-i-kaigo-a-i) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]]
  <sub>weak: elder_child_care</sub>
  <sub>weak: patient_family</sub>

**stack** coqui, customtkinter, gpt-neo, groq, python, tensorflow, tkinter, transformers, tts, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 介護a.i. [kaigō a.i.]

## Body

Interface Caregiver Script User Recording Inspiration Over the summer of my junior year, I participated in multiple different community service and volunteering activities to gain experience. This led me to interact with numerous different caretakers, mostly of special needs individuals, as well as elders. Talking to them, I identified key issues within their line of work, that I was positive could be solved with a targeted approach to the problem. It was then that I came up with the idea of KaiGō A.I.. To make sure that it does answer some of the daily challenges faced, I contacted some caretakers and ran the idea by them. Most were certain that this would be a great idea if implemented properly, while some had doubts regarding feasibility. Nevertheless, I pushed through and came up with an early prototype. I once again asked them to review it, and this time, everyone was convinced. Incidentally, I chose to name it KaiGō A.I., taken from the Japanese word for caretaker/helper, 介護士 [KaiGōShi] as a mark of respect and admiration to these heroes ensuring equality for all. What it does KaiGō A.I., in its simplest form, provides appropriate answers to a user's query (assumed to be a neurodivergent individual) in the voice of the caretaker, building on previously established emotional connections. It is engineered to work regardless of internet connection, with a backup Offline Mode relying on local computation. It takes two inputs, one permanent audio sample from the caretaker to recreate his/her voice, and a temporary audio sample from the user that can easily be recorded through the intuitive U.I. How we built it I first established a trial (testing) version testing each of the five individual components, i.e. Openai-Whisper, EleutherA.I.'s GPT-neo, Groq llama3 78b thru groq-api, CoquiTTS, and DistilBERTa, and then I integrated it into a Custom/Tkinter based GUI, and built QOL functionalities into it, and finalized the 1.0 version. Challenges we ran into Some Challenges we ran into were: Multiple conflicting dependencies due to deprecated modules used by some of the components that had to be overridden and patched before operation could be initialized. Integrating components into a singular script. Lengthy processing times that were cut short by implementing APIs Accomplishments that we're proud of End-to-end working application, it is task oriented and has a well-defined and clear-cut purpose, as well as incorporating an intuitive GUI with plenty of information on how to use it. It is engineered to make sure that absolutely everyone can understand What we learned I personally learnt how to implement TTS into my projects, and use multiple different APIs and modules seamlessly. What's next for 介護A.I. [KaiGō A.I.] Japanese Language Translation API conversion for mobile device use Increasing Efficiency by using a better workflow <div