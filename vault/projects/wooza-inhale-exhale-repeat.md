---
slug: "wooza-inhale-exhale-repeat"
url: "https://devpost.com/software/wooza-inhale-exhale-repeat"
title: "Wooza - Inhale, Exhale, Repeat"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 615
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/mental_health"
  - "substrate/video_visual"
---

# Wooza - Inhale, Exhale, Repeat

> Relaxing your work schedule by introducing natural breaks - with guided breathing exercises presented as fun minigames. Boost your health and reduce stress while gaining awesome (virtual) hats!

[Devpost](https://devpost.com/software/wooza-inhale-exhale-repeat) · hackathon [[HackZurich 2021]]

## Facets

**mechanism** [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[mental_health]]
**substrate** [[video_visual]]

**stack** html5, jitsi, love, react, snap-camera, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wooza - inhale, exhale, repeat

## Body

Main image Browser Plugin Camera overlay Breathing mini game Inspiration As remote work is here to stay, its drawbacks might as well: back-to-back meetings with context switches all day long. Especially in todays (and tomorrows) fast-paced world, consciously taking a break is more important than ever. We strongly believe that this is best achieved when "pausing" is naturally embedded into our daily work routines. It should also be fun and engaging, that's why we introduce guided breathing exercises in the form of mini games into the dreaded online video calls. Indeed, slow-paced breathing is a very effective method to reduce stress levels. It has benefitial effects both on our physical and mental health and even helps strengthen our personal resilience, as research has shown. It is super simple: Inhale, exhale, repeat . What it does Wooza enhances online video calls. When a meeting starts, all participants are forwarded to an individual lobby where they are greeted with a mini game. They see a small reward getting buried under a pile of sand. Through slow and deep breathing they can blow away the sand and claim their reward. The exercise ends after 3 minutes and they are forwarded to the actual video call. They take their respective rewards with them into the call - awesome hats, gimmicks or virtual pets added as video filters! Of course there are also leaderboards, additional settings and admin dashboards. How we built it Wooza works by intercepting the "Join"-Links in your calendar events. We redirect you to our own lobby built in React-JS, where most of the magic happens: Your breathing intensity and duration is recorded through the headsets microphone, which is used to interact with our minigame. After the minigame is finished, you are redirected to the original video call. To add the reward / gimmicks to the video feed we pipe your webcam feed through Snap-Camera, which provides facial tracking and enables custom filters. The proof-of-concept is built on top of Jitsi (with our own custom user interface), but the architecture allows us to support basically any video conferencing software which accepts our virtual camera feed. Challenges we ran into The trickiest part was to come up with a solution which users will engage with for a longer time. Too many health apps today lack a fun component or are not embedded into the user's daily habits (getting users to abandon them very quickly). We are confident that our idea creates a "comfort zone" in a naturally stressful environment. Also, engaging the whole team instead of only individuals should create a stronger incentive to keep going. Some other more technical challenges: The breath recording was very sensitive to background noise. We solved this by using a noise cancelling headset from Logitech, and by calibrating the recording to the user. The particle rendering and physics engine for the sand simulation was very tricky. We switched to a new framework late during the development. This framework was less advanced but allowed us to apply custom adjustments tailored to our use case. Accomplishments that we're proud of We built a working prototype which already helped us reduce our own stress levels during the Hack. Getting healthier definitively can be fun! What we learned Getting early feedback from potential users and workshop partners helped us shape the solution for real life challenges. Also, actually building the minigame based on our mockups and ideas was harder than expected. What's next for Wooza - Inhale, Exhale, Repeat Wooza won't be out of breath for a long time! We already gathered a lot of interest with multiple parties and are looking forward to putting our concept to the real-world test with an innovative partner. <div