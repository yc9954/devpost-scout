---
slug: "pulmonai-jefryq"
url: "https://devpost.com/software/pulmonai-jefryq"
title: "PulmonAI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 594
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# PulmonAI

> Helping doctors diagnose lung conditions faster, smarter, and anywhere!

[Devpost](https://devpost.com/software/pulmonai-jefryq) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** base64imagehandling, fastapi, gradcam, jspdf, materialui, python, pytorch, react.js, torchxrayvision, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pulmonai

## Body

Inspiration Chest X-rays are one of the most common tools used to detect lung diseases, but interpreting them correctly takes years of training. In rural or under-resourced areas, there may not be a radiologist available. I wanted to build an accessible tool that could help give doctors a second opinion, and help patients get care faster, especially where medical staff are overworked or equipment is limited. What it does PulmonAI is a web-based application that allows users to upload a chest X-ray image and receive AI-generated predictions for potential lung conditions. The app displays these predictions in a ranked, color-coded list that indicates risk level (high, medium, or low) to help prioritize clinical review. It also generates a heatmap highlighting suspicious regions of the X-ray to improve interpretability. Additionally, PulmonAI creates a structured diagnostic report summarizing the predictions and recommended next steps, which can be copied or downloaded for easy sharing. How we built it Frontend: React + Material UI for sleek dark mode UI with custom theming Backend: Python + FastAPI for quick response and image handling AI Model: Trained using PyTorch on chest X-ray datasets, called TorchvisionXrays, to classify lung conditions Visualization: Grad-CAM and saliency maps to generate attention-based heatmaps PDF Report: Generated on the frontend using jsPDF Challenges we ran into One of the biggest challenges I faced was finding and properly integrating an AI model that was not only affordable but also capable of accurately scanning chest X-rays to identify and predict conditions within the lung. Additionally, getting the heatmap overlays to work and align correctly with the original X-ray image required careful tuning and testing. Styling the user interface to look clean and modern without relying on external libraries like Tailwind also posed a challenge, so I focused on using Material UI’s theming and components to achieve a professional and cohesive design. Accomplishments that we're proud of I am really proud of creating a medical app which not only produces predictions of what conditions might be in the lung from the xray, but also the impact this app serves. I am proud of creating a tool which can not only serve as a second opinion for doctors when scanning xrays, but mainly that this app can help countless doctors in poor and rural areas who don't have proper equipment to scann xrays of lungs. With this app, they have a chance to identify any lethal conditions in the lung early on, which could save someone's life. What we learned This project taught me how to connect a deep learning backend to a modern React frontend and deliver a complete AI product. I learned how to use Grad-CAM to visualize what a CNN is seeing, which is critical for trust in medical AI. I also learned a lot about PDF generation with jsPDF, Material UI theming, and the importance of good UX in healthcare apps. Most importantly, I gained an appreciation for explainable AI and its role in building trust with clinicians. What's next for PulmonAI Next, I plan to deploy the AI model on a cloud GPU server to make predictions faster and scalable. I want to add multilingual support for reports to increase accessibility. Other goals include integrating user feedback or manual corrections to improve model performance, supporting additional imaging types like CT scans, and ultimately connecting with hospital systems or EHRs to pilot this in real clinics. I also hope to find and fine-tune an even better deep learning model than I am currently using right now, to get even more accurate predictions for the conditions. <div