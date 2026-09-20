---
slug: "neurolens-2qgdm8"
url: "https://devpost.com/software/neurolens-2qgdm8"
title: "NeuralLens"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1228
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/researcher"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NeuralLens

> An agentic system that models visual attention and neural engagement to autonomously optimize your content.

[Devpost](https://devpost.com/software/neurolens-2qgdm8) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[measured_ablation]] [[multi_agent]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[labor_employment]] [[transportation]]
**user** [[researcher]] [[small_business]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** claudinary, colab, fetch.ai, ngrok, python, react, replicate, runpod, stripe, tribe

## How they structured the write-up

- inspiration
- what it does
- how it works
- what you get back
- how to use it
- the stack
- challenges
- accomplishments
- what we learned
- what's next
- built at la hacks 2026

## Body

NeuralLens Logo NeuralLens Dashboard NeuralLens 🧠 Neuromarketing for every business — not just the Fortune 500. Inspiration There are 400 million small businesses worldwide. They employ over 2 billion people — more than half the global workforce. In the US alone, small businesses account for 99.9% of all companies and generate 44% of economic activity. And almost every single one of them is invisible because the tools that determine whether marketing works — the tools that decode why someone stops scrolling or places an order — have been locked behind a price tag that only the Fortune 500 can afford. Nike paid $200,000 last year to put their homepage through an fMRI machine. They know exactly which headline makes your brain light up with desire. McDonald's knows which menu layout drives you toward the high-margin item before you've read a word. Sephora knows which product image activates the brain's reward circuits in the first 400 milliseconds of exposure. This is not guesswork. This is neuroscience — applied systematically, at scale, by companies with research budgets larger than most small businesses' annual revenue. NeuralLens changes that. What It Does NeuralLens simulates how a real human brain responds to any visual asset — Instagram posts, menus, flyers, logos, webpages — and automatically optimizes both the image and copy until neural engagement improves. No waiting for traffic. No A/B test cycles. No neuromarketing firm. Just an image and a goal. How It Works 1. Simulate Human Viewing NeuralLens renders your image exactly as a visitor would see it. For webpages, Playwright scrolls, captures screenshots, and extracts content in reading order — watching the page the way a human would. 2. Predict Where Eyes Go DeepGaze IIE — trained on real human eye-tracking data — generates a saliency map showing precisely where a human eye would fixate, in what order, and for how long. This tells us which parts of your image actually get seen through generating a heatmaps. 3. Score Neural Engagement The visible regions are scored using Meta's TRIBE v2 — a recently released foundation model trained on over 1,000 hours of real fMRI brain scan data from 720 people. TRIBE v2 uses 70,000 voxels to predicts activation across seven cortical regions: Brain Region What It Measures Amygdala Emotional response — is your content moving? Ventral Striatum Desire and reward — do they want it? Hippocampus Memory encoding — will they remember you? Prefrontal Cortex Cognitive load — is it too confusing? Intraparietal Sulcus Visual attention — do they see your CTA? Medial PFC Self-relevance — does it feel personal? Insula Trust — does something feel off? We combine TRIBE v2's brain activation map with DeepGaze's gaze map to classify every zone of your image: Power zones — high gaze + high brain response → protect these Attention traps — high gaze + low brain response → fix these Hidden value — low gaze + high brain response → elevate these Dead zones — low gaze + low brain response → remove these 4. Generate Optimized Output Our scoring algorithm produces a Neural Engagement Score (NES) from 0–100, identifies the specific issues dragging it down, and generates targeted change instructions for both the image and copy. Changes are applied via Cloudinary's generative AI API — color grading, background replacement, text overlay, object removal. The result: an optimized image and ready-to-paste copy, both grounded in the same neuroscience signal. 5. Multi-Agent Pipeline on Fetch.ai NeuralLens runs as a six-agent system on Fetch.ai's Agentverse, discoverable and invocable through ASI:One: Payment Agent — validates FET payment via Fetch.ai & Stripe Payment Protocol before pipeline starts Orchestrator — user-facing, Chat Protocol, coordinates the pipeline Sensor — calls TRIBE v2 and DeepGaze, generates heatmaps and raw data Interpreter — extracts ROI values from 70,000 voxels, computes NES, runs zone analysis Strategist — generates specific change instructions targeting identified issues Executor — applies changes via Cloudinary AI, returns final result One message to ASI:One. Five agents working in sequence. One optimized output. What You Get Back NES score before and after — the delta is your ROI Zone analysis — which parts of your image are working and which aren't Optimized image — changes applied via Cloudinary AI Ready-to-paste copy — written to trigger the right brain responses for your industry Before and after brain heatmaps — the attention shift is visible Plain English explanations — every change comes with a neuroscience reason How To Use It Send a message to NeuralLens on ASI:One: https://yoursite.com/post.jpg optimize this Instagram post for my bakery That's it. No signup. No configuration. No neuromarketing degree. The Stack Layer Technology Brain simulation Meta TRIBE v2 (70,000 voxels) Eye tracking DeepGaze IIE NES scoring Custom ROI extraction algorithm Image AI Cloudinary generative transforms Orchestration LLM ASI:One (Fetch.ai native) Agent framework Fetch.ai uAgents + Agentverse Page rendering Playwright GPU inference Google Colab A100 Payments Fetch.ai Payment Protocol + Stripe Challenges TRIBE v2 is a research model, not a production API. Open-sourced six weeks before this hackathon with no inference endpoint and documentation written for neuroscientists. We built the entire serving layer from scratch, designed the ROI extraction logic from raw voxel output, and calibrated the NES formula against established neuroscience literature — all in 36 hours. It was difficult to implement the TRIBE v2 model because it's new and we had to experiment with differnet VMs and cloud providers. The ROI index problem. TRIBE v2 outputs 70,000 voxel activations mapped to cortical surface coordinates. Translating those into the seven brain regions we needed required manually mapping MNI atlas coordinates to voxel index ranges from the paper's appendix. Multi-agent data routing on Fetch.ai. uAgents Model fields are primitive-typed. Passing complex data structures between five agents required serializing everything to JSON strings and designing the entire inter-agent protocol around that constraint. Accomplishments We were the first team to point TRIBE v2 at small business marketing. The model was open-sourced 30 days before this hackathon. Nobody had built a product with it. We built a genuine multi-agent system — five independent agents with distinct roles, communicating through typed message protocols on Agentverse, invokable by ASI:One without any custom frontend. What We Learned The neuroscience is real. A 2007 Stanford study found ventral striatum activation predicted purchase behavior better than stated preference. Cornell found menu engineering alone lifts restaurant revenue by 15%. Nielsen found neurologically pre-tested ads outperform untested ones by 23% on brand recall. Large companies operationalize this every day. We want to make it accessible to everyone else. What's Next Validation loop — connect NES scores to real A/B test results and calibrate against actual conversion rate changes Industry benchmarks — build comparison databases per vertical so scores have context ("top 25% of bakeries score above 74") Iterative optimization — run the score → change → rescore loop N times, compounding improvements SaaS — $99/month for SMBs, API access for agencies. The comp is neuromarketing firms at $50,000 per study Built At LA Hacks 2026 36 hours. One weekend. UCLA's Pauley Pavilion. Meta's TRIBE v2 was open-sourced March 26, 2026. We were the first to point it at small business marketing. The gap between what Fortune 500 companies know about their customers' brains and what a local bakery knows has existed for 20 years. We closed it in a weekend. Powered by Meta TRIBE v2 · DeepGaze IIE · Cloudinary AI · Fetch.ai Agentverse <div