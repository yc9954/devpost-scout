---
slug: "lotion-ai-ar"
url: "https://devpost.com/software/lotion-ai-ar"
title: "Lotion AI/AR"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 388
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Lotion AI/AR

> Lotion is the Notion Killer. Lotion provides slippery smooth notes supercharged by AI and AR. Our immersive platform combines Augmented Reality and AI to make assisted learning available to all!

[Devpost](https://devpost.com/software/lotion-ai-ar) · hackathon [[ShellHacks 2024]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** axios, chatgpt, computer-vision, expo.io, firebase, flask, google-vision, huggingface, javascript, mongodb, python, react-native, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lotion ai/ar

## Body

Inspiration We came up with this idea when one of our teammates was studying for statistics before the beginning of the Hackathon. He realized that he was spending ages and ages navigating through the uncountable amounts of hopelessly long notes he had taken for his first exam. Thus, we had the idea to create an AI powered note taking platform that classified, stored, and retrieved notes whenever you needed. Not only does it take away all the headache of searching through your notes by providing a note querying system based on your questions, it has an immersive AR based system that scans your homework to return the most relevant notes! What it does ✨ Note Classification: Automatically classifies and stores your handwritten or typed notes based on content and the classes you are taking 🚀 AR Note Annotations: Overlays relevant notes based on scanned information from your camera 🔧 Note Querying: Returns relevant notes based on text input questions or statements 📈 Interactive Interface: Ease of access to all taken notes How we built it Using React Native, we created a fully functioning note taking app. In the Flask backend, we used Google's Cloud Vision API to process handwritten notes into processable text to be read using the ChatGPT API. A combination of Firebase for authentication and MongoDB for document storing/querying was used. We tied it all together into an AR feature using ExpoGo's Camera tools. Challenges we ran into One of our major bottlenecks was connecting our backend and frontend. This was a result of poor communication, perhaps because we didn't sleep. We worked around this by creating a quick api documentation and having a meeting to discuss what endpoints the frontend needed. We also had issues using FireStore because of the collection - document system, which we didn't need. We switched to MongoDB for its simplicity. Accomplishments that we're proud of We are proud of interlinking so many moving parts into one working product. It was satisfying seeing every endpoint, react component, and api call come together as we finished our AR feature. What we learned We learned how to use Google's API What's next for Lotion AI/AR If we get positive impact, we would push out a more mature version; we hope students could actually use this product. Made with ❤️ from Team Lotion <div