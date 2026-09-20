---
slug: "melmii"
url: "https://devpost.com/software/melmii"
title: "MELMII"
hackathon: "GNEC Hackathon 2026 Spring - Compete For UN-Affiliated/NGO Internships & Prizes"
organization: "Global NGO Executive Committee"
winner: true
words: 808
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MELMII

> Sight for all

[Devpost](https://devpost.com/software/melmii) · hackathon [[GNEC Hackathon 2026 Spring - Compete For UN-Affiliated-NGO Internships - Prizes]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]] [[general_public]] [[legal_professional]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** deep-translator, depthpro, fastapi, next.js, onnxruntime, python, tailwindcss, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for melmii

## Body

The home page of the web application(camera permission denied) Mobile home page of the web application(camera permission denied) Testing distance calculation and object detection Testing distance calculation and object detection Inspiration In Mongolia, the poor living conditions of visually impaired individuals and the insufficient financial aid provided to them are commonly overlooked problems. In fact, there’s only one school for the visually impaired in the whole country. Furthermore, out of 1200+ visually impaired children, only 125 go to school and kindergartens. Alongside this, they face many inconveniences on a daily basis, such as discrimination and bumping into objects or people, leading to most experiencing difficulties in having a satisfactory quality of life. As such, most visually impaired individuals are often unhealthy. We thought to ourselves how we could tackle this issue as students, and embarked on this project. What it does Our project aims to help and assist those with visual impairment by creating an easily accessible web application and software. Our web application can detect 80 daily life objects and obstacles through the user’s camera using machine learning, and tell them what’s ahead of them in Mongolian, making it the first ever web application that is fully in the Mongolian language and designed specifically for the visually impaired in the country. How we built it The project has two modes. One with the intention to be used indoors; specifically, this mode is for when a visually impaired individual is looking for an object. The second one is for traversing outside. With this mode enabled, the user will be alerted to objects ahead of them within a 2-meter distance. Detecting objects in an indoor environment Utilizing YOLO11 and ONNX Runtime, we created the web application. YOLO11(You only look once) is an object detection model trained on the COCO(Common Objects in Context) dataset. The model can identify 80 objects, and by using ONNX Runtime, we deployed the project on Vercel. This section was written with Next.js and TailwindCSS. After detecting the objects, we first clean up the data. For example, the model detects humans thrice, so we clean it to “3 humans”. Afterwards, using n2words.js, we change it to “three humans” because the translation is incompatible with just numbers (the number 3 in this scenario). This is then sent to our Python backend we connected using FastAPI. Using deep-translator(a translating Python library), we translate the English labels into Mongolian before it is said aloud using Chimege Sonur, a Mongolian screen reader. The web application is fully functional with this mode on Android devices, MacBooks, iPads, and Laptops. Distance calculation and object detection when outside Similar to the first mode, this part also uses YOLO11, deep-translator, and Chimege Sonur. However, we have the addition of Depth Pro, Apple’s open-source distance calculating AI model. Unlike other metric depth estimating models, Depth Pro does not need any camera intrinsics, making it the first of its kind. This section currently uses a laptop as the middleman to process and calculate distances. As such, you can test it out for yourself on the provided Google Colab link, but not on the web application. Challenges we ran into There are very limited resources on using both YOLO11 and Depth Pro for real-time inference, so we had to learn by trial and error. We first attempted to train YOLO11 on our own custom Mongolian dataset, but we greatly misjudged how much training data an object detection model required. The model had near-perfect accuracy for only 2 of the 20 classes. As such, we decided on using a pretrained YOLO11 model with Mongolian translations. This ended up being the better choice as we could get feedback from our visually impaired testers much faster than if we took weeks to annotate over 1000+ training images. Accomplishments that we're proud of This was our first time working with computer vision models, ONNX runtime, and even FastAPI. Because of this, we were impressed at how much we had learned within these two months. Most of all, we pride ourselves on sticking with the project until the end despite the challenges we encountered. The project is something we’re truly passionate about, and knowing we were making a change in the visually impaired community in Mongolia motivated us immensely. What we learned Through this journey, we have learned in detail about the reality of visually impaired individuals: the typical problems they face, the struggle of having no sight, as well as organizations intended to support the blind. It was a great experience to be part of a community and meet people that we wouldn’t have met if we hadn’t started this project. What's next for MELMII We plan to further develop our project by improving the technology, alongside conducting more research and surveys about visually impaired citizens of Mongolia, in order to explore what we could enhance in our project additionally. <div