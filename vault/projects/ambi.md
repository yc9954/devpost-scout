---
slug: "ambi"
url: "https://devpost.com/software/ambi"
title: "Ambi"
hackathon: "AngelHacks 2.0"
winner: true
words: 447
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# Ambi

> Ambi's goal is to help its users become ambidextrous! The app provides habit tracking for daily non-dominant hand activities, hand-strengthening tap games, and guided writing and sports exercises.

[Devpost](https://devpost.com/software/ambi) · hackathon [[AngelHacks 2.0]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[video_visual]]

**stack** expo.io, reactnative, redux, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ambi

## Body

Inspiration As people who've always had ambidextrous ambitions, we wanted an app to keep track of our progress and guide us as we trained to strengthen our non-dominant hands. Given no such app existed, we decided to build it! What it does Ambi provides a multitude of features to help you on your journey: Habit tracking to keep track of if you've been performing daily actions with your non-dominant hand; users can select which habits they'd like to track and earn streaks for consistent completion. Three activity tracks with a plethora of exercises to help the user strengthen their finger and hand muscles and improve their non-dominant hand handwriting and athletic precision. The three tracks are: Handwriting, Tap Games (interactive tap and drag games on the app), and Sports. "Subscribe" to a track to see its actives in your daily feed. A progress feed to track your habit completing and handwriting with photos over time. It's awesome to watch your handwriting transform from messy to neat! How we built it We used React Native (Expo) to build the app. We used Redux for state management, and all information is stored in your phone's local storage. Challenges we ran into We initially wanted to do handwriting analysis to check how closely the users submitted handwriting photos matched to the assigned text. Unfortunately, we weren't able to implement OCR without ejecting from Expo, so we decided to scrap that idea for now and invest more time into other features of the app. We also only had time to create one tap game, as we were new to working with react-native-gesture-handler. Accomplishments that we're proud of Actually completing an app during a hackathon! In previous hackathons, we were unable to complete our projects (likely because we were new to the technologies implemented). This time, we actually completed nearly everything we set out to accomplish and ultimately produced a robust application. We are also proud of the design! We feel it's the right mix of professional and playful. What we learned It was a few members' first time using React Native, but they now feel more comfortable with the framework and learned more than ever during this hackathon. We also learned a lot about structuring an app with a lot of global state. Redux to the rescue! We also learned a lot about react-native-gesture-handler, and a team member claims they have finally overcome their fear of class components. What's next for Ambi We'd love to ultimately eject from expo and implement handwriting recognition and score the submitted handwriting images. We would also love to create more tap games, as they comprise an exciting and surprisingly effective corner of the application. <div