---
slug: "rinky-dink-sigma"
url: "https://devpost.com/software/rinky-dink-sigma"
title: "Pala"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 770
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# Pala

> Transforming the pickleball coaching space.

[Devpost](https://devpost.com/software/rinky-dink-sigma) · hackathon [[NexHacks]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]] [[legal_justice]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** elevenlabs, framermotion, gemini, next.js, node.js, overshoot, python, react, tailwind, tensorflow, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pala
- links

## Body

Inspiration Our inspiration stems from a deeply personal understanding of the barriers athletes face in their development journey. We've both experienced the frustration of hitting plateaus without access to quality coaching, watching progress stagnate because private lessons are financially out of reach, or because the overwhelming noise of contradictory YouTube tutorials leaves you more confused than coached. We wanted to democratize high-quality sports coaching and create a tool that provides personalized, actionable feedback to anyone with a smartphone and a passion to improve. Pala represents our commitment to breaking down the financial and accessibility barriers that prevent millions of pickleball players from reaching their full potential. What it does Pala is an AI-driven virtual coaching platform that transforms how pickleball players train and improve. By leveraging cutting-edge computer vision and artificial intelligence, Pala analyzes uploaded game footage to deliver comprehensive performance insights that rival professional coaching. The platform identifies strengths and weaknesses in your gameplay, provides detailed shot-by-shot breakdowns, and offers personalized recommendations for improvement. With integrated voice narration powered by ElevenLabs, players receive their analysis in an engaging, conversational format, while the interactive AI chat feature powered by Google Gemini allows users to ask follow-up questions and receive tailored advice. Whether you're a beginner learning the fundamentals or an advanced player fine-tuning technique, Pala provides the personalized guidance you need to elevate your game. How we built it We built Pala on Next.js 16.1.3 with React 19.2.3 and TypeScript 5 for a robust foundation. The Overshoot SDK (v0.1.0-alpha.2) powers our core video analysis with sophisticated AI vision that comprehends shot techniques, court positioning, and strategic decision-making, not just detecting objects but understanding gameplay context. We crafted detailed prompts guiding Overshoot to analyze pickleball-specific metrics like serve quality, footwork patterns, and reaction times. TensorFlow.js (v4.22.0) with COCO-SSD provides real-time player tracking overlays, while ElevenLabs API delivers natural voice narration and Google Gemini API enables interactive coaching conversations. Zustand (v5.0.10) manages our global state elegantly, handling complex data flow between upload, processing, and playback, with Tailwind CSS 4, Framer Motion, and react-dropzone rounding out our polished UX. Challenges we ran into Building Pala in 24 hours tested us significantly, GitHub version conflicts threatened our progress until we implemented strict branching strategies, and integrating the Overshoot SDK presented our biggest technical hurdle as we refined prompts and error handling to ensure reliable, actionable feedback rather than generic responses. Frontend development demanded balancing professional polish with simplicity, laptop crashes struck during critical deployments, and random project breaks from dependency updates and CORS issues required constant creative problem-solving. Finding project alignment early was crucial, once we landed on Pala, our shared passion for democratizing sports coaching sustained us through every frustration and late-night debugging session. Accomplishments that we're proud of We're immensely proud of building an application we genuinely want to use—Pala isn't just a hackathon project, it's a tool that can make a real difference for millions of pickleball players worldwide. Successfully integrating Overshoot's powerful AI vision capabilities into a production-ready application stands as a major technical achievement, with the quality of insights validating our architecture and prompt engineering efforts. The seamless user experience from video upload through interactive analysis with synchronized annotations and voice narration demonstrates our attention to detail, while our technical resilience in debugging complex integrations and building robust state management with Zustand strengthened both our codebase and skills. Most importantly, we've built a platform that embodies our values of accessibility and quality—proof that technology, when utilized thoughtfully, can break down barriers and empower anyone to pursue excellence, answering "I can't afford that" with a solution that makes world-class coaching accessible to all. What we learned This hackathon taught us Zustand's elegant state management for clean data flow, real-time SDK integration orchestrating Overshoot and ElevenLabs into cohesive experiences, and how AI's transformative power requires thoughtful prompt crafting and UX design. We learned frontend principles through iteration, the value of collaboration under pressure, and that perseverance—breaking insurmountable problems into manageable pieces—defines successful projects. The connections we forged and technical skills we gained will carry forward into everything we build. What's next for Pala Immediate next steps include injury prevention with MediaPipe Pose to identify harmful movement patterns and provide corrective exercises, multi-sport expansion to tennis and badminton, progressive training programs with structured skill assessments, social features for community building, and wearable integration for biometric data. Our mission remains democratizing world-class coaching—proving you don't need unlimited resources to achieve excellence. Every player deserves quality coaching regardless of financial situation or location, and Pala amplifies expert guidance to millions who previously had no path to improvement. Links Live site | Pitch deck <div