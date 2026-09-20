---
slug: "inkphony-the-world-is-your-instrument"
url: "https://devpost.com/software/inkphony-the-world-is-your-instrument"
title: "Inkphony – The World is Your Instrument"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 672
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Inkphony – The World is Your Instrument

> Inkphony is a mixed-reality musical sketchpad app for the Meta Quest 3/3s that uses the Logitech MX Ink Stylus to teach music theory concepts.

[Devpost](https://devpost.com/software/inkphony-the-world-is-your-instrument) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** c#, elevenlabs, gemini, metasdk, pca, unity

## How they structured the write-up

- inkphony – the world is your instrument
- inspiration
- what it does
- who is it for?
- how we built it
- what's next for inkphony

## Body

Inkphony – The World Is Your Instrument Inkphony is a mixed-reality musical sketchpad app for the Meta Quest 3/3s that uses the Logitech MX Ink Stylus to teach music theory concepts. Users can play and experiment with music at their own pace by composing their own musical melodies and creating a unique musical orchestra using objects from their world. Inspiration Inkphony addresses the lack of music education for K-12 students. While a majority of music programs focus on the playing of instruments, almost none focus on music theory, construction, or composition. Inkphony creates a highly interactive learning environment where audiences can learn music concepts such as clefs, staffs, atonal notation, and chords, while using their direct surroundings to create unique melodies. What it does Inkphony allows users to write their own music and create their own instruments using the Logitech MX Ink Stylus. To start, users can place blank musical staffs on any tabletop surface and simply tap anywhere on this staff to create notes that correspond to atonal notation. As users create these notes, they not only see how musical notes are constructed on a staff, but hear these notes in real-time as they are being created. Additionally, the precision of the MX Ink gives extra placement accuracy, and the pressure sensitivity of the tip allows users to create soft- and loud-sounding notes with ease. Users can chain or stack the placement of notes to create beautiful melodies and chords, and add new musical measures to lengthen their creations. When they are finished placing notes, users can playback their creations in their entirety. The instrument used for this playback can also be changed by selecting one of the pre-determined instruments or by using Inkphony’s real-time AI-powered instrument extractor. This feature analyzes objects in a user's immediate environment and ‘extracts’ a custom instrumental tone based on these objects that can be used immediately within a musical composition. Inkphony merges education, experimentation, and expression into one fluid experience — a new way to learn and create music that’s tactile, visual, and alive. Who is it For? Inkphony is for music students and composition enthusiasts, including those who previously found it once tedious to write and rehearse musical notation by hand or having to learn audiation. It is also designed for creatives who are curious about making their own musical melodies, but do not have any prior music theory experience or instrument hardware. How We Built It Inkphony was built using Unity/C# and the MetaSDK. By pairing the passthrough capabilities on Meta Quest 3/3s with the Logitech MX Ink SDK, we created a variety of gameplay features, including tracking pressure-sensitivity for staff placement, tip-based precision for note placement, auxiliary buttons on the MX Ink for menu activations, and logic for tactile UI interactivity. In developing our AI-powered instrument extraction feature, we incorporated the latest Meta PCA feature, which provides time-stamped stereo camera access on the Quest camera. Bundling this frame capture with specific AI pipelines, including Gemini API for bounding box and object detection, ElevenLabs for text-to-sound effect creation, and our own advanced filtering system, we were able to build an asynchronous, continuous background recognition that generates stylized icons and sound-effect instruments from your surroundings. What's next for Inkphony In the next few months, we are ramping up Inkphony for public launch on the Meta App Store. We have more features we hope to include for a 1.0 release, including making our design system more cohesive to improve the user experience, the ability to save/load musical creations across sessions, and the functionality to add multiple tracks of instruments or tracks to enable multi-layered music creation. In the future, we plan to add the ability to share musical creations with other users and allow users to remix each other's creations, which tremendously expands the possibility-space for user-generated content within the app. These features, in addition to further improvements to our AI-powered instrument extraction feature, will create a solid set of educational ‘play’ that will make up version 1.0 of Inkphony. Channel your inner maestro! <div