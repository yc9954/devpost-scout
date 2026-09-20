---
slug: "swarm-ai-s6lhd0"
url: "https://devpost.com/software/swarm-ai-s6lhd0"
title: "Swarm AI"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1107
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Swarm AI

> Swarm AI empowers AI companies to test thousands of speech-to-speech conversations in parallel, measuring latency, coherence, memory, & engagement. We turn weeks of QA & model evaluation into minutes.

[Devpost](https://devpost.com/software/swarm-ai-s6lhd0) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[transcript_audio]]

**stack** fastapi, javascript, next.js, openai, python, render, supabase, vercel

## How they structured the write-up

- inspiration
- how it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for swarm ai
- funny moment

## Body

When your deployment fails... When your deployment works... Inspiration Picture this: there we were, running our AI restaurant waiter, feeling confident about our automated system taking phone orders. But then came the testing phase, and reality quickly set in. Our only option was to manually call our AI repeatedly to validate each conversation flow – a process that’s extremely bottlenecked by a major limiting factor. Not exactly scalable when you're trying to ensure your AI can handle a million different things, ranging from simple reservations to complex menu customizations. We quickly realized we weren't alone in this challenge. From customer service to healthcare, everyone adopting voice AI was facing the same bottleneck. These AI agents needed to be thoroughly tested before deployment, but the testing tools hadn't caught up with the technology. In an age of automation, we were still relying on manual testing processes. And that didn’t sit well with us. That's when the idea for Swarm AI clicked: what if we could just create a platform that could spawn thousands of virtual callers, each with their own characteristics, accents, and conversation patterns? Just as load testing transformed web development from guesswork into a science, we believed voice AI testing needed its own revolution. By enabling developers to uncover edge cases and identify potential issues before they reach real customers, we could help ensure more reliable AI interactions across every industry. How it works At the core of Swarm AI is a system designed to run thousands of test calls at once. Users start by accessing our dashboard, where they can create and configure testing jobs through an intuitive interface. The dashboard lets them specify exactly how they want their test agents to behave – from setting specific conversation flows to selecting different accents, latency/network conditions, background noise, etc. for thorough testing coverage. Our backend, built with FastAPI, manages these testing requests through a smart batching system. Instead of starting all calls at once, we spread them out to keep everything running smoothly. Each batch runs independently, letting us handle many calls while keeping the system stable. For each call, we first save it to our database and then connect through Twilio. Once connected, calls flow through our real-time processing system. We use WebSockets to handle two-way audio, letting our AI agents listen and talk naturally. The audio is processed instantly using OpenAI for transcription, while our AI engine creates responses based on the test settings. The dashboard provides real-time visibility into ongoing tests through a live analytics panel. As calls progress, users can see key metrics updating in real-time – success rates, average call duration, and completion status for each test agent. The analytics interface pulls directly from our database, showing both aggregate statistics and detailed breakdowns of individual call performance. Our AI agents follow test settings that control their behavior, including accent, talking speed, and tone. These settings are loaded when each call starts, letting us test many different scenarios to find potential issues in the target voice AI system. Users can also access a detailed transcript view for any completed call, allowing them to analyze specific interactions or troubleshoot issues that arose during testing. After test completion, our platform generates comprehensive reports that highlight patterns, anomalies, and potential improvements for the voice AI system being tested. This data-driven approach helps users quickly identify and fix issues before they impact real customers. Challenges we ran into Our biggest technical hurdles centered around real-time communication and scalability. The WebSocket connection, important for maintaining live conversations between AI agents, proved particularly tricky – every disconnection meant a failed test and lost data. We overcame this by implementing robust connection handling and retry mechanisms. Call management also presented unique challenges. What seemed straightforward – ending a call – became complex when dealing with thousands of concurrent conversations. We had to carefully orchestrate call termination to ensure clean exits and proper resource cleanup. Our batching system underwent several iterations before we found the right balance between system load and testing throughput. One of our most interesting challenges was running simultaneous speech-to-text and speech-to-speech processing. This required careful stream management and precise timing to prevent feedback loops or processing delays. Figuring out how to transfer speech-based audio chunks efficiently and quickly proved was a major obstacle as well. After numerous debugging sessions and architecture revisions, we developed a stable solution that could handle both streams efficiently. Finally, our database architecture evolved significantly throughout development as we better understood our data needs. What started as a simple call logging system grew into a complex but efficient structure handling test configurations, real-time analytics, and detailed conversation transcripts. Accomplishments that we're proud of The both of us poured our expertise into crafting a robust testing platform that exceeded our initial vision. The clean, beautiful interface we designed masks the complex orchestration happening behind the scenes – something we take pride in. We're especially proud of our system's reliability. Through persistent debugging and optimization, we created a platform that can handle many concurrent test calls while maintaining stable performance. But beyond the technical achievements, what stands out is how well we worked together. The both of us brought our strengths to the table and stepped up when needed, allowing us to build something substantial in such a short timeframe. What We Learned It’s incredibly difficult to just pick a few, but here are our major takeaways. First and foremost, a well-designed system architecture will always outperform spontaneous solutions (no matter how quickly we think we can move). We also dove deep into how computers listen to and process phone audio, and we explored various approaches to optimize real-time communication. Additionally, mastering WebSockets and WebRTC allowed us to handle two-way audio in a hyper-efficient manner, ensuring smooth interactions even at scale. Along the way, we gained a solid understanding of parallel computing and batch processing, applying principles from our systems classes to balance performance and compute resources effectively. We also learned the importance of having great company (and food + boba) when building. What's next for Swarm AI While we initially set out to build a voice AI for restaurant ordering, developing this testing platform opened our eyes to a much bigger opportunity in the voice AI ecosystem. We're now pivoting our startup to focus on Swarm AI as a comprehensive testing platform for voice AI developers, with plans to expand our testing capabilities and add features like custom scenario builders, advanced analytics, and integration with popular voice AI development frameworks. Funny Moment Watching the AI agents making Dad jokes with one another (“What type of nut goes to space?” Answer: “An Astro-Nut”) <div