---
slug: "momental"
url: "https://devpost.com/software/momental"
title: "Momental: Meditate, Sleep, Focus"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 1113
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# Momental: Meditate, Sleep, Focus

> Escape the noise. Momental helps you find your moment — whether it's to meditate, sleep or focus. One page. One tap. Nothing more.

[Devpost](https://devpost.com/software/momental) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[measured_ablation]]
**domain** [[accessibility]] [[civic_government]] [[education]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[video_visual]]

**stack** adobefirefly, android, audacity, composemultiplatform, elevenlabs, firebase, firestore, google-cloud, ios, kotlin, kotlinmultiplatform, swift

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for momental

## Body

Momental Momental features Momental features 2 Inspiration It started with the noise. The constant notifications, the crowded commutes, the endless digital chatter. To find a moment of peace, I started meditating and even traveled to a monastery in Nepal to learn from monks. It was transformative. However, when I came home, the habit disappeared within a few days. The chaos returned. I tried every meditation app I could find, but they all felt like homework: endless taps, logins, courses to complete, and ads for features to unlock. I just wanted to sit, breathe, and feel the progress. That's when I realized: meditation doesn't need more features. It requires less friction. What it does For people overwhelmed by the noise of modern life. Momental offers a beautiful and minimalist timer with soundscapes to reduce the friction of mindfulness, so you can consistently find your moment of calm, deepen your sleep, and sharpen your focus. It’s built around a single principle: One page. One tap. Nothing more. Fall asleep faster. Choose sleep mode with calming soundscapes that fade gently, helping you transition from a racing mind to restful sleep. Set deep work sessions with interval bells that keep you in flow state. Find calm instantly with an easy-to-use meditation timer. Build lasting habits. Visual streaks and calendar tracking turn sporadic sessions into consistent practice. Create your perfect audio environment. Mix 60+ soundscapes — solfeggio frequencies, nature sounds, LoFi, ambient music — or choose pure silence. Every soundscape loops seamlessly and fades naturally at the end of the session. Find relief from mental noise — users with tinnitus report finding calm. Special education teachers use it with autistic children. Make it truly yours. Set any duration, warmup phase, add gentle bells for intervals and journal your insights. Sync everything across devices. No login required. No guided content. No decisions. Just you and the moment. How I built it The journey began on Reddit, where I found many users searching for a minimal meditation timer. Validated, I started developing the first version, sharing every step of my progress with the #BuildInPublic community on Twitter to get feedback as early as possible. I simultaneously started a Reddit community for the app and created a public feature voting board to ensure every decision was community-driven. Over 10 iterations, the app was refined through a cycle of user feedback, Google Analytics, and Firebase A/B testing. This data showed that users loved the soundscapes, so I doubled down on making that experience best-in-class. Tech Stack: Momental is built with Compose Multiplatform. Native components, like the music player, were developed for each platform (Swift/Kotlin). Android Studio & Claude Code are my main drivers. Soundscapes: To provide a rich audio library without expensive licensing, I used a combination of AI-powered music generation (via ElevenLabs) and tracks from freesound.org (Creative Commons 0). Every track was edited in Audacity to ensure high-quality, seamless looping, and images were AI-generated in Adobe to match the mood. Design Philosophy: Every design decision was about removing friction. If a feature added a step or a moment of confusion, it was cut. The entire app is designed around the principle that the best interface is the one that disappears. Challenges I ran into Audio Quality : The audio quality wasn't good in the beginning. The loops were recognizable on the iOS device. Finding the balance between quality and downloadable file size wasn't easy. The Simplicity Paradox : Making something straightforward is challenging. Early versions included tutorials and a complex onboarding process. Users were overwhelmed. I stripped it all away until there was nothing left to remove, trusting that an intuitive design needs no explanation. The Soundscape Challenge: Users wanted a wide variety of high-quality ambient sounds. I solved the licensing challenge with AI-generated music and copyright-free tracks, but this created a technical challenge: ensuring that over 60 tracks were perfectly loopable, high-quality, and could be layered together without issue. The Unexpected Use Cases: I built Momental for meditation. But users started sharing it for entirely different reasons: Parents use it to help their children fall asleep. People with tinnitus use it to mask the ringing. Students use it for deep work sessions. This taught me a valuable lesson: when you remove assumptions about how people should use your app, they'll show you what they actually need. This insight also made marketing easier, allowing me to find a unique position in a crowded market. Accomplishments that I am proud of Real Momentum: In just the last 4 weeks, users have started over 4,200 sessions with Momental, finding their own moments of calm. Seeing the Human Impact: The most significant accomplishment is seeing the app help people in meaningful ways. Reviews mentioning it "helps children fall asleep" or provides relief for someone with tinnitus are what make this project worthwhile. Shipping a Complex App, Solo: Delivering a feature-rich, cross-platform app for both iOS and Android in just a few weeks was a huge personal achievement for me. Going Beyond Code: Users consistently mention the beautiful design. That's the highest compliment I could receive. First Demo Video: Creating the submission video was a project in itself, and I'm proud of stepping out of my comfort zone to record and edit it. What I learned Music Creation. It's my first time editing music. It was a challenge making it loopable in high quality, providing it as downloadable content, and playing multiple tracks in parallel on iOS and Android. Build an Audience First. I started building for my own problem, but I learned that growing a community before writing the first line of code is even more powerful. Build for Outcomes, Not Features. Users don't care about an "innovative streak system." They care about feeling calmer, sleeping better, or focusing longer. Every feature must serve a real-world outcome. Let Users Define Your Product. I built a meditation timer. My users turned it into a tool for sleep, focus, and relief. When you create space, people will fill it in ways you never imagined What's next for Momental Short-term Continue developing based on community feedback via Featurebase Grow the audience on Reddit , Twitter and expand marketing efforts on TikTok. A/B test the onboarding flow and monetization strategies. Add more high-quality soundscapes, also created by professionals. Begin development for Apple Watch and Desktop (Mac/Windows). Long-term vision My vision is to help thousands of people escape the noise in their own way—not by telling them how to meditate, but by giving them a beautiful tool that gets out of the way. The chaos of modern life isn't going anywhere. But maybe, for just a few minutes a day, Momental can help us step outside of it. <div