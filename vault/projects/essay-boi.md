---
slug: "essay-boi"
url: "https://devpost.com/software/essay-boi"
title: "Essay Boi"
hackathon: "MLH Local Hack Day (2018)"
winner: true
words: 470
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Essay Boi

> Scan any handwritten text and automatically translates it into electronic text document on Google Drive

[Devpost](https://devpost.com/software/essay-boi) · hackathon [[MLH Local Hack Day -2018-]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[education]] [[retail_commerce]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]

**stack** azure, azure-bing, azure-computer-vision, computer-vision, google-cloud, google-drive-api, javascript, node.js, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for essay boi

## Body

High Level Architecture Diagram Best of Times - React Native Mobile App Best of Times - Node.js Server Best of Times - Google Drive Essay Boi - React Native Mobile App Essay Boi- Node.js Server Google Drive Folder Google Doc App Test 1 Server Test 1 Docs Test 1 Inspiration We aim to automate the process of translating handwritten text to an online text document. Whether it be a cooking recipe, an essay, or any other type of text, our application will completely automate the entire process. This application will help millions of students who have written a rough draft on paper and then need a typed final draft. This will convert all quick handwritten notes to everlasting digital copies. What it does For anyone who wants to scan their hand written work onto their computers or want a quick spell check, they can use this application. Microsoft Azure has Computer Vision APIs and Spell Check APIs which allow us to translate handwritten text to a string and also spell check the string. Google Drive API allows us to automatically push our text document onto your personal account. How we built it The front-end is an app which was created using React Native and Expo. You take the picture using the app and it instantly sends it to the Node.js server running in the back-end. The server takes the image and stores it locally in a folder. The image is then hosted to the web by making the localhost available using Serveo. The serveo link is given to Microsoft Azure's Computer Vision Recognize Text API which takes our image and returns a JSON stating what text it sees. That text is converted into a string and then uses the Google Drive API to upload it into a public Google Drive folder which can be accessed and edited. Checkout the expo link below to try out the app yourselves! (Have to install the expo interface first from the Google Play Store or Apple App Store) Challenges we ran into Uploading images to image hosting websites. Recognizing bad handwriting. JavaScript memory leakage. Configuring the JSON file to how you want it Accomplishments that we're proud of Creating a application that uses your phone's built in camera to successfully analyze the text and translates it to an electronic text document on Google Drive. What we learned We learned how to use Microsoft Azure's Machine Learning/AI APIs as well as set up Node.js servers. We also learned how to add a license to the Github repository. What's next for Essay Boi With more time, we'd definitely integrate the Microsoft Azure Spell Check as well as translation services. Afterwards, we want to extend the functionality to Augmented Reality so people can directly see what spelling/grammar errors there are while they are writing in real-time. <div