---
slug: "friendtimeline"
url: "https://devpost.com/software/friendtimeline"
title: "Friendy+"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 584
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Friendy+

> Never forget a weak tie again. Friendy+ helps you capture details, recall conversations, and turn fleeting contacts into lasting connections.

[Devpost](https://devpost.com/software/friendtimeline) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** grdb, ios, onesignal, revenuecat, swift, swiftui, telemetrydeck

## Body

Inspiration We’ve all met someone at an event, had a great exchange, and weeks later can’t recall their role, project, or even their name. These “ weak ties ” often hold the most potential value— professionally and personally —but they’re the hardest to manage. That pain point inspired Friendy+, a streamlined app for managing these connections effortlessly, so you're always prepared, intentional, and ready to turn a one-off encounter into something meaningful. How We Built It We focus on quick entry and instant recall : Easy Capture — A guided quick form for key details, and photos auto-sorted by date/location. Instant Recall — A timeline shows every interaction and follow‑up; A profile highlights static essentials (company, title, contacts) at a glance. Smart Reminders — before events, after first contact, and when ties go cold. How We Leveraged Sponsor Tools RevenueCat — Built contextual paywalls and used Remote Config to iterate experiments without app updates. OneSignal — Set up persona-based Journeys and tracked Outcomes to refine retention and messaging. ElevenLabs + Gemini — Generated realistic video footage and voiceover narration for our demo video. Building in Public We shared our journey in six YouTube videos —covering prototypes, pivots, and key lessons learned. In the final video, we revealed our biggest takeaway: “From Wrong Audience to Data-Driven Strategy.” Essentially, we discovered we'd targeted the wrong audience just before launch. To pivot effectively, we prioritized data by integrating TelemetryDeck for user tracking and OneSignal for better engagement. Our next steps will be guided entirely by the insights from these metrics. Challenges & Learnings Product–market fit pivot Challenge — We started by targeting “close friends.” TestFlight feedback showed people don’t forget close pals; the real pain is staying on top of weak ties. What we did — We added instrumentation and feedback loops to observe real behavior and ran smaller experiments instead of big bets. Learning — Listen first, instrument early. We now validate ideas with data before major changes—saving time and avoiding guesswork. Persona‑driven messaging under time pressure Challenge — In the final week we shifted to weak‑tie use cases and defined two personas, but we didn’t have time to rework all in‑app copy. What we did — We kept UI text neutral and used OneSignal to deliver persona‑specific push notifications, so messaging can evolve without shipping a new build. Learning — Decouple messaging from releases. Personalization at the edge lets us move fast and target the right users without blocking on app store cycles. Shipping while building in public Challenge — We aimed to qualify for the Build‑in‑Public Award, but weekly iterations plus video production were tough. We didn’t publish consistently; many drafts felt “not good enough” because we couldn’t clearly articulate what we were doing. What we did — We turned that friction into a signal. If we couldn’t record a clear video quickly, we paused publishing, stepped back to reassess the problem and simplify the approach, then re‑recorded only if time allowed. Learning — The video became our rubber duck: a forcing function to stop and explain the work out loud. If we can’t explain it fast, the direction needs a rethink. What’s Next With initial real user data in hand, we'll target our top persona with: AI Voice Logging: Hands-free note capture on the go. Smart Nudge Suggestions: AI-driven, context-aware follow-ups Business card scan → instant profile creation. Expanded Channels: Emails for deeper, timely engagement. Friendy+ isn't just a memory tool—it's your edge for building intentional, lasting networks in a fast-paced world. <div