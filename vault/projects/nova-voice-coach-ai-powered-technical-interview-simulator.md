---
slug: "nova-voice-coach-ai-powered-technical-interview-simulator"
url: "https://devpost.com/software/nova-voice-coach-ai-powered-technical-interview-simulator"
title: "Nova Voice Coach: AI-Powered Technical Interview Simulator"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 919
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/mental_health"
  - "user/developer"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# Nova Voice Coach: AI-Powered Technical Interview Simulator

> Democratizing technical interview preparation through AI—realistic voice practice in 10 languages with objective, actionable feedback.

[Devpost](https://devpost.com/software/nova-voice-coach-ai-powered-technical-interview-simulator) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[mental_health]]
**user** [[developer]] [[educator_student]]
**substrate** [[transcript_audio]]

**stack** amazon-web-services, amplify, aws-sdk, bedrock, express.js, node.js, nova

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nova voice coach: ai-powered technical interview simulator

## Body

https://nova.awslearn.cloud/#/ Inspiration While mentoring junior engineers in Latin America, I witnessed a heartbreaking pattern: talented developers with strong technical skills were failing interviews—not because they lacked knowledge, but because they couldn't articulate it confidently, especially in English. One mentee told me: "I know the answer, but when I try to explain it in English during the interview, my mind goes blank." Traditional mock interviews cost are pretty expensive per session, require scheduling weeks in advance, and provide subjective feedback. When Amazon Nova 2 Sonic launched with speech-to-speech capabilities, I realized we could democratize technical interview preparation—making high-quality practice accessible to anyone, anywhere, in many language, 24/7. What it does Nova Voice Coach is a real-time AI-powered technical interview simulator that conducts realistic voice interviews and provides intelligent feedback: Core Features: 🗣️ Natural voice conversations using Amazon Nova 2 Sonic (speech-to-speech) 🎯 Personalized interviews adapted to your role (e.g., Senior Cloud Architect), tech stack (AWS, Kubernetes, Terraform), and preferred interviewer personality (Friendly, Professional, Strict) 🌍 Multi-language support: 10 languages with 20 voice options (male/female per language) 📊 Intelligent analysis using Amazon Nova 2 Lite to evaluate: Technical Accuracy (40%) : Correctness of answers Communication Clarity (30%) : Explanation quality Seniority Level (30%) : Depth of reasoning and strategic thinking 💡 Actionable feedback: Specific strengths, weaknesses, and study recommendations 🔒 Privacy-first: No data persistence, client-side processing, BYOK model The experience feels like talking to a real interviewer—with natural pauses, follow-up questions, and adaptive difficulty. How we built it Architecture Frontend (Vue 3 + Quasar) ↕️ Socket.IO Backend (Node.js + Express) ↕️ AWS SDK v3 Amazon Bedrock (Nova 2 Sonic + Nova 2 Lite) Tech Stack Frontend : Vue 3, TypeScript, Quasar Framework, Socket.IO Client, Web Audio API Backend : Node.js, Express, Socket.IO Server, AWS SDK v3 AI Models : Amazon Nova 2 Sonic (amazon.nova-2-sonic-v1:0), Amazon Nova 2 Lite (us.amazon.nova-2-lite-v1:0) Challenges we ran into 1. Audio Latency (3-5s delays) Problem: Initial implementation felt robotic and unnatural. Solution: Reduced buffer size from 8192 to 4096 samples Implemented audio scheduling with AudioContext.currentTime Used bidirectional streaming instead of request-response Result: Achieved <1.5s end-to-end latency ✅ 2. Silence Detection Problem: AI didn't know when user finished speaking, causing awkward pauses or interruptions. Solution: Implemented 2-second silence timeout with visual feedback (green rings pulse while speaking) Added manual "End Turn" button as fallback Result: 95% accuracy in detecting turn-taking ✅ 3. Audio Format Conversion Problem: Browser captures Float32 at 48kHz, Bedrock requires Int16 PCM at 16kHz. Solution: javascript // Downsample and convert function downsample(buffer, fromRate, toRate) { const ratio = fromRate / toRate; const newLength = Math.round(buffer.length / ratio); const result = new Float32Array(newLength); for (let i = 0; i < newLength; i++) { result[i] = buffer[Math.round(i * ratio)]; } return result; } function float32ToInt16(float32Array) { const int16Array = new Int16Array(float32Array.length); for (let i = 0; i < float32Array.length; i++) { const s = Math.max(-1, Math.min(1, float32Array[i])); int16Array[i] = s < 0 ? s * 0x8000 : s * 0x7FFF; } return int16Array; } 4. Prompt Engineering for Structured Output Problem: Nova 2 Lite returned markdown-wrapped JSON or inconsistent formats. Solution: Added explicit instruction: "Output ONLY valid JSON (no markdown)" Provided exact schema in prompt Implemented fallback regex parsing Result: 99% success rate in JSON parsing ✅ Accomplishments that we're proud of 1. Sub-1.5s Latency Achieved conversational-quality voice interaction that feels natural and human-like—a critical requirement for realistic interview simulation. 2. Multi-Language Accessibility Supporting 10 languages with native voices breaks down barriers for non-native English speakers worldwide. 3. Intelligent Feedback System Nova 2 Lite's analysis goes beyond generic advice—it provides specific, actionable recommendations based on role and tech stack. What we learned 1. Speech-to-Speech is a Game-Changer for Realistic User Experiences Before Nova 2 Sonic, creating natural voice interactions required chaining multiple services: Speech → Transcription (Transcribe) → LLM (Text) → Text-to-Speech (Polly) Result: ~5 seconds latency, robotic feel, lost emotional context Nova 2 Sonic's direct speech-to-speech capability eliminates this pipeline entirely: Speech → Nova 2 Sonic → Speech Result: <1.5 seconds latency, natural conversation, preserved tone Key insight: For use cases requiring realistic human interaction—like interview simulations, customer service training, language tutoring, or therapy bots—speech-to-speech is not just faster, it's fundamentally more authentic. Users don't feel like they're talking to a machine; they feel heard and understood. 2. AWS Nova Models are Exceptionally Fast and Versatile We were blown away by Nova's performance: Nova 2 Sonic : Consistent <1.5s response times even with complex technical prompts Nova 2 Lite : Analyzed 10-minute interview transcripts (~3,000 tokens) in under 2 seconds with structured JSON output Cost efficiency : ~$0.50 per 10-minute interview session (vs. $100-300 for human mock interviews) What's next for Nova Voice Coach: AI-Powered Technical Interview Simulator Phase 1: Enhanced Feedback Video analysis : Body language and eye contact evaluation Code editor integration : Live coding questions with syntax highlighting Multi-turn memory : AI remembers previous answers for follow-up questions Custom question banks : Upload company-specific questions Phase 2: Team Features Team dashboards : Engineering managers track team progress Collaborative learning : Share feedback and best practices Progress analytics : Track improvement over time with visualizations Role-based simulations : Practice specific interview types (system design, behavioral, coding) Phase 3: Advanced AI Features Multi-agent interviews : Simulate panel interviews with multiple AI interviewers (Strandsagents orquestrator) Emotional intelligence : Detect stress levels and provide calming techniques Whiteboard mode : Visual problem-solving with diagram recognition Real-time hints : Subtle guidance when user is stuck (training mode) Built with ❤️ using Amazon Nova 2 | #AmazonNova #VoiceAI #AIforGood <div