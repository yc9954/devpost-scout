---
slug: "stemvue"
url: "https://devpost.com/software/stemvue"
title: "StemVue"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 663
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/video_visual"
---

# StemVue

> Generate fully narrated, beautifully animated STEM video solutions in under 2 minutes

[Devpost](https://devpost.com/software/stemvue) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** celery, docker, fastapi, next.js, redis, supabase

## How they structured the write-up

- what it does 🚀
- inspiration 💡
- how we built it 🛠️
- challenges we ran into 🛑
- accomplishments that we're proud of ✨
- what's next for stemvue 🗺️

## Body

What it does 🚀 StemVue is a platform that transforms static STEM problems into fully narrated, mathematically precise animated video solutions in under 2 minutes! ⏱️ Users can upload an image of a handwritten homework problem or type out a physics/math query. StemVue’s AI pipeline processes the multimodal input, reasons through the solution, and generates custom Python code. It then renders the animation seamlessly and layers on a synchronized AI voiceover. 🗣️🎬 Inspiration 💡 STEM subjects are inherently visual, while AI has made text-based tutoring highly accessible, yet high-quality visual education remains a massive bottleneck. Generating educational videos via traditional AI diffusion models is painfully slow, cost-prohibitive, and often inaccurate while the manual solutions require teams of teachers, scriptwriters, graphic artists, and video editors which is costly and time-consuming. I wanted to bridge this gap by treating video generation not as a pixel-rendering problem, but as a code-generation problem. Inspired by 3Blue1Brown’s visually intuitive videos, the result is a platform that makes high-quality, mathematically precise visual tutoring instant and accessible for students everywhere by making it cost-effective and fast for scale. 📐✨ How we built it 🛠️ The core architecture is built around highly constrained LLM orchestration and asynchronous task management to handle CPU-heavy rendering. The AI Orchestration 🧠: The pipeline was originally architected and optimized around Gemma 4, proving that a sub-26B parameter model could handle complex Manim code orchestration, drastically reducing the inference costs typically associated with frontier models. We aggressively constrained the prompt engineering to keep total token consumption under 4k tokens per request. (Note: To ensure maximum speed and concurrency for the live hackathon demo, the deployed version is currently utilizing Gemini Flash). The Rendering Engine 🎬: Instead of generating raw video, the LLM outputs executable Manim (Python) scripts. This guarantees perfect mathematical accuracy in the animations and completely bypasses the hallucinations common in traditional AI video generators. The Scalable Backend ⚙️: Rendering video is computationally expensive. To prevent server timeouts, we implemented a Celery + Redis task queue for asynchronous job processing. This architecture isolates video generation per user IP and allows the system to scale horizontally under concurrent load. Challenges we ran into 🛑 Code Syntax Hallucinations 🧩: LLMs are powerful but frequently hallucinate outdated or deprecated Manim syntax. We had to build strict few-shot prompt templates and robust output parsers to ensure the generated code would actually compile. Token Optimization 🪙: Passing entire documentation contexts to the LLM was too slow and expensive. Refining our retrieval and system prompts to consistently execute under the strict 4k token limit required significant engineering and iteration. Concurrency Bottlenecks ⚡: Managing simultaneous video renders on the backend initially caused massive slowdowns. Implementing Celery and Redis was a steep learning curve, but absolutely necessary to unblock the main thread and provide users with a stable, queue-based experience. Accomplishments that we're proud of ✨ Sub-2-Minute Rendering ⏱️: Taking a raw image of a physics problem and outputting a completely custom, narrated, programmatic animation in under 120 seconds is a massive leap in educational accessibility from traditional manual production processes. Cost-Efficient Architecture 🪙: Proving that this pipeline can run effectively on smaller, sub-26B models (like Gemma 4) proves that this tool can be scaled and democratized globally without burning through massive API budgets. What's next for StemVue 🗺️ B2B Scaling for EdTech Enterprises 🏢: Currently, major EdTech companies spend millions of dollars maintaining massive content production pipelines—employing whole teams of teachers, scriptwriters, graphic artists, and video editors just to publish homework video solutions online. We plan to scale StemVue into an enterprise-grade SaaS API, allowing EdTech platforms to automate their entire textbook solution pipeline instantly, cutting production costs by 90%. Hyper-Multilingual Expansion 🌍: While our "Hinglish" mode is a proof of concept for localized learning, the next step is deploying a fully modular audio pipeline. We will add seamless support for over a dozen regional and global languages (including Hindi, Spanish, Mandarin, and Tamil) to ensure true educational equity across different demographics. <div