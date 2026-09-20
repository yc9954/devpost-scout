---
slug: "llmix"
url: "https://devpost.com/software/llmix"
title: "LLMIX"
hackathon: "AWS Presents: Breaking Barriers Virtual Challenge"
organization: "Amazon"
winner: true
words: 389
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LLMIX

> LLMIX puts AI in offline communities: a Pi-powered hotspot with chat, code, med & wiki models—totally local. Flash the image, boot, connect to its Wi-Fi, and let multiple users learn, solve, thrive.

[Devpost](https://devpost.com/software/llmix) · hackathon [[AWS Presents- Breaking Barriers Virtual Challenge]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: structural_withholding</sub>
**domain** [[education]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** faiss, javascript, llama.cpp, python, raspberry-pi, sagemaker, websockets

## How they structured the write-up

- inspiration
- what we built
- what we learned
- challenges we faced

## Body

LLMIX began with a simple, stubborn question: “What good is the AI revolution if half the planet can’t reach it?” According to the ITU, 2.6 billion people still live without reliable internet. Yet modern language models—packed with knowledge, creativity, and code—sit locked behind cloud APIs and broadband paywalls. We wanted to Break the Barriers and deliver real AI to classrooms, community clinics, and crisis zones that may never see a fiber-optic cable. So we built LLMIX : a fully-offline “LLM-in-a-box” that runs on a Raspberry Pi 5, spins up its own Wi-Fi hotspot, and serves four local chat modes—General, Medical, Coding, and Wikipedia-grounded RAG—to anyone nearby. Inspiration Kiwix and Internet-in-a-Box proved offline knowledge libraries matter. Rural teachers asked for coding tutorials that don’t need YouTube or ChatGPT. The Raspberry Pi community showed how far you can stretch 8 GB of RAM. We realized a single Pi could host lightweight language models and change how offline communities learn and solve problems. What We Built Layer Tech Highlights Inference llama.cpp Hot-swappable GGUF models: Granite-Chat, Medicanite , Qwen-Coder RAG FAISS + sentence-transformers 1-million-chunk Simple English Wikipedia index Backend FastAPI · WebSockets Live token streaming, multi-user queue Frontend Vanilla HTML/CSS/JS 30 kB total; mobile-first; no frameworks Edge Network hostapd · dnsmasq Pi boots as “LLMIX” hotspot Image Raspberry Pi OS One flash-and-go .img Medicanite —our fine-tuned medical model—scores 55.82 % avg on Open Medical-LLM Leaderboard benchmark, topping the < 3 B leaderboard. And yes, it chats fluently on a Pi. What We Learned Context is gold – even a 2 B model shines when you add local RAG. Streaming beats spinners – token drip keeps users engaged at Pi speeds. Licensing rabbit holes – combining GPL firmware, Apache code, and CC-BY data is an exercise in patience. Benchmarks motivate – watching Medicanite inch past JSL-MedPhi2 at 3 AM was the caffeine we needed. Challenges We Faced RAM budget – fitting model + FAISS + OS into 8 GB without swap thrashing. Wi-Fi isolation – juggling hostapd, dnsmasq, and NetworkManager in read-only image. Medical safety – making it clear Medicanite is educational , not diagnostic. Time – condensing gigabytes of models, graphics, and licences into a single downloadable image before submission. LLMIX brings AI to those who need it—anywhere, anytime. Flash the image, power the Pi, join the hotspot, and start the conversation. <div