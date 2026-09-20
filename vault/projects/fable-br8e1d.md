---
slug: "fable-br8e1d"
url: "https://devpost.com/software/fable-br8e1d"
title: "Fable"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 711
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Fable

> Fable tells stories that adapt to your state of mind. As your brainwaves shift, we generate a story and create an immersive visual journey that mirrors your inner state in real time.

[Devpost](https://devpost.com/software/fable-br8e1d) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**substrate** [[geospatial]] [[video_visual]]

**stack** 3.js, eeg, elevenlabs, glsl, javascript, javascript/typescript-(next.js), lumalabs, mind-monitor, muse, ocs, openai-api, perplexity, python-(fastapi), tailwind-css

## How they structured the write-up

- inspiration💡
- what it does 🔮
- how we built it 🧱
- challenges we ran into 🚧
- accomplishments that we're proud of 🏆
- what we learned 📚
- what's next for fable 🚀

## Body

1 2 3 4 5 Inspiration💡 Fable began with a simple question: What if a story could adapt to your state of mind? As our team explored EEG technology, we became excited about the idea of measuring brain waves and uncovering hidden patterns of thought. What if a narrative could respond to your level of focus and relaxation—your shifting mental state? With EEG headsets reading brain activity, Fable dynamically shapes its plot, characters, sound effects, and visuals, crafting a living, breathing story that unfolds uniquely for you. This isn’t just storytelling—it’s an experience powered by your mind. What it does 🔮 Fable reads your brainwaves to craft a living story that responds to your every thought. As your mental state shifts, the plot dynamically evolves—changing tone, pacing, or twists to reflect how you feel. Simultaneously, the visuals adapt to match the unfolding narrative, immersing you in a real-time, brain-driven adventure where each scene is shaped by your mind. Even the moving gradient color background gradually fades and shifts, mirroring your inner state and heightening the immersive feel of your journey. How we built it 🧱 We built Fable by combining a Muse 2 EEG headset with a dynamic storytelling pipeline, powered by a Python FastAPI backend and a Next.js frontend styled with Tailwind CSS. The headset reads beta, alpha, theta, and gamma wave patterns—interpreted as relaxed, neutral, or focused states—using Mind Monitor and streams this data in real time through OCS. Our main story loop runs every 30 seconds, checking the user’s current state and using the OpenAI API to generate story scripts (and corresponding sound effect prompts) based on those EEG readings. We map each state to a specific narrative direction—for neutral, we steer the story toward fresh discoveries; for focused, we introduce more details or challenges; and for relaxed, we invite ease and wonder. To enhance immersion, we integrated 3.js and GLSL shaders to create an EEG-based dynamic gradient background that shifts in real time with the user’s mind state. We then feed both the text-to-speech lines and OpenAI-generated SFX prompts into ElevenLabs (streamed via WebSocket), allowing us to seamlessly produce both TTS dialogue and ambient sound effects. Finally, we bring the story to life visually with the Luma Labs API. Throughout this process, we employ a multithreading approach to process text, voice, and video asynchronously, ensuring smooth, parallel generation of each element. Challenges we ran into 🚧 We faced several hurdles bringing Fable to life. Hooking up OpenAI’s story generation so that each paragraph was generated sentence by sentence required careful orchestration within our webapp. Integrating ElevenLabs’ text-to-speech to ensure that audio and subtitles streamed seamlessly in real time was another challenge. Working around lengthy inference times on video generation models forced us to asynchronously and concurrently queue and segment videos to keep up with the script and audio. Our hacking led us to benchmark at least 10 different video generation APIs against each other for speed, including text-to-image and image-to-video generation. We also developed our own text-to-image and image-to-text pipeline to improve efficiency and control over the entire process. Accomplishments that we're proud of 🏆 We’re proud of creating a seamless, real-time storytelling platform that translates brainwave data into dynamically shifting narratives, audio, and visuals. By integrating multiple APIs—Muse for EEG, OpenAI for generative text, ElevenLabs for audio, and Luma Labs for visuals—we managed to build an immersive, multi-sensory experience that feels both personalized and technically robust. And most of all, we love the experience of listening to the stories that come out of our product! What we learned 📚 Through developing Fable, we gained a deeper understanding of real-time data processing, from parsing EEG signals to synchronizing audio and video outputs. Integrating diverse tools like OpenAI, ElevenLabs, and Luma Labs taught us the value of modular design and clear communication between APIs. We also discovered how critical it is to balance technical complexity with user experience, ensuring that the shifting storyline remains both immersive and coherent. What's next for Fable 🚀 We’re excited to broaden Fable’s capabilities by refining our EEG interpretation for an even wider range of emotions and deeper engagement tracking, exploring additional wearable sensors beyond the Muse headset, and advancing our storytelling techniques—potentially introducing multiple branching storylines, co-op experiences, and VR integration. <div