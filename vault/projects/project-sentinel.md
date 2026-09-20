---
slug: "project-sentinel"
url: "https://devpost.com/software/project-sentinel"
title: "Project Sentinel"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 811
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/security_privacy"
---

# Project Sentinel

> Your real-time AI shield against voice fraud. Sentinel analyzes live calls to detect vishing and social engineering instantly, warning vulnerable users before they fall victim to scams.

[Devpost](https://devpost.com/software/project-sentinel) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: retrieval_grounding, simulation_digital_twin</sub>
**domain** [[finance_payments]] [[security_privacy]]
  <sub>weak: elder_child_care, retail_commerce</sub>
  <sub>weak: geospatial, transcript_audio</sub>

**stack** bash, cerebras, chatgpt, cloud, cobe, css, deepgram, docker, elevenlabs, fastapi, framer-motion, gemini, hooks, kubernetes

## Body

Raindrop Utilization Project Sentinel 🛡️ Silence the Deception. "Most security apps are shields. Sentinel is a sword." 💡 The Inspiration In 2024, voice fraud and "vishing" (voice phishing) cost victims over $10 billion. But the victims aren't just statistics—they are our grandparents, our parents, and the vulnerable. Scammers have evolved. They use AI to clone voices, automate attacks, and target millions. Yet, our defenses are stuck in the past; we just "hang up." But hanging up doesn't stop them—it just moves them to the next victim on the list. We asked a radical question: What if we could turn the tables? What if, instead of just blocking the call, we could intercept it, waste the scammer's time, and gather forensic evidence automatically? 🤖 What It Does Project Sentinel is the world's first AI-Native Active Defense Grid for voice calls. It protects users in real-time and counter-attacks when threatened. The Silent Guardian (Real-Time Monitoring) Sentinel listens to live audio using Deepgram Nova-2. As the conversation flows, it visualizes the call on a cinematic 3D globe. Simultaneously, Cerebras Inference analyzes the semantic patterns for indicators of fraud (urgency, gift card requests, financial coercion) with sub-second latency. The Intercept ("Ghost Protocol") 👻 When a threat is detected, the user can engage Ghost Protocol. This disconnects the user's microphone and hot-swaps them with an AI Agent. The user can now sit back and listen as the AI takes over the call. Active Counter-Measures (The "Troll" Mode) The Ghost Agent—powered by ElevenLabs—adopts a persona (e.g., a confused elderly person or a distracted executive). It utilizes Raindrop SmartBuckets to retrieve known "counter-scripts" and stall tactics, keeping the scammer on the line to waste their time and resources. The Evidence Locker Every interaction is logged. Using Raindrop, we store the transcript, the threat analysis, and the audio as an immutable "Police Report" that can be used by law enforcement. ⚙️ How We Built It (The Stack) We engineered Sentinel for the "Speed of Voice." If the AI lags by even 500ms, the illusion is broken. This required a best-in-class stack: 🧠 The Brain: LiquidMetal Raindrop & Cerebras LiquidMetal Raindrop (The Backbone): We built the entire backend orchestration on the Raindrop Platform. SmartBuckets: We use sentinel-evidence-sb to securely store sensitive voice logs and agent-memory-sb as a vector store for our "Known Scam Scripts." SmartInference: Raindrop handles the logic routing between our frontend and the AI models. Cerebras (The Speed): We utilized Llama 3.3-70b via Cerebras Inference. Standard LLMs were too slow for a fluid conversation. Cerebras allowed us to perform complex semantic analysis on every sentence with near-zero latency, enabling the Ghost Agent to "think" as fast as a human. ⚡ The Muscle: Vultr Cloud Compute To handle full-duplex audio streaming without jitter, we deployed our backend on Vultr High-Frequency Compute. The raw processing power of Vultr ensures that our WebSocket connections (handling audio streams) remain stable even when processing heavy AI workloads. 🗣️ The Voice: ElevenLabs We integrated ElevenLabs Turbo v2.5 for the Ghost Agent. Why it matters: The AI needs to sound convincing. We tuned the model to include hesitations ("uhm," "ah," "let me find my glasses") to fool human scammers into thinking they are talking to a real victim. 🔐 The Gatekeeper: WorkOS & Cloudflare WorkOS AuthKit: We implemented enterprise-grade SSO and user management to ensure that personal call data is locked down. Cloudflare: protecting our edge and ensuring global availability. 💰 The Economy: Stripe We built a custom Stripe Embedded Checkout. Users can upgrade to "Sentinel One" (Premium) to unlock the Ghost Protocol features, demonstrating immediate business viability. 🚧 Challenges We Ran Into The "Human" Latency: Paradoxically, the Cerebras inference was too fast. The AI would reply instantly, which sounded robotic. We had to program artificial "thinking noises" and delays to make the Ghost Agent sound like a confused human. State Management: Handling the hot-swap between a live microphone stream (User) and an AI-generated audio stream (Ghost Agent) required a complex WebSocket dance between the browser, Vultr, and Deepgram. 🏆 Accomplishments We're Proud Of The "Troll" Success: Watching our Ghost Agent successfully keep a simulated scammer on the line for 2 minutes was a massive win. Raindrop Integration: Successfully implementing the Raindrop MCP Server to manage our entire data flow was a breakthrough in simplifying our backend architecture. Production Ready: This isn't just a prototype. With WorkOS for auth and Stripe for payments, Sentinel is ready to ship. 🔮 What's Next for Sentinel Telephony Integration: Porting the web-audio logic to a native mobile dialer to intercept actual cellular calls. Crowd-Sourced Intelligence: Using Raindrop to share anonymized scam scripts across the Sentinel network, inoculating all users against new threats instantly. Enterprise API: We are opening the Sentinel API for banks to integrate our threat detection directly into their support lines. Built with: ❤️, LiquidMetal Raindrop, Cerebras, Vultr, ElevenLabs, WorkOS, Stripe, Deepgram, Cloudflare, Gemini & React. <div