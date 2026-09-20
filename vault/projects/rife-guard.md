---
slug: "rife-guard"
url: "https://devpost.com/software/rife-guard"
title: "Rife Guard"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 322
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Rife Guard

> Rife Guard is a model classification system for rice diseases, featuring a user-friendly interface to help you classify rice diseases more easily.

[Devpost](https://devpost.com/software/rife-guard) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** fastai, fastapi, gradio, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rife guard

## Body

Inspiration The frist time We dont have a idea what to make, Upon discovering CNNs in the hackathon description, we saw an opportunity to apply them for social good. Hence, we decided to develop a rice disease classification system to aid agriculture, aiming to assist farmers in early disease detection What it does Rife Guard is a web application designed to classify rice diseases from images. Users can upload or take a images of rice plants, and our CNN model processes these images to determine the presence of any diseases. How we built it We built Rife Guard using a combination of FastAPI for host Html that use tailwind with jinja and use Gradio for creating the user-friendly interface and then use Gradio pass html iframe for make page to use model. Our CNN model, trained on a dataset of annotated rice disease images from kaggle use fastai because it easy for not complex model and can make model faster than other framework to fit in time of hackathon. Challenges we ran into Throughout the development process, we encountered several challenges. Fine-tuning the CNN model to achieve optimal accuracy demanded extensive experimentation and parameter tuning. Additionally, integrating Html with Gradio while maintaining smooth functionality. Accomplishments that we're proud of We are successful implementation of our CNN model for accurate disease classification. Furthermore, crafting a visually appealing and user-friendly web interface was a significant achievement. What we learned The journey of developing Rife Guard provided invaluable insights into the basic of CNNs and their applications in image classification. Additionally, navigating the integration of various frameworks and technologies enhanced our skills in backend development and user interface design because This is ours firsttime use Fastapi What's next for Rife Guard Future plans include refining the CNN model or trying new model for improved accuracy, and implementing features for real-time feedback and analysis make user know what should do next after know rice diseases. <div