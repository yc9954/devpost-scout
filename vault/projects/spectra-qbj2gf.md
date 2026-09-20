---
slug: "spectra-qbj2gf"
url: "https://devpost.com/software/spectra-qbj2gf"
title: "SPECTRA"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 694
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# SPECTRA

> Turning iPhone's $25 LiDAR into industrial-grade dense depth maps. On-device, real-time, no cloud.

[Devpost](https://devpost.com/software/spectra-qbj2gf) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[transportation]]
**user** [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, fastapi, gx10, html, javascript, python, pytorch, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spectra

## Body

SPECTRANet View Demo View Inspiration Depth perception is the bottleneck for almost every embodied AI system — robots, AR headsets, accessibility tools, autonomous vehicles. And yet the depth-sensor market is bizarrely bimodal: an industrial Velodyne or Ouster will run you $8,000–$75,000, while the solid-state LiDAR Apple ships in every iPhone Pro since 2020 is $3–$25 in component cost. Same physics, three orders of magnitude in price. The catch is that the iPhone's depth output is sparse — a 192×256 map with a per-pixel confidence flag — and at full camera resolution it looks like a smear. The hardware gap closed years ago; the software gap never did. Plain bicubic upsampling gets you to camera resolution but ignores the RGB image entirely and bleeds across object boundaries, missing exactly the thin obstacles (chair legs, wires, pet ears) that matter most for robotics. We wanted to write the missing software layer: a model small enough to ship on-device, that takes cheap consumer LiDAR + RGB and produces a dense metric depth map you can actually plan a path on. What it does SPECTRA turns the iPhone Pro's sparse 192×256 LiDAR signal into a dense 768×1024 metric depth map, in real time, on-device. It has two halves: SPECTRANet — an RGB-guided depth upsampler. It takes the camera frame, the raw LiDAR depth, and the per-pixel confidence mask, and predicts a sharpening residual on top of a bicubic baseline. The output is metrically faithful but follows real surface boundaries instead of smearing across them. SPECTRALive — a SwiftUI/ARKit iOS app with three modes: Live Depth (raw LiDAR colormap overlay), SPECTRANet (our enhanced depth, on-device via CoreML or remote via an ASUS Ascent GX10 server), and Demo (A/B side-by-side). You can capture and share RGB+depth composites straight from the shutter. How we built it The model. A RGBGuidedDepthUpsampler (SPECTRANet/spectranet/model.py) — ImageNet-pretrained MobileNetV2 RGB encoder with feature taps at strides 2/4/8/16, a parallel lightweight depth+confidence encoder at strides 1/2/4/8/16, and a decoder that bilinearly upsamples and concatenates RGB+depth features at every scale. Training. ARKitScenes upsampling split (Faro laser scans as ground truth), trained on the ASUS Ascent GX10 edge GPU. Deployment. PyTorch checkpoint → fp16 CoreML .mlpackage (~2 MB) loaded on iOS through ZeticMLange. A FastAPI server.py serves the GX10 backend. App. SwiftUI + ARKit, processing each ARFrame at 15 Hz with vDSP-accelerated normalization. Challenges we ran into Coordinate systems. ARKit's depth map is rotated relative to the RGB frame depending on device orientation; the confidence mask is yet another grid. Aligning all four modalities (1440×1920 RGB, 192×256 depth, 192×256 confidence, 1440×1920 ground truth) to a common 768×1024 working resolution took longer than the model itself. On-device size. CoreML conversion broke repeatedly on MobileNetV2 ops. We spent hours tracing, then re-wrote a few layers to be CoreML-friendly to land at 2 MB fp16. Two backends, one app. Toggling between on-device Zetic and the remote GX10 server without UI flicker required careful state management in SPECTRANetProcessor. Accomplishments that we're proud of A 2 MB depth model that runs on a phone and visibly beats Apple's bicubic baseline on edges — without sacrificing metric accuracy. The Demo mode flip view, where you can A/B the same frame between raw LiDAR and SPECTRANet, makes the improvement obvious to non-technical viewers in under a second. A clean two-backend architecture that lets the same app run fully offline or offload to an edge GPU on the local network. What we learned Edge GPUs like the GX10 are real. Training a non-trivial vision model outside a datacenter is now genuinely practical, and the same checkpoint deploys to phones unchanged. Hackathon scope discipline matters: we cut three "nice to have" modes to ship the three that worked. What's next for SPECTRA Temporal consistency. Right now each frame is upsampled independently, which causes subtle flicker. A lightweight recurrent or optical-flow-warped prior should smooth this out without sacrificing the on-device budget. Outdoor + long-range. ARKitScenes is indoor-only; we want to fine-tune on outdoor LiDAR datasets so SPECTRA works for AR navigation and accessibility outside. Mesh export. Combine successive dense depth maps with ARKit's pose into a real-time TSDF mesh — turning a phone into a handheld 3D scanner. <div