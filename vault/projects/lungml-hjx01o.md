---
slug: "lungml-hjx01o"
url: "https://devpost.com/software/lungml-hjx01o"
title: "LungML"
hackathon: "Cognition"
organization: "VITMAS VIT Vellore"
winner: true
words: 549
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LungML

> High-tech care, anywhere.

[Devpost](https://devpost.com/software/lungml-hjx01o) · hackathon [[Cognition]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[health_clinical]] [[labor_employment]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]] [[web_dom]]

**stack** ml

## How they structured the write-up

- 💡 inspiration
- 💻 what lungml does
- 🔨 how lungml is built
- 🔜 what's next for lungml

## Body

💡 Inspiration The overarching idea was sparked by the infamous fight against lung cancer and lung disease. Not only have such maladies killed millions of individuals worldwide, but they have also indirectly harmed our collective well-being as a species. Indeed, vulnerable populations, as well as ill patients, can no longer meet with their doctors at their typical hospital, due to the risks such contact poses in terms of the ongoing pandemic. In addition, physicians can only identify the risk of lung disease with a bewildering and terrifying 30% accuracy, despite lung-related illnesses being responsible for millions of deaths annually. Not to mention, lung cancer is the leading cause of death among all types of cancer. Despite acquiring over 4 million cases per year, and occurring with the subtlest of symptoms that, in reality, require immediate medical attention, most patients simply cannot access the help they need. My youngest sister—Sophie—was recently diagnosed with stage four bronchial (lung) cancer. The issue was that the disease was not properly diagnosed by the doctors once it had begun, and her condition was left untreated for months. Had she been properly diagnosed prior, would she have gotten the necessary medical treatment to handle the disease, and she could have avoided escalating to stage four cancer. As a result, LungML noticed the urgency for a reliable, convenient, and accurate mechanism to correctly diagnose patients who potentially suffer from pulmonary illnesses. We learned about the most common and severe conditions plaguing third-world nations, and countless areas that do not have proper access to medical care. Striving to change these ongoing predicaments, and to allow people to become informed about their health consistently, easily, and effectively: LungML was created. 💻 What LungML Does LungML is an application that allows images of Pulmonary X-Ray's of the chest, as well as MRI scans, to be used to detect if a patient has lung cancer or lung disease using machine learning. Enables the accessibility of accurate diagnosis of a patient for maximum convenience and reliability. Empowers medical and healthcare workers with a second opinion/second pair of eyes in the diagnosis of a patient. As an app additionally created for Third World countries & rural areas, it is also for individuals who do not have access to medical support or fast and efficient examination. LungML is designed to be used frequently to evaluate the severity of pulmonary conditions, and to provide users with knowledge of their current health. 🔨 How LungML is Built Created using TensorFlow and then converted into a TensorflowJS model, the machine learning model uses numerous Kaggle datasets. When the user clicks on the 'Diagnose' button, the request is sent to the backend server which calls the model with all its factors, and then takes the uploaded user image and diagnoses whether or not the patient has pulmonary disease or cancer. The front end was made using HTML, CSS and JavaScript, and the server side was created using nodeJS. 🔜 What's next for LungML Future endeavours for LungML include updating and polishing LungML's business model for medical and healthcare workers, as well as correcting the margins so it can additionally be used by regular users who may or may not have an educational background in medicine. Indeed, there are a plethora of opportunities that can be explored! <div