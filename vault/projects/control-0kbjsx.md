---
slug: "control-0kbjsx"
url: "https://devpost.com/software/control-0kbjsx"
title: "Control."
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1250
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "substrate/structured_db"
---

# Control.

> Your AI companion for addiction recovery - available at 2am when no one else is

[Devpost](https://devpost.com/software/control-0kbjsx) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[mental_health]] [[security_privacy]]
**substrate** [[structured_db]]
  <sub>weak: geospatial</sub>

**stack** firebase, firestore, framermotion, geminiapi, nextjs, react, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for control.

## Body

plant growth based on the active days community page nova avatar profile user jouney map cbt dashbaord Inspiration It starts the same way for millions of people. It's 2am. The craving is loud. You reach for your phone — and nothing reaches back. Alcohol addiction affects 400 million people globally . 3 million die from it every year — more than AIDS and tuberculosis combined. And yet 80% of those who need help never receive it. Not because they don't want to get better. Because the support doesn't exist when they need it most. Therapy has waitlists. Helplines are reactive. Apps feel clinical and cold. Nobody had built a recovery companion that actually shows up — at 2am, mid-craving, judgment-free, and powered by real AI. That's what inspired Control. What It Does Control. is a gamified, AI-powered recovery companion for alcohol addiction that combines three things no existing app has put together: NOVA -AI Voice Companion Talk to NOVA out loud. Tap, speak, and NOVA responds in real time using a full voice conversation loop - no typing, no waiting, no judgment. Available 24/7. CBT Thought Reframing NOVA detects negative thought patterns and rewrites them using Cognitive Behavioural Therapy techniques: "I always fail. I'm weak." → "You've tried many times. That's not weakness. That's someone who refuses to give up." AI Risk Assessment A 10-question onboarding assessment feeds a dynamic risk scoring model. The app adapts its entire experience — exercises, AI tone, check-in sensitivity — to each user's unique profile. $$\text{Risk Profile} = \begin{cases} \text{High} & \text{if score} \geq 15 \ \text{Moderate} & \text{if score} \geq 8 \ \text{Low} & \text{otherwise} \end{cases}$$ 🌱The Living Plant A plant that grows with every single check-in: $$\text{Plant Stage} = \begin{cases} \text{Seed} & n = 0 \ \text{Sprout} & 1 \leq n \leq 6 \ \text{Flowering} & 7 \leq n \leq 20 \ \text{Full Bloom + Fruit} & n \geq 21 \end{cases}$$ Miss a day? It doesn't die. It waits — exactly like real recovery. Craving Shield Box breathing, 5-4-3-2-1 grounding, a 15-minute craving timer, and one-tap SOS with direct helpline connection. Crisis support in under 3 seconds. Gamification XP, streaks, levels, and badges. 50 XP for every sober day. 10 XP even if you slipped — because showing up honest is already courage. The same dopamine loops billion-dollar apps use to keep people hooked — turned completely around to heal. AI Insights Mood and craving charts, trigger pattern detection, body recovery timeline, and real stats: money saved, calories avoided, health score climbing. How We Built It Tech Stack Layer Technology Frontend Next.js, React, Framer Motion AI / LLM Google Gemini API Voice Web Speech API (STT + TTS) Database Firebase Firestore Auth Firebase Anonymous Auth + Google OAuth Deployment Vercel NOVA's Voice Architecture $$\text{User Voice} \xrightarrow{\text{Web Speech API (STT)}} \text{Text} \xrightarrow{\text{Gemini LLM}} \text{Response} \xrightarrow{\text{Web Speech API (TTS)}} \text{NOVA Speaks}$$ We optimised latency by streaming the Gemini response and beginning TTS synthesis as soon as the first sentence completed — rather than waiting for the full response. CBT Engine NOVA's empathy and reframing behaviour is driven entirely by a carefully engineered system prompt fine-tuned over dozens of iterations. The prompt instructs Gemini to: Detect distorted thinking patterns (catastrophising, all-or-nothing thinking) Apply specific CBT reframing techniques Maintain a warm, non-clinical tone at all times Never use language that implies judgment or failure Anonymous-First Architecture Firebase Anonymous Auth gives every user a unique ID with zero personal data attached. A recovery code system allows users to transfer their streak, plant, and XP across devices — without ever creating an account. Challenges We Ran Into Making NOVA feel human, not robotic Getting Gemini to respond with genuine warmth in a recovery context took dozens of prompt iterations. Too clinical felt cold. Too casual felt dismissive. Finding the exact tone was the hardest single problem we solved. Voice loop latency STT → Gemini → TTS introduces real-world delay that breaks the feeling of natural conversation. We solved this by streaming Gemini's output and beginning audio synthesis mid-response. Designing for emotional safety A relapse screen that feels punishing could cause genuine harm to a vulnerable user. We went through multiple iterations of the "I had a drink" flow before landing on something truly compassionate — not performatively so. Anonymous auth with persistent data Firebase anonymous sessions don't persist across devices by default. Building a seamless recovery code transfer system — that feels simple to a non-technical user — was an unexpected but important engineering challenge. Accomplishments That We're Proud Of NOVA works. A real, live, two-way voice conversation with an AI that responds with empathy — in a browser, with no external voice service, powered entirely by Web Speech API and Gemini. The plant is alive. The most emotional feature in the app — a living visual record of every day someone chose themselves. Watching it grow during testing genuinely moved us. Zero punishment design. Every single flow — relapse screen, missed check-in, low mood — was designed to feel compassionate. No red warnings, no reset buttons, no shame. This was intentional and we're proud of it. A complete, shippable product. 13 fully designed pages, a consistent fantasy medieval design system, Firebase integration, live AI voice, gamification, crisis tools — all built and working. The design matches the mission. The fantasy medieval aesthetic isn't decoration. It reframes recovery as a quest — something worth taking, not something to be ashamed of. What We Learned Empathy is an engineering problem. The difference between a helpful AI and a cold one is entirely in how you prompt it. We spent more time on NOVA's system prompt than any other feature. Shame is the biggest barrier to recovery. Every design decision — anonymous auth, no relapse punishment, the compassionate reflect screen — was made because shame kills recovery before it starts. Gamification works because the brain does. XP and streaks aren't gimmicks. They create the same dopamine reward loop that keeps people hooked on harmful apps — pointed in the opposite direction. Voice changes everything. Typing "I'm struggling" feels clinical. Saying it out loud and having something respond — that's a completely different emotional experience. The moment NOVA talked back for the first time in testing, the whole team went quiet. Design is therapy. The visual language of an app sends a message before a single word is read. A dark, warm, medieval aesthetic says "you are safe here" in a way that clinical blues and whites simply cannot. What's Next for Control. Phase 2 — Beyond Alcohol The craving loop is identical whether the addiction is food, social media, gambling, or screen time. Our next phase expands Control. to every compulsive behaviour — same AI companion, same plant, same quest framework. Phase 2 — Psychologist Marketplace NOVA gets users stable at 2am. A licensed psychologist gets them all the way home. We're building an in-app marketplace of verified therapists for Pro users — on-demand, anonymous, and affordable. Phase 3 — Holographic NOVA Not on a screen. In your room. A holographic companion that is physically present with you during your hardest moments. The technology is almost there. Control. will be ready when it is. The bigger vision: $$\text{Control.} = \text{AI Companion} + \text{Human Therapist} + \text{Holographic Presence}$$ "Alex came in at 2am. Craving loud. Hope quiet. Six weeks later — Alex is still here. The plant is in full bloom." Control. — Because everyone deserves a companion on the hardest quest of their life. ᚠ ᚢ ᚦ ᚨ ᚱ <div