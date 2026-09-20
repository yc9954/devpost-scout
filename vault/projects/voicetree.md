---
slug: "voicetree"
url: "https://devpost.com/software/voicetree"
title: "Voicetree - AI Meeting Notes for Work & Study"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 1205
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Voicetree - AI Meeting Notes for Work & Study

> Smartest AI-powered meeting assistant for students and professionals that helps them take high-quality notes automatically.

[Devpost](https://devpost.com/software/voicetree) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** expo.io, node.js, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voicetree

## Body

Inspiration We are 2 indie developers, and we constantly discuss new ideas, changes, or improvements to our products. We often do this face-to-face in a co-working space or a coffee shop. After each meeting, the first Slack message goes, "what did we agree to do?" and we start pulling things from memory, always forgetting something important. Being app builders, we were certain there was a better way to do that. After trying tens of existing apps and constantly facing various issues in different aspects, from UI/UX to app quality, missing features, and pricing, we decided to build a better one. This is how the idea for Voicetree was born - the fastest, smartest, and most user-friendly AI meeting assistant that works for any type of meeting, whether it's a work call or a university class. With powerful AI integrations, it allows users to easily organize and structure all notes and lets them focus on the meeting or class they're in. And so we built it. Now, each time we meet and discuss apps, we record our meeting with a phone or watch, share a note in Slack afterwards, and then use AI chat to extract all the action items. Magic! What it does Voicetree packs a lot of features, but essentially it allows a user to record or upload any audio and turn it into structured and organized notes automatically. Once the note is created, the user can edit a note or create "AI transformations" from it, such as meeting notes, blog posts, email drafts, and more. The user can also chat with a note to extract insights in a more flexible way. Voicetree includes all the features you’d expect from a powerful note-keeping app, but on top of it, stands-out from competition with some unique features, such as: Apple Watch app for quick on-the-go note creations without the need to get the phone Deep system integrations with widgets, Siri intents, live activity, and more enable quick entry and let users build more powerful integrations Support for a ton of different audio and video formats thanks to the custom audio encoder Multiple AI models with smart routing picking the best one for each task - from overview creation to chat How we built it The mobile app is built using React Native and Expo with quite a bit of custom Swift code for things like Apple Watch app, widgets, Siri intents and other system integrations. On the backend we're using NodeJS and our custom lightweight frameworks on top of NitroJS. For this project we also built a smart router for AI models which automatically sends queries to the most appropriate model. Postgres is our database of choice. Challenges we ran into Voicetree is one of the biggest apps we’ve built to date and we had multiple product, engineering and growth challenges along the way. Just to name a few: Picking the right MVP scope. Our backlog of ideas was growing faster than we can ship, so we had to be strategic and really focus on the most important things first which was challenging. Finding a profitable growth channel . Right from the start we decided to experiment with multiple channels to see what worked and not. We picked Apple Ads and Meta as the first channels. Finding a right campaign setup, picking correct keywords, adjusting bids and budgets was and still is one of the biggest challenges we have. As one of engineering challenges, ensuring audio data integrity and recovery . Losing recording or notes is one of the worst things that can happen when using an app such as Voicetree. So we put a lot of effort into ensuring that the app can gracefully handle as many edge-cases as possible, from receiving an incoming call during the recording to getting memory-warnings from the system. iOS26 integration . We wanted to be ready on day 1 and use some of the new APIs. Early XCode Beta versions were quite unstable, to say the least. But we managed to utilize the on-device transcription API for our chat with notes along with some other improvements. Accomplishments that we're proud of First, we're really proud of the final product in general - the app is performant, crash-free, and it solves a real problem for our users. We believe it's currently one of the best apps on the market in our category. Our main accomplishment is getting the initial user traction within the first weeks from launch. Getting more than 1k app installs as well as growing to about $2k in revenue during this period proves the viability of the project and gives us a positive signal to continue investing into Voicetree and double-down on product and marketing. What we learned We did a lot of things for the first time with Voicetree and had many learnings, such as: Working with audio files and audio recordings gets really hard as soon as you want any customization besides basics. We had to really learn a lot about audio formats and inputs and had to build our custom "standardization" library that allowed us to support a wide range of input files. It was the first time we launched a Facebook campaign for an app and had to learn a lot about all the aspects of it, from tracking and attribution to content production and ad configuration. While we didn't succeed ROAS-wise at all (our cost per trial was 2-3x higher than expected), we had a lot of learning we're already applying for the future campaigns (we’re iterating on our onboarding flow and on our creatives to improve targeting). What's next for Voicetree We already have a lot of things planned and in progress to grow Voicetree to massive scale. Some of them include: Narrowing down to different audiences. Currently, the app targets a broad cohort of users, and we’re working on onboarding-based customization so that students and professionals will see the most appropriate tools first. This should help us with positioning in general and assist users in getting value from the app in the easiest way possible. Android & Web versions : We plan to focus heavily on organic marketing, and having both iOS and Android versions will be extremely helpful when doing so. While Voicetree is a React Native app, we’ve built a lot of iOS-specific integrations with Swift, and porting them isn’t straightforward and takes time. Automations & Integrations : One of the ways we’re using Voicetree ourselves is to record a note with a description of new features or bugs, get a structured version of it, and create a Linear ticket. Now we’re working on Zapier integration so that this flow can be automated and enable a lot more powerful integrations. Input from other sources : Some of our users want to input PDF files or get notes from YouTube videos so that Voicetree can be their single note-taking app, and we’re working to enable it. In-app Feedback platform : Our roadmap is formed mainly based on user feedback, so we’re adding an in-app platform to collect bugs and feature reports. The most important focus for us now is growth and marketing, mostly focusing on getting as much feedback as possible and refining the product where necessary. <div