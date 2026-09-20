---
slug: "memora-nqg2ra"
url: "https://devpost.com/software/memora-nqg2ra"
title: "Memora"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 585
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/video_visual"
---

# Memora

> Making memories visible, making images accessible.

[Devpost](https://devpost.com/software/memora-nqg2ra) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[video_visual]]

**stack** gemini, react-native

## How they structured the write-up

- 🌱 inspiration
- 🤖 what it does
- 🛠️ how we built it
- ⚠️ challenges we faced
- 🌍 why memora matters

## Body

Caption Description 📸 Memora – AI-Powered Image Captioning Making memories visible, making images accessible 🌱 Inspiration The digital world today is overwhelmingly visual. Photos are how we share memories, learn in classrooms, and communicate online. Yet for millions of visually impaired users, these images remain silent and inaccessible. A friend may send a picture on WhatsApp, a teacher may share a diagram in class, or someone may browse their own photo gallery — but without meaningful descriptions, every image becomes a blank file. This problem is deeply personal for us. One of our teammates, Pranav , is blind and experiences this exclusion daily : from academic diagrams that cannot be interpreted to personal photos labeled only as “unknown image.” During our discussions, one thing became clear: “I don’t need perfect AI. I just want to know what’s happening in my own photos like everyone else.” That insight shaped Memora . We set out to build an accessibility tool grounded in lived experience, not assumptions — one that quietly works in the background to make images understandable, private, and inclusive by default. 🤖 What It Does Memora is a mobile app that automatically generates meaningful, accessibility-focused captions for images, designed specifically for blind and visually impaired users. The app continuously monitors a user’s photo library and, using a vision-language AI model, generates two types of descriptions: Concise alt text optimized for screen readers Detailed contextual descriptions explaining objects, people, spatial relationships, and scene context These captions are embedded directly into the image metadata, allowing screen readers like TalkBack and VoiceOver to read them instantly — across apps and platforms. Memora removes the need for manual uploads or repeated actions. Every new photo becomes accessible automatically, helping users independently understand their own memories, messages, and educational content. 🛠️ How We Built It Memora is built as a cross-platform React Native application using Expo , with accessibility and privacy as first-class design principles. Core Architecture React Native (Expo SDK 51) for cross-platform mobile development Gemini 3.0 Flash-Light for fast, cost-effective image understanding Background processing using expo-background-fetch to automatically detect new images OCR pipelines to extract and interpret text from images such as notes and diagrams EXIF/XMP metadata embedding to store alt text directly inside image files Native Text-to-Speech for immediate audio output via screen readers Redux Toolkit + Redux Persist for reliable state management By embedding accessibility at the metadata layer, Memora ensures that captions persist across galleries, messaging apps, and photo platforms — rather than remaining locked inside a single app. ⚠️ Challenges We Faced Building Memora required addressing several real-world technical and accessibility challenges: Ensuring reliable background processing on mobile platforms with strict OS limitations Avoiding generic captions by carefully prompting the AI to produce meaningful, non-vague descriptions Handling metadata differences between Android and iOS (EXIF/XMP compatibility) Designing a fully accessible UI , including focus order, large touch targets, and screen-reader-first navigation Maintaining user privacy , ensuring images remain on-device by default and are never stored externally We tackled these challenges through iterative testing, accessibility-first design decisions, and continuous feedback from visually impaired users — including within our own team. 🌍 Why Memora Matters Memora demonstrates how AI can be inclusive, responsible, and culturally grounded . It empowers users across generations — from students in classrooms to elders revisiting lifelong memories — and aligns closely with the principles of inclusivity. By making accessibility automatic rather than optional, Memora moves one step closer to a future where technology adapts to people, not the other way around. <div