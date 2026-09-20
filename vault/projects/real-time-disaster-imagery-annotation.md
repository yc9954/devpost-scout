---
slug: "real-time-disaster-imagery-annotation"
url: "https://devpost.com/software/real-time-disaster-imagery-annotation"
title: "Real time disaster imagery annotation and search analytics"
hackathon: "Pinecone Hackathon: Jumpstart Real-World AI Applications"
organization: "Pinecone"
winner: true
words: 569
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Real time disaster imagery annotation and search analytics

> Using advanced state of art AI capabilities to perform real time disaster imagery annotation and search to accelerate the disaster response during the "Golden Hour" to save lives and minimize damage.

[Devpost](https://devpost.com/software/real-time-disaster-imagery-annotation) · hackathon [[Pinecone Hackathon- Jumpstart Real-World AI Applications]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[security_privacy]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-dynamodb, amazon-lambda, amazon-web-services, hugging-face, langchain, openai, pinecone, python, sagemaker, streamlit, transformers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for real time disaster imagery annotation and search analytics

## Body

High Level Solution Design Solution Architecture Inspiration It is estimated that over the past decade (2010s), natural disasters have caused an average of roughly 60,000 deaths per year globally. During disaster events, the "Golden Hour" emphasizes importance of rapid response in disaster situations, as the first hour following such an event is often the most critical for saving lives, mitigating further damage, and setting the stage for successful recovery efforts. With availability of huge corpus of imagery data collected in real time from UAV's, Aerial surveliance vehicle and Satellite images, provide us with a rich information about the extent of the damage and disaster conditions. Harnessing this information and providing it to the ground first responder teams in real time give a tremendous value saving the lives and mitigating further damages. This was our key inspiration to build project Golden Hour - Real time disaster imagery annotation and search to accelerate disaster response. What it does Live dashboards of the disasters mapped on to the geospatial dashboard Geospatial search of the disaster images powered by the natural language querying Life safety navigation guidance to the first responder and disaster relief teams Areas of Application Disaster Image Search and impact analysis Satellite/UAV Image Search Wild Fire detection Threat detection and monitoring for defense applications How we built it Building Blocks of the Solution Image Annotation to identify text features and annotate disaster images. Extract metadata from the images, such as Geospatial data. Centralized content repository to store image files in segregated folders. Index the features and metadata to categorize and catalog the images Search the features and metadata to find the images with the relevant features and filter with metadata Natural Language Understanding to identify the user intent and derive the semantics for response generation. Tech Stack AWS : end-to-end solution: Includes Amazon SageMaker, S3, DynamoDB, Lambda, SQS, API GW, IAM Pinecone : centralized repository to store the features data (embeddings) and metadata of the Images. Open AI : semantic processing of the user query – NLU and the CLIP framework to train the image, text pairs. Hugging Face : transformer architecture, the base model uses a ViT-B/32 Transformer Architecture. We fine-tuned the CLIP Network from OpenAI with satellite images and captions from the LADI dataset LangChain : prompt engineering and orchestration of the end-to-end query processing. Streamlit : interactive user interface and user state management. Challenges we ran into Training domain specific AI model. It is easy to distinguish between a lake and flood. But when you are looking at an aerial photograph factors like angle, altitude, cloud cover and context make the task more difficult. We augmented the images with the text that is generated from the labels that are captured as part of the human annotations and generated relevant captions for images that are used to prevent the underfitting of the model. Accomplishments that we're proud of Now we have a live dashboard that can map the disaster images along with the map location on the geospatial maps in real time. Geospatial search of the disaster images powered by the natural language querying and can be done at damage specific and location specific. What we learned What's next for Real time disaster imagery annotation and search analytics Extending this solution to provide navigation guidance avoiding the disaster areas (Ex: Avoiding the Bridge that was damaged or avoiding the road that is washed out due to landslide) <div