---
slug: "offline-education"
url: "https://devpost.com/software/offline-education"
title: "Noor"
hackathon: "Google's Women Techmakers presents She Builds AI"
organization: "Google"
winner: true
words: 420
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
---

# Noor

> Afghan girls have been banned from school since 2021, with limited internet access. Noor is an offline AI tutor that runs locally, helping them prepare for college and continue learning from home.

[Devpost](https://devpost.com/software/offline-education) · hackathon [[Google-s Women Techmakers presents She Builds AI]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]

**stack** gemma, python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for noor

## Body

Initial device setup Fine-tuned Gemma 2B running locally on the Raspberry Pi 5 with Ollama Raspberry Pi 5 connected to speakers Inspiration Noor addresses an acute crisis affecting millions of girls. When the Taliban banned girls' education in 2021, our teammate Dunya witnessed her friends and family lose access to schooling. Many don't have access to reliable internet, making learning from home nearly impossible. This drove us to create a solution that works without internet and within current restrictions - an AI tutor that brings education directly to girls who need it most. What it does Noor is an offline AI tutor that girls can speak with naturally in both Farsi and English. It provides personalized guidance for college applications, answers questions about educational opportunities, and offers academic support - all without internet access. The conversational interface makes learning feel natural and supportive, similar to talking with a knowledgeable friend who understands their unique circumstances. How we built it We fine-tuned Gemma 2B model with context-specific knowledge about education access, college applications, and the unique challenges faced by Afghan girls. Our pipeline includes: Speech input using Google Speech Recognition Local inference using Fine-tuned Gemma via Ollama Coqui text-to-speech model for natural Farsi responses Everything runs offline on a Raspberry Pi 5, making it truly accessible anywhere Challenges we ran into Ensuring accurate Farsi language processing throughout the pipeline Optimizing the model to run smoothly on limited hardware Dealing with hardware constraints (had to do a last minute dongle run when we realized the audio jack is missing on Pi 5) Balancing model size with performance for offline use Creating culturally appropriate responses that reflect local realities Working as a remote team made it more difficult to test the project live Accomplishments that we're proud of Created something that could make a real difference in girls' educational access What we learned The challenges of multilingual AI development and complexity of building offline-first solutions What's next for Noor We absolutely want to make this project a reality. This is a real and urgent problem. Hardware optimization: Finding the most cost-effective hardware configuration to make Noor widely accessible Enhanced learning materials: Including offline educational content, interactive exercises, and games Personalization: Implementing memory features so each Noor device builds context about its user over time Expanded subjects: Adding comprehensive tutoring for English, math, science, and history Community feedback: Working with Afghan girls to continually improve the system Distribution strategy: Developing safe ways to get devices to girls who need them Thumbnail source: https://www.abc.net.au/news/2023-03-23/afghanistan-taliban-ban-high-school-girls-education-impacts/102107162 <div