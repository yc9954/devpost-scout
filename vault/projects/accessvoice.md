---
slug: "accessvoice"
url: "https://devpost.com/software/accessvoice"
title: "AccessVoice - Voice Driven Browsing"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 780
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AccessVoice - Voice Driven Browsing

> A Chrome Extension that lets visually impaired users browse the internet through natural voice conversation, powered by Amazon Nova Sonic and Nova 2 Lite working in concert.

[Devpost](https://devpost.com/software/accessvoice) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[finance_payments]] [[labor_employment]] [[retail_commerce]] [[supply_logistics]]
**substrate** [[document_pdf]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** amazon-nova-lite, amazon-nova-sonic, aws-bedrock, aws-strands-sdk, chrome, fastapi, python, react, socket.io, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for accessvoice

## Body

Access Voice - Helping 2.2 billion people globally have vision impairments System architecture - Nova Sonic voice + Nova 2 Lite vision pipeline AccessVoice start screen - Chrome Extension sidepanel CNN news reading - headlines summarized by voice Apartment search results with voice summary Amazon shopping scenario - winter jacket search results Voice session active - connected and listening Autonomous browsing - Nova 2 Lite navigating Apartments.com Inspiration 2.2 billion people globally have vision impairments (WHO, 2023). Current assistive technology for web browsing — screen readers like JAWS ($100+/year), NVDA, VoiceOver — requires users to learn complex keyboard shortcuts, understand DOM structure, and navigate element-by-element. Everyday web tasks — searching for an apartment, shopping for clothes, reading the news — are disproportionately difficult for visually impaired users. We wanted to remove the technical barrier entirely. What it does AccessVoice replaces the traditional screen reader + keyboard navigation paradigm with natural voice conversation. Users speak commands like "Search for apartments in Seattle" and AccessVoice autonomously browses the web, reads page content, refines searches, and reports results — all through real-time spoken dialogue. The system runs as a Chrome Extension that controls the user's own browser, combining two Nova models: Nova Sonic handles bidirectional voice conversation with sub-700ms latency, including async tool calling mid-sentence Nova 2 Lite serves dual roles: analyzing browser screenshots to plan DOM actions (click, type, scroll, navigate) AND generating accessibility-friendly page summaries Users interact via voice or text through the extension's sidepanel. The system acknowledges commands immediately ("Let me search for that..."), performs the browsing action in the user's active tab, and responds with a natural spoken summary of what it found. How we built it Chrome Extension Architecture : AccessVoice is a Manifest V3 Chrome Extension with four components: a service worker managing Socket.IO communication with the backend, a content script injected into every page to execute DOM actions and capture screenshots, an offscreen document for microphone capture and audio playback via Web Audio API, and a sidepanel built with React showing the conversation transcript and browser screenshots. Nova Sonic integration : We use the Strands SDK's BidiNovaSonicModel with bidirectional HTTP/2 streaming. Audio flows continuously in both directions — the user's microphone PCM streams through the extension to Nova Sonic, and the model's spoken responses stream back for gapless playback. Nova 2 Lite as Action Planner : Our key innovation — using Nova 2 Lite's vision capabilities for autonomous browser control. When the user requests a browsing task, the browse_website tool enters a multi-step loop (up to 10 steps): Request a screenshot from the extension's content script Send the screenshot + user goal to Nova 2 Lite as an action planner Nova 2 Lite analyzes the page visually and returns a structured action The backend sends the action to the extension, which executes it in the user's browser Repeat until the task is complete This vision-based approach works on any website without site-specific integrations — it sees the page like a human would. Challenges we ran into Audio keepalive protocol : Nova Sonic requires continuous audio input. We implemented a silent-frame keepalive that maintains the bidirectional stream during tool execution, preventing timeouts. Cross-component messaging : Chrome's Manifest V3 architecture requires careful message passing between service worker, content script, offscreen document, and sidepanel — each in a separate context. Vision-based action planning reliability : Getting Nova 2 Lite to consistently return valid CSS selectors required extensive prompt engineering and structured output parsing. Accomplishments that we're proud of Two-model pipeline via Chrome Extension : Screenshots flow from browser → content script → service worker → backend → Nova 2 Lite → action commands → back through the extension → DOM execution, all during a live voice conversation. Async tool execution during live voice : Nova Sonic says "Let me search for that..." while simultaneously executing the browse_website tool. No awkward silence. Zero deployment friction : Users install a Chrome extension — no servers, no Docker, no technical setup. What we learned Nova Sonic's bidirectional streaming with async tool calling is powerful for conversational agents that perform real-world actions. Vision-based action planning (screenshot → structured action) generalizes across websites better than DOM parsing. Chrome Extension architecture is superior to cloud-based browser automation for accessibility — it respects users' preferences, bookmarks, and authenticated sessions. What's next for AccessVoice Multi-tab support for managing multiple browsing tasks simultaneously Form filling assistance for complex forms (job applications, insurance) through voice Personalized browsing profiles that remember preferences for frequently visited sites Add a BYOK settings panel to the extension Each user provides their own AWS credentials through the extension UI Backend uses those credentials per-session, never stores them This eliminates your cost exposure entirely <div