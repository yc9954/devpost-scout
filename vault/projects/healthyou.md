---
slug: "healthyou"
url: "https://devpost.com/software/healthyou"
title: "HealthYou"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 394
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/web_dom"
---

# HealthYou

> Creating the future in health but empowering you to take charge fo your own data!

[Devpost](https://devpost.com/software/healthyou) · hackathon [[HackZurich 2021]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[document_pdf]] [[medical_record]] [[web_dom]]

**stack** flask, javascript, jupyter-note, keras, pytesseract, python, tensorflow

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for healthyou

## Body

Inspiration In Switzerland, many medical records are saved on paper, so delays in diagnosis and resource planning happen. Our centralized data platform enables users to share their data with health care providers. How we built it Front-end We used JavaScript , HTML , CSS as well as Bootstrap to create a graphical user interface fo the user to sign up, login, show health-related updates and other interesting features. Back-end We set up a Flask server to save the user input data and then output relevant information or predictions. We also integrated an OCR functionality to interpret handwritten or printed medical documents using Python and Google's Pytesseract library. ML/Data Science We leveraged Tensorflow , Keras , and a LOT of research to build a predictive model that not only takes into account a user's health and daily habits, but also leverage the Switzerland's open data to generate and augment health data in order to build the best possible immediately available predictive model. Challenges we ran into Learning Flask in a very short time sounded a challenge to us, but we could easily overcome thanks to the proper documentation on their official website. We initially didn't have any user's health data to train/test the model, so we had to read and research papers to learn how a person's life can affect the life expectancy, and get thousands of data for the neural model from the Swiss Government's API. Accomplishments that we're proud of We are proud to have trained and built a predictive model that not only takes into account a user's health and daily habits, but also leverages the Switzerland's open data to generate and augment health data. Also, our progress to learn and develop a web application with Flask from scrach is comparatively fast. What we learned All of us have some knowledge of Python, but this is the first time for most of us to develop a web application with Flask. We also learned the advantages of OCR for digitalization, Tensorflow, Keras, and other works to develop a neural network to train and test life expectations according to their daily habits. What's next for HealthYou As next steps, we can further improve our machine learning model to predict more parameters and show results in a more interactive way. We can also add an online appointment system with the general or specialist doctors. <div