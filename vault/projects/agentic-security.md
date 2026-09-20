---
slug: "agentic-security"
url: "https://devpost.com/software/agentic-security"
title: "Agentic Security"
hackathon: "SANS AI Cybersecurity Hackathon"
organization: "sans"
winner: true
words: 404
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/video_visual"
---

# Agentic Security

> Agentic LLM Vulnerability Scanner Aggregator / AI red teaming kit 🧪 Multimodal Attacks 🖼️Multi-Step Jailbreaks 🌀Comprehensive Fuzzing 🧪 RL-Based Attacks 📡

[Devpost](https://devpost.com/software/agentic-security) · hackathon [[SANS AI Cybersecurity Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- the future is bright:

## Body

Agentic LLM Vulnerability Scanner Aggregator 🧪 Inspiration I was deep into a project building a RAG system with AI agents for a user-facing app. Security was non-negotiable, but when I tested existing tools for jailbreaks, prompt injections, and adversarial attacks, they disappointed—too limited, too stiff, and missing the mark. Frustrated, I decided to create Agentic Security, a solution that does it right. What It Does Agentic Security is an open-source security suite that protects large language models (LLMs) by combining powerful testing methods into one tool: Probes vulnerabilities across text, images, and audio. Simulates multi-step jailbreaks mimicking real-world attacks. Stress-tests models with randomized, edge-case fuzzing. Uses reinforcement learning for adaptive, evolving attack probes. Provides smart reporting with early stopping and token optimization. It’s a one-stop shop for securing LLMs, no extra tools needed. How We Built It I started with a modular design, integrating multimodal attack frameworks, jailbreak simulators, and fuzzing engines. Reinforcement learning was layered in to make attacks smarter, while a reporting system was built for efficiency and clarity. The next leap—turning it into a Model Context Protocol Server—meant crafting an interface to hook into LLM chat UIs like ChatGPT, enabling real-time testing from a single command. Challenges We Ran Into Balancing comprehensive testing with performance was tricky—fuzzing and RL probes can get resource-heavy. Integrating multimodal attacks (text, images, audio) into a unified system took some trial and error. And making the server chat-compatible? That required rethinking how security tools talk to LLMs without breaking their flow. Accomplishments That We’re Proud Of Built a first-of-its-kind, all-in-one LLM security suite that’s open-source and accessible. Successfully turned complex attack methods into a simple, chat-driven interface. Delivered detailed vulnerability reports without wasting tokens or time. Created a tool that’s already flexible enough for personal projects and enterprise systems alike. What We Learned Security isn’t static—AI threats evolve, so our tools must too. Reinforcement learning can unlock attack patterns we’d never have scripted manually. And bridging security testing with chat interfaces isn’t just cool—it’s practical, making it easier for developers to stay proactive. What’s Next for Agentic Security The future is bright: Expand the Model Context Protocol Server for broader LLM compatibility. Add community-driven attack libraries to keep pace with emerging threats. Optimize for scale, so enterprise teams can deploy it effortlessly. Push the boundaries of real-time security—think live monitoring as AI runs. Agentic Security is just getting started. Let’s make AI safer, together. 🌍 <div