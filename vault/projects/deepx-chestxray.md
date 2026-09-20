---
slug: "deepx-chestxray"
url: "https://devpost.com/software/deepx-chestxray"
title: "DeepX-ChestXRay"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 442
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# DeepX-ChestXRay

> DeepX is an AI-powered diagnostic tool that analyzes chest X-ray images to detect pneumonia and generate explainable visualizations to support medical research and education.

[Devpost](https://devpost.com/software/deepx-chestxray) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]]
**substrate** [[geospatial]] [[video_visual]]

**stack** deep, gradcam++, gradients, integrated, keras, learning, machine, numpy, opencv, python, streamlit, tensorflow, tf-keras-vis

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- future improvements

## Body

DeepX Diagnostic System Explainability Diagnosis Result Inspiration Medical imaging plays a crucial role in diagnosing respiratory diseases such as pneumonia. However, analyzing chest X-ray images requires expertise and time. I was inspired to explore how Artificial Intelligence could assist in this process by automatically analyzing medical images and highlighting important regions that influence the model's decision. The goal of this project was to build an AI-powered system that can analyze chest X-ray images and provide explainable predictions to support research and educational exploration of AI in healthcare. What it does DeepX-ChestXray is an AI-powered web application that analyzes chest X-ray images and predicts whether the image indicates normal lungs or pneumonia . The system also generates explainable AI visualizations that highlight the regions of the image that most influenced the model’s decision. Key capabilities include: Chest X-ray classification using deep learning Probability-based prediction results Explainable AI visualizations using GradCAM++ and Integrated Gradients Interactive web interface for real-time image analysis This allows users to better understand how deep learning models interpret medical images. How I built it The system was developed using Python and TensorFlow for building and running the deep learning model. The workflow includes: Data preprocessing Chest X-ray images are resized and normalized before being fed into the neural network. Deep Learning Model A convolutional neural network (CNN) was trained to classify X-ray images into normal or pneumonia categories. Explainable AI Integration Techniques such as GradCAM++ and Integrated Gradients were used to generate heatmaps highlighting the most important regions influencing the prediction. Web Application The model was deployed through a Streamlit web interface that allows users to upload X-ray images and receive real-time predictions with visual explanations. Challenges I ran into One of the main challenges was integrating explainable AI techniques with the trained model in a way that generates meaningful visualizations. Handling image preprocessing and ensuring compatibility between TensorFlow models and visualization libraries also required careful debugging. Additionally, optimizing the user interface to make the system easy to use while displaying complex outputs like heatmaps was another challenge. What I learned Through this project I learned: How deep learning models are applied to medical image classification How explainable AI techniques help interpret model predictions How to deploy machine learning models in an interactive web application using Streamlit How to integrate visualization tools such as GradCAM++ and saliency maps for model interpretability This project strengthened my understanding of AI deployment, explainable AI, and practical machine learning workflows . Future improvements Future enhancements could include: Multi-class disease detection (e.g., tuberculosis, lung opacity) Support for medical DICOM image formats Improved model accuracy using transfer learning architectures Clinical report generation based on predictions <div