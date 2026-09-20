---
slug: "civilink"
url: "https://devpost.com/software/civilink"
title: "Tailored Labs"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 350
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Tailored Labs

> AI-powered video timeline editor that lets creators build professional edits through natural language commands, perfectly analyze raw video, and outputs end to end "one-shot" video generation.

[Devpost](https://devpost.com/software/civilink) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

  <sub>weak: structured_db</sub>

**stack** amazon-web-services, bolt.new, lamda, react, service, stripe, supabase, tailwind, typescript

## Body

## Inspiration 🎬✨ Building Bolt.new for Video Editing Manually editing your professional video takes HOURS of sifting through edits and raw video! Then you have to clip it, then you have to arrange it, then you have to ..... you get it. That's when it hit me: What if you could just TALK to your video editor? What if editing was as simple as saying "Hey, make this clip 5 seconds shorter" or "Add some text that says 'Hello World' for 3 seconds" ? What if I could have AI Edit my entire video from start to finish!? Tailored Labs was born from this "aha!" moment—combining the power of professional video editing with the simplicity of having a conversation. ## What it does 🚀 💳 One-Shot Generation – Generate a finished video from raw clips by utilizing AI 🗣️ Chat-to-Edit Magic – Type commands like "remove the second clip" or "add a fade transition" and watch your timeline update instantly 📚 Smart Media Library – Upload, organize, and AI-powered search through your video assets, which includes clipping to the correct time, and removing bad takes, not just text based 🎛️ Professional Timeline Interface – Full-featured drag-and-drop timeline with tracks, transitions, and precise editing controls ☁️ Cloud Rendering via Remotion – Generate high-quality videos without melting your laptop ## How we built it 🛠️ The Stack That Dreams Are Made Of: 🔮 Next.js 15 – Our rock-solid foundation with the latest server actions 🤖 OpenAI GPT-4/Claude Opus – The brain that understands "make it snappier" means "reduce duration" 🎥 Remotion – Turns our timeline data into gorgeous, rendered videos 🗄️ Supabase – Database, auth, and file storage that just works 💰 Stripe – Because even AI assistants need to eat (electricity) 🎨 Tailwind – Making it look slick without the CSS tears AWS Lamda – Agentic Flows for analyizing clips and generating final video The Magic Sauce: // When you say "create witty video", this happens: const completion = await video_generator.create({ edl: {}, // Our ai generated script to align with videos vidoes: [{ analysis: 'analysis', metadata: {} }] });``` <div