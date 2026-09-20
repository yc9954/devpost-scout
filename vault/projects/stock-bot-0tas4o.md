---
slug: "stock-bot-0tas4o"
url: "https://devpost.com/software/stock-bot-0tas4o"
title: "RDKxPaddle-OCR Data Curation Platform"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 718
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# RDKxPaddle-OCR Data Curation Platform

> Curate OCR datasets on edge effortlessly

[Devpost](https://devpost.com/software/stock-bot-0tas4o) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** paddle-ocr, python, rdx

## How they structured the write-up

- inspiration
- problem statement
- why this is important
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rdkxpaddle-ocr data curation platform

## Body

RDKxPaddle-OCR Data Curation Platform Original Data - Medicine container images Synthesized dataset Curated dataset ready for Paddle-OCR finetuning Architecture Inspiration OCR technology powers critical workflows in industries like healthcare, finance, and logistics. From reading prescriptions to processing invoices, OCR is everywhere. But when you need OCR to work for a specific domain—say medical codes or lab reports—the generic models often fail. The solution is fine-tuning, but fine-tuning starts with data. And that’s where the real pain begins. Developers spend hours manually cropping text regions, labeling them, and filtering out poor-quality samples. This slows down innovation and makes edge AI projects harder to deploy. We were inspired to solve this bottleneck because we believe developers should spend time building models, not cleaning data. Our goal was to create a platform that automates dataset preparation so teams can move faster and deliver reliable OCR solutions. Problem Statement High-quality data is the foundation of accurate OCR models, but creating that data is slow, manual, and error-prone. Today, developers must: Extract text regions from raw images. Label each crop correctly. Check image quality for blur, brightness, and clarity. Format everything to match training scripts. This process takes days and introduces inconsistencies. Without clean data, fine-tuning fails or produces unreliable models. For edge AI projects, the challenge is even bigger because compute and time are limited. There’s no easy way to curate datasets based on quality metrics like blur, brightness, or confidence. This gap delays deployment and increases costs Why this is important Speeds up development: Automating synthesis and curation saves hours of manual effort. Improves accuracy: Clean, curated datasets lead to better fine-tuned models. Reduces errors: Consistent labeling and quality checks prevent bad data from entering training. Edge-ready: Optimized for environments where compute and time are scarce. Flexible: Works for fine-tuning or building validation engines, giving developers options. How I built it We started with the RDK-X5 robotics development kit as our edge computing platform because it’s optimized for AI workloads and gives us real-world constraints like limited memory and processing power. The first step was integrating PaddleOCR’s detection model to automatically identify text regions in raw medical images. Instead of manually cropping thousands of samples, the detection model extracts bounding boxes for each text instance, and we use these coordinates to generate clean, single-text crops. Once we had the crops, we built a custom labeling algorithm that calculates key quality metrics for every image—blur using variance of Laplacian, brightness using pixel intensity histograms, and confidence scores from the recognition model. These metrics are stored in a structured CSV file, creating a transparent view of dataset quality. The next challenge was curation. We designed an interactive user interface that allows developers to filter and select images based on these metrics. For example, they can choose blur values between 100 and 300 or confidence below 0.9. This dynamic filtering ensures that only high-quality samples make it into the final dataset. The curated dataset is then exported along with a label file formatted exactly as PaddleOCR expects, so developers can plug it directly into the training scripts without additional preprocessing. Throughout the build, we focused on making the pipeline lightweight and edge-friendly. All processing happens locally on the RDK-X5, and the UI is optimized for quick filtering and dataset generation. The result is a platform that automates synthesis, labeling, and curation—tasks that traditionally take hours—into a process that runs in minutes. Challenges I ran into Computing blur and brightness efficiently on large batches without slowing the pipeline required careful optimization. Designing a responsive UI for dynamic filtering on thousands of samples also pushed us to implement lightweight rendering and smart data handling. Accomplishments that I'm proud of We built a fully functional pipeline that goes from raw images to a curated dataset in minutes. The platform automates what used to take hours of manual effort. We also captured a complete demo video showing the process end-to-end. What I learned High-quality data is the foundation of reliable OCR models. Even when fine-tuning isn’t possible, curated datasets can power validation engines and improve OCR reliability. We also learned how critical resource optimization is for edge AI projects. What's next for RDKxPaddle-OCR Data Curation Platform We plan to add: Lightweight fine-tuning workflows optimized for edge devices. A post-processing validation engine that improves OCR accuracy without retraining. <div