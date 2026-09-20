---
slug: "visionguard-smart-vision-for-smarter-driving"
url: "https://devpost.com/software/visionguard-smart-vision-for-smarter-driving"
title: "VisionGuard: smart vision for smarter driving"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 929
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# VisionGuard: smart vision for smarter driving

> Our AI-powered system analyzes in-car video footage to transcribe and interpret driver behavior in real time. By detecting safe/unsafe actions, we provide actionable insights to improve road safety.

[Devpost](https://devpost.com/software/visionguard-smart-vision-for-smarter-driving) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[civic_government]] [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]

**stack** apis, colab, gpt, python, reinforcement, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what’s next for visionguard
- tech stack

## Body

Inspiration Driving in extreme conditions like icy roads and blizzards often leads to accidents due to poor visibility or slippery surfaces . Having personally experienced car accidents caused by vehicles losing control on ice, it’s clear how critical it is to ensure that drivers are cautious and aware. Similarly, my teammates from the crowded Bay Area face challenges with complex road systems and traffic , where crashes are just as frequent. This inspired us to develop VisionGuard , a system that leverages AI to analyze driver behavior and road conditions , ultimately helping drivers make safer decisions. Our goal is to build smarter driving tools that reduce accidents and save lives . What It Does VisionGuard leverages cutting-edge Vision-Language Models (VLMs) to analyze in-car video footage , transcribing and interpreting driver behavior with high precision. By detecting both safe and unsafe actions , VisionGuard generates actionable insights to encourage safer driving practices. Our system identifies critical situations such as: ✅ Distracted driving (e.g., phone use, drowsiness). ✅ Reckless maneuvers (e.g., sudden lane changes, aggressive driving). ✅ Hazardous environmental conditions (e.g., low visibility, icy roads). While we aimed for real-time inference , we found that current VLM models are too computationally expensive for low-latency performance . However, through optimizations, we significantly improved processing efficiency and benchmark accuracy , making this approach feasible for future deployment . Beyond individual drivers, VisionGuard’s insights can benefit: Insurance companies – Enhancing risk assessments and reducing fraud. Fleet managers – Monitoring driver behavior for safety compliance. Autonomous vehicle systems – Providing explainability layers for AI-driven decisions. Our AI-driven approach aims to make roads safer at scale . How We Built It Computer Vision Framework We leveraged state-of-the-art Vision-Language Models (VLMs) , including Gemini Pro 2.0 and Pixtral (13B) , optimizing them with inference-time techniques such as: Chain of Thought (CoT) Prompting: Inspired by OpenEMMA , guiding multi-step reasoning for complex driving scenarios. Ensembling Methods: Majority Voting (best-performing approach). Weighted Confidence Scores to prioritize high-certainty outputs. Self-Consistency Decoding (multiple runs, selecting the most consistent answer). Bias Mitigation for QA Tasks: Detected a bias toward first/last answer choices (A/D) . Shuffled response orders and aggregated multiple generations to improve reliability. Temperature Annealing: Dynamically adjusting sampling temperature based on uncertainty. Logit Smoothing: Preventing overconfident but incorrect predictions. Mixture of Depth (MoD): Reducing computation on low-complexity frames to optimize performance. Although these optimizations reduced inference time , achieving true real-time performance on large VLMs remains a challenge . AI-Powered Reasoning We integrated OpenAI’s GPT-4 API to enhance natural language reasoning . VisionGuard translates raw detections into human-readable feedback , such as: "You seem distracted—keep your eyes on the road." "Road conditions are hazardous—reduce your speed." Additionally, we implemented causal reasoning chains , allowing VisionGuard to explain why alerts were triggered , increasing transparency and user trust. Reinforcement Learning for VLM Fine-Tuning We experimented with GRPO (Generalized Reinforcement Policy Optimization) to fine-tune the Qwen VL-2B model, leveraging 4× A100 NVIDIA GPUs . Implementation Details: Used Hugging Face TRL library for RL training. Tensor sharding across GPUs to fit the model in memory. Trained on the NuScenes-QA dataset , similar to Tesla-provided data . Implemented reward shaping for deeper reasoning ability. Despite our efforts, batch size constraints (1) and long training times (6+ hours) prevented meaningful improvements over API-based VLMs , reinforcing the importance of scaling laws for multimodal AI. Inference Pipeline & Bottlenecks We developed a high-throughput processing pipeline , but achieving real-time inference on large VLMs was infeasible due to: High computational cost per frame (especially for complex scenes). Memory bandwidth limitations when streaming video into large models. Latency bottlenecks in API-based reasoning (due to network-dependent processing). To improve performance, we explored: Frame Sampling & Preprocessing: Used event-based sampling to prioritize critical driving moments . Applied contrastive normalization for better video clarity. Parallelized Inference: Asynchronous execution of multiple VLM instances. ONNX Runtime + TensorRT optimizations for acceleration. Edge Deployment Optimization: Investigated distillation-based lightweight VLMs for future on-device inference. Implemented multi-threaded execution to minimize bottlenecks. Challenges We Ran Into 1. Real-Time Inference Limitations We originally aimed for real-time inference but found that current VLM architectures are computationally too expensive to process full-resolution video at interactive speeds. Even with optimizations like tensor parallelism and ONNX acceleration , the latency was too high for real-time driver feedback. 2. GPU Memory Constraints Frequent OOM (Out-Of-Memory) errors when fine-tuning large VLMs locally. Used DeepSpeed, FP16 precision, and tensor sharding to fit models within 4× A100 GPUs . 3. API Integration Challenges Rate-limiting issues when interfacing with OpenAI and Google Gemini. Latency bottlenecks with cloud-based reasoning models. Accomplishments That We're Proud Of ✅ Functional Prototype: Built a working system that analyzes driving behavior and environmental hazards . ✅ VLM Fine-Tuning Exploration: Pushed the limits of reinforcement learning for multimodal AI . ✅ Pipeline Optimization: Developed low-latency video processing techniques , bringing VLM-powered driving intelligence closer to real-time feasibility . ✅ Cross-Disciplinary Collaboration: Our team bridged AI, reinforcement learning, and computer vision , tackling one of the hardest challenges in multimodal AI . What’s Next for VisionGuard 🚗 Improving Real-Time Feasibility – Exploring smaller, distilled VLMs for on-device deployment . 📊 Data Partnerships – Collaborating with insurance & fleet management to enhance risk prediction. 👁 Multimodal Expansion – Integrating LiDAR, GPS, and radar for enhanced environmental awareness. ⚡ Edge Optimization Research – Experimenting with efficient quantization strategies for mobile and embedded systems . Tech Stack 🔹 Vision-Language Models: Google Gemini, Mixtral AI (Pixtral 13B), OpenAI 🔹 Deep Learning Frameworks: Hugging Face Transformers, DeepSpeed, Torch 🔹 GPU Acceleration: CUDA, ONNX Runtime, TensorRT 🔹 Computer Vision: OpenCV <div