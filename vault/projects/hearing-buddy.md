---
slug: "hearing-buddy"
url: "https://devpost.com/software/hearing-buddy"
title: "Hearing Buddy"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 622
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/transcript_audio"
---

# Hearing Buddy

> Hearing Buddy is a real-time transcription app that helps people with hearing challenges follow conversations. It learns familiar voices, provides AI summaries, and streams to Watch and Mac apps.

[Devpost](https://devpost.com/software/hearing-buddy) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]] [[general_public]]
**substrate** [[transcript_audio]]

**stack** appleintelligence, revenuecat, swiftui, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for hearing buddy

## Body

Live now for iOS 26! Real time captions for every conversation Inspiration Hearing Buddy was inspired by love and technology. First and foremost, I built it for my partner. She is Hard of Hearing, and I’ve seen how challenging it can be in everyday situations where it’s tough to follow conversations. I love her deeply and wanted to create even a small way to make those moments easier and more connected. The second spark came from Apple’s announcement of new speech-to-text models at WWDC 2025. I had already begun experimenting with Hearing Buddy, but when these APIs were released, I knew I could build something better than what was out there. Many existing apps were charging steep premiums for accurate transcription, but Apple’s on-device model opened the door to build a fast, private, and affordable solution. My partner would often turn to a friend or loved one and call them her “hearing buddy” ~ someone who could help her catch what she missed. That’s exactly what I wanted this app to be: a buddy that’s always there, so no one feels invisible or left out of the moments that matter. What it does Hearing Buddy provides unlimited, high-quality, real-time captions to make conversations easier and more inclusive for people who are Hard of Hearing or experience hearing loss. It reduces isolation, helps people stay connected, and works in everyday environments like classrooms, workplaces, and social gatherings. Pro features expand this even further with options like streaming captions to Apple Watch or Mac and speaker detection for clearer conversations. How we built it The project was built on the Xcode beta, since the app depends on iOS 26. That created challenges at times. I used WhisperKit at the start as a speech-to-text model but later replaced it with the new native Apple Speech framework introduced in iOS 26. I also integrated RevenueCat to manage the Pro plan and paywall, and used CoreML with an open-source diarization model for speaker detection. Challenges we ran into One major challenge was implementing speaker diarization. Apple’s APIs don’t currently provide this, so I had to explore open-source models that could run efficiently on device. Training and segmenting speakers is still a work in progress, but the results so far are promising. Another challenge was working on iOS 26 beta, which occasionally made development unstable. Migrating from WhisperKit to Apple’s new native Speech framework also required significant refactoring, but ultimately improved performance, accuracy and battery life. Accomplishments that I'm proud of Building a private, affordable transcription app powered by Apple’s latest on-device models. Creating an accessible tool that doesn’t require special hardware or expensive services. Designing a clean UI for training and recognizing speakers, making speaker detection approachable for everyday users. Creating companion Watch and Mac apps for Pro users Doing a launch post on Reddit at /r/hardofhearing and getting dozens of positive comments What we learned Building Hearing Buddy taught me how widespread hearing loss is and how deeply it affects daily life. Almost everyone I spoke with either had hearing loss themselves or knew someone who did, which made the need for this app even more clear. I also learned a great deal about speaker diarization, privacy-first transcription, and CoreML. Beyond the technical side, I learned how fun and powerful it is to build something that helps someone close to you. What's next for Hearing Buddy The next steps are to: Get featured on App Store as App of the Day Add a web app component so teachers could stream live captions easily from their phone to their students laptops. Improve speaker diarization accuracy. Continue refining the user experience based on feedback from a growing list of beta testers in the Hard of Hearing community. <div