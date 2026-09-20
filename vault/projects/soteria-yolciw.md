---
slug: "soteria-yolciw"
url: "https://devpost.com/software/soteria-yolciw"
title: "Soteria"
hackathon: "AWS Disaster Response Hackathon"
organization: "Amazon"
winner: true
words: 344
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Soteria

> Use Machine Learning with satellite imagery to map natural disaster impacts for faster emergency response.

[Devpost](https://devpost.com/software/soteria-yolciw) · hackathon [[AWS Disaster Response Hackathon]]

## Facets

**domain** [[climate_energy]] [[disaster_emergency]] [[security_privacy]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, figma, gradio, hugging-face, python, sagemaker-studio-lab, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for soteria

## Body

Inspiration The scale, scope and intensity of natural disasters ranging from hurricanes to wildfire is only increasing as the effects of climate change worsen. The lives lost and impacted continue to highlight peoples vulnerability to these disastrous events. As a team, we wanted to use our areas of interest and expertise to serve communities who have or will be impacted by natural disasters. We don’t need to be on the ground of a disaster to make an impact. Inspired by the potential that AI has for improving the quality of life, we applied this to natural disasters. We wanted our model to be applicable to all natural disaster globally, but first we start on the East coast of Malaysia. What it does Soteria uses machine learning with satellite imagery to map natural disaster impacts for faster emergency response. How we built it We built machine learning models that determine whether a disaster happened in the satellite image or not, classify the type of disaster that happened, identify the buildings in the image, finally output the damage level for the region in the satellite image. We use Amazon Sagemaker Studio Lab to design, build and train our models with Tensorflow as a machine learning framework, AWS to store our dataset and deploy the models for predictions, Hugging Face’s Space to host our ML model demo app with Gradio, finally we use Figma to prototype the web app. Challenges we ran into With limited storage and computation power on Sagemaker Studio Lab, we're able to build and demonstrate the core ideas of our models. What we learned We learned about the importance of communication and how much it can serve to strengthen every stage of the disaster management cycle. Which is why our data gathering and dissemination is so important to our project. It has also helped to deepen our understanding of the importance of the accessibility of centralised information to better emergency response time. What's next for Soteria To continue to improve our ML models to achieve better accuracy, implement our prototype web app. <div