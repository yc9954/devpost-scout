---
slug: "automatic-detection-of-covid-19-from-pocus-ultrasound-data"
url: "https://devpost.com/software/automatic-detection-of-covid-19-from-pocus-ultrasound-data"
title: "POCOVIDSCREEN- AI to detect COVID-19 with POCUS ultrasounds"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1172
team_size: 9
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# POCOVIDSCREEN- AI to detect COVID-19 with POCUS ultrasounds

> We want to provide a new AI-based diagnosis tool to screen Covid-19 at early stages in an easy, precise and faster way with ultrasound image analysis (POCUS).

[Devpost](https://devpost.com/software/automatic-detection-of-covid-19-from-pocus-ultrasound-data) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[health_clinical]] [[legal_justice]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** flask, github, keras, opencv, python, react

## How they structured the write-up

- problem statement
- our solution
- challenge we ran into
- solution's impact to the crises
- what's next?
- the value of our solution after the crisis
- code and other resources:

## Body

Our webservice - Upload images and test our ML model Manuscript on arXiv Performance of POCOVID-Net Find all code and instructions on https://github.com/jannisborn/covid19_pocus_ultrasound Problem statement Fast and extensive testing has proven to be a key factor in preventing the spread of COVID-19 in the current crisis. So far, the most reliable and widely used test method is RTPCR. However, during the initial states of the infection, viral RNA detection has been questioned for its low sensitivity and its limited availability since it relies on advanced resource management and supply-chain dependencies. For this reason, lung imaging becomes central to bring a more available and sensitive test. We focus on point-of-care ultrasound (POCUS) images rather than CT scans or X-rays, because ultrasound imaging is an easy, cost-effective, non-invasive method that is available in almost any medical facility. It has been validated in multiple studies to have better performances than X-rays for a wide range of diseases from pneumonia to pleural effusion. With respect to CT scans, similar sensitivities were reported for POCUS to detect COVID-19. In detail, the benefits are Cost of the equipment: For 2000 USD you can acquire a professional echography probe that plugs into your smartphone and allows you to get all the answers you need. Ease to use: You can bring the probe to the patient and perform a “point-of-care-assessment”. Instead, CT and X-Ray require patient relocation that is time-consuming, costly, risky (COVID19 can be spreaded) and tedious. For critical care patients, any displacement is a time-consuming and potentially life-threatening situation. Ultrasound can be repeated anytime at bedside thus providing a perfect tool not only for diagnosis, but also for patient monitoring. Safety of use: With echography, you don't use any irradiating element. Period. Any X-Ray or CT examination slightly increases the lifetime-risk of cancer, especially for younger patients. However, medical doctors must be trained thoroughly to detect COVID-19 on POCUS, since the relevant patterns are hard to discern for the human eye. Therefore, automatic detection is highly relevant to assist doctors and thus to make POCUS applicable as a reliable diagnosis tool. Our solution We have developed a proof-of-concept automatic detection system for the diagnosis of COVID-19 from ultrasound. Our work is outlined in the following steps: We started with some background research about existing methods of medical image analysis for covid-19 (US, but also X-ray and CT's) to confirm the legitimacy and effectiveness of our work. It was confirmed that our project is indeed the first attempt for the automatic detection of COVID from ultrasound. Collection of a POCUS dataset : We assembled all data we could find online and reviewed them with our MD's specialist to validate the quality. The data was then pre-processed by cropping and excluding any artefacts visible. The dataset is available on our GitHub page as an open-access initiative: https://github.com/jannisborn/covid19_pocus_ultrasound . We trained a convolutional neural network named POCOVID-Net to classify the images and evaluated it with 5-fold cross validation. The model achieves a very promising accuracy of 89% to classify images as COVID-19, pneumonia and healthy, and a sensitivity of 96% for detection COVID . We wrote a scientific article detailing the dataset, our ML approach and scientific evidence of the great potential of the usage of ultrasound. https://arxiv.org/abs/2004.12084 We developed a frontend application in form of a web platform with React JS, hosted it on a webspace and deployed the model. On https://pocovidscreen.org users can upload their own images and the probabilities for COVID-10, pneumonia and healthy as predicted by our model will be displayed. On the other hand, users can also upload labeled images on the website to contribute data. Challenge we ran into It is very difficult to collect ultrasound data, as any form of medical data has high-level legal protection. The data belongs to the patient, and the hospital is only allowed to store the data but does not in any case owns it (at least accoring to swiss law) and since the emergency / ICU doctors usually are hospital's employees, they should obey the rules of their organisation. So if a doctor wants to share some data, he/she needs the patients agreement and the hospital authorization. Solution's impact to the crises The solution we are developing here could give physicians a rapid assessment method to evaluate the risk of a COVID-19 infection. When this approach is successfully implemented, it can significantly improve testing capacities and speed, and thereby reduces the risk of transmission of the virus. Also, specific therapy is started faster. We want to stress that POCUS is even more promising as a diagnosis tools for developing countries, where other testing methods such as CT are hardly available. Our approach is thus not only inclusive on a global scale, but also novel (the first of its kind) and serves the need of the medical community (which heavily advocated for an amplified role of ultrasound, for references see our paper). What's next? Our proof of concept is done and was already published as a preprint. To improve the model, we need more data and data of higher quality. Specifically, we aim to find collaborators that provide us with reliable data sources, ideally in a clinical setting. If multimodal imagery data (CT, X-Ray, ultrasound) from the same patients could be provided, this would allow a fair assessment of the predictive power of each method and could deliver evidence on the practical feasibility and clinical relevance of our method. But even a clinical study exclusively focused on ultrasound would be a huge step forward. After extensive validation on test data, we vision the project to move towards a real application which could be tested in a real-life scenario. From a technical point of view we are planning to create a public REST API so that people can use our trained models from any other application. On the website, there is also a lot of features to add. First of all, we wouldd like to terminate the login/register functionalities in order to trust the people that are giving images to train the AI. We also need to add a legal notice to inform the users about the data we are collecting. The value of our solution after the crisis Here, we have developed a general framework for both data collection and machine learning inference on ultrasound images. First, the neural network can be trained on the classification of other medical conditions from ultrasounds. For example, the general distinction between viral and bacterial pneumonia can be tackled with our approach. Secondly, our open-access data collection initiative also contains pneumonia and healthy POCUS recordings that are already pre-processed, which can therefore be used for other tasks as well. Therefore, we are convinced that our work can serve as a valuable medical diagnosis tool in the future. Code and other resources: The open source of our code (with instruction and code for both the website POCOVIDSCREEN and the CNN neural-network POCOVID-Net) is available here: https://github.com/jannisborn/covid19_pocus_ultrasound Our preprint is available on arXiv: https://arxiv.org/abs/2004.12084 Find a video demonstration at: https://www.youtube.com/watch?v=qOayWwYTPOs Visit our website https://pocovidscreen.org <div