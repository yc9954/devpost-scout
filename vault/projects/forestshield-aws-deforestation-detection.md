---
slug: "forestshield-aws-deforestation-detection"
url: "https://devpost.com/software/forestshield-aws-deforestation-detection"
title: "ForestShield: AWS Deforestation Detection"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 646
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ForestShield: AWS Deforestation Detection

> Serverless forest monitoring system using AWS Lambda, Sentinel-2, and SageMaker — tracks deforestation in real-time with zero manual effort.

[Devpost](https://devpost.com/software/forestshield-aws-deforestation-detection) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** amazon-dynamodb, amazon-elasticache, amazon-web-services, apprunner, java, lambda, nestjs, python, sagemaker, step-functions

## How they structured the write-up

- 🌲 inspiration
- ⚙️ what it does
- 🧱 how we built it
- 🧗 challenges we ran into
- 🏅 accomplishments we're proud of
- 📚 what we learned
- 🔭 what's next for forestshield
- 🚀 final thoughts

## Body

Portal Screenshot Deforestation Analysis Step Functions Flow Generated Report PDF by Lambda Overall Architecture 🌲 Inspiration Satellite monitoring of forests is often slow, manual, and reactive. We wanted to flip that — building a platform that makes forest surveillance automated , scalable , and real-time , powered by serverless infrastructure and modern ML. AWS Lambda gave us the perfect foundation: zero infrastructure, granular billing, and near-instant scalability. With tools like Lambda SnapStart , Step Functions , and SageMaker , we could build something that’s not just reactive — but predictive. That’s why we created ForestShield : a scientifically grounded, production-grade deforestation detection system that proves even complex geospatial ML pipelines can run entirely serverless. ⚙️ What it does ForestShield is a fully serverless platform for real-time vegetation monitoring, built on AWS Lambda and SnapStart. It processes Sentinel-2 imagery to compute NDVI indices, detect biomass changes using K-means clustering, and deliver live alerts — all without a single server. But it doesn’t stop there. ForestShield is designed to learn . As more regions are processed, it reuses and refines clustering models — reducing noise, increasing accuracy, and building a historical index of vegetation patterns. This evolving knowledge base can power predictive modeling , helping scientists forecast deforestation risk or evaluate recovery after conservation efforts. Core Flow: User defines a region and timeframe via the dashboard. API triggers a Lambda-orchestrated Step Functions workflow. Satellite imagery is fetched, streamed, and processed into NDVI maps. Lambda extracts feature vectors; SageMaker clusters them via K-means. Clustering results are visualized, and detailed PDF reports are emailed via SNS. All activity updates the live dashboard through WebSocket streams. 🧱 How we built it At its core, ForestShield runs entirely on AWS: Lambda : Orchestrates analysis, processes imagery, triggers ML pipelines. SnapStart (Java) : Accelerates ingestion functions down to ~200ms. Step Functions : Coordinates multi-step processing pipelines. SageMaker : Performs unsupervised clustering for deforestation detection. SNS + WebSocket Gateway : Powers real-time alerting and UI updates. NDVI is computed using the red and near-infrared bands: NDVI = \frac{(NIR - Red)}{(NIR + Red)} Each pixel becomes a 5D vector (NDVI, reflectance, geo). These vectors are clustered using K-means, with the number of clusters optimized using the Elbow Method. Clustering models are reused and gradually refined to reduce compute costs and improve long-term pattern recognition. 🧗 Challenges we ran into Cold Starts : Solved using Lambda SnapStart — no extra code required. Memory Constraints : Streamed large images from S3 and used parallel Lambdas to avoid hitting the 10GB limit. Cluster Optimization : Integrated the Elbow Method into Lambda to dynamically determine the ideal number of clusters. 🏅 Accomplishments we're proud of Delivered a 100% serverless ML platform with near-zero ops overhead Achieved sub-second startup for Java Lambdas via SnapStart Built a scalable clustering pipeline for 1M+ pixels/month under \$10 Automated full provisioning via CLI + CloudFormation Designed a system that improves accuracy over time and can generalize to new regions 📚 What we learned SnapStart is a serious unlock for latency-sensitive Java workloads Step Functions make even complex scientific pipelines maintainable and transparent Serverless doesn’t mean simplistic — it means smart design and stateless logic SageMaker + Lambda can power real-time geospatial analytics at scale 🔭 What's next for ForestShield Streaming ingestion via EventBridge for continuous satellite feeds Biome-aware ML tuning — different clustering thresholds based on regional ecology Model registry to track region-specific learning and improvements Predictive deforestation modeling to forecast risk and support early intervention 🚀 Final Thoughts ForestShield isn’t just detecting change — it’s learning from it . Every region it analyzes makes the system smarter, faster, and more accurate. These evolving models lay the foundation for real scientific insight: predictive deforestation maps, recovery analytics, and data-driven policy support. It’s fully serverless, ML-native, and battle-tested on real satellite data. This is ForestShield 🌳 — forest intelligence at the speed of Lambda. <div