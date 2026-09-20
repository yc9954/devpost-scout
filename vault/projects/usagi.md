---
slug: "usagi"
url: "https://devpost.com/software/usagi"
title: "Usagi AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 290
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "substrate/structured_db"
---

# Usagi AI

> 🚦 Usagi AI uses YOLO + OCR to detect helmetless riders and read number plates in real time, helping traffic authorities enforce rules, improve road safety, and reduce accidents.

[Devpost](https://devpost.com/software/usagi) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[transportation]]
**substrate** [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** googlecolab, gradio, labellmg, matplotlib, ocr, opencv, os, python, roboflow, yolo

## Body

testimage1 testimage3 Testimage2 testimage4 Inspiration Traffic accidents caused by riders without helmets claim thousands of lives every year. Manual monitoring is inefficient, and enforcement often misses violators. We wanted to build an AI-powered solution that not only detects these violations but also helps authorities respond quickly—saving time, resources, and most importantly, lives. What it does Usagi uses YOLOv8 to detect whether a rider is wearing a helmet. If not, it triggers OCR to capture and recognize the number plate. The system can work on live CCTV/dashcam feeds or recorded video, providing authorities with real-time violation reports. How we built it Created and annotated a custom dataset of helmet/no-helmet riders. Trained YOLOv8 for helmet detection. Integrated OCR for automatic number plate recognition. Built a pipeline that processes video streams → detects violations → extracts plate numbers → logs/report generation. Challenges we ran into Gathering diverse training data across lighting, weather, and traffic density conditions. Ensuring real-time detection without losing accuracy. Handling low-quality or tilted number plates with OCR. Synchronizing helmet detection and plate recognition into one smooth workflow. Accomplishments that we’re proud of Built a working prototype with strong detection accuracy. Achieved reliable OCR results even in challenging cases. Designed a scalable architecture that can be used city-wide. Developed a solution that can genuinely contribute to road safety. What we learned Advanced YOLOv8 training and optimization techniques. Practical OCR tuning for real-world conditions. The importance of dataset diversity and augmentation. How AI can be deployed beyond research—to solve impactful societal problems. What’s next for Usagi Integration with traffic authority databases for automated challans. Better OCR support for regional plate formats. Edge device deployment for faster, on-site detection. Expanding to detect other violations like triple riding, over speeding, or phone usage <div