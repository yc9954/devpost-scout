---
slug: "see-and-speak-spanish"
url: "https://devpost.com/software/see-and-speak-spanish"
title: "Language IRL"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 829
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Language IRL

> Immersion is the easiest and most fun way to learn a new language. Turn your world into a classroom, and let your tutor turn you into a pro!

[Devpost](https://devpost.com/software/see-and-speak-spanish) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** azur-cognitive-services, azure-speech, c#, hand-tracking, meta-xr-passthrough, meta-xr-scene-api, mochineko-voice-activity, quest-3, quest-3s, unity, unity-playerprefs, unity-sentis, yolo-onnx

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for language irl

## Body

Language IRL Cover Photo Main Menu Full Sentence Lesson Success! Inspiration Language IRL began with a question I could not shake: What if there were a better way to learn a new language? Not by memorizing flashcards, but by turning the world around you into your own personal classroom. That question grew from an unexpected place. Eight years earlier, when I was just getting started in VR, I made an action comedy called Kungfuscius, a story about an AI mentor who appears in augmented reality to help you level up your life. It was wild and slapstick and I genuinely risked my life to make it, but the heart of it stayed with me: What if everyone could have a personal guide who sees the world alongside you, talks to you, and helps you grow? For years, that idea lived only as a VR film. Then Meta opened computer vision access on the Quest 3, and suddenly an AI mentor no longer felt fictional. I finally had the tools to build a companion that could recognize your environment, understand your voice, and interact with you in mixed reality. Language learning felt like the perfect place to begin; something millions attempt yet few ever get the immersive environment they need to succeed. What It Does Language IRL transforms your real environment into an interactive language-learning space. Your room becomes your vocabulary list. Your world becomes your lesson. Monobonobo, your mixed reality tutor, floats through your space teaching you words tied to real objects. You respond by speaking aloud. Wherever you go there’s a new lesson to be learned. Instead of abstract memorization, Language IRL lets you learn language the way the brain prefers, through spatial context. How We Built It For a two-person team with less than a month, the tech stack felt massive: computer vision, spatial mapping, gesture input, multilingual text-to-speech, pronunciation grading, and a fully animated mentor. We began by cloning Meta’s Passthrough API sample project and validating each system one by one. Meta’s tools gave us a huge head start; without them, there is no chance we could have built something this ambitious in time. I designed the UX, UI, and lesson plan, mapping out how learners move, gesture, and speak as their environment becomes the curriculum. Once the flow felt intuitive, Riko built the core architecture: lesson logic, gesture recognition, spatial UI, event sequencing, and Azure integrations for text-to-speech and pronunciation grading. With the foundation in place, I built Monobonobo, our Monkey Bot. Blending the spirit of Kungfuscius with the charm of Sunny from our first Quest game Monkey Tower. I wanted a joyful, expressive companion far from the uncanny valley. I modeled, rigged, and animated the character entirely in Blender. The breakthrough moment came when everything finally ran together: MB moved and spoke in sync. Objects were recognized. Gestures registered. Speech was understood. That was when I knew we were actually going to pull this off. Challenges We Ran Into The tech stack was enormous for two people in under a month. Getting all systems to work together - CV, gestures, TTS, speech scoring, MR UI - was far harder than validating them individually. Hand tracking required careful tuning to avoid frustration. Mixed reality UI composition needed precision to feel integrated. Pronunciation grading had to feel supportive, not punishing. Designing lessons tied to physical environments introduced new UX questions we had never considered before. Accomplishments That We're Proud Of We built a fully functional AI MR tutor in less than a month. Monkey Bot feels expressive, responsive, and emotionally engaging. We created a seamless interaction loop using CV, gestures, and speech. The experience genuinely teaches faster because it is grounded in the real world. We proved that mixed reality opens the door to meaningful, human-centered learning. And we turned a fictional concept from a silly action comedy into something that actually works. Riko arrived in Germany, and found the app really useful when preparing for the trip! What We Learned Vocabulary grounded in real objects dramatically improves retention. Hand tracking can feel magical when designed with forgiveness. Cloud plus on-device AI gives the best mix of speed and intelligence. Small touches like weekly tracking measurably boost engagement. Most importantly: learning feels more human when tied to your space, your actions, and your voice. What's Next for Language IRL Language IRL is just the beginning. We plan to: improve computer vision accuracy and streamline error correction expand gamification through challenges, collectibles, and progression add social features so friends can learn together build new lesson types that feel playful and rewarding But the long-term vision goes far beyond language. Once this technology reaches lightweight smart glasses, AI mentors will help people learn almost anything: fitness, cooking, creativity, mindfulness, emotional resilience - woven naturally into daily life. Language IRL is our first step toward that future, a future where learning is embodied, intuitive, and joyful, and where the playful spirit of Kungfuscius may finally come to life. <div