---
slug: "cognipredict"
url: "https://devpost.com/software/cognipredict"
title: "CogniPredict"
hackathon: "Maximally Vibe-a-thon"
organization: "Maximally (https://maximally.in)"
winner: true
words: 646
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# CogniPredict

> CogniPredict uses deep learning to classify Alzheimer's disease severity from brain MRI scans with 99.3% accuracy, while providing visual explanations that clinicians can actually trust and understand

[Devpost](https://devpost.com/software/cognipredict) · hackathon [[Maximally Vibe-a-thon]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** efficientnetv2-s, git, hugging-face-spaces, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cognipredict

## Body

Architecture Prediction MC Dropout and Uncertainity Analysis Grad-CAM++ Visualisation AI Assistant Inspiration Honestly, this project started when I learned that Alzheimer's affects over 55 million people worldwide, and that number is expected to triple by 2050. What really hit me was talking to friends whose grandparents struggled with memory loss—the families often didn't catch it early because diagnosis is so tricky. I thought, "What if AI could help doctors spot the signs earlier, before it's too late?" But here's the thing: doctors won't trust a black box. They need to see why the AI thinks what it thinks. That's what pushed me to build something that's not just accurate, but actually explainable. What it does CogniPredict analyzes brain MRI scans and classifies them into four stages: Non-Demented (healthy) Very Mild Dementia (early warning signs) Mild Dementia (noticeable cognitive decline) Moderate Dementia (significant impairment) But it doesn't just give you a label—it shows you why. Using Grad-CAM++, it highlights which brain regions influenced the decision. With Monte Carlo Dropout, it tells you how confident it is (and when it's uncertain). And with LIME, it breaks down the image into superpixels to show exactly what mattered. It's like giving the AI a voice to explain itself. How we built it I started with the Kaggle "Best Alzheimer MRI Dataset" (11,519 images) and built everything in Python using PyTorch. The backbone is EfficientNetV2-S—a state-of-the-art architecture that's both powerful and efficient. I used transfer learning with a two-phase approach: first freezing the backbone to train the classifier head, then unfreezing for fine-tuning with a lower learning rate. For explainability, I implemented three complementary methods from scratch: Grad-CAM++ for spatial attention visualization MC Dropout (50 stochastic passes) for uncertainty quantification LIME for local interpretable explanations The whole thing is deployed on Hugging Face Spaces with a Gradio interface, so anyone can upload an MRI and get a prediction with explanations in seconds. Challenges we ran into Oh man, where do I start? Class imbalance was a nightmare initially—the model kept overfitting to the majority class. Solved it with stratified splits and label smoothing. Grad-CAM++ debugging took forever. The gradients kept vanishing because I was hooking into the wrong layer. Spent 3 hours realizing I needed register_full_backward_hook instead of the deprecated version. LIME was slow—like, really slow. Each explanation took 30+ seconds. Had to optimize the prediction function and reduce samples from 1000 to 500. Deployment headaches: Hugging Face kept timing out because the model was too large. Had to optimize memory usage and use lazy loading. Accomplishments that we're proud of 99.30% test accuracy with only a 0.44% generalization gap—the model actually generalizes! Built a complete explainability pipeline with three different methods that actually work together Created a live demo that anyone can use: huggingface.co/spaces/Imperiex-1911/cognipredict The combined explainability dashboard that shows Grad-CAM++, MC Dropout, and LIME all in one view—that visualization took a lot of work but it's worth it Wrote clean, documented code that I'm not embarrassed to share What we learned Transfer learning is incredibly powerful—you really don't need to train from scratch for medical imaging Explainability isn't just a nice-to-have; it fundamentally changes how you trust (or distrust) your model MC Dropout is surprisingly simple to implement but gives you so much insight into model uncertainty Deploying ML models is half the battle—building locally is easy, making it work in production is hard Documentation matters! Writing clear code comments saved me so many times when debugging. What's next for CogniPredict 3D MRI support: Right now we're using 2D slices, but volumetric analysis could capture more structural information Multi-center validation: Training on data from different hospitals/scanners to ensure real-world robustness Longitudinal tracking: Predicting disease progression over time, not just current state Mobile app: Making it accessible for preliminary screening in areas with limited specialist access Clinical trials: Partner with neurologists to validate the system in real diagnostic workflows <div