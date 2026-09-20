---
slug: "devpilot-ai-j8z3tq"
url: "https://devpost.com/software/devpilot-ai-j8z3tq"
title: "DevPilot AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1243
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DevPilot AI

> AI developer copilot that combines code review, voice debugging, and autonomous doc research powered by Amazon Nova.

[Devpost](https://devpost.com/software/devpilot-ai-j8z3tq) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: provenance_signing</sub>
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** amazon-bedrock, amazon-nova-2-lite, amazon-nova-2-sonic, amazon-nova-act, amazon-web-services, css, fastapi, html, javascript, python, react, rest-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devpilot ai

## Body

Nova 2 Lite detects a CRITICAL SQL injection with 96% confidence — scores code 2/10 and pinpoints the exact line instantly. One click applies the fix. Side-by-side diff shows red for buggy original, green for secure refactored version. Nova 2 Sonic explains your code conversationally — context-aware, multi-turn, like a senior engineer at midnight. Nova Act searches official docs, OWASP, and Stack Overflow — returns a verified solution with real cited sources. Rewrites Python code in TypeScript using idiomatic patterns — async/await, typed parameters, key differences explained. Paste any GitHub URL — Nova reviews every source file and returns aggregate score, critical count, and per-file breakdown. Upload any IDE screenshot — Nova visually identifies what you're building, spots issues, and suggests improvements. Every fix decision tracked — accepted in green, rejected in red. Full audit trail across your entire session. Inspiration It was 11:47 PM. Deadline in 15 minutes. Bugs everywhere. Every developer has been there — staring at broken code, not knowing what's wrong, too tired to think straight. Stack Overflow tabs open everywhere. Documentation that makes no sense. No senior engineer to ask. That's what inspired DevPilot AI. What if you had a senior engineer sitting next to you at midnight? One who could instantly spot security vulnerabilities, explain them in plain English, research the official fix, and rewrite your code — all without judgment and in under 30 seconds? That's DevPilot AI. What it does DevPilot AI is an intelligent developer copilot powered by Amazon Nova that helps developers debug faster by combining three Nova capabilities in one unified workflow. 1. Code Review — Nova 2 Lite Paste any code and get severity-ranked findings (CRITICAL, HIGH, MEDIUM, LOW) with confidence scores on every issue, one-click Apply Fix that rewrites your editor, side-by-side diff view of original vs refactored code, and a full refactored version. 2. Voice Debugger — Nova 2 Sonic Ask spoken or typed questions about your code — "Why is this dangerous?", "Explain this error", "How do I fix this function?" Nova responds conversationally, remembers context across turns, and knows your code. 3. Doc Research Agent — Nova Act Describe any problem and the agent autonomously searches official documentation, GitHub issues, and Stack Overflow — returning the best solution with cited, verified sources. This is not three random tools. It is one unified debugging workflow. Additional Features: Multi-language code translation (Python → TypeScript, Go, Java, Rust, and more) Repo-level review — paste any GitHub URL and review every source file Screenshot analysis — upload an IDE screenshot for visual error detection Shareable review links — share any review with a unique URL Fix history tracking — track every fix accepted or rejected Session persistence — reviews auto-save and reload across sessions Export reports — download full analysis as a markdown file How we built it Architecture User → React Frontend → FastAPI Backend → Amazon Bedrock → Nova Models Tech Stack Frontend: React with custom CSS design system Backend: Python + FastAPI AI Models: Amazon Nova 2 Lite, Nova 2 Sonic, Nova Act Infrastructure: Amazon Bedrock, AWS Nova Model Integration Amazon Nova 2 Lite powers code review, bug detection, security analysis, language translation, repo-level review, and screenshot analysis via Amazon Bedrock Amazon Nova 2 Sonic powers the conversational voice debugging assistant with speech-to-speech capability Amazon Nova Act powers the autonomous documentation research agent that browses official docs, GitHub, and Stack Overflow Prompt Engineering The difference between a vague response and a precise JSON object with severity rankings, line numbers, confidence scores, and runnable fixes came entirely from carefully crafted system prompts with strict output schemas and chain-of-thought reasoning instructions. Challenges we ran into JSON reliability — Nova sometimes returns markdown-fenced JSON or slightly malformed responses. We built a robust multi-stage parser that strips fences, finds JSON object boundaries, sanitizes control characters, and handles edge cases gracefully without crashing the user experience. Voice context awareness — Making the voice assistant feel like it truly "knows" your code required injecting the full code context and conversation history into every prompt while carefully managing token limits to avoid truncation on longer files. Repo-level review at scale — GitHub's API rate limits and varying file sizes meant we had to build smart file filtering, size caps, and sequential processing to review an entire codebase without hitting timeouts or burning through tokens. Keeping it one workflow — The hardest design challenge was making three separate Nova models feel like one coherent product. The solution was shared context — the voice assistant knows what code was reviewed, the research agent knows what error was found, and the fix history tracks decisions across all panels. The 3-minute demo — Fitting 13 features into a compelling 3-minute story was harder than building the features themselves. The solution: a drama script set at 11:47 PM the night before a deadline. Every developer relates. Accomplishments that we're proud of Real Nova integration — Every feature uses real Amazon Nova models via Amazon Bedrock. No mocks, no placeholders. Nova 2 Lite catches a CRITICAL SQL injection vulnerability with 96% confidence in under 3 seconds. 13 features in 3 days — From a blank repo to a fully working application with code review, voice debugging, doc research, language translation, repo-level review, screenshot analysis, shareable links, fix history, session persistence, diff view, export, confidence scores, and severity filtering — all built and tested in 72 hours. The unified workflow actually works — A developer can go from "I have no idea what's wrong" to "fixed, understood, and documented" in under 3 minutes. We tested it live and it works exactly as designed. Production-grade UI — The interface is dark, clean, and fast. It looks and feels like a real developer tool — not a hackathon prototype. What we learned Nova 2 Lite is remarkably good at code reasoning. It doesn't just find bugs — it understands context, suggests idiomatic fixes, and explains issues in ways a junior developer can actually understand. It caught a SQL injection vulnerability with 96% confidence on the first try. Prompt engineering is everything. The quality of Nova's output is directly proportional to the quality of the system prompt. Role definition, output schema specification, chain-of-thought instructions, and explicit guardrails all make a measurable difference. The unified workflow matters more than individual features. Each Nova model becomes dramatically more useful when they share context. The voice assistant giving generic answers is good. The voice assistant knowing exactly which SQL injection is on line 6 of your current file is great. Ship fast and test everything. We ran test cases for every single feature before recording the demo. Three features had bugs that only showed up during testing. Catch issues before the camera turns on. What's next for DevPilot AI VS Code Extension — Bring DevPilot directly into the editor. Inline suggestions, hover-over explanations, and one-click fixes without leaving VS Code. Team Mode — Share reviews, fix history, and research results across an entire engineering team. One developer's fix becomes everyone's knowledge. CI/CD Integration — Run DevPilot automatically on every pull request. Block merges with CRITICAL security issues before they reach production. Nova 2 Sonic Full Duplex — Real-time voice conversation while coding. Ask questions out loud and hear answers spoken back — no typing required. Confidence Score Learning — Track which fixes developers accept vs reject over time and tune confidence scores based on real-world feedback. Built with love for the Amazon Nova AI Hackathon 2026 #AmazonNova <div