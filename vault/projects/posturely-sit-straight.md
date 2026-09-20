---
slug: "posturely-sit-straight"
url: "https://devpost.com/software/posturely-sit-straight"
title: "Posturely"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 579
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Posturely

> Posturely keeps your spine aligned with smart slouch detection via phone, AirPods, or laptop—plus exercises, scans & progress tracking to build pain-free posture habits.

[Devpost](https://devpost.com/software/posturely-sit-straight) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[video_visual]]

**stack** cmp, composeui, kmp, kotlin, kotlinmultiplatform, multiplatform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for posturely

## Body

Inspiration Like most of us, I spend hours at a desk — coding, solving problems, and sometimes even solving Rubik’s cubes. Over time I noticed how easy it is to slip into poor posture, and how it silently drains focus, energy, and confidence. I wanted to fix this for myself and others without needing expensive posture belts or sensors. That was the spark for Posturely — a smart posture companion that works with devices you already own: your phone, laptop, and even AirPods. What it does Posturely is a smart posture companion that works with devices you already own: Phone Camera → real-time detection, quick posture scans and guided exercises. Laptop Webcam → real-time detection while working. AirPods → tilt-based detection for neck and head posture. Key features: Real-time posture tracking and gentle reminders to “sit straight.” AI posture coach with personalized feedback and exercises. Progress reports, and a posture calendar. Fun giraffe mascot to motivate users. Option to block distracting apps until you finish posture exercises. No extra sensors, no belts, no bulky devices — just the tech you already use every day. How we built it Kotlin Multiplatform (KMP) for sharing core logic across iOS, Android, and desktop. Compose Multiplatform (CMP) for building a unified UI with one codebase. Integrated camera posture detection, AirPods motion sensors, and desktop webcam inputs. Reminders, streaks, and progress tracking. Integrated Revenuecat to show a force paywall in my app. Built with a privacy-first approach, ensuring posture data stays with the user. Used Junie and Cursor to help Vibe Code this and used Supabase as the backend. Challenges we ran into First time with Kotlin Multiplatform + Compose: coming from a Flutter background, I had to quickly learn new build tools, project structures, and debugging methods while racing against hackathon time. Tooling surprises: IDE hiccups, Gradle configuration issues, and multiplatform quirks often slowed progress — sometimes a “simple” fix took hours. Device input complexity: combining posture detection from webcams, phone cameras, and AirPods tilt sensors wasn’t straightforward. Each platform had its own APIs, limitations, and calibration needs. Finding the right balance: designing reminders that are helpful without being annoying was harder than expected — too soft and people ignore it, too harsh and it feels intrusive. Time pressure: building, testing, and polishing cross-platform features during a hackathon meant trade-offs — I had to prioritize core functionality over “nice to have” extras. Context switching: juggling learning, coding, and storytelling (while sneaking in Rubik’s cube solves during AI wait times) tested my focus, but also kept the process fun. Accomplishments that we're proud of Built my first Kotlin Multiplatform app from scratch. Delivered a working prototype that runs on Android and iOS with a single codebase. Created a posture solution that’s affordable, fun, and hardware-free. Meeting the deadline with Revenuecat Integrated. What we learned The power of KMP + Compose Multiplatform for real cross-platform apps. How posture impacts not just health, but also productivity, energy, and confidence. That vibe coding (building in flow and iterating quickly) can be surprisingly effective. Hackathons aren’t just about speed — they’re about storytelling, focus, and enjoying the process. What's next for Posturely Expanding guided exercise libraries with gamified challenges. Offering Enterprise/B2B posture wellness packages for companies. Smarter notifications and reminders to help users stay consistent. Building a Chrome app so posture tracking is available in-browser. Diving deeper into Kotlin Multiplatform to strengthen cross-platform support. Releasing Desktop Apps. Fixing bugs and polishing the user experience for upcoming releases. <div