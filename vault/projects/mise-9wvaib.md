---
slug: "mise-9wvaib"
url: "https://devpost.com/software/mise-9wvaib"
title: "— Mise —"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 720
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# — Mise —

> Redefining the cooking experience with Augmented Reality.

[Devpost](https://devpost.com/software/mise-9wvaib) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[supply_logistics]]
**substrate** [[video_visual]]

**stack** metaspatialsdk, oculus, openai

## How they structured the write-up

- 💡 inspiration
- ✨ key features & experience design
- 🛠️ how we built it & technical implementation
- 🧗 challenges & learnings
- 🚀 what's next for mise

## Body

Mise is your AR cooking assistant. First, update your pantry from a curated list of hundreds of common ingredients. Roughly estimate the amount of a given ingredient that you have so Mise understands exactly what is in your kitchen at all times. Add your cooking time and cuisine preferences, along with dietary restrictions and allergies in the settings menu. Based on your ingredients, dietary restrictions, and preferences, Mise will automatically curate the perfect recipes for you. Mise splits complex recipes into easily digestible, step-by-step micro-tasks, making cooking easier and more enjoyable. Mise's recipe instructions are intuitive and easy to understand, unlike complicated recipes online. This makes it perfect for beginners. Incorporated spatial timers and floating instructions allow for a hands-free, premium cooking experience. Ask Mise questions at any point to get expert AI feedback. Mise leverages the Passthrough Camera API to become context aware. Our integrated voice assistant will chat with you and assist you as you cook, offering personalized guidance. Manage your pantry easily in seconds and update it with ease to make cooking seamless and simple. 🍳 Mise: Your AR Cooking Assistant 💡 Inspiration We have all had that moment: opening the fridge, staring at a random assortment of ingredients, and thinking, "I have nothing to eat." I wanted to eliminate that decision fatigue entirely. I also wanted to solve a problem every home cook faces: trying to scroll through a recipe on a phone while your hands are covered in flour or sauce. Mise (short for Mise en place ) bridges the gap between your physical kitchen and digital guidance. By leveraging the Meta Spatial SDK , I built an assistant that lives inside your kitchen without taking up physical space, making cooking effortless, clean, and genuinely fun. ✨ Key Features & Experience Design Mise transforms your kitchen into an intelligent, immersive environment. Feature Description 🤖 AI Sous-Chef (Vision) Have a question? Leveraging the Passthrough Camera API , you can ask our Voice Assistant anything. It can "see" your pot to tell you if the water is boiling or if your potatoes are cooked. 🧠 AI Recipe Disks Don't know what to cook? Simply populate your digital pantry, and our AI Engine generates recipe "disks" based on exactly what you have, your dietary needs, and how much time you have. 🖐️ Hands-Free Cooking No more dirty phone screens. Follow step-by-step spatial instructions with Hand Tracking . Interact with floating timers and tips without touching a thing. 🗑️ Zero Waste Mise tracks your digital inventory and suggests meals to cook before your food expires, saving you money and reducing waste. "Mise brings your kitchen into the future — giving you a sous-chef that can see, think, and guide you." 🛠️ How We Built It & Technical Implementation We built Mise as an AR-first experience tailored for the Meta Quest 3/3S. We heavily utilized the Meta Spatial SDK to ensure high performance (60 FPS+) and reliable tracking. Core Technologies Meta Spatial SDK: Used for spatial anchors (locking UI panels to your walls), hand tracking for hygiene-friendly control, and passthrough environment integration. Passthrough API & Multimodal AI: We pipe visual data from the Quest’s cameras to a Vision LLM, allowing the user to ask context-aware questions about the physical food in front of them. Interactive UI: Custom Android-style components built for Horizon OS that allow for rapid pantry management and intuitive recipe navigation. 🧗 Challenges & Learnings Spatial UI Alignment: Getting VR UI panels to feel naturally placed in a real kitchen without obstructing the user's view of dangerous items (knives/stoves) required careful design and calibration. Latency vs. UX: AI recipe generation and visual analysis can be slow. We optimized caching and "debouncing" AI calls so the user never feels stuck waiting inside the headset. Instruction Translation: Translating flat text recipes into 3D animated guidance was a major UX hurdle. We iterated several times to make the instructions feel native to spatial computing rather than just floating text. 🚀 What's Next for Mise We are just getting started. Here is our roadmap for the next updates: [ ] Smart Grocery Lists: Auto-generation based on low inventory. [ ] Hardware Sync: Integration with smart fridges and ovens for auto-timers. [ ] Community Cookbook: Share your generated "Recipe Disks" with other users. Cooking shouldn't be stressful. With Mise, it's the future. <div