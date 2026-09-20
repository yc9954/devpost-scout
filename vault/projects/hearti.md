---
slug: "hearti"
url: "https://devpost.com/software/hearti"
title: "Hearti"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 977
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Hearti

> Simplifying congenital heart disease diagnosing, and treatment planning, and medical explanations for doctors and patients using computer vision, machine learning, VLMs, and more.

[Devpost](https://devpost.com/software/hearti) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** elevenlabs, fastapi, lumaai, meta-quest, next.js, numpy, nvidia, plotly, python, pytorch, react.js, tailwindcss, typescript, vespaai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hearti

## Body

Inspiration Congenital heart disease (CHD) is the most common birth defect in the United States, and thanks to advances in medicine, more children with CHD are surviving into adulthood. But with this improved survival comes a lifelong need for careful monitoring - as symptoms can change over time. Recognizing this challenge, we set out to build an AI-powered web application that helps both doctors and patients navigate the complexities of CHD. Our vision is simple: provide a tool that offers clear, reliable insights for global healthcare professionals and their patients while ensuring that patients receive a smooth transition into their medical journey. What it does Interactive 3D model of the input 2D heart. Instead of relying on flat 2D images, users can explore a fully interactive 3D representation of the heart. This provides doctors and patients with a clearer, more intuitive understanding of the condition. Multi-classification of CHD categories. The model identifies the most likely congenital heart disease (CHD) categories based on the uploaded scan, helping users understand potential diagnoses. Severity Classification. Users can also view how serious their CHD symptoms are. Model Confidence . We understand that AI may not always be correct, so a confidence score is included in the web application to guide a doctor’s conclusion with the AI findings. Feedback Form. For doctors, we have a space for them to accept or reject the model’s findings and explain their reasonings. This will help better fine-tune the model and ensure continuous improvement in its accuracy and reliability for diagnosing CHD conditions. AI Voice Chat. Guided by the previous datapoints, the AI voice chat is ready to discuss with the user any questions they have about the model's output and reasoning. Custom Heart Segmentation Model Currently, CMRI segmentation is performed manually to ensure accuracy. To automate this process, we developed a custom segmentation model trained on an NVIDIA A100 GPU using Brev Compute. While the model requires additional data and refinement for full accuracy, it successfully identified regions of interest despite the limited training dataset. Our architecture is specifically designed for cardiac imaging, labeling 3D volumes into eight major heart structures (four chambers and four arteries/veins). With further data and training, we aim to eliminate the need for manual segmentation in the pipeline. How we built it Surface Intensity and Segmented Heart Models Combining density and resonance information from the CMRI and the segmentation boundaries, we built an algorithm that can map and shade the volume of the heart based on the intensity of the MRI scan. This algorithm removes the background, carefully maps MRI data to volumes of the heart. This ensures that we do not impart any unwanted artifacts or information, an integral safety feature for this application. In addition to mapping MRI intensity, we also implemented an algorithm that generates smooth meshes using image processing techniques to provide an easy-to-read interpretation of the heart’s many shapes and volumes, without focusing too much on the color of the MRI data. We realized that all of this data can take quite a bit of memory to render, so we created optimized models that prioritize surfaces over volume, use sparse views to provide a lightweight model, and have the ability to select which specific major volumes of the heart you would like to view at a time. Embedding similarity using VespaAI We converted our data into vector embeddings paired with CHD labels and leveraged VespaAI to run precise, rapid queries. By using an angular metric, we account for both the direction and magnitude of our high-dimensional data. Web App Tech Stack For the frontend and backend, we used FastAPI, React.js, Next.js, Typescript, and TailwindCSS. Challenges we ran into While the dataset we found online was extremely useful and new, it was very limited (59 hearts only). To train a truly accurate model, we need a much larger sample size. Accomplishments that we're proud of -We successfully built and rendered 3D representations of 2D heart CMRI scans. Besides looking extremely cool, it is both new and valuable for the ways in which we treat people with CHD . - Optimized the models to prioritize surface pixels, smooth representations, and segment-specific views to make them more accessible across devices and browsers. -We built a web-based AI agent that can not only predict a user’s CHD conditions but can also act as a source of medical information for decades . If inputted with enough patient data, it can even more effectively provide accurate information that doctors can approve. What we learned We had a lot of ideas for this project, so we needed to quickly define what was most relevant and useful for our target audience (not what sounded the coolest). We moved quickly from talking with each other frequently and truly as a team. Some technical highlights: learned how to process research/medical data into more intricate + interpretable visualizations that capture features of the heart while minimizing artifacts, learned about different metrics to assess how correlated 2 embeddings are, and learned how to learn quickly using VespaAI’s querying functionality. What's next for Hearti While building Hearti, we considering incorporating AI-style transfer to turn the MRI data insights into realistic textures of real heart tissue. While exciting, this has a lot of challenges that have to be approached carefully because hallucinations can have consequences. Allowing Hearti to take advantage of a greater range of medical imaging techniques and scans. It would be great if we could upload a full-body or chest MRI and have Hearti extract the important regions and use our model to create stunning visuals of the heart. Incorporating time series data would be interesting because it would allow us to make use of our optimized models to create 4D reconstructions of the heart. We aim to expand our custom segmentation model’s capabilities by processing more heart scans directly and enhancing automation in cardiac imaging. <div