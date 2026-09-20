---
slug: "cyberdrive"
url: "https://devpost.com/software/cyberdrive"
title: "CyberDrive"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 352
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# CyberDrive

> CyberDrive - Transforming driving footage into intelligent insights.

[Devpost](https://devpost.com/software/cyberdrive) · hackathon [[TreeHacks 2025]]

## Facets

  <sub>weak: vision_ocr</sub>
  <sub>weak: civic_government, transportation</sub>
  <sub>weak: video_visual</sub>

**stack** amazon, async, gemini, google, openai, opencv, python, pytorch

## Body

I've always been inspired by Tesla's Full Self-Driving technology and its potential to revolutionize transportation safety. The prospect of having vehicles that can navigate autonomously, eliminating stress and enhancing safety, is incredibly exciting. I believe this future is extremely close, and Tesla is leading the way in making it a reality. The development of CyberDrive has been an enlightening journey that revealed how hard and complex computer vision and self-driving tasks really are. While I initially faced significant challenges implementing CNNs and other low-level image neural networks from scratch, I found success by pivoting to vision capabilities in large language models, which demonstrated superior performance. The final implementation leverages multiple LLM calls and incorporates advanced techniques such as mixture of experts, majority decision systems, and reasoner reward models to achieve robust driving scenario analysis. Below is a paragraph that goes more into detail about my final project. The system employs a sophisticated multi-stage pipeline that begins with cv2 extracting 5 equally-spaced keyframes from each video, overlaying frame numbers for reference, and storing them with semi-transparent labels using alpha blending. These frames feed into an LLM-based analysis process that leverages prompt engineering to focus the model's attention on specific visual elements relevant to the question at hand (like road signs, lane markings, or potential hazards) while enforcing a structured frame-by-frame analysis methodology. The system makes three independent GPT-4V attempts at analyzing the same frames, implementing concurrent processing with asyncio and rate limiting via semaphores to efficiently handle the API calls. Each attempt generates both an answer and detailed reasoning, which are then aggregated and evaluated by a separate LLM stage using a reasoner model. This meta-analysis stage systematically compares the observations and logic across all three attempts, looking for consensus, unique insights, and potential discrepancies. By having multiple independent attempts and a dedicated reasoning layer to synthesize them, the system can triangulate more reliable answers, catch details that might be missed in a single pass, and critically evaluate the strength of different logical pathways - ultimately leading to more robust and well-justified conclusions than would be possible with a single analysis attempt. <div