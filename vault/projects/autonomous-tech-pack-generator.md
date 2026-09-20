---
slug: "autonomous-tech-pack-generator"
url: "https://devpost.com/software/autonomous-tech-pack-generator"
title: "Autonomous Tech Pack Generator"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 218
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Autonomous Tech Pack Generator

> Designed and developed an AI agent deeply integrated with the laptop operating system to autonomously devise innovative tech packs based on user input regarding patterns, designs, colors.

[Devpost](https://devpost.com/software/autonomous-tech-pack-generator) · hackathon [[Frostbyte Hackathon]]

## Facets

  <sub>weak: realtime_stream</sub>
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** contolnet, diffusers, keras, lora, python, scipy, seaborn, tokenization

## Body

#Inspiration- The project seeks to solve the slow "Sketch-to-Manufacturer" cycle by allowing designers to iterate on technical flats using text prompts. #Structure and Working- Data Pipeline: The system follows the notebook's structure of Preprocessing Images (resizing to 512x512 and normalizing pixels to a [-1, 1] range) and Assembling Text Datasets containing descriptive prompts. Textual Inversion: A unique placeholder_token (such as ) is initialized and added to the model’s vocabulary to represent the specific garment style. Accomplishments- Successfully generated 2D technical flats that maintain structural consistency while varying colors (VIBGYOR) and patterns (checkered, geometric) and through parametric scaling, achieved visual modulation of garment dimensions, such as "chest width," purely through text-based prompt engineering. What we learned- Precision Matters: Technical drawings require higher fidelity in "Latent Space" than artistic images to ensure lines are straight and measurements appear proportional. Optimizer Stability: Using an Adam optimizer with a Cosine learning rate is critical for preventing the model from "forgetting" general shirt structures during training. What's next for • Gen-AI Tech Pack Generator- a)Extending the 2D tech pack generation into 3D cloth simulations for virtual fitting. b)Developing a multi-modal agent that generates the Bill of Materials (text-based list of fabrics/buttons) simultaneously with the technical image. c)Building an interface for designers to "tweak" specific seams or stitches in real-time using ControlNet guidance. <div