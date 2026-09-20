---
slug: "medchex"
url: "https://devpost.com/software/medchex"
title: "MedCheX"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 358
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MedCheX

> An e-Alert system for automatically detecting pneumonia from chest x-rays

[Devpost](https://devpost.com/software/medchex) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** apache, laravel, mysql, php, python, pytoch, vue.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medchex

## Body

Inspiration As we continue to face the rapid increase in confirmed Coronavirus cases around the world, our team created a pneumonia detection platform for COVID-19. The purpose is to assist doctors in recognizing patients who are infected. What it does The system is built to automatically detect high-risk patients with pneumonia that will then send the information to doctors. With that information, the doctors are then able to make decisions and provide a treatment plan for the diagnosis. Any x-ray images taken for patients will automatically be uploaded to our system. Our system will then scan the images to determine whether the patients are infected. If the test is positive, the doctors will receive an e-Alert (on computer or mobile phone) that contains the original scans and detection results. How we built it Doctors from Department of Medical Imaging gave us thousands of positive and negative chest x-rays for pneumonia. We created a Unet++ based machine learning model to automatically detect the presence of pneumonia using this dataset. We consulted with engineers in order to better integrate our model to assist doctors with their diagnoses. Transfer of x-ray scans, server construction, and prediction response were all needed to build this e-Alert system. Challenges we ran into Automatic detection of pneumonia on x-rays continues to be an important issue. We did not have the medical knowledge to do so, and needed to cooperate with doctors to design the training strategy for the model. Accomplishments that we're proud of Our system has already been tested with and adopted by doctors at the National Cheng Kung University Hospital. It has reduced testing time, and has increased efficiency. The system achieved 92% accuracy to detect the pneumonia symptom, based on 1400 images. What we learned We learned that making accurate diagnosis and alerting medical professionals require multiple experts from different domains of knowledge, such as doctors and engineers. We also learned that collaboration between all parties is essential. What's next for MedCheX In the future, other medical scans, such as CT scans or MRIs, may be included in our system to provide doctors with even more accurate information to diagnose patients. <div