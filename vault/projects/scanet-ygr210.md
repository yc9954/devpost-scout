---
slug: "scanet-ygr210"
url: "https://devpost.com/software/scanet-ygr210"
title: "ScaNet"
hackathon: "Hack It Out"
organization: "SGSITS Indore"
winner: true
words: 549
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ScaNet

> Towards a better future with AI Radiology

[Devpost](https://devpost.com/software/scanet-ygr210) · hackathon [[Hack It Out]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[developer]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** azure, css3, firebase, flask, html5, python, react.js, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scanet

## Body

Inspiration Lung diseases like pneumonia have been killing more than 800K children in a year under the age of 5. Also, around 238 BILLION US DOLLARS were the annual Economic burden of lung diseases in Europe alone. 3 key challenges that we wish to solve with our proposed solution were There is an Absence of an AI-driven universal and deployed lung disease classifier using Chest Radiographs with high accuracy. There is no GUI solution especially for medical usage for training custom deep learning model And Even for Radiologists, Reading X Rays requires careful observation and knowledge of Anatomical principles, physiology, and pathology. Hence we wanted to create a one-stop solution for normal people, radiologists, doctors, and AI engineers in healthcare. What it does ScaNet helps in various ways to different user groups: For Common People / Patients: Users can classify amongst 14 different lung diseases using Chest Radiographs with high accuracy by uploading them on the ScaNet website. If the user is not satisfied with the result, they can report the false positive/negative with a correct label for model retraining. Users can also find doctors near their location. For AI Engineers in Healthcare: Use pre-trained weights from ScaNet for training custom deep learning models with 0 lines of code. Tweek hyperparameters, optimizers, and networks architectures, etc for better model accuracies. For Radiologists and Doctors: Classify and report lung diseases using chest radiographs to assist them in interpreting the x-ray image. How we built it We used DenseNet121 with weights of imagenet of the publicly available NIH dataset and Pneumonia Dataset moreover we have created a multi-label classification model to predict 14 diseases mentioned below: Atelectasis, Consolidation, Infiltration, Pneumothorax, Edema, Emphysema, Fibrosis, Effusion, Pneumonia, Pleural Thickening, Cardiomegaly, Nodule, Mass and Hernia We Trained our model on a total of 112,120 frontal-view chest X-ray png images. Moreover, we have deployed the solution as a website to make it accessible for everyone and find doctors nearby using Google Maps API. Also, users could use ScaNet to train custom models using our weights to achieve higher accuracies. Challenges we ran into Cuda Setup for TensorFlow was a big hurdle and the Model would take enormous time to train on CPU alone. Also, after deploying the website prediction would not reflect back to the user due to a CORS error. Accomplishments that we're proud of Our solution is lightning fast, SCALABLE & intuitive. Our model has a 94% accuracy for detecting amongst 14 diseases. It's a one-stop solution for doctors radiologist patients and AI engineers to detect diseases, find doctors and create custom models. What we learned We learned how to use Flask and Microsoft Azure App Services for deploying a deep learning model for public use, on the web. We also learned a lot about the functioning and implementation of CNN models with transferlearning and using firebase services. What's next for ScaNet The proposed work will assist radiologists and doctors in better predicting diseases in minimal time with high efficiency. The aggregation of this will contribute to the health care system for better patient satisfaction and care. The model currently classifies between 14 diseases without much reasoning of why? Further, a multi-task learning model could be trained to highlight regions in the x-ray enabling better visualization and understanding of the foreseen result. <div