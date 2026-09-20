---
slug: "real-time-detection-nudity-and-violence-images-2oga16"
url: "https://devpost.com/software/real-time-detection-nudity-and-violence-images-2oga16"
title: "Real Time Detection Nudity And Violence Images And Videos"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 478
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Real Time Detection Nudity And Violence Images And Videos

> Real-time AI image & Video analysis to detect nudity and violence, helping keep digital content safe using the Gemini 3 Flash API

[Devpost](https://devpost.com/software/real-time-detection-nudity-and-violence-images-2oga16) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[video_visual]] [[web_dom]]

**stack** express.js, javascript, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned

## Body

extension logo video showcase violence blocked image showcase violence blocked required parental pin to pause protection safe image parent set pin ( security ) protection paused ui blocked content dashboard ui extension dashboard ui (the rest ) extension dashboard ui Inspiration The idea for this project came from my daily experience surfing the internet , where I constantly encounter violent and explicit images and videos **. This type of content can be especially harmful for **teenagers , who may be exposed without any warning or protection. I wanted to build something useful that could help make online platforms safer by detecting sensitive content automatically and in real time . What it does Analyzes images in real time to detect nudity and violent content . Supports real-time video detection , analyzing the entire video by gemini in the background. Accepts images from URLs or external sources . Uses the Gemini 3 Flash API for fast and reliable image understanding. Automatically flags sensitive content to protect users, especially teenagers . Provides a clear safety decision : safe or inappropriate . Designed for easy integration into web platforms , applications , and moderation systems . Integration of ** test.html ** file in order to test the extension . How I built it I started by integrating the Gemini API for image analysis, focusing on detecting nudity and violence . The workflow is simple: Collect an image or a video Fetch and preprocess the data Send it to the * Gemini * Analyze the response and flag sensitive content In theory: $$ \text{Safety Decision} = f(\text{Image / Frame}) \rightarrow {\text{Safe}, \text{Sensitive}} $$ Where ( f ) is powered by the Gemini vision model . Challenges I ran into Gemini 1.5 did not perform well for this use case Gemini 2.5 Flash required tuning to achieve stable results Handling images from URLs caused parsing and format issues Ensuring real-time performance without latency was challenging Extending detection to processes the entire video holistically in the background before deciding if it is harmful in real time After multiple iterations, Gemini 3 Flash provided the best balance of speed , stability , and accuracy . Accomplishments that I’m proud of Built a real-time detection system for both images and video streams Successfully integrated the Gemini 3 Flash API Solved the challenge of processing images directly from URLs Implemented real-time video frame analysis Designed a clear and scalable moderation workflow Created a project focused on online safety , especially for teenagers Gained hands-on experience in API debugging , AI model selection , and performance optimization What I learned How to work with AI vision APIs , especially Gemini models How to handle image and video frame inputs from external sources How to debug API limitations and version issues How to design a real-time moderation system That choosing the right AI model version is critical for success <div