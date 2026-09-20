---
slug: "sayme"
url: "https://devpost.com/software/sayme"
title: "Sayme"
hackathon: "Facebook Hackathon: Messaging"
organization: "Facebook"
winner: true
words: 411
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Sayme

> A chatbot assistant for travers, with the use of translations an image processing.

[Devpost](https://devpost.com/software/sayme) · hackathon [[Facebook Hackathon- Messaging]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ai-applied-language-detection, facebook-messenger, google-cloud, node.js

## How they structured the write-up

- 🦄 a mission in front a problem 🧟‍♀️
- 🔮 architecture
- 👨🏻‍💻 tech stack
- 👩🏻‍🔬 what i learned
- 📝 what's next for sayme
- 🐨 fun facts
- test and tell me what do you think?

## Body

🎒 Sayme 📚 A messenger attendance for keep speaking 🦄 A Mission in front a problem 🧟‍♀️ In my city, as in many other cities, the internet has a low bandwidth, and when tourists visit it, they may find it difficult to access applications that consume too much data, but messenger continues to work despite having an internet of low bandwidth and the fact of integrating a translation solution, in a messenger conversation it could help people who are traveling or who live in remote regions and who want to learn another language. ✨ if you see something that I can fix or integrate I'm open for feedback. 😊 🔮 Architecture I create a webhook through the use of node and express, I exposed my localhost to the Facebook webhook with ngrok, through which I send and receive the requests to messenger, when I receive a specific request For a translation I consume an internal service that I use to call the google translations API, I clean the request and send input back, some of the requests I send them as JSON to IA Platform where I use them for self-training and the result I return it as a JSON to be able to use it in some future. The part of the images I receive the request if when I receive it I detect it as an image I receive it, I send it to my service and I consume the image processing API to be able to detect the elements of the image. 👨🏻‍💻 Tech Stack ✅ Messenger Platform ✅ Ngrok ✅ Node.js ✅ Express ✅ IA Platform ✅ Vision API ✅ Natural Language API 👩🏻‍🔬 What I learned In this awesome travel between different assistants platforms and ecosystems, I take the opportunity to create awesome things with the use of messenger, a backend core build in node.js and express and build an IA model with the use of IA Platform ( Google Cloud Platform ) References used for this project. Course of Chatbots by Developer Circles Mexico City, Thanks Adan Messenger Platform Chatbot Concepts - Google Cloud Integrate the Vision API Chatbot Using Google Cloud AI Building Blocks 📝 What's next for Sayme ✨ Add new languages ✨ Training with a big data set ✨ Increase Vocabulary ✨ Add a Learning Mode 🐨 fun facts When I was testing on the subway, I fell down the stairs 😭. Test and tell me what do you think? m.me/okeysayme <div