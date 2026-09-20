---
slug: "browserdelta"
url: "https://devpost.com/software/browserdelta"
title: "BrowserDelta"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 190
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# BrowserDelta

> BrowserDelta cuts browser-agent context by ~78% while matching the vision-full-state baseline on 12/12 next-action predictions! Compression layer for browser use.

[Devpost](https://devpost.com/software/browserdelta) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[cross_origin_web]] [[vision_ocr]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** arize, browserbase, browsergym, fastapi, gpt-4.1-mini, miniwob++, openai-responses-api, opencv, pillow, playwright, pytest, python, react, tesseract-ocr

## How they structured the write-up

- inspiration
- what it does
- results

## Body

MiniWoB Inspiration I love making my agents do things on the web -- what limits me, however, is just how expensive it is! Browser agents waste context by repeatedly sending full screenshots and page state, even when only one textbox or button changed. BrowserDelta asks whether an agent can keep the next-action signal while seeing only the browser state delta. What it does BrowserDelta is an intermediate layer between BrowserBase / Playwright and your agent. It is built with a FastAPI backend and can fit any browser use tool with a run-folder contract. Playwright / Browserbase records screenshots and page state, the codec writes a compaction version of the observations, and the replay eval compares the compact context vs full-state baselines. BrowserDelta behind the scenes uses a few techniques to compact images. DOM diffs noise-filtered pixel diffs region segmentation SSIM / phash metrics OCR Results On the core visual benchmark suite, BrowserDelta matched the vision-full-state baseline on 12/12 next-action predictions while cutting estimated context by about 76%. On imported MiniWoB++ demos, the compact representation reached about 96% token reduction with only a small parity gap against a full-state baseline. <div