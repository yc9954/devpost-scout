---
slug: "gait-analyzer"
url: "https://devpost.com/software/gait-analyzer"
title: "Gait Analyzer"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 727
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Gait Analyzer

> Gait Analyzer analyses the gait from the given video locally using marker free pose-estimation techniques and explains the gait pattern in an easily understandable manner to the end-user using LLM.

[Devpost](https://devpost.com/software/gait-analyzer) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[health_clinical]] [[scientific_research]] [[transportation]]
**user** [[clinician]] [[frontline_worker]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ai, docker, langchain, llama2, mediapipe, ml, ollama, python, streamlit

## How they structured the write-up

- inspiration
- why
- how
- what it does
- how i built it
- usage
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for gait analyzer

## Body

GIF Annotated video with pose estimation Chart left leg Chart right leg Gait data Gait explanation - 1 Gait explanation - 2 Gait Analyzer Architecture Inspiration When ever I visit my spine doctor , the first thing he asks me to do is to walk for checking my gait . I've been wanting to analyze my gait myself for a long time and only now its been possible due to accessible & efficient ML/AI and the ability to run complex models on local computer using Docker. Why Gait abnormalities can be attributed to various musculoskeletal and neurological conditions and so gait analysis is being used as an important diagnostic tool by doctors. Automated gait analysis requires expensive motion capture or multiple-camera systems. But with Gait Analyzer one can analyze their gait in comfort and privacy of their home on their computer. How Gait Analyzer implements the algorithm published in the paper titled Automated Gait Analysis Based on a Marker-Free Pose Estimation Model . This algorithm for gait analysis is shown to be as reliable as a motion capture system for most scenarios. Gait Analyzer further uses Llama 2 large language model to interpret the gait data to the end user in simple terms . What it does Do gait analysis on videos locally on your computer. Annotated video with pose-estimation. Distances, Peaks and Minima plotted for each leg. Displaying gait data. Download of gait data as .csv file. Gait pattern explanation using Large Language Model. Annotated video Charts Gait Data Gait pattern explanation How I built it Video is uploaded by the user using Streamlit . Pose estimation is done on the video using MediaPipe's Pose Landmarker Heavy model and data for key points like left/right hip and left/right foot index is got from the landmarks data. After gap-filling and filtering the data, distances between hip and foot index, peaks(heel strike), minima(toe-off) for the legs are calculated and plotted on the graph. Stance time, swing time, step time, double support times for both legs are calculated and stored in a data-frame. The video is annotated using the landmark data and stored. Video, charts and gait data from the data-frame is displayed to the user using Streamlit. Gait data is sent to the Llama2 model in Ollama via Langchain for explanation. The streamed response containing the explanation is shown back to the user using Streamlit. The application is made available to the end user using Docker and Docker Hub . Install scripts enable easy CPU or GPU deployment of Gait Analyzer via Docker. Usage Docker Use Gait Analyzer to analyze your gait on your computer using Docker . Setup Run the LLM model on CPU mkdir gaitanalyzer && cd gaitanalyzer sh -c "$(curl -fsSL https://raw.githubusercontent.com/abishekmuthian/gaitanalyzer/main/install.sh)" Run the LLM model on GPU Note: Requires Nvidia drivers and Container Toolkit to be installed. mkdir gaitanalyzer && cd gaitanalyzer sh -c "$(curl -fsSL https://raw.githubusercontent.com/abishekmuthian/gaitanalyzer/main/install-gpu.sh)" Challenges I ran into Implementing the algorithm from the paper without any reference code was a challenge, I overcame it by reading and understanding the key concepts mentioned in the paper and through trial and error. Accessing the Ollama container from the gaitanalyzer container was a challenge, I overcame it by using the network host mode in the Docker compose. Enabling the GPU acceleration in Ollama for end-users was a challenge, I overcame it by creating a separate Docker compose file with Nvidia GPU configuration. Accomplishments that I'm proud of I'm proud to have built Gait Analyzer to enable common people like me to analyze their gait in the comfort and privacy of their home on their computer without the need for expensive equipment and experts. I'm also proud to have built Gait Analyzer within the stipulated time of the hackathon. What I learned I learnt about using MediaPipe for pose estimation, Implementing the algorithm for gait analysis from a research paper, running large language model locally using Ollama with GPU acceleration in Docker, accessing it via Langchain and displaying the streaming response to the user. What's next for Gait Analyzer Showcasing Gait Analyzer to the authors of the paper, comparing the efficiency of Gait Analyzer to the software they built and improving Gait Analyzer from their feedback. Showcasing Gait Analyzer to medical professionals and researchers to get their feedback and to improve its efficiency. Building a custom version of MediaPipe for GPU acceleration during pose-estimation. <div