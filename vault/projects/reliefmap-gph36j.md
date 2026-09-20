---
slug: "reliefmap-gph36j"
url: "https://devpost.com/software/reliefmap-gph36j"
title: "ReliefMap"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 955
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# ReliefMap

> ReliefMap is a mobile-first app that helps disaster victims quickly find nearby resources like shelter, food, medical aid, and more—all through an interactive map.

[Devpost](https://devpost.com/software/reliefmap-gph36j) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]] [[housing_homeless]] [[security_privacy]]
**substrate** [[geospatial]]

**stack** bolt.new, chatgpt, google-maps, google-translate

## How they structured the write-up

- about
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for reliefmap

## Body

Onboarding List of Disasters LA Fires with Filter Button Hurricane Milton near Tampa News & Updates Settings Page Settings Page with Spanish Translation NOTE: PLEASE TRY TO DEMO THE APP USING ANDROID STUDIO OR AT LEAST THE PWA VERSION OF THE WEB APP. It was meant to be used and experienced as a mobile app first. About ReliefMap is a mobile-first disaster relief app built for Android, IOS, and the web (as a PWA). It helps people quickly find nearby disaster resources like shelter, food, supplies, and medical help, all on an interactive map. Users select a current disaster (mock disasters for this prototype include the LA Fires, Maui Fire, Asheville Flood, or Hurricane Milton), filter by the kind of help they need, and tap color-coded pins to see detailed information on shelters, supplies, and more. News and updates are also filtered based on the selected disaster. ReliefMap includes Spanish translation, because in a crisis, non-English speakers are often the most vulnerable. This app may seem simple, but there is nothing like it. There is no central place for disaster relief and recovery information. ReliefMap aims to fix that. And here’s the kicker: I’m 55. I’ve never coded before. I thought Metro was a subway system and Cocoapods were marshmallows. I spent more time in my terminal this month than I have in my lifetime. But I built it, and it works. Inspiration I used to work for the Red Cross and was struck by the chaos that follows disaster—not just physically, but digitally. Reliable information is one of the most prized commodities during a disaster, but its often scattered, outdated, or buried throughout the web. There is no single, easy-to-use tool to find help nearby. On someone’s worst day, they shouldn’t have to work even harder to figure out where they're going to stay or what they're going to eat. ReliefMap is my answer to this informational gap. What it does Choose a current disaster from the list. View a zoomed-in, touch-responsive map of the affected area. Filter by the type of assistance: food, shelter, supplies, etc. Tap a pin to see detailed information about the resource. Click the address to open it up in Google to get directions. Click the phone number to call from the app. Get disaster-specific news and updates. Translate the entire app into Spanish, cache files for offline mode, get notified of new resources, and locate yourself on the map. It's designed for phones because in an emergency, that's what people have. How I built it I built the app using React Native with a Google Maps API. I ran into API key issues, display inconsistencies, and most persistently, dependency conflicts. Every time I fixed one problem, another would surface, but I eventually made it work. As someone new to coding, I had to learn everything from file structure to build processes, versioning issues, and mobile debugging. I relied on AI tools to assist, but I still had to make sense of the underlying architecture and logic. It was a crash course in app development, and I was often the crash test dummy. Challenges I ran into Dependency Hell: This was, by far, the steepest part of the learning curve. Conflicting packages, mismatched versions, and missing peer dependencies derailed progress regularly. Routing and Layout Errors: At one point, I encountered a frustrating "multiple files match the route name ./layout" error. This led to a deep dive into file naming conventions, Metro bundler behavior, and platform-specific file resolution. This is ultimately what led to the demise of Expo. AI couldn't figure it out and neither could I. I tried everything! Map Integration: While Google Maps seemed like a straightforward integration, it brought a host of problems—blank maps, token issues, billing restrictions, and constant API errors. After several days of troubleshooting, I ultimately got Google Maps to work. Supabase Integration: It took me multiple attempts to make this work. Problems included environment variable setup issues, dependency clashes, and bugs I couldn’t resolve. Ultimately, I did get this to work. Platform Issues: I thought that React and Expo would play well with the different platforms (IOS, Android, web). No one played well in the sandbox with others. Even icons were causing major problems. Working with the AI: I found the AI always wanted to make substantial changes which then led to more errors. If it was a surgeon, it would always be cutting! I had to continually remind it to think and analyze before it acted. This process taught me more than just how to code—it gave me a deep respect for the complexity behind apps we often take for granted. I’ve never spent more time in the terminal, but I’ve also never been more invested in solving a problem. Accomplishments that I'm proud of I brought a working prototype to life with no prior experience. I designed something that could actually help real people in real disasters. I proved that age and background are not barriers to building tech that matters. What I learned Having a baseline understanding of code would’ve saved a lot of late nights. I came up with a ton of ideas for future features—some practical, some just cool. The app works but its probably not clean and efficient. Bolt AI even gave me suggestions about what to do next. The power of AI is amazing, but it still needs a human to guide the vision and keep pushing when it hits a wall. What's next for ReliefMap I want to: launch a public version; build Supabase to handle web-scraping and real-time data feeds; and secure funding or partnerships to keep it maintained and disaster-ready. This app deserves to exist—not because it's flashy, but because it’s needed. <div