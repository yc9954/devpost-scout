---
slug: "osteoai-ai-based-osteoporosis-risk-detection"
url: "https://devpost.com/software/osteoai-ai-based-osteoporosis-risk-detection"
title: "OsteoAI: AI-Based Osteoporosis Risk Detection"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 539
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# OsteoAI: AI-Based Osteoporosis Risk Detection

> AI-powered osteoporosis screening using routine X-rays and patient data for affordable, early risk detection without expensive DEXA scans.

[Devpost](https://devpost.com/software/osteoai-ai-based-osteoporosis-risk-detection) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[structural_withholding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[elder_child_care]] [[health_clinical]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** cnns, deep-learning, efficientnetv2s, google-colab, grad-cam-explainable-ai, image-processing, jupyter-notebook, keras, matplotlib, numpy, opencv, pandas, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next for osteoai?
- use case & impact

## Body

Homepage Homepage Login page Doctor's Dashboard Risk Prediction Result of x-rays Result of x-rays Patient Records Chatbots Patient History Patient Dashboard Consultancy Appointment Booking Booking Confirmation Message consultants Call consultant Treatment cost Patient (Health Advice) Health advice for Patient OsteoAI: AI-Based Osteoporosis Risk Detection Inspiration Osteoporosis is a silent disease that often remains undetected until severe fractures occur, leading to reduced mobility, loss of independence, and long-term health complications, especially among elderly individuals. Millions of people in low-resource areas cannot access expensive DEXA scans for early diagnosis. We wanted to build an accessible and assistive healthcare solution that could use existing hospital X-ray infrastructure to enable affordable, early osteoporosis risk screening and help individuals maintain healthier, more independent lives. What It Does OsteoAI is an AI-powered osteoporosis risk screening system that analyzes routine hand/wrist X-ray images along with patient metadata such as age and gender. The system predicts osteoporosis risk levels and generates explainable AI heatmaps to help healthcare professionals understand the model’s predictions. By enabling early detection, OsteoAI supports preventive healthcare, reduces fracture risks, and improves accessibility to screening in underserved communities. How We Built It We developed OsteoAI using Python, TensorFlow, Keras, OpenCV, and Scikit-learn. The project uses a multi-modal deep learning architecture combining EfficientNetV2S for medical image analysis with patient metadata for improved prediction accuracy. We trained and fine-tuned the model on the RSNA Bone Age dataset using transfer learning, focal loss, and class balancing techniques. Explainable AI with Grad-CAM was integrated to make the predictions more transparent and clinically interpretable. Challenges We Faced One of the major challenges was handling severe class imbalance in medical datasets, where high-risk osteoporosis cases were limited. We addressed this using focal loss and balanced class weights. Another challenge was ensuring the AI system remained interpretable and accessible for healthcare professionals without AI expertise, which we solved using Grad-CAM visualization heatmaps. Managing large medical image datasets with limited GPU resources was also a significant optimization challenge. What We Learned Through OsteoAI, we gained practical experience in medical AI, deep learning optimization, explainable AI, and healthcare-focused problem solving. More importantly, we learned how assistive and inclusive technology can improve healthcare accessibility, support independent living, and create meaningful social impact for vulnerable populations. What's Next for OsteoAI? In the future, we aim to improve the model using advanced transformer architectures, validate it with real clinical datasets, and deploy it as a scalable assistive healthcare screening tool for hospitals, rural healthcare centers, and underserved communities. Use Case & Impact Target Audience Elderly individuals and postmenopausal women at high risk of osteoporosis Rural and low-resource healthcare centers lacking access to DEXA scans Hospitals, clinics, radiologists, and healthcare professionals Individuals requiring preventive bone health monitoring Real-World Applications Early osteoporosis risk screening using routine X-rays Preventive healthcare support to reduce fractures and mobility loss Assistive healthcare technology for improving independent living among elderly patients Affordable large-scale screening in underserved and rural communities AI-assisted clinical decision support for healthcare professionals Future Scalability Deployment as a cloud-based screening platform for hospitals and clinics Integration with PACS and existing radiology systems Expansion to detect additional bone-related conditions such as fractures and arthritis Multi-language support for broader accessibility in diverse regions Potential integration with telemedicine and remote healthcare platforms <div