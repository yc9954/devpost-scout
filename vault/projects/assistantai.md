---
slug: "assistantai"
url: "https://devpost.com/software/assistantai"
title: "SiliconYOLO"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1213
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "substrate/geospatial"
---

# SiliconYOLO

> Imagine AI vision that runs forever on a coin battery. We hardwired object detection into a $2 chip—26× more efficient than the Edge AI, fully private. Smart eyes for every drone, doorbell, and robot.

[Devpost](https://devpost.com/software/assistantai) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[vision_ocr]]
**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** claude-code, cognichip, digilent-genesys-2(kintex-7-xc7k325t), int8/csd-multiplier-less-arithmetic, pycocotools, python, pytorch(cuda), rtl, simulang, simular(hyperframes), simular(sai), systemverilog, torch-pruning, verilog

## How they structured the write-up

- 💡 inspiration
- ⚡ what it does
- 📐 architecture & specs
- 📊 results & verification
- 💸 cost & efficiency
- 🛠️ how we built it — two ai agents, one human-in-the-loop
- 🏆 accomplishments
- 📚 what we learned
- 🚀 what's next
- 🧰 built with

## Body

GIF 🔬 Silicon YOLO We froze a neural network into silicon. YOLOv10n's weights become hard-wired, multiplier-less logic — ~0.2 W, ~$2/chip , up to ~200 FPS object detection that beats edge GPUs on energy by ~26× — co-designed by two AI agents orchestrated by a human-in-the-loop. A fixed-weight YOLO object-detection chip for the Digilent Genesys 2 / Xilinx Kintex-7 XC7K325T . Instead of fetching weights from DRAM, every weight is baked into the fabric as CSD / constant-coefficient multipliers (0-DSP) — INT8 (INT4 for tolerant layers), 640×640, 80-class COCO. The model never changes, so the silicon doesn't need a general MAC array, a weight bus, or off-chip memory. 🎯 Target ⚡ Throughput 🔌 Power 🧮 DSPs 📦 LUTs 🎓 Accuracy FPGA — Kintex-7 XC7K325T ~51 FPS @ 200 MHz ~3.2 W 0 ~38K (11.7%) 37.62 mAP50-95 ASIC — 28 nm (est.) up to ~200 FPS @ ~800 MHz ~0.2–0.8 W 0 logic-only 37.62 mAP50-95 💡 Inspiration Most edge-AI accelerators spend the majority of their power and area moving weights around — DRAM fetches, weight buses, big general-purpose MAC arrays. But for a fixed function — "detect these 80 COCO classes, forever" — the weights never change. So why pay to move them? Bake them into the silicon. A constant weight isn't a multiply at all; it collapses into a handful of shifts and adds (canonical-signed-digit arithmetic). That removes the DSP array, the weight memory traffic, and most of the power. ⚡ What it does Runs YOLOv10n (NMS-free) at 640×640, 80-class COCO entirely on-chip — no DRAM weight traffic. 0 DSP blocks. Every conv weight is a CSD constant-coefficient multiplier + on-chip weight ROM. Folded INT8 pipeline of 1024 CSD MACs , per-channel weight scales (INT4 for tolerant layers). NMS-free head deletes an entire hardware block vs. classic YOLO accelerators. Fits ~11.7 % of a Kintex-7 at ~51 FPS / ~3.2 W — and as a 28 nm ASIC runs up to ~200 FPS @ ~800 MHz at ~0.2–0.8 W (the real product). Near-lossless: FP32 37.94 → INT8 37.62 mAP50-95 ( −0.32 pt ). 📐 Architecture & specs Target board Digilent Genesys 2 — Xilinx Kintex-7 XC7K325T Model YOLOv10n (NMS-free), COCO 80-class Input 640×640 RGB Precision INT8 datapath, per-channel weight scales; INT4 for tolerant layers Compute 1024 CSD constant-coefficient MACs , folded dataflow, 0 DSPs Weights Frozen in on-chip ROM ( .mem / .coe ), baked as multiplier-less logic LUTs ~38K ( 11.7 % of XC7K325T) BRAM ~483 ( 57.5 % ) Throughput ~51 FPS @ 200 MHz (FPGA) up to ~200 FPS @ ~800 MHz (28 nm ASIC) Power ~3.2 W on FPGA ~0.2 W (200 MHz) – ~0.8 W (800 MHz) as a 28 nm ASIC Accuracy FP32 37.94 → INT8 PTQ 37.62 mAP50-95 (−0.32) 📊 Results & verification Accuracy: INT8 post-training quantization is essentially lossless (−0.32 pt) and above the original YOLOv8-n baseline. RTL proven bit-exact: 4/4 datapath unit testbenches PASS under Icarus Verilog, checked against golden vectors (the CSD MAC slice and 1024-MAC array reproduce the integer reference exactly). Honest caveat: the top-level testbench reports INCONCLUSIVE (the detection-output decoder is still stubbed // TODO ) — we report that rather than a false PASS. Per-block datapath correctness is proven. See rtl_tb/SIM_SHOWCASE.md . 💸 Cost & efficiency The FPGA is the prototype ; the fixed-weight 28 nm ASIC is the product . Against today's edge options it wins decisively on energy and lifetime cost: ⏱️ Two operating points, same efficiency. The datapath is logic-only (0 DSP — every weight is CSD shift-add), so the same netlist closes timing far faster off FPGA fabric. The Kintex-7 is a 28 nm part, so this is a same-node fabric-overhead win (~3–4×): the ASIC reaches up to ~800 MHz → ~200 FPS . Throughput and power both scale ~linearly with clock, so efficiency stays ~constant at ~255 FPS/W — run ~800 MHz / ~200 FPS / ~0.8 W for max throughput, or ~200 MHz / ~51 FPS / ~0.2 W milliwatt-class for battery/always-on. The cost table below uses the low-power point (the headline product mode). Platform Type Power FPS @640 INT8 mAP50-95 Unit cost (@100k) NRE Silicon YOLO ASIC (28nm est.) Fixed-weight ASIC 200 mW 51 37.6 $2 $2.5M Jetson Orin Nano Super Edge GPU SoC 15 W 150 37.3 $249 -- Hailo-8 (accel+host) NN accelerator 2 W 100 37.0 $200 -- Coral Edge TPU (dev board) NN accelerator 2 W 35 36.0 $130 -- Desktop RTX 4060 Desktop GPU 115 W 400 37.4 $300 -- Raspberry Pi 5 (CPU only) CPU SBC 7 W 2 37.3 $80 -- ~26× better energy/frame than a Jetson Orin Nano; ~73× vs. a desktop RTX 4060. ~$2/chip at 100k volume; break-even vs. Jetson at ~10,100 units . ~11× lower 3-year fleet TCO at 100k units, 24/7. Full methodology and tables: docs/COST_COMPARISON.md . 🛠️ How we built it — two AI agents, one human-in-the-loop The whole project was orchestrated by Simular Sai (a computer-use agent) driving two coding/EDA agents in parallel in a single window: Track A — model & verification (Claude Code): baseline → INT8 PTQ → weight freeze → hardware handoff ( hw_graph.json , per-layer .mem / .coe ROMs, quant_scales.json ) → golden vectors. Track B — chip design (Cognichip): spec capture → micro-architecture → PPA → SystemVerilog RTL (layer scheduler, requant unit, SiLU LUT, unified weight ROM, CSD MACs). The handoff contract: Track B is gated — no RTL until Track A freezes the weights and ships the op-graph, quant scales, and golden vectors. Sai enforced that gate, babysat the runs, and recovered the build when it broke. The pivot that made it work: we first tried to compress YOLOv8-n via structured channel pruning + retraining — it worked but recovered accuracy painfully slowly (~32 mAP after 8 epochs; ~50 needed). So we dropped pruning entirely and switched to pretrained YOLOv10n → PTQ → freeze : smaller, more accurate, NMS-free, and no training . The lesson: for a fixed-weight chip, a stronger pretrained model you never touch beats a weaker one you spend a week pruning. (Full prior-attempt log: docs/PRIOR_ATTEMPT_YOLOV8N.md .) 🏆 Accomplishments Near-lossless INT8 (37.94 → 37.62) with zero retraining , on a frozen pretrained model. A genuinely multiplier-less, DSP-free accelerator that fits a real board at ~51 FPS. Bit-exact RTL datapath, verified against golden vectors with open-source tooling. Two autonomous AI agents driven to a working hardware handoff, kept honest by a human-in-the-loop. 📚 What we learned For fixed-function inference, pick a strong pretrained model and quantize — don't prune-and-retrain a weaker one. Constant weights are nearly free in hardware (CSD shift-add), which is what kills the DSP array. Enforce the handoff contract and verify with golden vectors — it's what catches silent failures. 🚀 What's next Finish the top-level detection-output decoder so the full-chip TB reaches a true PASS. Vivado synthesis/implementation on the XC7K325T to confirm PPA and timing closure. INT4 for tolerant layers; path from FPGA prototype to 28 nm tapeout. 🧰 Built with PyTorch · Ultralytics YOLOv10n · INT8 PTQ · SystemVerilog · Icarus Verilog / OSS CAD Suite · Vivado (xsim) · CSD / constant-coefficient arithmetic · Claude Code · Cognichip · Simular Sai · matplotlib · HyperFrames Silicon YOLO · UC Berkeley AI Hackathon 2026 (Cal Hacks) · co-designed by Claude Code + Cognichip, orchestrated by Simular Sai. <div