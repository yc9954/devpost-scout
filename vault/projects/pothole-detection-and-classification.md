---
slug: "pothole-detection-and-classification"
url: "https://devpost.com/software/pothole-detection-and-classification"
title: "Pothole Detection and Classification"
hackathon: "Hack The League Chapter 2"
organization: "Hack The League"
winner: true
words: 425
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Pothole Detection and Classification

> Introducing our revolutionary project that aims to make the roads safer for everyone. Our smart system uses cameras to detect potholes on the road and maps them on a user-friendly interface.

[Devpost](https://devpost.com/software/pothole-detection-and-classification) · hackathon [[Hack The League Chapter 2]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[vision_ocr]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** flutter, google-cloud, machine-learning, mongodb, node.js, postman, python

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we built
- what we learned
- what's next for pothole detection and classification

## Body

Potholes Location for management by the regulatory authority Potholes Location for management by the regulatory authority ## Inspiration The deteriorating condition of the roads and the increasing number of accidents due to potholes inspired us to come up with a solution to detect and classify potholes. What it does Our project uses a camera to capture video feed of the road, which is then processed through a machine learning algorithm to classify whether it is a plain road or a pothole. The potholes detected are mapped on a user-friendly interface along with their latitude and longitude. Potholes get automatically mapped and the users earn incentives for their contribution. How we built it We built the project using computer vision techniques and machine learning algorithms. We take individual framed from the captured video feed from the camera and TensorFlow to train our classification model. We integrated the Google Maps API to map the potholes on a user-friendly interface. Challenges we ran into One of the biggest challenges we faced was collecting a diverse dataset for training our machine learning model. Accomplishments that we're proud of We are proud of creating a solution that addresses a real-world problem and has the potential to save lives. We are also proud of the user incentives feature, which encourages people to report potholes and contribute towards making the roads safer. What we Built Using a pre-trained CNN model for predicting and classifying potholes captured by the user in real time and register it to our App. Federated learning and the concept of decentralisation was integrated to reduce space and time complexity. We extracted the images through web scraping for a binary classification between a pothole or a plain road. After associating the labels by using the inbuilt Tensorflow’s API and preprocessing the input by scaling the images to appropriate size for affordable computation of the model training, we loaded a pre-Trained Xception model with entitled weights of the IMAGENET dataset and trained it. What we learned During the development of the project, we learned a lot about computer vision techniques, machine learning, and integrating APIs. We also learned about the importance of data collection and how to ensure that our algorithm is robust enough to handle different scenarios. What's next for Pothole Detection and Classification In the future, we plan to expand the functionality of our system by adding features such as real-time alerts for drivers and automatic reporting to local authorities. We also plan to improve the accuracy of our algorithm and explore other applications of the technology. <div