---
slug: "convey-wg5bnj"
url: "https://devpost.com/software/convey-wg5bnj"
title: "Convey"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 1045
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/sensor_telemetry"
---

# Convey

> Convey is a web extension that uses NLP and ML to give real-time communication feedback - imagine Grammarly for speech. Leverage your unique voice and convey with confidence!

[Devpost](https://devpost.com/software/convey-wg5bnj) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**substrate** [[sensor_telemetry]]

**stack** cockroachlabs, googlecloudproducts, natural-language-processing, python, pytorch, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for convey
- business viability

## Body

Convey with confidence! Convey pops up before a meeting to give reminders and help you set an intention After a call, Convey gives an analysis of where you did well, progress over time, improvement areas, and feedback on your presence Inspiration Effective communication is one of the most important skills ; I'm sure we've all been in a position where we know what to say but can't quite present ourselves how we want in order to convey. The inspiration stemmed from this exact issue and the desire to speak with confidence. During the pandemic, nearly every meeting is virtual and we saw this as a massive opportunity to create a tool that gives feedback on something everyone already does. What it does Convey uses natural language processing and AI to analyze speech and give helpful insights. It's a Chrome extension that pops up before a user enters a call, reminding them of areas to focus on such as filler words and pacing. Users can also set an intention for the call of what kind of impression they want to make (ex: confident, enthusiastic, calm). After they leave the call, a dashboard pops up showing them how they did, what they did well, and a graph of their progress over time. Most importantly, it also tells them where they need to improve and actionable advice. Additionally, it shows how closely their presence aligned with their intention. Convey is super easy to use and essentially trains you to drastically improve on something you already do every day! How we built it We started with sticks and stones - well almost at least. It began with using Google Colab and sentiment analysis data to train a Bert-Transformer model. Now we’re newbies when it came to PyTorch and Attention mechanisms, but we eventually got a working model that could detect the tone! We hooked it up with countless packages to record audio, transcribe it into text. feed it into the model --> and it worked! But that was only the start. We wanted to go bigger! Infrastructure! Connecting to users! Long-term storage of Metrics! Capability to scale up! Reinforce habits through text messages! We noticed 3 sponsors that could help us out: Google Cloud, Cockroachdb, and Twilio! So now the process goes like this: Data is recorded during Google Meet / Zoom --> This is sent to Google Cloud Storage. Using Google Speech to Text we transcribe the audio into a text format. Now we take the mp3 audio and text and put it into the ML Model (which was re-trained on Google Cloud). This outputs the sentiment analysis, which is sent back to the user, and sent to Cockroachdb for long-term storage. Through Twilio’s API we send text messages to the users to remind them throughout the day on how to improve, acting as their own digital personal assistant. Challenges we ran into This hackathon was filled with many challenges - we purposely choose an ML area where we didn't know too much in (NLP, Attention, PyTorch), which was a challenging and humbling experience. In addition to that, we choose to somewhat restart our project and move everything to the sponsor's side. We had never played with Google Cloud, Cockroach DB SQL, or Servers before so it was an interesting learning experience! This proved to be a great decision after seeing all of the powerful tools and features they included. We made it somewhat purposefully challenging for ourselves because we wanted to maximize our learning. Accomplishments that we're proud of We're really proud of being able to step up to the challenges and be able to use so many new areas of ML (NLP, Attention, PyTorch) and SWE tools (Google Cloud, Cockroach DB, and Twilio). In addition, we are proud that we were able to come together as a team and fulfill our roles to complete the hackathon! It was stressful at times (like submitting literally last minute). But we did it! What we learned We learned so much in terms of the technical areas; using machine learning and having to pivot from one software to the other, figuring out how to store data on Cockroach DB, trying to utilize Google Cloud to the best of our ability, and more! We kept preaching that done was better than perfect to keep the flow going and to our surprise, it kept us captivated by the problem we were trying to solve and everything from the design to the actual code itself! The biggest thing for us was to keep moving forward and we'll be taking that mantra with us into the next competition! What's next for Convey We want Convey to empower future leaders, entrepreneurs, and founders on their journey to become the best presenters they can be. We don't have to imagine a system that helps us identify our presentation pitfalls in real-time, we have that! We hope the extension will be used far and wide to improve the flow of speakers everywhere and help them gain confidence in their abilities. Business Viability We aim for Convey to have two separate plans: a free Basic version and a paid Premium version. The Basic version contains speech-to-text software that analyzes your tone, pacing, clarity, pausing and progress over time. For a small monthly fee, the Premium version gets you more advanced features like analyzing the number of filler words you used and providing detailed feedback on your presence (enthusiasm and confidence over the duration of the call) in addition to all the Basic features. Effective communication is something we all need, but in terms of tools, this is pretty much an untapped market. There are a few apps on the market that make users do specific and often tedious vocal exercises and give critique. These have amassed a small but loyal user base, acting as proof of concept for Convey. Now think if a tool could integrate into a user’s actual life in real-time, helping them convey ideas a little bit better with every meeting. Imagine Grammarly, but for speech - there's no product on the market like this. Your voice is solely unique to you, and it’s an asset we believe people should be able to train and improve … so that anyone can convey with confidence! <div