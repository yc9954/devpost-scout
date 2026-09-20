---
slug: "weekwin"
url: "https://devpost.com/software/weekwin"
title: "weekwin pro"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 510
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/video_visual"
---

# weekwin pro

> WeekWin pro is a weekly task tracker that holds you accountable — not just with checkboxes, but with real proof.

[Devpost](https://devpost.com/software/weekwin) · hackathon [[DSH Hacks V1]]

## Facets

  <sub>weak: realtime_stream, vision_ocr</sub>
**domain** [[finance_payments]]
**substrate** [[video_visual]]

**stack** datetime, json, pathlib, pillow, python, pyttsx3, thinker, threading

## Body

Inspiration The inspiration behind WeekWin Pro came from the struggle of staying consistent with tasks and goals. Most productivity apps allow users to mark tasks as completed without any real accountability, which often leads to procrastination and loss of motivation. I wanted to create an app that makes productivity feel more rewarding, interactive, and real. The idea of uploading proof for completed tasks and receiving motivational feedback made the experience unique and engaging. What it does WeekWin Pro is a productivity and accountability app that helps users manage weekly tasks. Users can: Create tasks with specific days and deadlines Receive voice reminders before deadlines Upload proof images to verify task completion Detect fake or AI-generated images using a custom verification system Track completed and pending tasks View a summary page with motivational compliments and progress tracking The app combines productivity with motivation and accountability in one experience. How we built it We built WeekWin Pro using Python and Tkinter for the graphical user interface. The project also uses: Pillow (PIL) for image processing and verification pyttsx3 for offline voice reminders JSON for storing task data Threading for running timers and reminders in the background The image verification system was built using image analysis techniques such as edge detection and smoothness analysis to identify unrealistic or AI-generated images. Challenges we ran into One of the biggest challenges was building an image verification system without relying on expensive AI APIs. Early versions using external AI services required payment credits and API keys, which made the project harder to use. We then redesigned the system completely using local image analysis. Another challenge was designing the interface so it stayed clean and functional while supporting multiple features like reminders, summaries, and task verification. Managing timers and voice alerts in the background without freezing the UI was also difficult. Accomplishments that we're proud of We are proud that WeekWin Pro works fully offline without requiring paid AI services. The custom verification system, voice reminder system, and motivational features make the app feel unique compared to traditional task managers. We are also proud of: Building a complete desktop productivity application from scratch Creating a clean dark-themed UI Adding real-time deadline warnings Designing a task accountability system using proof uploads Making the app motivational and user-friendly What we learned During this project, we learned: How to build desktop applications with Tkinter How image processing works using Pillow How to manage files and persistent data with JSON How threading works in Python How difficult but important user experience design can be How to create custom systems instead of depending fully on APIs We also learned the importance of balancing functionality with simplicity. What's next for WeekWin Pro In the future, we want to add: Cloud syncing across devices User accounts and profiles Better AI-based verification models Achievement badges and streak systems Calendar integrations Mobile and web versions Dark/light mode customization Advanced statistics and productivity analytics Our goal is to turn WeekWin Pro into a powerful productivity platform that helps people stay disciplined and motivated every single week. <div