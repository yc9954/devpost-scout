---
slug: "wisespirit-trolleyops"
url: "https://devpost.com/software/wisespirit-trolleyops"
title: "WiseSpirit & TrolleyOps"
hackathon: "HackMty 2025"
organization: "TEC ACM"
winner: true
words: 449
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# WiseSpirit & TrolleyOps

> WiseSpirit & TrolleyOps: AI solutions powered by Google Gemini and ElevenLabs that bring accuracy, automation, and accessibility to airline catering—error-free, hands-free, for everyone.

[Devpost](https://devpost.com/software/wisespirit-trolleyops) · hackathon [[HackMty 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**substrate** [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** elevenlabs, gemini, next.js, node.js, postgresql, prisma, react, typescript, websockets

## How they structured the write-up

- wisespirit & trolleyops
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for wisespirit & trolleyops

## Body

WiseSpirit & TrolleyOps Inspiration Our team was inspired by the desire to push our technical limits during this hackathon and to create something meaningful for GateGroup, a company that powers millions of in-flight experiences. After analyzing their operations, we noticed a recurring pattern: manual processes, low visibility, and high error rates. We set out to tackle these problems by building two complementary AI-powered solutions — WiseSpirit and TrolleyOps — both designed to improve airline efficiency and accessibility. What It Does WiseSpirit enhances accessibility and safety in alcohol bottle handling. It uses the Google Gemini API to interpret airline-specific regulations and reason through decisions. Then, using ElevenLabs’ text-to-speech , it communicates clear, natural-sounding voice instructions to the crew — allowing them to work hands-free , even in low-light or high-pressure scenarios. TrolleyOps redefines airline catering through AI computer vision . By simply pointing a camera at products, our AI can identify over 20 items in under 2 seconds — no barcodes required. It also tracks what goes onboard and what comes back, automatically generating real-time sales analytics. Together, these tools eliminate human error, boost efficiency, and ensure traceability across the entire catering process. How We Built It We developed a full-stack system integrating: Frontend: React + TypeScript Backend: Node.js + Express Database: PostgreSQL AI Layer: Google Gemini Robotics-ER 1.5 for product detection and decision logic Voice Layer: ElevenLabs API for realistic speech feedback Real-Time Updates: WebSocket communication between AI and UI Our stack is production-ready , with modular architecture for scalability and performance. Challenges We Ran Into We spent more time brainstorming and refining the concept than anticipated, which delayed the build phase. Integrating multiple APIs — especially aligning Gemini’s vision models with real product data — also required extensive testing. Finally, balancing AI accuracy with accessibility design pushed us to think creatively about UX and performance. Accomplishments We’re Proud Of Successfully integrated Google Gemini and ElevenLabs into functional, real-world prototypes. Built AI tools that directly address GateGroup’s operational challenges. Delivered two working systems — one focused on accessibility and another on automation — within the hackathon timeframe. Designed an interface that is inclusive, intuitive, and powered by real AI. What We Learned We learned the importance of structured planning, early validation, and cross-functional coordination. Most importantly, we realized that combining accessibility and AI creates technology that serves not just efficiency — but also people . What’s Next for WiseSpirit & TrolleyOps Our next steps include: Expanding product recognition to over 100 SKUs with higher accuracy. Adding multi-language voice feedback for international crews. With the right support, WiseSpirit & TrolleyOps can transform airline operations from error-prone to error-free , proving that accessibility and innovation can truly fly together . <div