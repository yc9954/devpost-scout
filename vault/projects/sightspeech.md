---
slug: "sightspeech"
url: "https://devpost.com/software/sightspeech"
title: "SightSpeech"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 784
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/legal_justice"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SightSpeech

> Text-to-speech is a near-essential tool for the legally blind; However, normal things like signs, classroom boards, etc., do not have this tool. SightSpeech aims to help solve this issue.

[Devpost](https://devpost.com/software/sightspeech) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[legal_justice]]
**substrate** [[video_visual]] [[web_dom]]

**stack** ai, easyocr, flask, gemini-api, git, github, html, javascript, mediapipe, next.js, python, react, tailwind-css, text-to-speech-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for sightspeech

## Body

Inspiration On a computer, accessibility tools like screen readers are lifelines for the millions of people on the spectrum of legal blindness. The ability to navigate a webpage and have text read aloud provides critical access and independence. But what happens when you step away from the screen? That essential accessibility vanishes. The physical world that is full of crucial text on street signs, menus, and classroom boards is now completely silent. For many of us, a pair of glasses is an instant fix for blurry vision. For the legally blind, however, there is no simple tool to decipher this environment. Our inspiration was to bridge this gap. We wanted to take the simple, powerful concept of a screen reader and apply it to the real world. SightSpeech was born from a simple question: What if you could point your camera at any text and have it read aloud, bringing the accessibility of the web into your daily life? What it does SightSpeech is an assistive tool for the legally blind that combines hand gestures, Optical Character Recognition, and text-to-speech. Users can perform gestures like “capture scene” to hear a spoken description of their surroundings, or “capture POV” to detect nearby text and navigate it with “tab forward” and “tab backward” gestures. With each tab, the system reads aloud the highlighted word, giving users hands-free awareness of both their environment and any text in view. How we built it SightSpeech is powered by computer vision and multimodal AI. We used EasyOCR to detect words in the camera’s point of view and draw bounding boxes around them. With the capture POV gesture, users can tab forward or backward through those words, each one being read aloud via text-to-speech. To improve accuracy, we also incorporated the Gemini API to cross-check and enhance word detection when OCR alone might miss details. For hands-free interaction, we integrated Google’s MediaPipe Vision to recognize ASL and custom gestures, mapped to actions like “tab forward,” “tab backward,” “capture scene,” and “capture POV.” These gestures make it seamless for users to explore text or capture their surroundings without relying on physical input, ensuring both accessibility and independence. Challenges we ran into The challenges we ran into were with flask and the different apis, that we tried to use. This was our first computer vision project, coming in we did not know anything about any of tools used. At first we tried using tesseract api, however with tesseract it was not able to detect hand writing or anything that was not sans serif. Oftentimes it would detect words in nothing. Working with flask was a piece of work as we had a hard time trying to figure out how we would combine Mediapipe.js with EasyOCR, as both wanted their own camera. Mediapipe.js was in the frontend and easyocr was in the backend which was a headache because both wanted live videos to work, which would require two cameras to work. we tried doing Mediapipe in python however the probem became that the dependencies would clash with each other so they had to be seperate, and even if they could be both installed with their dependencies, it would not have worked as we would need a beefy computer. One of my teammates had this problem: " I tried using Google Colab to train custom models for the gesture detection, but due to my OS being a mac and incompatible installations of pip, python3, etc, I had to resolve the issue by mathematically calculating the different distances provided by Mediapipe's skeletal motion tracking system." Accomplishments that we’re proud of We’re proud that we successfully integrated EasyOCR with MediaPipe to create a working prototype of SightSpeech. Despite being our first computer vision project, we managed to get text detection, gesture control, and text-to-speech all working together in a seamless pipeline. Building a system that can recognize gestures and navigate text in real time felt like a big step forward for us. What we learned We learned how to work with OCR models, gesture recognition libraries, and Flask to bridge the backend and frontend. Along the way, we gained experience in debugging dependency issues, handling live video streams, and combining multiple APIs into one cohesive system. Most importantly, we learned how to collaborate as a team to solve tough integration problems and turn ambitious ideas into a working prototype. What's next for SightSpeech Right now we are using two cameras: one as a usb video cam and one as the laptops's camera. We want in the future to only have one camera, and to just have it small enough where it can be placed on your glasses or as the glasses itself like the Meta raybans <div