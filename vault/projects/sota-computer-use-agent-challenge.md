---
slug: "sota-computer-use-agent-challenge"
url: "https://devpost.com/software/sota-computer-use-agent-challenge"
title: "SOTA Computer use agent challenge"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 149
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
---

# SOTA Computer use agent challenge

> Competing to build a SOTA computer use agent (Cua + Hud + Ollama)

[Devpost](https://devpost.com/software/sota-computer-use-agent-challenge) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[vision_ocr]]
**substrate** [[structured_db]]

**stack** cua, hud, ollama

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sota computer use agent challenge

## Body

Inspiration Test the limits of current computer-use agents on realistic desktop tasks. What it does Executes high-level natural language instructions (e.g. “download dataset, unzip, open in Excel, make pivot table”) by perceiving the screen and controlling mouse/keyboard. How we built it Screen capture + OCR for visual grounding Vision-language model for reasoning Action planner for granular interactions Safety/retry logic for robustness Challenges we ran into UI variability across themes/states Long-horizon task planning Latency vs. accuracy in perception Accomplishments that we're proud of Agent completed multi-step workflows end-to-end Modular architecture for adding new skills Automatic recovery from common failures What we learned Robust grounding is the bottleneck, not just model quality Simple guardrails/retries greatly boost success Human-like adaptability > perfect execution What's next for SOTA Computer Use Agent Challenge Benchmark on standardized real-world tasks Extend to hybrid environments (desktop + web + APIs) Release starter framework for community use <div