---
slug: "synapseai"
url: "https://devpost.com/software/synapseai"
title: "SynapseAI"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1095
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SynapseAI

> Transforming Thoughts into Visual Expression - Empowering Minds Beyond Words

[Devpost](https://devpost.com/software/synapseai) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[accessibility]] [[health_clinical]]
  <sub>weak: developer_tools</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** chromadb, google-cloud, langchain, luma-ai, muse-sdk, numpy, openai-api, pandas, python, pytorch, scipy, tensorflow, terra-api, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for synapseai

## Body

Our veterans are twice as likely to develop PTSD compared to the rest of us, with 87.5% experiencing at least one traumatic event during their service. To make matters worse, nearly 20% have suffered traumatic brain injuries in the past two decades. These invisible wounds often leave them struggling to communicate, manage stress, or reintegrate into everyday life. When we think about pushing the frontiers of a soldier's productivity, we often focus on the battlefield—but what about catalyzing their transition back to civilian life post service? This identified pain point germinated SynapseAI, a groundbreaking system that bridges the gap between thought and expression for veterans who experience neurological disorders. Using a combination of brainwave sensors (Muse) and biometric data (Terra), SynapseAI transforms thoughts into vivid visual representations in real time. Our veterans face PTSD and TBI, hindering communication. SynapseAI uses brainwave sensors (Muse) and biometric data (Terra) to transform thoughts into vivid AI generated visuals, enabling expression in real time. Inspiration Driven by a shared passion for healthcare, our team sought to tackle this track. When further research was conducted, we had the shared consensus that there was a disproportionate level of emphasis on soldier’s productivity during service, but rarely on catalyzing their transition back to civilian life. Our veterans are twice as likely to develop PTSD compared to the rest of us, with 87.5% experiencing at least one traumatic event during their service. To make matters worse, nearly 20% have suffered traumatic brain injuries in the past two decades. These invisible wounds often leave them struggling to communicate, manage stress, or reintegrate into everyday life. Current rehabilitation methods have proven to be ineffective. Up to two-thirds of veterans still meet the diagnostic of PTSD post-treatment, and dropout from treatment ranges from 25 to 48%. A recurring pain point for those undergoing rehab is the inability to express themselves, which can lead to frustration, avoidance, and disengagement from rehab. Heightened stress levels is further exacerbated by cognitive impairments from conditions like Aphasia that make verbal communication difficult. This inspired us to innovate in the intersection of empowerment and expression. A tool that both empowers and catalyzes veterans to better express themselves and regulate their stress levels. Introducing, SynapseAI What it does SynapseAI transforms brain waves and biometric data into vivid visual representations in real time, enabling non-verbal communication and emotional expression for veterans with PTSD, TBI, or aphasia. Here's how it works: Pre-Flow: Veterans are equipped with a Muse EEG headband and a Terra-enabled wearable that sends stress level data. Brainwave patterns and biometric data are captured and transformed into embeddings using machine learning. These embeddings are stored in a vector database as "thought categories." User Flow: In real time, SynapseAI captures brainwave activity and stress levels. The system uses cosine similarity to match current brainwave patterns with stored embeddings. Based on the match, a multi-agent AI system (LangChain) expands, refines, and synthesizes a prompt, generating a video via Luma AI, dynamically modulated by the user’s stress levels. The result? Veterans can express thoughts and emotions visually, enabling communication and emotional regulation even under high stress. How we built it EEG Signal Processing → Processed EEG Brainwaves and extracted features using FFT, PSD, and Wavelet Transforms. Thought Embedding Model → Trained a CNN-based triplet loss model to create embeddings for thoughts based on 5 main categories. Doctor Helps Patient - Thoughts of care, empathy, concern; Sister argues with brother - Thoughts of conflict, frustration; Fire burns house - Thoughts of emergency, fear, rapid reaction; Child cries for mother - Thoughts of sadness and distress; Null - To account for no thoughts Muse Headband Testing → We collected 50 10-second brainwave readings, changing between the different emotion clusters Vector Search Database → Stored thought embeddings in ChromaDB for real-time retrieval. Multi-Agent Thought Processing (LangChain): Expansion Agent → Adds vivid details to enhance thought clarity. Reasoning Agent → Breaks down complex thoughts into a logical sequence. Emotional Agent → Adds emotional layers to thought. Adapts thought representation based on stress and biometric feedback from Terra API using the Garmin Watch. LLM-Powered Thought Refinement → Uses OpenAI-based agents to structure thoughts before video generation. Adapts thought representation based on stress feedback from Terra API using the Garmin Watch. AI Video Generation → Converts structured thought output into an AI-generated cinematic experience using Luma AI Challenges we ran into EEG Data is Noisy → Required extensive filtering and preprocessing to extract meaningful patterns. Mapping Thoughts to Meaningful Outputs → Training an EEG-to-thought model was difficult due to limited labeled datasets and the complex/unstructured nature of EEG data. We had to collect data on our own using the Muse Headset and train on that. Vector Search Optimization → Fine-tuned cosine similarity in ChromaDB to improve thought-matching accuracy. Biometric Adaptation Complexity → Integrating real-time stress data into the thought expansion process required careful balancing. We did extensive research on how stress can affect characteristics of thought, like its imagery. LLM Constraints & Rate Limits → Had to optimize API calls to avoid delays and costs. Despite these challenges, we successfully built a working pipeline that converts raw EEG signals into structured AI-generated videos. Accomplishments that we're proud of We are proud of bridging research in neuroscience, AI, and social impact. This bridge has spurred an innovation that will empower affected veterans to more effectively express their chain of thought, allowing healthcare professionals to better engage with each individual's unique situation. This ultimately catalyzes the transition back to civilian life for post-service veterans. Additionally, we are likewise proud of hacking and building moving pieces that we have never worked on before like training a model What we learned We learned a lot in this hack. For the majority of us, this is our first hackathon. We primarily learned how to integrate different components of a large project, from the ML model, to the pipeline, and the frontend. Additionally, collecting data from the EEG was substantially tricky, and we learned that EEG-based communication is promising but complex. What's next for SynapseAI We’re excited to bring our project to life! We plan to talk to our Ideal Customer Profile(s) (ICP) to run pilot studies, assessing product-market fit. Additionally, we want to: Expand EEG Model Training → Collect more data to refine thought embeddings and improve accuracy. Fine-Tune Real-Time Thought Adaptation → Enhance biometric-driven AI reasoning for better personalization. Incorporate more biometric variability like heart-rate or perspiration to our agent pipeline. Enable Continuous EEG Streaming → Allow real-time, uninterrupted thought-to-video processing. Optimize AI Video Generation → Improve coherence, storytelling, and realism in generated videos. <div