---
slug: "mole"
url: "https://devpost.com/software/mole"
title: "MoleML"
hackathon: "PennApps XII"
winner: true
words: 588
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/clinician"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MoleML

> App for detecting Melanoma and Basal Cell Carcinoma using OpenCV/ML.

[Devpost](https://devpost.com/software/mole) · hackathon [[PennApps XII]]

## Facets

**domain** [[finance_payments]]
**user** [[clinician]] [[general_public]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** big-data, cloud-computing, css, flask, html, javascript, jquery, machine-learning, materialize, opencv, phonegap, photoshop, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moleml

## Body

Inspiration As a health-conscious team, we decided to analyze common health issues facing Americans. We found that skin cancer is one of the most prevalent diseases in the United States, with five million people being treated each year and one in five Americans developing it in a lifetime. Additionally, we knew that although early detection of skin cancer leads to the greatest chance of survival and better treatment options, many Americans may be reluctant to check with their doctors due to the time commitment, great cost of doctor visits (especially without insurance), and personal reasons, such as privacy. Knowing this, we wanted to make a tool that people could easily use at home to check privately whether or not they were at risk of skin cancer. We were further encouraged by one of our teammates, who had several potentially cancerous moles removed as a child but still had some moles remaining. What it does MoleML is a cross-platform mobile application which puts the power of machine learning into the hands of everyday users. MoleML allows users to take or submit a picture of a mole that they suspect is cancerous. A self-developed algorithm analyzes the image and makes a prediction whether or not the mole is cancerous, also providing a confidence level. MoleML then allows users to track their moles over time, providing data and graphs as visual aids to help determine whether or not the moles are becoming more dangerous. How we built it MoleML was developed using Adobe’s Phonegap, which builds the Android, iOS, and Windows versions of the mobile app from the framework we created in HTML/CSS/JQuery. It first allows users to take or upload a picture from gallery of a mole. This image is then sent to a server and processed by a Random Forest Classifier, a machine learning algorithm that integrates OpenCV and is trained on a public, HIPAA-compliant data set containing over a thousand images of potentially cancerous moles. The algorithm returns its prediction and confidence, calculated by analyzing up to ten parameters of both the mole and the user. This prediction may be improved by the user providing basic data that may put them at greater risk of skin cancer. Then, data of each test are saved in a Parse database and visually plotted with Charts.js. Challenges we ran into There were a great many challenges that we faced in the course of creating such a technically intensive app. We spent many hours creating the machine-learning algorithm, processing images accurately, setting up our servers to successfully run data sent by users through the algorithm, as well as creating a polished and functional UI. Accomplishments that we're proud of Above all, we are proud that we were able to create an app that could be useful for millions of Americans in just 36 hours. MoleML may not only save millions of Americans time and money but also warn them if they are at great risk of a life-threatening disease. What we learned Not only did we learn a myriad of technical skills, such as working with databases and algorithms, we also learned that we could feasibly create a working app with the potential to help millions of people in just a day and a half of hard work (and no sleep). What's next for MoleML We are hoping to further refine our algorithm to provide results with greater accuracy. In addition, we want to provide options to contact doctors and dermatologists about results, and more detailed statistics about the user’s health. <div