---
slug: "medecoder"
url: "https://devpost.com/software/medecoder"
title: "Prescriptor"
hackathon: "AWS Health AI Hackathon"
organization: "Amazon"
winner: true
words: 397
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Prescriptor

> Prescription reading made easy

[Devpost](https://devpost.com/software/medecoder) · hackathon [[AWS Health AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, css3, django, html5, javascript, opencv, postgresql, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prescriptor

## Body

all prescriptions view user uploaded prescription view single prescription view with functionalities annotator view medicine dosage information digitized prescription image digitized prescription example Inspiration The enormous scope of patient welfare that Digital Therapeutic (DTx) carries with itself is affected by the nature of prescriptions. Handwritten prescriptions carry a plethora of information like data for medicines, dosage, and frequency, all but on a piece of paper. All this information in case made accessible in a computerized arrangement can be utilized in numerous ways to move forward the understanding encounter, treatment travel, and decision management framework. What it does Our project, Prescriptor extracts text from the prescription image, containing the doctor's handwritten information as well as typed information. The required entities in the text that will be shown in the user interface of our web application are then located and classified by a named entity recognition model, which receives the extracted text as its input. The client will have the option to validate our model's predictions using an interactive and convenient annotator tool. It also creates a digitized prescription that can be downloaded by the user. How we built it We used Amazon Textract to extract data from handwritten prescriptions. We built an annotator tool using HTML and JavaScript. We used Amazon Comprehend Medical to extract information from medical text accurately and quickly Using Django framework, we integrated the functional components. Challenges we ran into The absence of state of art OCR models for doctors' handwriting recognition and variations between different prescriptions issued by doctors at different clinics are the major challenges to overcome in ideating this solution. Accomplishments that we're proud of Being able to automatically extract and relate a variety of information from handwritten prescriptions. A user-friendly annotator tool to accurately and systematically cross-check the predicted data. In spite of the differences that exist between doctors' prescriptions, we were able to precisely recognize the various attributes present and digitize the same into a common format. What we learned We explored Amazon Web Services and got introduced to the numerous tools AWS provides which can further broaden the horizons for digital therapeutics and a seamless user experience on health apps. What's next for Prescriptor Prescriptor can be used as a microservice for Amazon Pharmacy, where the process of entering medicine details can be automated and achieved just at a single click and uploaded of doctor's prescription . <div