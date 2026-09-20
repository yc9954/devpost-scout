---
slug: "fambai-cv-btnw54"
url: "https://devpost.com/software/fambai-cv-btnw54"
title: "Offline AI Farming Advisor for Zimbabwe"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 411
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "user/government_staff"
---

# Offline AI Farming Advisor for Zimbabwe

> An offline AI advisor that helps Zimbabwean farmers diagnose livestock diseases and get crop guidance by Natural Region — no internet, no cloud, running entirely on the laptop already on their desk.

[Devpost](https://devpost.com/software/fambai-cv-btnw54) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**domain** [[agriculture_food]] [[health_clinical]]
**user** [[frontline_worker]] [[government_staff]]

**stack** bash, git, python

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration Cloud-hosted LLMs require stable fibre, sustained electricity, and ongoing API fees — none of which are guaranteed for a smallholder farmer, extension officer, or agri-dealer in rural Zimbabwe. Meanwhile, tick-borne cattle diseases alone account for 20-30% of recorded cattle deaths annually in the country, and farmers often lack fast access to a vet when symptoms first appear. We wanted to put expert-level triage and crop advisory directly on the laptop already sitting in these communities — no connectivity required. What it does Offline AI Farming Advisor is an on-device LLM that runs entirely locally on an 8GB laptop and helps with two core tasks: Livestock disease triage — a farmer describes symptoms (fever, unusual behavior, discoloured urine, etc.) and the model identifies the likely condition (e.g. theileriosis, gallsickness, redwater, heartwater), flags urgency, and recommends next steps including when to contact a vet. Crop advisory— pest/disease identification and planting-window guidance tailored to Zimbabwe's Natural Regions (I-V), since correct advice in one region can be wrong in another. Every answer is grounded in a locally-stored knowledge base of verified Zimbabwe-specific agricultural and veterinary information — not just the model's general training data. How we built it Model:Qwen2.5-3B-Instruct, quantized to GGUF (Q4_K_M) to fit comfortably within the 7GB RAM budget on the ADTC Standard Laptop profile. Inference: llama.cpp, CPU-only, matching the integrated-graphics-only hardware spec. Knowledge grounding (RAG): a hand-curated corpus covering cattle tick-borne diseases, fall armyworm, Natural Region planting guidance, and [poultry/goats — fill in what you completed], retrieved locally at inference time with zero external calls. Validation: the ADTC profiler, run repeatedly to check throughput, peak memory, and thermal behavior against the reference hardware target. ## Challenges we ran into Getting the download pipeline working cleanly on Windows vs. the Ubuntu 22.04 reference environment," "Balancing corpus depth against the 6-day build window," "Making sure the model gives appropriately cautious answers (recommending a vet) rather than overstating confidence on serious symptoms. ## Accomplishments that we're proud of A model that runs fully offline, grounded in real Zimbabwean agro-ecological and veterinary data rather than generic agricultural text — built to be genuinely usable by someone with no internet access and no technical background. ## What we learned RAG design ## What's next for Offline AI Farming Advisor for Zimbabwe Expanding the knowledge base to cover more livestock (goats, sheep in more depth), more crops, and additional languages (Shona/Ndebele support), plus exploring a lightweight LoRA fine-tune on the local corpus to further improve accuracy. <div