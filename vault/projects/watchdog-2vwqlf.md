---
slug: "watchdog-2vwqlf"
url: "https://devpost.com/software/watchdog-2vwqlf"
title: "Watchdog"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 513
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
---

# Watchdog

> Help us make our schools safer.

[Devpost](https://devpost.com/software/watchdog-2vwqlf) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]

**stack** chroma, convex, deepgram, express.js, fetch.ai, groq, hyperbolic, javascript, next.js, python, tailwindcss

## How they structured the write-up

- what inspired us to build it
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for watchdog

## Body

What inspired us to build it Guns are now the leading cause of death among American children and teens, with 1 in every 10 gun deaths occurring in individuals aged 19 or younger. School shootings, in particular, have become a tragic epidemic in the U.S., underscoring the urgent need for enhanced safety measures. Our team united with a shared vision to leverage AI technology to improve security in American schools, helping to protect children and ensure their safety. What it does Our product leverages advanced AI technology to enhance school safety by detecting potential threats in real-time. By streaming surveillance footage, our AI system can identify weapons, providing instant alerts to security personnel and administrators. In addition to visual monitoring, we integrate audio streaming to analyze changes in sentiment, such as raised voices or signs of distress. This dual approach—combining visual and auditory cues—enables rapid response to emerging threats. How we built it We partnered with incredible sponsors—Deepgram, Hyperbolic, Groq, and Fetch.AI—to develop a comprehensive security solution that uses cutting-edge AI technologies. With their support, we were able to conduct fast AI inference, deploy an emergency contact agent, and create intelligent systems capable of tracking potential threats and key variables, all to ensure the safety of our communities. For real-time data processing, we utilized Firebase and Convex to enable rapid write-back and retrieval of critical information. Additionally, we trained our weapon detection agent using Ultralytics YOLO v8 on the Roboflow platform, achieving an impressive ~90% accuracy. This high-performance detection system, combined with AI-driven analytics, provides a robust safety infrastructure capable of identifying and responding to threats in real time. Challenges we ran into Streaming a real-time AI object detection model with both low latency and high accuracy was a significant challenge. Initially, we experimented with Flask and FastAPI for serving our model, followed by trying AWS and Docker to improve performance. However, after further optimization efforts, we ultimately integrated Roboflow.js directly in the browser using a Native SDK. This approach gave us a substantial advantage, allowing us to run the model efficiently within the client environment. As a result, we achieved the ability to track weapons quickly and accurately in real time, meeting the critical demands of our security solution. Accomplishments that we're proud of We are incredibly proud of the features our product offers, providing a comprehensive and fully integrated security experience. Beyond detecting weapons and issuing instant alerts to law enforcement, faculty, and students through AI-powered agents, we also implemented extensive sentiment analysis. This enables us to detect emotional escalations that may signal potential threats. All of this is supported by real-time security data displays, ensuring that key decision-makers are always informed with up-to-the-minute information. Our system seamlessly brings together cutting-edge AI and real-time data processing to deliver a robust, proactive security solution. What we learned We learned that the night is darkest right before the dawn... and that we need to persevere and be steadfast as a team to see our vision come to fruition. What's next for Watchdog We want to get incorporated in the American school system! <div