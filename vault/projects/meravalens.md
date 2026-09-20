---
slug: "meravalens"
url: "https://devpost.com/software/meravalens"
title: "MeravaLens"
hackathon: "LaunchHacks IV"
organization: "LaunchHacks"
winner: true
words: 485
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MeravaLens

> Turning satellite imagery into actionable Earth insights.

[Devpost](https://devpost.com/software/meravalens) · hackathon [[LaunchHacks IV]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]]
**user** [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** django, fastapi, huggingface, mui, react, three.js, torch

## How they structured the write-up

- 💡 inspiration
- 🚀 what it does
- 🛠️ how we built it
- 🧗 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔭 what’s next for meravalens

## Body

💡 Inspiration Every day, satellites capture terabytes of imagery covering every inch of Earth’s surface — but turning that raw data into meaningful, actionable insights remains a challenge. We built MeravaLens to change that. Inspired by the growing urgency of urban expansion, environmental degradation, and the need for real-time geospatial intelligence, we set out to build a platform that empowers researchers, planners, and decision-makers to understand the land — pixel by pixel. 🚀 What It Does MeravaLens is an AI-powered platform that transforms satellite imagery into rich, structured geospatial insights. It combines: 🛰️ Open-access satellite data 🌦️ Environmental APIs (weather + air pollution) 🤖 A custom-built ResUNet for semantic segmentation 🧠 Large Language Models (LLaMA 3) for summarizing land use With this pipeline, users can: Retrieve satellite imagery for any global coordinate Segment the landscape into classes (e.g. buildings, roads, water, forest, agriculture) Add live environmental context Generate easy-to-understand textual summaries of land use and conditions 🛠️ How We Built It Frontend: React + MUI for an intuitive, interactive UI Backend: Django & FastAPI power data access and model integration AI Models: ResUNet (custom) with pretrained ResNet-18 encoder for segmentation Trained on the LoveDA dataset for robust urban/rural generalization Classification head for urban vs rural domain prediction APIs: Google Maps Static API for satellite imagery OpenWeatherMap & Air Pollution API for environmental data LLM Integration: Hugging Face’s Llama-3.3-70B-Instruct to generate human-readable insights from segmentation maps 🧗 Challenges We Ran Into Training a dual-task model (segmentation + classification) with stable gradients was tough — balancing the losses took iteration Ensuring consistent dimensions and skip connections when adapting UNet to a ResNet encoder required careful decoder design Integrating multiple data sources (imagery + weather + air quality) and syncing them spatially and temporally wasn’t trivial Turning raw segmentation into natural language summaries using an LLM required thoughtful prompt engineering 🏆 Accomplishments That We're Proud Of Built a full-stack, production-ready platform combining computer vision, environmental data, and LLMs Achieved strong urban-rural generalization on the LoveDA dataset Designed a custom decoder architecture to mirror ResNet skip connections — improving segmentation performance Seamlessly integrated LLM-generated summaries from structured pixel data 📚 What We Learned How to build a scalable deep learning pipeline for semantic segmentation in geospatial settings How to blend structured vision outputs with LLMs for multimodal understanding How model performance varies between urban and rural domains — and how datasets like LoveDA help bridge that gap The value of combining visual AI with environmental and textual intelligence for richer insights 🔭 What’s Next for MeravaLens 🌍 Launch a public demo that allows users to drop a pin and get full land + weather analysis 📦 Expand model support to temporal satellite data for change detection 🛰️ Integrate other datasets (Sentinel, Landsat, etc.) 🧠 Fine-tune the LLM summarization for domain-specific users like urban planners or ecologists ⚡ Optimize performance for faster real-time inference using quantized models and ONNX <div