---
slug: "brainsafe-browser"
url: "https://devpost.com/software/brainsafe-browser"
title: "BrainSafe"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 751
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
---

# BrainSafe

> AI-powered browser extension that protects infant brain development by detecting, modifying and filtering harmful digital content in real time across different video platforms like YouTube, etc.

[Devpost](https://devpost.com/software/brainsafe-browser) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
  <sub>weak: education</sub>

**stack** adk, django, gcp, gemini, javascript, multimodalaiagents, openai, promptengineering, python

## Body

1. News Articles 2. Research Findings 3. Current State 4. BrainSafe 5. Proposed Solution 6. Implementation 7. Architecture Diagram Inspiration One of us recently came across an Instagram video explaining how children’s content is deliberately engineered to capture attention and create dependency to the point where many kids cannot perform routine tasks, like eating meals, without being given a phone. This resonated with our own observations of younger children in our families, who often insist on screen time whenever food is involved. What initially felt like a small family struggle suddenly connected to a larger concern: if this pattern continues unchecked, it could have serious long-term effects on children’s development. Research shows that shows like CoComelon are scientifically designed using child testing to maximize “stickiness” rather than educational value , exposing developing brains to engineered addiction . Modern children’s content often relies on sensory overload with scene changes every 1–3 seconds, extreme color saturation, and rapid stimuli that exceed natural human processing capacity. This exposure is widespread: CoComelon alone generates 7.8 billion monthly YouTube views with 134 million subscribers , reaching millions of infants during critical stages of brain development. The effects are measurable, with studies linking high screen exposure to structural brain changes, altered EEG patterns, elevated stress hormones, and persistent executive function deficits that can last into school age. Despite this, there remains a regulatory gap . No existing technology automatically detects and moderates the visual characteristics (pace, contrast, content safety, etc.) that research has proven harmful. Motivated by both personal experience and this growing body of evidence, we built BrainSafe , a protective technology layer designed to safeguard the developing brains of infants and toddlers. What We Learned Neuroscience foundations : How screen exposure, especially today’s high-contrast, fast-paced content, shapes early cognitive development by altering brain wave patterns, attention mechanisms, and executive function. Applied multimodal AI : How multimodal AI can be leveraged to analyze multiple video features simultaneously (i.e., in parallel) to address a real-world social problem. AI orchestration with ADK : Practical challenges of deploying AI agents using the Google Agent Development Kit (ADK), including coordinating multiple agents for real-time, low-latency analysis and decision-making. How We Built It We developed BrainSafe as a browser extension that operates in real time with minimal latency. Using the Google Agent Development Kit (ADK) , we integrated APIs for video frame analysis and added custom logic to perform: Contrast & Visual Filtering : Detection of oversaturated colors and flashing sequences, with adaptive filters applied to reduce intensity while preserving content clarity. Pace Detection & Speed Control : Monitoring scene-change frequency and slowing playback when rapid cuts exceed safe thresholds, reducing sensory overload for developing visual systems. Content Safety Analysis : AI-powered evaluation of content themes against developmental guidelines, issuing warnings for material lacking educational or age-appropriate value. The prototype was built in Python and JavaScript , connected with a Django backend , and enhanced with prompt engineering and Google ADK multimodal agents for optimized video analysis. Challenges Real-time performance : Achieving reliable analysis without playback lag was the biggest technical challenge. New toolkit learning curve : Mastering the Google ADK during the hackathon required rapid experimentation and adaptation. Balancing intervention and usability : Designing filters and playback adjustments that protect children without making content unwatchable. Cross-platform testing : Ensuring consistency across video formats and platforms like YouTube and Instagram. Results We tested BrainSafe on a set of popular children’s videos. The extension: Successfully adjusted playback speed when content had rapid scene changes Reduced overstimulating visual intensity through adaptive filtering Triggered warnings for videos flagged as developmentally inappropriate These outcomes demonstrated the feasibility of real-time AI protection for infants and toddlers during digital content consumption. Future Scope and Scalability With a basic working application in place, BrainSafe can be extended in several ways to maximize its utility and impact: Customizable Moderation : Parents will be able to personalize filtering settings for their child’s needs. For example, if a child has a phobia (such as dogs), parents could specify this, and the AI would flag or block videos containing such triggers to prevent unnecessary stress. Mobile Integration : Extending BrainSafe beyond the browser into mobile environments using a “display over other apps” service. This would allow the system to monitor video content across popular mobile apps and apply the same real-time protections. By iteratively building on this foundation, BrainSafe can grow into a comprehensive AI-powered safety layer for children’s digital media consumption , bridging the regulatory gap with scalable, customizable protection. <div