---
slug: "mock-mentor"
url: "https://devpost.com/software/mock-mentor"
title: "Mock Mentor"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 822
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Mock Mentor

> Practice interviews with AI mentors anytime, anywhere - tailored to your resume and dream job.

[Devpost](https://devpost.com/software/mock-mentor) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[labor_employment]] [[mental_health]]
**user** [[government_staff]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** gemini, googlegemini, heygen, mongodb, next, node.js, react

## How they structured the write-up

- 💡 what inspired this project
- 🚀 how i built it
- 🧠 what i learned
- 🚧 challenges faced & solutions
- 🎯 key features implemented
- 🔮 what's next
- 🏆 impact & reflection

## Body

GIF Website Gif About MockMentor 💡 What Inspired This Project The inspiration for MockMentor came from a personal pain point I've experienced throughout my career journey. As someone who's been through countless interviews, I noticed that the biggest barrier to interview success isn't knowledge—it's confidence . Traditional mock interviews require scheduling with friends or mentors, generic practice questions don't reflect your unique background, and many people (myself included) felt awkward practicing with other humans. I wanted to create a solution that would: Be available 24/7 without scheduling conflicts Provide personalized questions based on your actual resume Feel realistic enough to build genuine confidence Remove the social anxiety of practicing with real people When I discovered HeyGen's streaming avatar technology, I realized I could create something truly revolutionary— AI mentors that look and feel like real interviewers . 🚀 How I Built It Tech Stack & Architecture Frontend : Next.js 15 + React 19 + TypeScript + Tailwind CSS AI/ML : Google AI SDK, OpenAI GPT, HeyGen Streaming Avatar API Voice : ElevenLabs voice models + Deepgram speech-to-text Backend : Next.js API routes + MongoDB + Mongoose Auth : Clerk for seamless user management Development Process Phase 1: Core Infrastructure (Day 1) // Set up the streaming avatar session management const { initAvatar, startAvatar, sessionState, stream } = useStreamingAvatarSession(); // Configure real-time voice chat const config: StartAvatarRequest = { quality: AvatarQuality.High, voiceChatTransport: VoiceChatTransport.WEBSOCKET, sttSettings: { provider: STTProvider.DEEPGRAM } }; Phase 2: AI Integration (Day 2) Implemented resume parsing and analysis using Google AI Built job description processing for tailored questions Created intelligent conversation flows that adapt to user responses Phase 3: User Experience (Day 3) Designed responsive UI with real-time video streaming Added timer functionality for focused 3-minute sessions Implemented mentor selection with 6 different AI personalities 🧠 What I Learned Technical Insights Real-time Streaming : Managing WebSocket connections while maintaining smooth video performance requires careful state management and error handling. AI Orchestration : Combining multiple AI services (GPT for conversation, ElevenLabs for voice, Deepgram for STT) taught me about API latency optimization and fallback strategies. Context Management : Building AI that remembers both resume details AND job requirements while maintaining natural conversation flow was more complex than expected. Product Insights User Experience : The difference between "technically working" and "feels natural" is enormous—small details like avatar lip-sync and voice emotion make huge impact. Performance Matters : Users expect instant responses in conversational AI. Every 100ms delay breaks immersion. Progressive Enhancement : Starting with core functionality (text chat) then adding voice made development more manageable. 🚧 Challenges Faced & Solutions Challenge 1: Streaming Performance Problem : Video streaming would lag when processing voice input simultaneously. Solution : Implemented efficient state management and optimized WebSocket connections: // Optimized avatar event handling avatar.on(StreamingEvents.AVATAR_START_TALKING, (e) => { console.log('Avatar started talking', e); }); avatar.on(StreamingEvents.STREAM_READY, (event) => { setLoading(false); setStartTime(new Date()); }); Challenge 2: Context-Aware AI Conversations Problem : Making the AI understand both resume content AND job requirements while maintaining natural flow. Solution : Developed a sophisticated prompt engineering system that: Analyzes resume for key skills and experience Extracts job requirements and responsibilities Generates contextual questions that bridge both Maintains conversation memory throughout the session Challenge 3: Natural Voice Interactions Problem : Achieving realistic back-and-forth conversation without awkward pauses or overlaps. Solution : Integrated multiple services with careful timing: Deepgram : Real-time speech-to-text with low latency ElevenLabs : Natural voice synthesis with emotion Custom logic : Interrupt handling and turn-taking management Challenge 4: Mobile Responsiveness Problem : Streaming video and voice chat on mobile devices with varying network conditions. Solution : Implemented adaptive quality settings Added fallback options for slower connections Optimized UI for touch interactions and smaller screens 🎯 Key Features Implemented 6 AI Mentor Personalities : Each with unique conversation styles Smart Resume Analysis : AI extracts and understands your background Job-Tailored Questions : Custom interviews based on job descriptions Real-time Voice Chat : Natural conversations with interrupt handling Timed Sessions : Focused 3-minute practice rounds Cross-platform : Works seamlessly on desktop and mobile 🔮 What's Next The hackathon version proved the concept works beautifully. Next steps include: Performance Analytics : Detailed feedback on speaking pace, filler words, confidence Industry Specialization : Tailored interview modules for tech, finance, healthcare, etc. Team Interviews : Multi-person interview simulations Integration : Connect with job boards for real-time practice opportunities 🏆 Impact & Reflection Building MockMentor in 3 days taught me that the best products solve real problems you've experienced yourself . The combination of cutting-edge AI technology with genuine user need created something that feels magical to use. The most rewarding moment was testing the first complete interview session—having a natural conversation with an AI mentor about my actual experience felt surreal and genuinely helpful for building confidence. This project showcases how modern AI tools can create entirely new categories of solutions that weren't possible just a year ago. We're living in an incredible time for builders. <div