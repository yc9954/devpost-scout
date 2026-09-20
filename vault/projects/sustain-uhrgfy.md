---
slug: "sustain-uhrgfy"
url: "https://devpost.com/software/sustain-uhrgfy"
title: "sustAIn"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 974
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "domain/climate_energy"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# sustAIn

> sustAIn makes AI more sustainable by compressing prompts without hurting quality, reducing token usage, costs, and the water and energy needed to power AI.

[Devpost](https://devpost.com/software/sustain-uhrgfy) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[structural_withholding]]
**domain** [[climate_energy]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** css, html, javascript, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for sustain

## Body

sustAIn integrates into AI tools like ChatGPT, letting users compress prompts with adjustable compression levels directly in their workflow. The sustAIn dashboard shows estimated savings from prompt compression, including tokens, water, energy, and CO₂. Inspiration What inspired me to build sustAIn was the realization that every AI prompt has an environmental cost that most people never see. Behind every response are data centers consuming electricity, cooling systems using water, and infrastructure producing carbon emissions. As AI becomes part of everyday life, even small inefficiencies repeated millions of times can turn into a much bigger environmental problem. I wanted to build something that makes that invisible impact visible. Instead of telling people to stop using AI, I wanted to help them use it more responsibly. sustAIn was inspired by the belief that smarter prompting can mean less wasted computation, less wasted energy, less water consumed, and less CO₂ emitted. To me, this project is about showing that innovation and sustainability can go hand in hand, and that even a small change in how we interact with AI can scale into something meaningful. What it does sustAIn is a browser extension that makes AI prompting more efficient by compressing long prompts into shorter ones while preserving the core instructions and intent. It integrates directly into platforms like ChatGPT, Claude, Gemini, Perplexity, Microsoft Copilot, and DeepSeek, so users can improve their prompts without changing the way they already work. The tool gives users different compression levels, lets them instantly undo changes, and tracks the estimated environmental impact of their savings through metrics like water, energy, and CO₂. In simple terms, sustAIn helps people use AI more responsibly by reducing unnecessary prompt bloat while keeping output quality strong. How I built it I built sustAIn as a Chrome extension using HTML, CSS, and JavaScript, focusing on making the experience feel seamless inside the AI tools people already use. I designed and implemented the full frontend, including the in-page compression controls, onboarding tutorial, popup dashboard, settings panel, and environmental impact displays. I also built the site integrations so the extension can work directly across platforms like ChatGPT, Claude, Gemini, Perplexity, Copilot, and DeepSeek. On the technical side, the extension uses a lightweight AI model for prompt compression that runs locally in the browser. Instead of generating full responses like a typical large language model, this AI analyzes the prompt and estimates which words carry the most important information for the model to understand the task. Words that contribute less meaning are removed while the key instructions, constraints, and intent are preserved. Because the model focuses on token-importance analysis rather than text generation, it is significantly smaller and efficient enough to run directly on the user’s device without requiring a cloud backend. The computation needed for this analysis is extremely small compared to running a full large language model request, so the compression step adds minimal overhead while helping reduce the total computation required for the main AI response. I also implemented multiple compression modes to control how aggressively prompts are shortened, along with instant undo functionality so users can revert to the original prompt at any time. The extension tracks estimated savings from prompt compression and converts them into environmental impact metrics such as water usage, energy consumption, and CO₂ emissions. A major part of the development process was balancing compression strength with output quality so that prompts could be shortened while still producing reliable results from AI systems. Challenges I ran into One of the biggest challenges I ran into was figuring out how to make prompt compression actually work inside a real Chrome extension instead of just as a local prototype. Running advanced compression locally sounds simple in theory, but browser extensions have strict packaging, performance, and compatibility limits. I had to rethink the architecture so the tool could stay lightweight, responsive, and practical enough for everyday use. Accomplishments that I'm proud of I’m proud that I was able to take an idea that started as a technical concept and turn it into a real, usable product. sustAIn became much more than a prototype, I built it into a working browser extension with a polished interface, an onboarding tutorial, different compression levels, undo functionality, and a popup dashboard. I think one of the things I’m happiest about is that it actually feels like something people could use in their everyday workflow. I’m also proud that the project connects technology with a larger purpose. The extension helps reduce unnecessary AI prompt bloat, but it also makes people think about the hidden environmental impact of AI by showing estimated water, energy, and CO₂ savings. I also spent a lot of time testing compression settings to make sure the tool could save resources while still keeping output quality strong. To me, the biggest accomplishment was building something that feels practical, thoughtful, and meaningful at the same time. What I learned I learned how important tradeoffs are in engineering. There was no perfect solution that gave maximum compression, perfect quality, zero friction, and zero cost all at once. I had to make decisions about what mattered most and test where the best balance was. More than anything, this project taught me that even small improvements in efficiency can become meaningful when they scale, especially in something as widely used as AI. What's next for sustAIn What’s next for sustAIn is turning it from a hackathon project into a real tool people can install and use every day. One of my biggest goals is to publish sustAIn as a Chrome extension so it can be publicly available and accessible to anyone who wants to make their AI usage more efficient and sustainable. I also want to keep improving the compression engine so it handles a wider range of prompts more accurately, especially structured prompts like code, JSON, and detailed formatting instructions. <div