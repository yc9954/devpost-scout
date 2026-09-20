---
slug: "lumen-ai-neonatal-specialist"
url: "https://devpost.com/software/lumen-ai-neonatal-specialist"
title: "Lumen - AI neonatal specialist"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1231
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/legal_professional"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Lumen - AI neonatal specialist

> AI neonatal danger-sign screening for community health workers — Qwen Cloud when online, a fine-tuned on-device Qwen3-VL when not, so it never goes dark.

[Devpost](https://devpost.com/software/lumen-ai-neonatal-specialist) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[on_device_local]] [[realtime_stream]]
**domain** [[agriculture_food]] [[health_clinical]] [[labor_employment]] [[transportation]]
**user** [[legal_professional]] [[patient_family]] [[social_worker]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** alibaba, android, c++, cloud, docker, fastapi, gradle, java, lightgbm, llama.cpp, mcp, python, qwen, qwencloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- built on a prior project — completely redesigned for this hackathon
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lumen - ai neonatal specialist

## Body

architecture workflow Inspiration Every year 2.3 million newborns die within 28 days of birth — about three-quarters in sub-Saharan Africa and South Asia, and three-quarters within the first week. Most of these deaths are preventable, and the bottleneck usually isn't medicine — it's detection . The WHO IMNCI protocol defines a systematic newborn danger-sign assessment, but in the field a community health worker (CHW) is often the only health contact a baby gets: trained knowledge decays, there's no diagnostic equipment, and a paper checklist can't calculate a dose or reason over a photo. Field studies put CHW danger-sign sensitivity anywhere from 33% to 91% . The cruel twist is that the places where this matters most are exactly the ones with no reliable internet . A cloud-only medical agent abandons those babies; a purely offline one leaves the cloud's best multimodal reasoning on the table. That tension is the whole reason EdgeAgent is the right track for this problem — and why I built LUMEN to be both , and to switch between them automatically. What it does LUMEN turns the phone or laptop a CHW already carries into an AI neonatal specialist that follows the WHO postnatal home-visit workflow end to end. A single guided encounter collects voice intake (in 12 languages), a camera-guided 7-capture visual exam (face, eyes, chest, umbilicus, full body, foot sole, optionally placenta), a tap-to-count respiratory measure, and a 10-second cry recording . From those inputs it produces 21 structured danger-sign checks , a WHO IMNCI classification with a RED / YELLOW / GREEN traffic light, an action plan with exact medication doses , a referral letter, and a follow-up date — and it escalates RED/YELLOW cases to a supervisor queue for human sign-off. Encounters are stored locally and sync to the cloud when the network returns, so the worker is never blocked and the record always arrives. Crucially, every safety-critical number is computed in code, not written by the model — online or offline. How we built it LUMEN is one provider interface with two backends — Qwen Cloud and a local model — behind a FailoverRouter that picks per request on connectivity, latency, and a privacy flag. Cloud reasoning uses the best-fit Qwen flagship per stage through DashScope: qwen3-vl-plus for the visual exam, qwen3-omni-flash for native cry-audio understanding, and qwen3.7-plus for agentic synthesis. The assessment runs as a small society of specialist agents — Visual, Audio, Classifier, Triage , plus a MemoryAgent that recalls prior visits — orchestrated with Qwen-Agent . The five deterministic WHO skills (dosing with hard caps, weight-for-age z-score, ORS volume, referral letter, follow-up) are exposed over MCP , so the model decides which tool to call and the tool decides the number. The offline brain is Qwen3-VL-4B-Instruct , fine-tuned with QLoRA on a single RTX 4070 into LUMEN-Q — a two-stage recipe (text IMNCI, then vision jaundice/skin-tone) over the same neonatal corpus the cloud path is calibrated against — then exported to a quantized GGUF and run through llama.cpp's multimodal mtmd API. A calibrated LightGBM ensemble (an IMNCI head + a CIE-Lab jaundice-colorimetry head) supplies the safety-critical traffic light in both modes. The same FastAPI image deploys to Alibaba Function Compute 3.0 , with encounters synced to OSS ; a native Android build runs the identical edge↔cloud logic on a phone, with on-device inference through a C++/JNI llama.cpp bridge. Built on a prior project — completely redesigned for this hackathon An earlier, offline-only version of this neonatal-screening idea existed before this hackathon's Submission Period, built around local models. LUMEN is inspired by it, but everything that defines this entry was designed and built new during the Submission Period. New for this hackathon: Entire model layer → Qwen. Qwen Cloud ( qwen3-vl-plus , qwen3-omni-flash , qwen3.7-plus ) for online reasoning, and a newly fine-tuned Qwen3-VL-4B (LUMEN-Q, QLoRA) for the offline path — validated with a fresh held-out base-vs-fine-tuned evaluation. The EdgeAgent architecture itself — a FailoverRouter with automatic edge↔cloud switching on connectivity, latency, and privacy. The prior app was offline-only; cloud reasoning and graceful failover didn't exist before. A multi-agent layer — Visual, Audio, Classifier, and Triage agents plus a Memory agent — orchestrated with Qwen-Agent, with the deterministic WHO clinical skills exposed over MCP. Alibaba Cloud deployment — Function Compute 3.0 (custom container) and OSS offline-sync — new. Longitudinal patient memory and a supervisor triage/escalation queue — new. A native Android app doing on-device Qwen3-VL inference via llama.cpp, with the same edge↔cloud routing. What carried over is domain knowledge, not code: the WHO IMNCI clinical framing. Everything this hackathon actually judges — the Qwen Cloud integration, the EdgeAgent failover design, the multi-agent/MCP orchestration, and the Alibaba Cloud deployment — was built during the Submission Period. Challenges we ran into The offline model had to be clinically trustworthy, not just present. A stock 4B vision model is unreliable on neonatal imagery, so fine-tuning wasn't optional — it was the EdgeAgent thesis. Getting the two-stage QLoRA recipe to run on 12 GB (and fixing a real dataset-pipeline bug along the way) took the most iteration. Class imbalance is dangerous here. Severe jaundice is ~1% of the data, and the fine-tuned model still under-grades the rarest, most critical cases. Rather than hide that, I made the deterministic IMNCI rules + jaundice colorimetry , not the LLM, own the safety-critical decision. Cloud and local have to behave identically or failover isn't safe — so both share one tested streaming/tool-call core, and the traffic light is decided the same way in every path. A hallucinated paediatric dose can kill. Designing the MCP boundary so the model never writes a number — only requests a tool — was a deliberate constraint, not an afterthought. Porting to a real standalone Android app (native llama.cpp mtmd for Qwen3-VL, edge↔cloud routing, an in-app Qwen-API option) on top of the laptop build. Accomplishments that we're proud of A working edge↔cloud failover , not a slide: the same encounter completes on Qwen Cloud or on-device, with an honest badge showing which ran. Safety by construction — every dose hard-capped in code, "when in doubt, refer," an explicit disclaimer on every output, and supervisor escalation. It really runs offline and on a phone : a fine-tuned multimodal Qwen3-VL in a quantized GGUF, plus a standalone native Android app, in 12 languages . What we learned A small, targeted fine-tune buys enormous reliability even when it doesn't ace every class — going from 65% to 100% parseable clinical answers matters more in the field than a few accuracy points. But a fine-tune won't fix a rare class on its own; the lesson reinforced is that the trustworthy design is hybrid — the LLM reasons and explains, deterministic code decides anything that can hurt a baby. Designing for cloud↔local parity from day one (one provider interface, one streaming core) is what makes graceful degradation actually graceful. Qwen3-VL runs genuinely well on-device through llama.cpp mtmd , which makes the offline half of an EdgeAgent realistic rather than aspirational. What's next for Lumen - AI neonatal specialist Field pilots on low-cost Android with CHW partners, and the Qwen-ecosystem-native MNN runtime as a second on-device engine. Extend the same edge↔cloud pattern across childhood IMNCI — pneumonia, malnutrition, dehydration, and malaria — since the architecture is condition-agnostic. Clinical validation toward a real deployment. The code is open and the weights are published, because these babies can't wait. <div