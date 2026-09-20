---
slug: "pocketlab-a-field-blood-diagnosis-tool"
url: "https://devpost.com/software/pocketlab-a-field-blood-diagnosis-tool"
title: "PocketLab"
hackathon: "PennApps XII"
winner: true
words: 363
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# PocketLab

> A field blood diagnosis tool for doctors in third world countries without access to big expensive lab equipment

[Devpost](https://devpost.com/software/pocketlab-a-field-blood-diagnosis-tool) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]

**stack** ios, objective-c, opencv, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that i'm proud of
- what we learned
- what's next for pocketlab - a field blood diagnosis tool
- features and possible health problems detected

## Body

The following medical information, and the data we have produced has been verified by medical professionals and is accurate to the best of our knowledge. Inspiration Doctors in third world countries, perhaps without readily available big, expensive hospital equipment, are often unable to perform various diagnostic blood tests. Using just an iPhone and a $12 attachment, we enable doctors to perform these tests, such as centrifuging and microscopy. It also doubles as an educational tool for trainee doctors with its built in sample data. What it does We have built a blood diagnostics tool kit that contains many features: In order to perform a haematocrit (see the level of plasma/red blood cells), one must first centrifuge the blood. Using the accelerometer in the iPhone to track the progress, we allow the doctors to perform hand held centrifugation, resulting in the separating of the blood. We use advanced image processing to analyse the results of the blood fractionation, to detect the ratios of the blood components, and to give a diagnosis accordingly. (For example, we can detect possible anaemia, by lack of red blood cells) Using a combination of the microscope and image filtering, we can allow the doctors to look at blood smears using the iPhone. We are able to detect a range of diseases based on the data of the blood cells such as shape, variance and size, to give subsequent diagnoses. By using the Epic platform, we can securely manage multiple patients' data; we enrich this by adding our blood samples to it. How we built it OpenCV, Quartz and native methods for image processing Objective-C, Swift, C++ for programming Challenges I ran into Merge conflicts. A lot! Accomplishments that I'm proud of Enabling doctors to leverage today's readily available technology to improve care. What we learned A huge amount of medical knowledge What's next for PocketLab - A field blood diagnosis tool To open source and let the community improve, perhaps eventually making it available for actual use by doctors to save lives! Features and Possible Health Problems detected Centrifugation Anemia Leukemia Hereditary Elliptocytosis Sickle Cell Hemolytic Anemia High Red Blood Cell Distribution Width (RDW) Low Blood Oxygenation levels <div