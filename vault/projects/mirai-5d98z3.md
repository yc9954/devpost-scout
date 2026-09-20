---
slug: "mirai-5d98z3"
url: "https://devpost.com/software/mirai-5d98z3"
title: "Mira3D"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 343
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# Mira3D

> Turn your surroundings into immersive 3D scenes using AI-powered Gaussian splatting

[Devpost](https://devpost.com/software/mirai-5d98z3) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[video_visual]]

**stack** birefnet, brush, colmap, hpaistudio, mlflow, python, reactthreefiber, swagger

## How they structured the write-up

- inspiration
- what it does
- how it is built
- challenges i ran into
- what i learned
- what's next for mira3d

## Body

Inspiration We live in a 3D world, yet most of our digital interactions are still two-dimensional. Whether it's online shopping, memory capture, or education, we're often stuck with flat media. Mira3D was built to change that. By enabling users to turn short 2D videos into realistic, interactive 3D models, we make high-quality 3D content creation fast, local, and intuitive—without relying on the cloud. What it does Mira3D transforms 2D video footage into interactive 3D point clouds using a combination of AI-driven photogrammetry and real-time Gaussian splatting rendering. The platform operates entirely on local hardware through HP AI Studio, offering privacy, speed, and control. Key capabilities include: AI-based background removal (Birefnet) COLMAP-based 3D reconstruction with CUDA acceleration Real-time rendering with the Brush engine In-browser 3D model viewing and editing On-prem, secure pipeline execution with MLflow tracking and export How It is built Preprocessing : Background removal using Birefnet (ONNX) 3D Reconstruction : COLMAP with CUDA for Structure-from-Motion and Multi-View Stereo Rendering : Gaussian splatting via the Brush engine (Vulkan-based) Frontend : React with Three Fiber for the 3D interactive editor Deployment : MLflow and Swagger within HP AI Studio containers Persistence : Exported binaries and artifacts tracked using MLflow Challenges I ran into Integrating CUDA-enabled COLMAP within containerized HP AI Studio environments Ensuring Vulkan GPU support inside the container for hardware-accelerated rendering Managing VRAM and compute limits on mid-range GPUs Making binary dependencies persistent across container restarts Debugging gsplat compatibility issues with newer GPU architectures (Blackwell) What I learned How to deeply integrate MLflow for model/artifact tracking and UI deployments The trade-offs and practical limits of combining classical photogrammetry with neural rendering Containerization strategies for GPU-heavy workloads (Vulkan, CUDA, ONNXRuntime) The nuances of running low-level graphics APIs (like Vulkan) in remote and containerized environments What's next for Mira3D Texture generation from prompts using models like Trellis and Hunyuan Migration back to gsplat for faster CUDA-accelerated Gaussian splatting Advanced UI features for interactive editing of splats and model refinement Optimized low-VRAM workflows for wider hardware support Streamlined deployment via packaged binaries for non-technical users <div