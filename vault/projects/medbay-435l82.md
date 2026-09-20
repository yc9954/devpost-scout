---
slug: "medbay-435l82"
url: "https://devpost.com/software/medbay-435l82"
title: "MEDBAY"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 450
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/video_visual"
---

# MEDBAY

> Ensuring citizen health, Always.

[Devpost](https://devpost.com/software/medbay-435l82) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[video_visual]]

**stack** ajax, artificial-intelligence, bootstrap, celery, css3, deep-learning, django, html5, ibm-watson, jquery, machine-learning, posnet, python, rasa-nlu

## How they structured the write-up

- inspiration
- what it does

## Body

HomePage UI of MEDBAY Depression Chabot Interface Heart rate monitoring system Inspiration The global COVID-19 pandemic has introduced massive changes in both need and availability of telemedicine and telehealth services. Physicians have increased their use of telemedicine to care for individuals and populations who have difficulty accessing care because of geography, lack of available trained practitioners, or health limitations. If we can provide an application which would help in handling mental fitness, heart-rate monitoring and also a smart chatbot to be aware of symptoms and diseases and doctors needed to consult, then it would be highly beneficiary to the generation especially in this pandemic world. The motivation behind this idea was driven by wellness for the entire society in these times. People fret about their pulse or heartrate considering as a symptom for COVID, they suffer from anxiety or depression. They are unaware or worried about what symptoms would prompt what disease and which doctor to consult. Also, a medical platform to order medicines online through a voice based chatbot would benefit the older generation as well. Hence, our application MEDBAY comes to the rescue providing a one stop for all. What it does HEART RATE MONITORING SYSTEM Our application has an unique heart rate monitoring system, which is a non-contact based system to measure Heart Rate using real-time application using camera. Heart Rate (HR) is one of the most important Physiological parameter and a vital indicator of people‘s physiological state. The main principle is to extract heart rate information from facial skin color variation caused by blood circulation to monitor the user’s ‘physiological state Detect face, align and get ROI using facial landmarks Apply band pass filter with fl = 0.8 Hz and fh = 3 Hz, which are 48 and 180 bpm respectively Average color value of ROI in each frame is calculate pushed to a data buffer which is 150 in length FFT the data buffer. The highest peak is Heart rate Amplify color to make the color variation visible DEPRESSION CHATBOT In today’s pandemic situation, when everyone is at home, mental health has become an even more important thing to focus on. That is why our application comes with a depression chatbot which serves as the patient’s listener in these times of crisis. And using our NLP Sentiment analysis models trained in the backend on TensorFlow, it supports and cheers the person up person based on all the conditions they have mentioned. It suggests some appropriate quotes about life, love and family. It also suggests some songs that can uplift user moods and help get over the hard times. Hence, it reduces the mental stress or worry a person goes through especially on low days. <div