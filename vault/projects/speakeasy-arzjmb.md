---
slug: "speakeasy-arzjmb"
url: "https://devpost.com/software/speakeasy-arzjmb"
title: "SpeakEasy"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 474
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
---

# SpeakEasy

> SpeakEasy gives nonverbal users a voice. Built on Snap Spectacles, it detects the world around them, offers smart prompts, and speaks responses instantly.

[Devpost](https://devpost.com/software/speakeasy-arzjmb) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]

**stack** bluetooth, gemini, groq, lensstudio, spectacles, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for speakeasy

## Body

SpeakEasy (Colorful Home) SpeakEasy (Outdoor Evening) system architecture diagram lots of crashes later... Inspiration We were inspired by how isolating conversations can feel without a voice. Many existing assistive communication tools are bulky or require users to look away from others, making social interactions even harder. We wanted to create something that blends into daily life and helps nonverbal users feel confident and included in conversations. What it does SpeakEasy is an assistive communication device built on Snapchat Spectacles to empower people who are nonverbal or speech-impaired. Using an object detection system powered by Gemini and accelerated by Groq, the glasses analyze the user’s surroundings and generate context-aware conversation prompts on an interactive AR keyboard built in Lens Studio. Users select responses through a small handheld controller, which are then spoken aloud through the glasses. How we built it We integrated Gemini’s object detection model to understand the user’s surroundings and ran it through Groq for ultra-fast language generation. We then built a custom AR keyboard in Lens Studio where prompts are displayed and navigated via a handheld controller. Finally, the selected response is converted to speech and played through the glasses, completing an end-to-end assistive communication pipeline. Challenges we ran into Our biggest challenge was merging all the components together into one smooth experience. We also faced difficulties building the keyboard interface in Lens Studio, as none of us had prior experience with it or other AR platforms. Optimizing for low latency while managing multiple systems (LLM, controller, and speech output) was also challenging. Huge shout-out to the Snap mentors - Alessio, Jesse, and both Stevens - for their patience, insightful suggestions, and time! We learned so much from everything they shared. Accomplishments that we're proud of We’re proud to have taken on a challenging project in a completely new environment and pushed ourselves outside our comfort zones. Even though the system isn’t fully complete yet, we managed to connect multiple complex components and build the foundation for an assistive tool that could truly make a difference. This experience showed us that real-time object detection and language generation can be combined on wearable hardware - and that we’re capable of learning fast under pressure. What we learned We learned a lot about building for AR and using Lens Studio, from designing custom interfaces to integrating real-time content on Snapchat Spectacles. We also learned how to combine object detection with language generation, optimize inference on low-latency hardware using Groq, and rapidly prototype hardware-software systems while keeping user experience at the centre. What's next for SpeakEasy Next steps include enabling real-time object detection directly on the glasses (without interactive previews), expanding prompt options for each detected object, refining the keyboard and interface for faster navigation, attaching a louder speaker to improve conversational clarity, and conducting interviews with our intended user base of nonverbal users. <div