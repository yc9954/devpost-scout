---
slug: "study-spotify"
url: "https://devpost.com/software/study-spotify"
title: "Study Spotify"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 406
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Study Spotify

> You know how students struggle to focus and end up doom-scrolling instead of studying? Study Spotify combines beautiful Pomodoro timers with mood-based playlists in one aesthetic app.

[Devpost](https://devpost.com/software/study-spotify) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** css, lovable, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for study spotify

## Body

Inspiration We noticed students (including ourselves) constantly switching between timer apps, music apps, and productivity trackers—losing focus in the process. We'd set a timer, then spend 10 minutes finding the "perfect" playlist. We wanted to create a beautiful space where you could simply vibe and study without any friction. What it does Study Spotify is a focus timer that adapts to your study mood. Users select their current energy level (deep focus, chill study, energized cramming, or late night grind), set a customizable Pomodoro timer, and immediately get matched with curated playlists and ambient sounds. The app tracks study sessions, celebrates streaks, and provides a visually satisfying experience that makes you actually want to focus. How we built it We built Study Spotify using React for the component-based UI, with custom CSS animations for the timer visualizations and mood transitions. We integrated the Spotify Web API for playlist curation and used local storage to persist user stats and preferences. The particle effects and gradient backgrounds were crafted with Canvas API and CSS, creating that premium aesthetic feel. Challenges we ran into The biggest challenge was getting the Spotify API authentication flow working smoothly without disrupting the user's focus flow. We also struggled with making the timer accurate across different browser tabs and ensuring the audio continued playing seamlessly. Balancing aesthetic beauty with performance—especially with our particle effects—required lots of optimization iterations. Accomplishments that we're proud of We're incredibly proud of the UI/UX—it genuinely feels premium and calming. The mood-matching algorithm works surprisingly well, and our beta testers said it "actually helped them focus" instead of being just another productivity app they'd abandon. We also nailed the smooth transitions between study sessions that make the experience feel cohesive and intentional. What we learned We learned a ton about browser APIs, especially the Web Audio API and managing state across sessions. More importantly, we learned that good design isn't just about looking pretty—it's about removing friction. Every extra click or decision point kills momentum, so we obsessed over making the core flow effortless. What's next for Study Spotify We're planning to add collaborative study rooms where friends can sync timers and compete on streaks, integrate with calendar apps to auto-schedule study blocks, and build a mobile app for on-the-go studying. We also want to add ambient sound mixing (rain + coffee shop + lofi) and personalized playlist generation based on your actual focus patterns and music taste. <div