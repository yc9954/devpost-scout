---
slug: "speaksmartengineer"
url: "https://devpost.com/software/speaksmartengineer"
title: "SpeakSmartEngineer"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 625
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/legal_justice"
  - "user/developer"
  - "substrate/transcript_audio"
---

# SpeakSmartEngineer

> SpeakSmart is AI communication coach powered by that helps engineers translate tech jargon into business impact — with real-time voice coaching, 7-dimension analysis, and actionable feedback.

[Devpost](https://devpost.com/software/speaksmartengineer) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[realtime_stream]] [[voice_speech]]
**domain** [[legal_justice]]
**user** [[developer]]
**substrate** [[transcript_audio]]

**stack** amazon-amplify, amazon-nova, amazon-sonic, livekit, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for speaksmartengineer

## Body

Inspiration As engineers, we've all been in that meeting where an executive says, "Can you explain that in English?" or "But what does this mean for the business?" Research shows 56% of project failures stem from miscommunication — not bad code, not wrong architecture, but the inability to translate technical decisions into language stakeholders understand. We built SpeakSmart because we wanted the communication coach we wish we'd had: one that's available 24/7, gives honest feedback, and actually helps you practice before the high-stakes meeting. What it does SpeakSmart is a multi-agent Voice AI platform that coaches technical professionals on communicating complex ideas to non-technical audiences. Users select a scenario (like explaining architecture to executives or pitching a tech decision), deliver their explanation via voice, and receive a comprehensive 7-dimension evaluation covering jargon clarity, business impact framing, storytelling, structure, the "so what" factor, opening hook strength, and confidence. Coach Maya, our voice AI agent, engages in real-time coaching conversation, while the system detects jargon and suggests plain-language alternatives, counts filler words, and delivers personalized improvement plans with rewritten examples. How we built it We designed a multi-agent architecture on AWS Bedrock. Amazon Nova Sonic powers Coach Maya for natural, bidirectional voice coaching conversations. Amazon Nova Lite handles the intelligent 7-dimension speech analysis, generating structured JSON scoring and synthesizing actionable feedback. The frontend is built with React and LiveKit Client for real-time audio streaming, while the backend runs on Python with LiveKit Agents. AWS Transcribe handles live transcription, and we bridged Nova Sonic through Amazon Polly for voice synthesis. The entire system orchestrates through AWS Bedrock for scalable model inference. Challenges we ran into Integrating real-time bidirectional voice streaming with Nova Sonic while keeping latency low enough for natural conversation was our biggest hurdle. We also struggled with getting Nova Lite to return consistently structured JSON for the 7-dimension scoring — prompt engineering for reliable structured output took significant iteration. Coordinating three AI agents (Coach Maya, the Evaluator, and the Feedback Synthesizer) without creating race conditions or conflicting feedback was another challenge. Finally, calibrating the scoring rubric so it felt fair and actionable rather than arbitrary required extensive testing with real speech samples. Accomplishments that we're proud of We're proud of building a fully functional multi-agent voice AI system in a hackathon timeframe. The 7-dimension evaluation framework is something we genuinely believe captures what makes technical communication effective or ineffective. The jargon detection with real-time plain-language alternatives is surprisingly useful — it doesn't just flag problems, it teaches you how to fix them. Most importantly, Coach Maya feels like talking to a real mentor, not a chatbot reading a script, thanks to Nova Sonic's natural conversation capabilities. What we learned We learned how powerful Amazon Nova's model family is when used together as specialized agents rather than asking one model to do everything. Nova Sonic's voice capabilities are remarkably natural for coaching scenarios. We also gained a deeper appreciation for prompt engineering at scale — getting three agents to produce complementary, non-redundant feedback required careful system prompt design. On the product side, we learned that communication coaching is deeply personal — the same score can feel motivating or discouraging depending on how feedback is framed. What's next for SpeakSmartEngineer We plan to add progress tracking so users can see improvement over time across all 7 dimensions. We want to introduce industry-specific scenario packs (healthcare, finance, legal) and support multi-language coaching. A peer comparison mode would let teams benchmark their communication clarity together. We're also exploring integration with meeting platforms like Zoom and Teams for real-time, in-meeting coaching nudges. Longer term, we want to build a library of "golden examples" from top-scoring explanations that others can learn from — turning SpeakSmart into a community-driven communication learning platform. <div