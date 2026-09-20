---
slug: "bookbutler"
url: "https://devpost.com/software/bookbutler"
title: "BookButler"
hackathon: "Build your Flutter Butler with Serverpod"
organization: "serverpod"
winner: true
words: 511
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# BookButler

> Meet your AI Book Butler! 🎩 It summarizes PDFs, explains complex text, saves snippets and Notifies users via Serverpod. Stay sharp with reading streaks, leaderboards, and smart home-widget nudges.

[Devpost](https://devpost.com/software/bookbutler) · hackathon [[Build your Flutter Butler with Serverpod]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[developer]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** android, fcm, firebase, flutter, rive, serverpod, serverpodcloud, vscode

## How they structured the write-up

- project story
- built with

## Body

Dashboard pdf screen AI text assistant explaining sections Homewidget Reminder Ask AI feature Point notifications Project Story Inspiration The spark for Book Butler came from a personal need for accountability. While digital libraries are convenient, they often lack the motivational "nudge" of a reading partner. I wanted to move beyond just having a folder of PDFs and create a true companion. My goal was to build a "butler" that could analyze complex text via AI, notify me to stay on track, and provide a sense of community by showing that others are reading alongside me. What it does Book Butler is an all-in-one reading ecosystem that gamifies the experience. It allows users to: Advanced PDF Interaction : Beyond simple viewing, the reader empowers users to summarize lengthy chapters, save snippets for future reference, and ask specific questions directly to the text. Server-Side AI Intelligence : Using a robust backend, the app can explain complex concepts in real-time using Gemini-powered AI, ensuring the heavy lifting is handled by the server rather than the device. Stay Accountable : Maintain reading streaks and view progress through home screen widgets. Join a Community : See real-time leaderboards and receive notifications when friends start new books. Track Analytics : Visualize reading habits through dynamic activity heatmaps. How I built it Leveraging my experience as a software engineer in the Flutter ecosystem, I chose Serverpod as the backbone for this project. Backend : I utilized Serverpod for push notifications (FCM), authentication, a PostgreSQL database, Serverside AI book assistant, Leaderboard Realtime Data Display and notification. Frontend : Built with Flutter, using Riverpod for state management and Rive for interactive 2D animations (Fluffy the Penguin Butler). Leaderboard Logic : Points are synchronized to the server using a specific conversion formula where . The overall ranking score is calculated as: $$Points = \text{round} \left( \frac{P}{5} \times 2 \right)$$ Where: P = Total pages read. Challenges I faced A significant hurdle was testing features using keys on the Serverpod cloud and managing database schema migrations without breaking the MVP. I overcame these by leaning heavily on the Serverpod documentation and using PostgreSQL visualization tools to monitor data integrity after schema updates. Accomplishments that I'm proud of I am incredibly proud of delivering a fully functional MVP within the hackathon timeframe. Successfully implementing smooth app interactions and integrating a real-time leaderboard via Serverpod streams were major technical wins. What I learned This project was a deep dive into the Serverpod ecosystem. I gained hands-on experience with Serverpod’s authentication flow, FCM integration, and AOT-ready Dart code. It reinforced my belief that staying close to the documentation is the best way to navigate "external territory" in backend development. What's next for Book Butler The roadmap includes: Expanded File Support : Adding .epub and .docx compatibility. Advanced Reminders : Include server-side scheduled email and push reminders. Enhanced Social Features : Adding direct "reading rooms" for collaborative study. Built With Flutter & Dart Serverpod (Backend Framework) PostgreSQL (Database) Google Gemini AI (Generative AI) Riverpod (State Management) Rive (2D Animations) Firebase Cloud Messaging (Push Notifications) Docker <div