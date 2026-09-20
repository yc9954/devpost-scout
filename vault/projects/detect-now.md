---
slug: "detect-now"
url: "https://devpost.com/software/detect-now"
title: "DetectNow"
hackathon: "#CodeVsCovid19"
winner: true
words: 663
team_size: 9
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
---

# DetectNow

> Deep learning to detect coughing related to COVID-19 from recordings

[Devpost](https://devpost.com/software/detect-now) · hackathon [[-CodeVsCovid19]]

## Facets

**domain** [[health_clinical]]
  <sub>weak: scientific_research</sub>
**user** [[clinician]]
  <sub>weak: developer</sub>
  <sub>weak: web_dom</sub>

**stack** bootstrap, flask, html, pyaudioanalysis, python, sklearn

## Body

Inspiration Testing and screening of SARS-CoV-2 require time, money, a good healthcare system, trained staff. It is still not sufficient in many countries. We want that everybody in need can get screened at zero costs from anywhere. What it does Cough is one of the main symptoms of COVID-19 and based on the idea of cough analysis via AI, our project aims to find the unique biosignals of the COVID19 cough and calculate the probability of a SARS-CoV-2 infection. The whole process is available through a web application, making it easy, convenient, and accessible even in low-resource areas. DISCLAIMER: The diagnostics function is not live yet, as this will require a medical trial first Challenges It needs to be clear that this can not be used to replace a medical examination but instead shall assist the national health care systems in the screening, outbreak prevention, and outbreak control process. We are awaiting verified data from COVID-19 positive tested people. This has to be done in a clinical trial to protect Data privacy. Team We are a group of machine learning experts, doctors, and entrepreneurs from Switzerland, Egypt, Germany, China, Ukraine, India, Pakistan, Greece, and Spain We initially found together through a Slack group during the #codevscovid19 challenge and are working completely remotely How we built it Web App: Frontend is built using bootstrap, Jquery, and integrated with the backend via SSL secure https protocol to the flask server. WebRCT combined with native JS API are used to cover a broad range of devices for recording media. The web app is deployed on scalable Azure web app with minor hacks including Kubernetes runtime initialization to include custom libraries for AI. Data Collection: As of June 2020 we have collected 600 cough samples through crowdsourcing. Now we are in the process of collecting confidential verified data in a clinical setting. Signal Processing: Considering that we want to CLEAN a drum recording (highly explosive sounds), we removed low frequencies below 40 Hz and high frequencies above 15 kHz - 18 kHz because of microphone limitations. We also used a gate to remove unwanted noise between the coughs and make sure that you do not remove the "silent coughs" or "heavy breathing" because this might probably be important features for the model. Finally normalizing the sound, so that we do not have different loudness/ amplitudes among the files. Check Signal Similarity: We used cross-correlation (or correlation coefficient as a normalized measure). Also as an alternative correlation approach, we will consider rank-based correlation. Moreover, the similarity of signals can be accessed in the frequency domain. So, we look for "coherence" to find more information. ML Model: we apply CNN as a binary classifier. This step is to classify cough sounds into two main categories; COVID19 cough (dry cough) and None COVID19 cough based on different cough patterns. What we are proud of Working on a common mission with a team of machine learning engineers, doctors, and entrepreneurs. We are non-profit, work for the social good, and are humanitarian. We plan to stay this way. Having built a functional prototype over a weekend: https://www.detect-now.org/ We got listed on Forbes , CNN , Live HUM TV interview and we are leading efforts for an umbrella organization with top research universities. What we learned Interdisciplinary learning and working is highly efficient and can achieve goals quicker Information privacy is very important no matter how limiting it is in innovation and progress in the healthcare field. What's next for DetectNow Collecting verified, qualitative data, therefore making it an ethical and responsible application to a philanthropic cause. Make it an official medical application. It shall stay easy, convenient, and accessible even in low-resource areas, for efficient outbreak control during epidemics. This approach to cough analysis might provide a foundation towards further clinical research with AI on pulmonary diseases. Share knowledge and promote research by creating an umbrella organization with top research organizations (MIT, Stanford, CMU, Cambridge, EPFL, Bill & Melinda gates foundation) <div