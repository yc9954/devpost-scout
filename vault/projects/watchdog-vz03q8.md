---
slug: "watchdog-vz03q8"
url: "https://devpost.com/software/watchdog-vz03q8"
title: "WatchDog"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 448
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# WatchDog

> A real time LLM based threat identification application.

[Devpost](https://devpost.com/software/watchdog-vz03q8) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** cv2, firebase, flutter, gemini, promptengineering, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for watchdog

## Body

Inspiration WatchDog was born from the desire to create a smarter and more proactive surveillance system. My first project was a framework for a surveillance bot, which laid the foundation for this idea. I wanted to go beyond just recording video—imagine a system that can actually "watch" what's happening and alert you when something unusual is going on. That’s how WatchDog came to life! What it does WatchDog is like having your own superhero security guard who never sleeps! It keeps an eye on things, analyzes video feeds in real-time, and uses AI to detect any suspicious activity. If it spots something fishy, it flags the event, writes up a detailed description of what happened, and saves the video snippet. Plus, it automatically uploads all this info to Firebase and logs it in Firestore so you can check it out anytime, anywhere. How we built it We built WatchDog using Python and OpenCV to handle video capture and processing. The real magic happens with Google Gemini AI, which analyzes the video and picks out any potential threats. Everything is managed with Firebase for storing videos and Firestore for logging events. We also built a smart queuing system to make sure all the video uploads and AI analyses happen smoothly, without a hitch! Challenges we ran into One of the biggest challenges was making sure WatchDog could handle a lot of data without getting overwhelmed. We had to set up a queue system to manage video uploads and AI processing, making sure nothing was missed. We also had to make sure all the different parts—like video capture, AI analysis, and cloud uploads—talked to each other perfectly without any miscommunication. Accomplishments that we're proud of We’re super proud of how WatchDog can actually understand what’s happening in the video. It’s not just recording—it's identifying suspicious behavior and alerting us in real-time. What we learned Building WatchDog taught us a lot about real-time video processing and cloud integration. We learned how to make different system parts work together like a well-oiled machine. We also learned the importance of having a strong error-handling and retry system so that if anything goes wrong, WatchDog can handle it smoothly without missing a beat. What's next for WatchDog Next up, we’re planning to give WatchDog some new superpowers! and less reliant on cloud based LLMs! we are planning to change our LLM to Llama's new local multimodel LLM - Llama 3.2:11b the only issue being it not available yet in development platforms like LMStudio or Ollama. Further we are gonna increase our scope to detect events like loitering or stalking though extensive fine tuning is needed for it. Nevertheless, we strive to achieve it. <div