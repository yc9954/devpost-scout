---
slug: "alerto-emergency-response-app"
url: "https://devpost.com/software/alerto-emergency-response-app"
title: "Alerto – Emergency Response App"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 798
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Alerto – Emergency Response App

> One life lost to delay was enough — Alerto ensures no one waits in silence.

[Devpost](https://devpost.com/software/alerto-emergency-response-app) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** dart, firebase, flutter, google-maps

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for alerto – emergency response app

## Body

I design it after complete project. Splash Screen & Authentication(User Part) Homepage if Already send a request Get Current Location & Send Request Get AEDs and Red Cross resources location and Details Profile Optimization AEDs and Red Cross resources Part and able to see user requesr see location user and AED Status Update after resolve problem of user Firebase Backend Firebase Backend Inspiration During my third year of university, everything changed. I had just returned home from my exams when I found my father on the verge of passing away. He wasn’t sick. There were no warnings. I froze. He looked at me from the door — I will never forget that moment. I lost all sense of what to do. My sister reminded me, “Maryam, give CPR — you know it.” I did. I tried. But he didn’t respond. We called an ambulance — they didn’t pick up right away. When they finally responded, they couldn’t find the route to our house. We lost crucial time. That moment shattered me. I felt everything had ended. But when I returned to university, my supervisor gave us a project idea — “Build something that helps in emergencies.” That hit straight to my heart. I knew this was my chance to build something meaningful — something that might save someone else’s parent. What it does Alerto is a real-time emergency response app designed to give ordinary people the tools to act fast. The app helps users: Locate nearby AEDs (Automated External Defibrillators) using Google Maps Platform. Find Red Cross resources such as first aid points or support centers. Share their exact GPS location in an emergency so rescuers or bystanders can reach them faster. Instead of waiting helplessly for help, bystanders can immediately find lifesaving equipment and trusted resources nearby — turning minutes of panic into moments of action. How we built it I developed the core logic and functionality using Flutter . We used Firebase for user authentication, cloud data storage, real-time tracking. Google Maps API powers the live location view and routing system for rescuers. My sister helped me design the UI to be simple and clear for anyone to use — even in panic. My friend helped choose the name Alerto . My supervisor and mentor guided me every step of the way through architecture and decision-making. Challenges we ran into Reliving that traumatic night while designing the solution — building this app was emotionally heavy, but it gave me purpose. Working tirelessly for 2 months , often with little sleep, just to bring the basic version of Alerto to life. Ensuring live tracking worked seamlessly using Firebase Firestore— maintaining real-time sync across users was technically demanding. Designing a UI that performs clearly and quickly during real emergencies — it had to be fast, easy to understand, and work under pressure. I also ran into limitations with Google Maps’ Directions API , exceeding the free cap of 10,000 requests during development. I reached out to their support team, and they sponsored me by waiving most of the fees. In the end, I only had to pay $12.47 , and their support meant everything to me as a student developer. Accomplishments that we're proud of Turning the most painful moment of my life into a project that could save others. -Building a functional emergency app — with AED/Red Cross locator, live GPS tracking, and clear instructions — in just 2 months. Receiving support and sponsorship from Google Maps API team , who waived charges when I exceeded usage limits during testing. Designing a clean, intuitive interface with help from my sister, making sure it's usable even in panic situations. Learning and integrating multiple Firebase services (Authentication, Firestore, Realtime Database, Cloud Messaging) and APIs as a student developer. Hearing from others that this app could truly make a difference — that is my biggest achievement. And finally, completing this as my final year project — I poured my heart into it, and I truly hope I get an A . What we learned That technology built with heart can create real impact. How to build cross-platform apps using Flutter, optimized for both low-end and modern devices. Deep integration of Firebase for real-time features, data sync, and authentication. Importance of user experience in high-stress moments — every second matters in an emergency. That help can come from unexpected places — like when the Google Maps team stepped in to support me during development. Most importantly: that grief, when channeled into action, can become purpose — and that purpose can solve real-world problems . What's next for Alerto – Emergency Response App Expand the database of AEDs and Red Cross resources worldwide. Partner with local health orgs to verify AED locations. Release more versions with improved features and real-world testing. <div