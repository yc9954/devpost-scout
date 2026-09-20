---
slug: "stealth-0oqm32"
url: "https://devpost.com/software/stealth-0oqm32"
title: "Cognit"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 400
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Cognit

> The world's first "Proof-of-Learning" protocol. We use biometric eye-tracking to prove you actually read the material, learned it, and we mint your certificate on the Kairo blockchain.

[Devpost](https://devpost.com/software/stealth-0oqm32) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** d3.js, gemini, kairo, meta-sam, next.js, python, react, solidity, tobii-sdk, websockets, wood-wide-ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for cognit

## Body

Eye Tracking Heatmap Statistics and Line Analysis Exam Inspiration In a world where AI takes tests instead of people, how do you verify knowledge? To answer this question, we built Cognit—the world’s first "Proof-of-Learning" protocol. We shift the focus from tracking simple inputs (clicks) to actual cognition using biometric hardware-backed verification. What it does Cognit is a "Proof-of-Focus" validation layer. Eye Tracking: We use a Tobii PC Eye 5 to track exactly where you are looking on the screen. Skim Detection: If you scroll past text without reading (missing horizontal saccades), the system locks the "Next" button. You can't proceed until you actually read. On-Chain Verification: Once you finish, we bundle your biometric data into an "Attention Score." If you pass, we mint a Soulbound Token on Kairo , proving you did the work. How we built it Hardware: We run a local Python script that interfaces with the Tobii SDK. It opens a WebSocket and streams raw (x, y) gaze coordinates to our frontend every 100ms. The Wood Wide AI model: We don't just check if you're looking at the screen. We batch the gaze data and send it to Wood Wide AI . Using Wood Wide AI, we trained a prediction model using 60,000 data points and use the model to determine if the user was actively parsing/reading the content. If not, their certificate is not minted on the blockchain. The Certificate (Kairo): We deployed a smart contract on Kairo that validates the Wood Wide score. It only allows minting if the "Focus Threshold" is met. Frontend: Built with Next.js . We used D3.js to render the realtime heatmap overlay on top of the PDF viewer. Challenges we ran into Coordinate Hell: Mapping raw eye-tracker coordinates (screen space) to the PDF text elements (DOM space) was a nightmare. We had to write a custom calibration offset so the heatmap didn't drift when the user scrolled. PCEye: The device is data locked and we had to reverse engineer the executable to intercept the data stream from the headset. Accomplishments that we're proud of The eye tracking is really good! We were able to use Kairo to successfully stamp and mint contracts onto the blockchain! What's next for Cognit Accessibility: Integrating ElevenLabs to read the text out loud if the system detects your eyes are getting tired. Integration: Building a plugin for platforms like Coursera or OSHA safety portals. <div