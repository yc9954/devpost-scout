---
slug: "focusmate-mbldun"
url: "https://devpost.com/software/focusmate-mbldun"
title: "FocusMate"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 414
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# FocusMate

> AI Powered Study Assistant

[Devpost](https://devpost.com/software/focusmate-mbldun) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Dashboard AI assistant Focus Sessions Analytics Home page Inspiration We noticed that students often struggle to stay focused during study sessions and don't get useful feedback on their learning habits. We wanted to create a smart study buddy that could track your attention in real-time and help you understand what works best for you. The goal was to make studying more effective by combining AI technology with personalized insights. What it does FocusMate is an AI-powered study assistant that tracks your focus, posture, and emotions while you study using your computer's camera. It generates personalized quizzes from your notes, helps you understand difficult concepts through an AI chatbot, and provides detailed analytics about your study patterns. The app also lets you connect with friends to compare study stats and stay motivated together. How we built it We built the frontend using React and Vite for a modern, responsive user interface with animations and real-time updates. The backend uses Python with Flask for the server, Google's Gemini AI for the chatbot and quiz generation, and MediaPipe for computer vision to track facial expressions and body posture. We integrated Clerk for user authentication and used Socket.IO to send live video frames from the browser to our ML models for analysis. Challenges we ran into Getting the computer vision to work smoothly was difficult because we had to balance accuracy with speed so the camera feed wouldn't lag. We struggled with version compatibility issues between MediaPipe and other Python libraries, which caused crashes until we found the right combination. Making all the different features work together (study sessions, AI chat, quizzes, analytics, and friends) required careful planning to keep the code organized and the user experience seamless. Accomplishments that we're proud of We successfully created a fully functional AI study assistant that actually works in real-time with live camera analysis and instant feedback. Our quiz generator can take any topic or uploaded document and create personalized practice tests with detailed explanations. The analytics dashboard provides meaningful insights that can genuinely help students improve their study habits and track their progress over time. What we learned We learned how to integrate multiple AI technologies (Gemini, MediaPipe, emotion detection) into one cohesive application that runs smoothly. Working with real-time video processing taught us about performance optimization and how to handle data efficiently between frontend and backend. We also gained experience in full-stack development, from designing clean user interfaces to building robust backend APIs and managing user data securely. <div