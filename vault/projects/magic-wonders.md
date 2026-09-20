---
slug: "magic-wonders"
url: "https://devpost.com/software/magic-wonders"
title: "Magic Wonders"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 538
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Magic Wonders

> Magic Wonders brings gesture-based spellcasting to mixed reality. Use a virtual or smart wand to duel, cast spells, and control your smart home in a world where your motions create real magic.

[Devpost](https://devpost.com/software/magic-wonders) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[housing_homeless]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, express.js, postgresql, react-native, supabase, typescript

## How they structured the write-up

- ✨ inspiration
- 🛠️ how we built it
- 🔄 updates made during the competition
- ⚔️ challenges we faced
- 🎓 what we learned
- 🚀 what’s next

## Body

App Showcase - A look at the core Magic Wonders experience in mixed reality Select Your Build - Choose your spell loadout and customize your strategy before each duel Duel Phases - See the flow of each battle—from selecting spells to resolving actions Spell Resolution - Watch spells collide as timing, accuracy, and effects determine the outcome Smart Home - Cast gestures to trigger lights, music, and routines through Alexa integration Magic Wonders — Bringing Real Magic Into Mixed Reality ✨ Inspiration Magic Wonders began with a simple spark: watching my daughter cast spells with an interactive wand at a theme park. The experience was magical and physical, but it ended the moment we left. That led to one question: What if magic followed you everywhere — into your home, your games, and your world? Magic Wonders was created to bridge the physical and digital worlds through gesture-based magic, AI, and mixed reality. 🛠️ How We Built It Magic Wonders is a true connected ecosystem combining hardware, AI gesture recognition, smart-home control, and an online multiplayer game. Our app is built with React Native, giving us a fast, cross-platform foundation for the entire experience. Smart-Home Spellcasting Magic Wonders connects to Alexa, allowing players to control their real-world environment through magical gestures. Players can: Turn lights on/off Change colors and brightness Play music or playlists Trigger Alexa routines Your home becomes an extension of the magical universe. Online Multiplayer Dueling Players can duel friends in a fast, witty online magical battle — a strategic, overpowered evolution of rock-paper-scissors where timing, prediction, and spell choices determine the winner. Hardware Custom smart wand IC and 3D design 9-axis IMU streaming motion data BLE communication with custom C++ firmware LED crystal tip integrated into the housing with interchangeable pointers (Crystals) AI Gesture Recognition We trained a TensorFlow model using real user motion data. Model architecture: A bi-directional LSTM feeding into a 64-unit Dense layer, followed by Softmax classification. Converted to TensorFlow Lite for efficient execution on-device. 🔄 Updates Made During the Competition Build 2.0 included the following major updates: 🌐 Multiplayer Duel v1.0 🤖 Bot Dueling (AI opponents for practice and matchmaking fills) 🔊 Improved Sound Effects, Spatial Audio & Asset Preloading 🎓 New Interactive Tutorials 🪄 New Wand 3D Model 🧠 Enhanced Gesture Recognition These enhancements significantly improved gameplay, immersion, and responsiveness. ⚔️ Challenges We Faced Responsive design adaptation to Meta Quest UI constraints Gesture diversity → built our own motion dataset pipeline Designing a sustainable and attractive progression system BLE bandwidth → optimized packet formats Hardware microcontroller upgrades to support on-device AI React Native limitations when accessing Meta Quest–specific sensor data 🎓 What We Learned Physical gestures dramatically increase immersion Real-world responsiveness makes the magic feel real Multiplayer adds social strategy and replayability Hardware constraints push cleaner architecture and optimization 🚀 What’s Next Improved dueling system Player & spell progression More advanced gesture models & better recognition A dedicated VR scene with real hand–tracked spellcasting for immersive gesture interactions Voice recognition support New elemental abilities Unified ecosystem across wand, mobile app, and smart home Magic Wonders began with a spark, now it lets anyone cast real magic in their home, on their device, and inside a shared magical world. <div