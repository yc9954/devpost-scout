---
slug: "studient"
url: "https://devpost.com/software/studient"
title: "Studient"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 903
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Studient

> Studient transforms any document into AI-powered flashcards, quizzes & spoken explanations. Built with Gemini & ElevenLabs, featuring Study-to-Earn rewards. Making premium education accessible to all.

[Devpost](https://devpost.com/software/studient) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** cluade-code, dart, dio, elevenlabs, firebase, flutter, gemini, glassmorphism, hive, lottie, onesignal, revenuecat, tempo

## How they structured the write-up

- 💡 inspiration
- 📚 what it does
- 🛠 how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📖 what we learned
- 🚀 what's next for studient

## Body

Onboarding Focus Timer Quizzes Statistics Upload your content Achievements Upload library Flash Cards About Studient 💡 Inspiration Right, so I'm the bloke who made FlowMind, and I've always been a bit obsessed with how AI can make us better at what we do. Picture this: it's 2am, I'm knee-deep in documentation trying to learn a new framework, and I'm juggling PDFs, sticky notes, and three different flashcard apps. Absolute chaos. That's when it hit me—why am I doing all this manual work when AI could just... get it? Like, it should understand what I'm trying to learn and sort me out with the perfect study materials. No faff, just results. Then RevenueCat Shipaton came along with £65,000 up for grabs, and I thought "brilliant, perfect excuse to build this thing." The meta aspect of using AI to build an AI study app? Chef's kiss. Armed with Claude Code and just 7 days, I set out to prove that premium education doesn't have to cost a fortune. 📚 What it does Studient is basically your ridiculously smart study mate that never gets tired. Chuck any PDF at it and it transforms it into proper study materials: Instant flashcards & quizzes : Upload a document, grab a cuppa, come back to perfectly crafted study materials (actually, it's faster than making tea) Pomodoro timer that doesn't suck : 25 minutes of focus, 5-minute break, with satisfying animations that make you actually want to use it Gamification that works : Achievements and stats tracking—turns out making studying feel like a game actually works Clean document library : Keep all your uploaded documents organised in one place The app has a glassmorphic design with smooth animations. Built it to be accessible and performant because everyone deserves quality study tools. 🛠 How we built it "Vibe-coding" sounds pretentious, but honestly, it's the best way to describe it. I basically had conversations with AI to build an AI app. Proper inception stuff. The setup: Claude Code : My tireless coding partner. I'd describe what I wanted, it would write the code. Felt like cheating, but in the best way Google Gemini : The brains behind the study material generation. Also helped me figure out the tricky algorithms Tempo : Kept the vibes right during those long coding sessions. 80+ hours in 7 days Flutter : Because who wants to build the same app twice for iOS and Android? RevenueCat : Sorting payments without the headache OneSignal : For those gentle "maybe you should study?" nudges The mad thing is, this approach was genuinely 10x faster than traditional coding. I'd explain features in plain English to Claude, focus on making things look nice, and we'd iterate at lightning speed. Built in 7 days what would've taken months the old way. 🚧 Challenges we ran into Seven days. SEVEN. : Started last week, needed to ship by September 30th, did it by the 2nd. Absolutely mental timeline. Zero room for error. PDF processing is harder than it looks : Large documents would blow through API token limits. Had to get creative with chunking—basically teaching the AI to read documents like a human would, bit by bit. Learning to talk to AI : Explaining technical requirements in conversation is a skill. Had to learn how to articulate what I wanted whilst keeping the code clean and maintainable. Making it smooth : Processing AI responses whilst keeping animations at 60fps? That's some serious juggling. Lots of all-nighters optimising and caching everything. Sleep? What's that? : Averaging 12+ hour days. Coffee became a food group. My flatmates thought I'd gone missing. 🏆 Accomplishments that we're proud of Actually shipped in 7 days : From nothing to App Store in a week. Absolutely bonkers It's genuinely beautiful : Those animations when you complete a study session? Satisfying Proper AI integration : Not just "AI-powered" marketing waffle—it's baked into everything Butter-smooth performance : 60fps even on older phones. Your iPhone 8 will thank you Works offline : Because the WiFi on the tube is still rubbish It actually works : Despite the insane timeline, it's stable and people are using it 📖 What we learned AI changes everything about development : It's not just faster—you think differently. You become an architect rather than a builder. Without Claude Code, this would've been impossible in 7 days. Extreme constraints force innovation : 7 days sounds impossible, but it forced absolute clarity. Every feature had to justify its existence. No overthinking, just ship. Students deserve better : The state of study apps is dire. Everyone's still using tools from 2010. There's so much room for innovation here. Perfect is the enemy of shipped : Could I have added more features? Sure. But shipping something that works beats planning something perfect. 🚀 What's next for Studient Soon (realistically): Multiple file format support (images, DOCX) Dark mode (everyone keeps asking) Voice explanations for flashcards Better quiz question variety Later: Web version for proper desktop studying Spaced repetition that actually follows memory science Study groups with mates Parent dashboard (for the helicopter parents) The dream: Open API so other devs can build on it Marketplace for verified study materials AI that properly learns how YOU learn Global peer tutoring network The endgame : Make Studient how everyone studies. Every PDF, every lecture slide, every textbook—all instantly interactive and personalised. Learning should be about understanding, not memorising. And honestly? We're just getting started. <div