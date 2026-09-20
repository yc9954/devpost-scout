---
slug: "gotrail"
url: "https://devpost.com/software/gotrail"
title: "GoTrail"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1055
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# GoTrail

> Turn every hike into a discovery. Doctors get a tool they can actually prescribe to treat mental and physical health. Patients get a fun reason to actually go.

[Devpost](https://devpost.com/software/gotrail) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** avfoundation, core-location, figma-make, mapkit, onnx, plantnet-300k, sqlite, supabase, swift, swiftui, zetic-melange

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gotrail

## Body

Turn every hike into a discovery. Inspiration People suffer from all sorts of health problems, whether it be mental health, such as anxiety or depression, or physical ones, such as cardiovascular disease. In response, doctors prescribe hiking and spending time in nature more than almost any other lifestyle intervention. However, consistent adherence to lifestyle prescriptions is famously low, and hiking specifically faces two problems: most people find it boring, and beginners feel intimidated and unsafe because they're in a new environment surrounded by unknown species they can't identify. GoTrail exists to fix both! What it does GoTrail is a native iOS app that turns hiking into a Pokédex-style nature discovery game. You start a hike, point your camera at any plant, and the on-device AI model identifies it in under a millisecond, even when you have zero internet connection. Your hikes are saved to your personal collection to gamify every hike. The app combines hiking statistics, plant species identification, and an interactive map to give the user a satisfying portfolio to build to continuously encourage them to go out and hike. Because the model runs entirely on the phone locally through Zetic's Melange tool, the app works exactly where it's most useful and applicable, deep on a hiking trail with no service. How we built it GoTrail is a native iOS app built in Swift and SwiftUI with feature-based folders. We chose native over cross-platform because camera latency and tight SDK integration with ZETIC mattered more than code reuse, and because every millisecond shows up in the user experience when you're trying to identify a plant in real time. The camera pipeline runs on AVFoundation , giving us direct control over capture quality, frame handling, and the moment the image is passed to the model. MapKit and CoreLocation power the trail map and tag every identification with the spot where you found it, so your collection becomes a personal map of where you've been. The heart of the app is on-device machine learning through the ZETIC Melange SDK . We deployed a plant classification model, trained on the PlantNet-300K dataset of roughly 300,000 real botanical images, directly to the phone via Melange's deployment dashboard (model ID: plantid_2 v2 ). Inference happens locally at millisecond-level latency, with no network calls in the critical path. This is the entire reason the app is able to work offline. Data is split deliberately between local and cloud. SQLite stores the user's collection on the phone, every plant they've ever identified, with its photo, location, and timestamp, and the app reads and writes to it during the hike with no internet required. Supabase handles authentication and syncs the collection to the cloud, but only when the phone is back on wifi. The on-device side owns the entire core experience and the cloud side is a nice-to-have for cross-device sync. For design, we used Figma Make early in the weekend to explore design system directions before writing a single line of SwiftUI. It let us prototype color palettes, typography, and component patterns for the "nature-dex" feel, playful, friendly, low-friction, and pressure-test them against the question we kept coming back to: will this make a beginner actually want to go outside? It helped us throw out a more rugged, technical outdoors direction early and commit to something warmer and more inviting. Challenges we ran into Deploying through ZETIC Melange: We initially explored using a React Native CLI architecture, planning to build our own bridge to connect to the ZETIC Melange Swift SDK, however, after discussing with the helpful ZETIC engineers, we understood that it would be much more efficient and realistic to program in Swift, despite us only having one shared Mac to share between the three of us. Surfacing model uncertainty: The plant species classification model we used was not perfect. It doesn't always provide a high confidence rating on the plant species it predicts. Due to this, we wanted to prioritize user safety and make it clear the confidence rating in the app, because it's possible for there to be moments where GoTrail prevents harm to the user. For example, if the user uses GoTrail to figure out that a particular plant is actually Poison Ivy, it may have just saved them from an allergic reaction or rashes. Accomplishments that we're proud of Our app genuinely works offline: It was so satisfying to see not only the millisecond on-device inference of plant species through ZETIC Melange, but also its ability to continue working in airplane mode. An approachable and comfortable UI/UX that was both welcoming to new hikers and felt like a game. What we learned Working with ZETIC's Melange taught us how much specific and unique architectural discipline on-device ML models demand. You still have to think carefully about the system design and the technicalities the model requires, such as the model size, export format, and what runs locally or in the cloud. Melange made the deployment using their Swift SDK really smooth, but we still have to take into account the specific needs of the model. Figma Make pushed us to actually learn what a design system is. Going in, we thought of design as just picking different fonts, colors, and using flexbox, but Figma Make made it obvious that a design system is a set of reusable decisions, such as tokens for color, spacing rules, component patterns, and more, so that all the screens and layout of the app feel organized without having to redesign components. Having spent a lot of time building the frontend early in the weekend allowed us to have a clear blueprint to follow for the rest of the features we added. What's next for GoTrail We wanted to fine-tune plant species classification models on specific regions the user is hiking in, to improve the accuracy for users' local environments. We also wanted to fine-tune an LLM for plant descriptions and have it run locally through ZETIC's Melange tool so that we can implement a feature that gives descriptions of each species the user identifies. Lastly, we thought it would further motivate our users to go out and hike if we added social hiking features . Being able to connect with friends, coordinate group hikes, and share collections would increase the mental health benefit and the physical exercise adherence through social accountability. <div