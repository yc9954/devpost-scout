---
slug: "adf-js2a0i"
url: "https://devpost.com/software/adf-js2a0i"
title: "DermRX: AI-Powered Skin Cancer Detection Assistant"
hackathon: "Predictive AI In Healthcare with FHIR®"
organization: "Darena Solutions"
winner: true
words: 555
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/video_visual"
---

# DermRX: AI-Powered Skin Cancer Detection Assistant

> DermRX integrates with MeldRX to deliver AI-driven skin lesion analysis, real-time alerts, and seamless EHR access, enabling doctors for faster, smarter skin cancer detection. 🚀

[Devpost](https://devpost.com/software/adf-js2a0i) · hackathon [[Predictive AI In Healthcare with FHIR-]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[video_visual]]

**stack** deep-learning, opencv, python, transformer, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dermrx: ai-powered skin cancer detection for smarter care

## Body

DermRX – AI-Powered Skin Cancer Lesion Detection Inspiration Skin cancer is the most common form of cancer, with approximately 9,500 new cases diagnosed daily in United States alone. When detected early, it has a 99% five-year survival rate, highlighting the critical need for timely diagnosis. Additionally, skin conditions account for 30% of primary care visits, yet most GPs lack specialized dermatology training. Long wait times for dermatologist appointments often lead to delayed diagnoses, increasing patient risk. Our inspiration stems from bridging this gap by providing an AI-powered assistant that empowers GPs to make informed decisions quickly and efficiently, improving early detection and patient outcomes. What It Does Seamlessly integrates with MeldRX via SMART on FHIR standards with both CDS Hooks & EHR Launch. Uses AI to analyze and detect suspicious skin lesions in uploaded images Provides risk classification (high, medium, low) with color-coded alerts Enables comparison of historical images for tracking lesion evolution Allows manual refinement of AI detections for enhanced accuracy Supports both EHR-integrated and standalone quick analysis options Facilitates easy follow-up scheduling for at-risk patients How We Built It Frontend: Developed using Vite and React for an optimized, responsive interface. Backend: Implemented with Python, utilizing OpenCV for precise image processing and lesion boundary detection alongside fine-tuned Google Vi sion T ransformers for multi-class lesion classification. The classification model has a training accuracy 96.14% and a validation accuracy of 96.95%. Integration: SMART on FHIR for seamless interaction with MeldRX and CDS Hooks for proactive clinical decision support Challenges We Ran Into Images captured under different lighting conditions, backgrounds, camera qualities, and angles posed a significant challenge in ensuring consistent and accurate lesion bounding box detection. Learning curve for implementing seamless integration with MeldRX. Optimizing real-time analysis for quick responses in a clinical setting Ensuring a user-friendly experience for non-technical healthcare professionals Training skin lesion classification models and improving their accuracy. Accomplishments That We're Proud Of Effective MeldRX Integration: We successfully implemented SMART on FHIR, allowing our AI tool to seamlessly interact with EHR systems while maintaining strict data privacy and security. User-Centric Workflow Design: Designed an intuitive interface that allows GPs to review, refine, and compare lesion analyses effortlessly, ensuring that AI augments rather than replaces clinical judgment. Technical Architecture: We developed a modular, microservices-based architecture that allows for seamless extension to additional dermatological conditions beyond melanoma. Explored training our own skin lesion classification model using an ensemble of CNN and Tree Based models (LightGBM & XGBoost) with good baseline accuracies. What We Learned The critical role of AI in augmenting, rather than replacing, clinical expertise Best practices for integrating AI-driven decision support tools within existing EHR workflows The importance of UX in healthcare applications to ensure adoption by medical professionals What's Next for DermRX: AI-Powered Skin Cancer Detection for Smarter Care Further AI model refinement to improve accuracy and reduce bias Expansion to detect other dermatological conditions beyond skin cancer Development of a mobile-friendly version for telemedicine applications Exploring partnerships with healthcare institutions for wider adoption Add a feedback loop to improve diagnosis and identify bias in model classification DermRX represents a transformative approach to dermatological care, combining state-of-the-art AI with thoughtful clinical workflow integration. By empowering primary care physicians with specialized analytical capabilities, we aim to democratize access to expert-level dermatological assessment, ultimately improving early detection rates and patient outcomes worldwide. <div