---
slug: "metermind"
url: "https://devpost.com/software/metermind"
title: "MeterMind"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 756
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MeterMind

> Automating manual gauge inspection for predictive maintenance at scale

[Devpost](https://devpost.com/software/metermind) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** android, ernie-4.5-vl, fastapi, flutter, gradio, huggingface, ios, lora, modal, numpy, nvidia-b200, nvidiab200, opencv, peft

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges we faced
- what we learned
- technical architecture
- results
- what's next

## Body

Integration with app in flutter Web demo with Gradio header Inspiration Walking through an oil refinery, a power plant, or a manufacturing floor, you'll see them everywhere — analog gauges . Pressure gauges, thermometers, ammeters, flow meters. Millions of them. And despite all our advances in automation, most are still read by humans walking inspection routes, clipboard in hand. The predictive maintenance market is projected to grow from $13.6B to $70B+ by 2032 . Yet this critical data entry bottleneck remains: a human squinting at a dial, writing down numbers, sometimes making errors that cascade into equipment failures and safety incidents. I asked a simple question: Can ERNIE-4.5-VL learn to read these gauges? What We Built MeterMind is an end-to-end solution for automated analog gauge reading: Synthetic data generator producing photorealistic gauge images Fine-tuned ERNIE-4.5-VL achieving 86.7% accuracy within ±1 unit Production API with sub-second inference (0.85s) The results exceeded expectations: Metric Before After Improvement Mean Absolute Error 2.82 0.60 79% ↓ Within ±1 unit 46.7% 86.7% +40% Within ±2 units 56.7% 100% +43% How We Built It Phase 1: The Data Problem No labeled dataset exists for industrial gauge reading. Stock photos lack ground truth. Real industrial images are proprietary. Solution: Procedural synthetic generation. We built a pipeline creating 600 gauge images with: Realistic dial faces (pressure, temperature, amperage) 3D perspective transforms simulating camera angles Industrial backgrounds (metal panels, concrete, machinery) Damage effects (scratches, dust, rust stains) Variable lighting (harsh sun, low-light, industrial fluorescent) Training set: 570 images Validation set: 30 images Gauge types: Standard pressure, Glycerin-filled, Bimetal thermometer Phase 2: Training at Scale ERNIE-4.5-VL-28B is a 28 billion parameter vision-language model. Training it required serious hardware. Infrastructure: NVIDIA B200 GPU (192GB VRAM) via Modal Images resized to 512×512 to fit memory constraints LoRA fine-tuning (rank=8, α=16) for parameter efficiency Training config: learning_rate: 2e-4 batch_size: 1 (gradient accumulation: 2) epochs: 1 (285 steps) training_time: ~45 minutes One epoch was enough. The model learned the task quickly — a testament to ERNIE's strong vision-language foundation. Phase 3: The Inference Nightmare Training worked. Evaluation looked great. Then came deployment. First attempt: Unsloth-based inference on H100 GPU. Result: 110 seconds per prediction. That's not a typo. Nearly two minutes to read a single gauge. Completely unusable. Phase 4: The 100x Speedup We refused to accept 110s latency. The optimization journey: vLLM migration — But ERNIE-4.5-VL support required nightly builds LoRA merging — vLLM needed full weights, not adapters Processor configs — Missing preprocessor_config.json crashed the image pipeline Prompt format debugging — Vision models need specific placeholder tokens After significant iteration: Before: 110.0 seconds After: 0.85 seconds Speedup: 129x Challenges We Faced GPU Memory Constraints The model barely fits on a B200. We had to: Reduce image resolution (512×512 max) Use 4-bit quantization during some experiments Carefully manage batch sizes vLLM Bleeding Edge ERNIE support was merged into vLLM recently. Documentation was sparse. We debugged through source code and GitHub issues to understand: How to format multimodal prompts Why processor configs were missing The correct way to pass base64 images Balancing Realism vs. Training Signal Synthetic data is a double-edged sword. Too simple = poor generalization. Too complex = model can't learn the core task. Finding the right balance of augmentations took experimentation. What We Learned Inference optimization is half the battle. A model that takes 2 minutes per prediction is useless in production, regardless of accuracy. Synthetic data works. 600 procedurally generated images achieved strong results. Careful augmentation design matters more than volume. Vision-language models are ready for industrial applications. Fine-tuning unlocks capabilities that zero-shot prompting can't match. The ecosystem is still maturing. vLLM + ERNIE required nightly builds and source-code diving. This will improve, but early adopters face friction. Technical Architecture ┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐ │ Gauge Image │────▶│ ERNIE-4.5-VL │────▶│ Reading: 70.5 │ │ (base64) │ │ (fine-tuned) │ │ (0.85s) │ └─────────────────┘ └──────────────────┘ └─────────────────┘ │ ┌──────────┴──────────┐ │ vLLM Runtime │ │ H100 GPU (Modal) │ │ API Key Auth │ └─────────────────────┘ Results Accuracy: MAE improved from 2.82 → 0.60 ( 79% reduction ) 100% of predictions within ±2 units Works across pressure gauges, thermometers, ammeters Performance: Inference latency: 0.85 seconds (down from 110s) Cold start: ~2.5 minutes (model loading) Production-ready with API authentication What's Next Edge deployment — Optimize for mobile/embedded inference Multi-gauge support — Digital displays, LCD readouts, seven-segment Video processing — Real-time monitoring from camera feeds Industrial integration — SCADA, IoT platforms, predictive maintenance systems Built with ERNIE-4.5-VL, Unsloth, vLLM, and Modal for the ERNIE AI Developer Challenge 2025. ** Demo Link: https://huggingface.co/spaces/luliuzee/metermind-demo <div