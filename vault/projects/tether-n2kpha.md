---
slug: "tether-n2kpha"
url: "https://devpost.com/software/tether-n2kpha"
title: "Tether"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 1151
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/transportation"
  - "substrate/structured_db"
---

# Tether

> A focus ritual for brains that freeze before they begin.

[Devpost](https://devpost.com/software/tether-n2kpha) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[accessibility]] [[health_clinical]] [[mental_health]] [[transportation]]
**substrate** [[structured_db]]

**stack** claude-api-(anthropic), express.js, framer-motion, grok, localstorage, node.js, react, tailwind-css, typescript, vite, web-audio-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next

## Body

What's your energy right now? What are you avoiding? That's the whole check-in. Tether handles everything else. Does your brain freeze in fog or in chaos? Two minutes to answer that once, and Tether never asks you to explain yourself again. Your session, built for your brain. Sound type, micro-action, and framing — all from two inputs. Pick a duration and the ritual begins. Sound environment. Micro-action. Brain framing. Why do focus apps give you a list when your brain just needs one door to walk through? No account. No onboarding wall. No "set up your workspace first." Just open it and start — exactly when you need it most. What if the hardest part of starting wasn't the task itself — but the app you used to track it? We made the entire ritual fit in one card. Foggy brain Pink noise. The warmer tones signal your nervous system to slow down first The color even shifts to match your brain state. This is brown noise visualized live via Web Audio API. The wave moves with the sound. Your brain has something to follow not just to hear. Binaural beats at 10Hz two sine waves, one per ear, generating a frequency your brain starts to follow. Best with headphones. No guilt if the answer is "not quite." Tether learns from both — and the next session gets a little more accurate because of it. Inspiration We didn't build Tether because we read about ADHD. We built it because we live it, the freeze before starting an assignment, the open tab that sits untouched for hours, the shame spiral when the same task shows up on your list for the third day in a row. Productivity apps kept telling us to plan better, break tasks down, use timers. None of them understood that the problem isn't knowing what to do. It's the moment right before doing it. What it does Tether is a focus ritual, not a to do list. It starts with a 2 minute onboarding conversation that learns your specific brain pattern, whether you freeze in a fog (slow, heavy, empty) or in chaos (scattered, racing, overwhelmed). Every session, you answer two questions: how's your energy right now, and what are you avoiding? You can type it or just say it out loud, Tether has a voice input mode using the Web Speech API, because for ADHD brains, even typing can be a barrier to starting. Tether then generates three things in seconds: a sound environment tuned to your brain state (brown noise, pink noise, or binaural beats synthesized live in the browser via the Web Audio API), a single micro action small enough that your brain can say yes before the freeze kicks in, and framing language matched to how your specific brain works, not generic cheerleading. If the same task appears multiple times across sessions, Tether recognizes the avoidance cycle and responds differently, directly naming the shame loop rather than pretending it isn't there. During your session, a quiet counter sits at the bottom of the screen: "14 brains focusing right now." No names, no chat, just the knowledge that you're not alone. This is body doubling, one of the most effective focus techniques for ADHD, built directly into the experience. The more sessions you run, the smarter it gets. After enough sessions, Tether generates a Pattern Reveal Card, a personalized behavioral insight report built from your session history: when you focus best, which sound works for you most often, which kinds of tasks you avoid the longest. Not generic advice. Your actual data, turned into something that feels like being understood. How we built it Frontend: React + TypeScript + Vite. Framer Motion for the cinematic landing page animations including parallax cloud scenes, scroll linked opacity transforms, and spring physics UI elements. Tailwind CSS for layout. Audio engine: Fully custom Web Audio API implementation, no libraries, no audio files. Brown noise uses Brownian motion filtering on white noise. Pink noise uses a 7 coefficient Voss McCartney approximation. Binaural beats use two stereo panned sine oscillators with a frequency delta at 10Hz (alpha range). All with gain ramping for smooth fade in and out. Voice input: Web Speech API for real time speech to text, removing the typing barrier entirely for users in a freeze state. AI layer: Grok API (xAI). Three distinct prompts, an onboarding turn by turn conversation that extracts a structured brain profile, a session recommendation generator that returns sound type, micro action, and framing as structured JSON, and a feedback processor that refines the user's profile notes after each session. Storage: localStorage only, no accounts, no database, no friction. The profile and session history live entirely on the user's device. Deployment: Replit, after hitting paywalls on Railway (free tier expired) and Render (required card verification), we pivoted to Replit which got us live with zero friction under deadline pressure. Sometimes the fastest path wins. Challenges we ran into Getting the Web Audio API to behave consistently across browsers without a user gesture was harder than expected, AudioContext has to be created inside a click handler or it silently fails. The binaural effect also only works with headphones and we had to decide how prominently to communicate that without breaking the flow. The onboarding conversation design was genuinely difficult. Too many questions and users with ADHD won't finish it. Too few and the profile isn't useful. We went through around a dozen prompt iterations to find the right balance, 3 to 4 turns that extract brainMode, stallType, and crashTime reliably. Deployment was its own challenge. With under 2 hours to deadline, Railway's free tier was expired and Render required card verification. We had to quickly restructure our thinking and get the app live on Replit instead, a reminder that under pressure, shipping beats perfection. What we learned That the hardest part of building for neurodivergent users isn't the technology, it's resisting the urge to add features. Every time we thought "wouldn't it be cool to add X," we had to ask whether X would make the frozen moment easier or harder. Simplicity is the product. We also learned that building something you personally need hits differently. Every design decision had a gut check: would this have helped me at 2am before an exam? That question cut through a lot of noise. What's next A browser extension that puts the Tether ritual one click away on any tab, so when you've had the same assignment open for 2 hours, help is right there without switching apps. A therapist or coach dashboard where a professional can view anonymized pattern data with the user's consent, turning Tether's behavioral insights into something clinically useful, not just personally validating. Longer term: wearable integration. If your watch detects elevated heart rate and stillness at 2am, Tether should already know you're in a freeze before you even open the app. <div