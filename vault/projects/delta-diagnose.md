---
slug: "delta-diagnose"
url: "https://devpost.com/software/delta-diagnose"
title: "Delta Diagnose"
hackathon: "XHacks 2021"
organization: "XHacks Organization"
winner: true
words: 636
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Delta Diagnose

> Classify Chest X-Ray Images as COVID-19, Viral Pneumonia, and Normal.

[Devpost](https://devpost.com/software/delta-diagnose) · hackathon [[XHacks 2021]]

## Facets

**mechanism** [[benchmark_measured]] [[structural_withholding]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css3, django, html5, javascript, keras, python, tensorflow

## How they structured the write-up

- delta diagnose
- 💡 inspiration
- 💻 what it does
- 👷‍♂️ how we built it
- ⚙️ how it works
- 🔨 tech stack
- 🧠 challenges we ran into
- 🏅 accomplishments that we're proud of
- 📖 what we learned
- 🚀 what's next for delta diagnose
- installing and running
- some glimps of the site

## Body

Delta Diagnose 💡 Inspiration The Delta variant of COVID-19 arrived in India in March 2021. It led to the deaths of 270,000 individuals in three months, more than twice the number we saw in the entire year of 2020. The Delta strain has a higher affinity for lung tissues than other strains, making it more lethal. The same mutation has now been discovered in other parts of the world. We wanted to aid the people in these countries, thus we created Delta Diagnose. Viral Pneumonia, a condition with identical symptoms, has made identifying COVID patients even more challenging. 💻 What it does Delta Diagnose aims to classify Chest MRI Images as COVID-19, Viral Pneumonia, and Normal. It can not only assist doctors but can also be directly used by the patients to self-diagnose (although we suggest confirming the results with doctors). 👷‍♂️ How we Built it Data related to the healthcare industry is not openly accessible. We were fortunate enough to find a relevant dataset on Kaggle (Link) . The Dataset consists of 251 Chest MRI Train images (111 - COVID, 70 - Viral Pneumonia, 70 - Normal) and 66 Test Images (26 - COVID, 20 - Viral Pneumonia, 20 - Normal). Then we did some image augmentation (Horizontal Flip) and obtained 502 total samples out of which 15% (76 samples) formed the Validation Set and rest (426 samples) formed the training set. Leveraging the power of Transfer Learning, we used VGG16 model pre-trained on imagenet dataset as our basemodel with it's weights freezed. We then flattened the output from the basemodel and passed it to a Dense Layer consisting of 3 neurons (1 for each class). Finally, we saved the model with least Validation Loss for future predictions. ⚙️ How it works User needs to upload a Chest MRI Image (Need some images to test on? Download them from here ) We would process the image and return the result 🔨 Tech Stack 🧠 Challenges we ran into We first attempted to build the model from scratch but failed terribly (due to lack of training data) reaching an accuracy of just about 39%. The accuracy was increased to roughly 59 percent when we utilized the ResNet50 model, but it was still below par, and the stored model size was around 300 MB, which could have caused problems when deploying the model on Heroku. Finally, we settled on the VGG16 model, which had an initial accuracy of 84 percent (later improved to 97 percent) while still keeping the size in check. Another challange was to integrate Twilio OTP while login. We tried to use twilio but the request was not apporved for the phone number so we were not able to integrate in our project. 🏅 Accomplishments that we're proud of When we started, we never thought we would be able to achieve an accuracy of 97%. We are really proud of that. Secondly our aim was to deploy this project so that anyone in the world can really use it and we are extremly happy for reaching our goal. 📖 What we learned We learned how to make an API and also how to deploy the ML part seperately and the UI seperately to enhance performance of the website. 🚀 What's next for Delta Diagnose We tested the model on only 66 images and those are not enough to get the real picture. We would love to test it on more images and improve the model accordingly. Installing and running Model API Send a POST request on URL http://covidclassifier.herokuapp.com/classify_image with JSON file containing URL of image to classify as a Parameter Sample JSON File { "url" : "https://i.ibb.co/FBSztPS/0120.jpg" } Sample Response { "class":"viral", "class_probability":55.93 } GUI Version pip install -r requirements.txt python manage.py runserver Some glimps of the site Home Upload and Test Result <div