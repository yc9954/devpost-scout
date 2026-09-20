---
slug: "bloom-ml0zi8"
url: "https://devpost.com/software/bloom-ml0zi8"
title: "Bloom"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 653
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Bloom

> Data-Driven Decisions for a Food-Secure Tomorrow

[Devpost](https://devpost.com/software/bloom-ml0zi8) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[developer_tools]]
**user** [[developer]] [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chart.js, css3, fastapi, git, google-gemini-api, html5, hugging-face, javascript, keras, python, render, tensorflow, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bloom

## Body

Inspiration The spark for Bloom came from an unlikely place, I read about how hedge funds use satellite imagery to count shadows cast by floating lids on oil storage tanks, estimating global supply reserves before official reports are released. It hit me that Why is this "Eye in the Sky" technology reserved for profit? In World, price crashes often happen because farmers blindly plant what was profitable last year, leading to massive oversupply. So I realized we could apply that same logic using orbital imagery to calculate ground truth to solve a human problem of Food Security. Bloom bridges the gap, bringing high-tech market intelligence to the Indian agricultural sector. What it does Bloom operates as a proactive Agricultural Advisory System designed to secure farmer profitability by aligning planting decisions with real-time market demand. By Analyzing Satellite Imagery to track exactly what is being grown across the region, the platform identifies potential oversupply risks ("saturation zones") before seeds are even sown. It then correlates this "Ground Truth" data with market needs to generate precise recommendations , guiding farmers away from crowded crops and towards high-demand opportunities . This ensures that every harvest meets an actual buyer, preventing price crashes and guaranteeing that farmers grow for profit, not just for yield . How we built it Custom Deep Learning Model : I trained a MobileNetV2 Convolutional Neural Network (CNN) using TensorFlow and Keras to classify aerial imagery of crops. The model is hosted on Hugging Face and downloaded dynamically by the server to optimize performance. FastAPI Backend (Render) : I built a robust REST API using Python FastAPI to handle image inference and aggregate regional supply statistics. It runs on Render and uses a custom "Lazy Loading" algorithm to process datasets without overwhelming server memory. Interactive Dashboard (Vercel) : The frontend is built with Vanilla HTML/JS and Chart.js to visualize real-time market saturation. It is deployed on Vercel for global, low-latency access. RAG Advisory System : I integrated the Google Gemini API to create a Retrieval-Augmented Generation system. The app feeds live JSON market data into the LLM as context, allowing the AI to generate mathematically grounded planting advice based on current supply levels. Challenges we ran into Hardware Limitations : Training a complex deep learning model on a standard laptop without a GPU was a major bottleneck, forcing us to prioritize efficiency over raw power. Dataset Scarcity : Manually curating and labeling thousands of satellite images for specific crops like Sugarcane in such a short timeframe was an exhausting manual process. Cloud Constraints : Deploying a heavy TensorFlow model to Render’s free tier caused immediate RAM timeouts. Integration : Debugging persistent CORS errors between our secure Vercel frontend and the public Python API consumed valuable development hours. Accomplishments that we're proud of Zero-Cost Engineering : Optimizing a heavy TensorFlow model to run smoothly on free-tier cloud hosting without crashing. First End-to-End AI Deployment : Taking a deep learning concept from a local notebook to a live, globally accessible web app for the very first time. What we learned Architected a full-stack AI solution utilizing FastAPI for a high-performance, asynchronous backend on Render, implementing lazyloading data pipelines to optimize cloud memory usage. The core intelligence is driven by a custom Convolutional Neural Network (CNN) built with TensorFlow/Keras, leveraging Transfer Learning (MobileNetV2) for efficient inference and hosted on Hugging Face for modular model versioning. The system features a Retrieval-Augmented Generation (RAG) pipeline powered by Google Gemini API, which synthesizes live telemetry into context-aware advice, all visualized through a responsive Chart.js dashboard deployed globally via Vercel's CDN. What's next for Bloom Taking Bloom Open Source, inviting developers worldwide to contribute to the future of food security. Our roadmap includes scaling the dataset to cover diverse regional crops, integrating drone telemetry for hyper-local pest detection, and launching an offline-first mobile app to ensure that every farmer regardless of internet connectivity has access to vital market intelligence. <div