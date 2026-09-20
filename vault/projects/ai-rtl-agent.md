---
slug: "ai-rtl-agent"
url: "https://devpost.com/software/ai-rtl-agent"
title: "Litho"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 389
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/formal_verification"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Litho

> Ai Agent that designs computer chips in VSCode.

[Devpost](https://devpost.com/software/ai-rtl-agent) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[formal_verification]] [[multi_agent]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** python, typescript, verilator

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai rtl agent

## Body

Inspiration My team has been speaking to hardware engineers across the semiconductor industry and we've noticed there is a major gap in AI adoption. While some teams have seen huge productivity boosts from AI, most haven't even started. Why? Because there is no unified tool. Instead each company and sometime each team has their own patched together workflow. This inspired us to build a platform that finally makes it easy to accelerate chip design with AI. What it does We built an AI assistant that designs computer chips, packaged directly into a seamless plugin for VSCode. Core Features: From English to Hardware: Automatically turns natural language descriptions into the complex code used to design semiconductors. Automated Testing: Automatically writes and runs tests to prove the hardware actually work before they are ever manufactured. Visual Debugging: Generates visual graphs (waveforms) of the electrical signals, making it easy for engineers to spot and fix bugs right inside their editor. How we built it We built a multi agent system with four different agents (Orchestrator, Spec, Writer, Tester). The Orchestrator routes tasks, Spec interprets requirements, Writer generates the code, and Tester verifies it. Splitting responsibilities this way keeps each agent's context window focused on a narrow task, which avoids the quality degradation you get when you cram an entire workflow into one prompt. We then packaged the agent alongside a custom waveform viewer as a VSCode extension, so the whole thing runs inside the editor developers already use. Challenges we ran into The hardest part was getting the agents to produce hardware that actually works, not just code that compiles. Its very easy to generate code that compiles but has edge cases that bug out. We also spent alot of time integrating verilator, the waveform viewer, and the multi-agent loop into a single VSCode extension. Accomplishments that we're proud of The agent crushed all the VerilogEval bench tests we threw at it. And we are proud that it feels like an actual tool you can use to do hardware design. What we learned We learned a lot on the product side. Engineers don't just want a chatbot they want a tool that fits into their existing workflow thats why we decided on a VSCode extension instead of a standalone app. What's next for AI RTL Agent More Features! (Formal Verification, UVM) <div