---
slug: "agrihealth-li5f2g"
url: "https://devpost.com/software/agrihealth-li5f2g"
title: "AgriHealth"
hackathon: "Microsoft Developers AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 517
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AgriHealth

> Revolutionalize Agriculture leveraging Generative AI

[Devpost](https://devpost.com/software/agrihealth-li5f2g) · hackathon [[Microsoft Developers AI Learning Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]

**stack** azure, openai, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for agrihealth

## Body

Inspiration As a Nigerian, in the past few months we have seen a skyrocket of prices and inflation across all sphere of which food has not been left out. Food is one of the most essential things to man and prices soaring is not a good omen as more families plunge deeper into hunger and poverty, which is a direct opposite to SDGs 1 and 2 which are No poverty and Zero Hunger respectively. Our hope is that if our local food production (both livestock and crops) becomes well developed then we can attain sustainable development as a country and reduce our dependency of foreign imports which is the major reason why food has been getting more expensive in the worsening economy. What it does The tool enables farmers or other agriculture stakeholders have a means to safeguard against agriculture produce crippling diseases. The tool can predict the status of the crops (and/or) livestock based on images sourced from the agricultural produce itself. Now GenAI has been applied with a azure powered GPT model that generates suggestions for farmers to mitigate the identified disease and do so in real time. How we built it This is a project the combines numerous ML techniques including computer vision with deep learning, traditional ml models, and GenAI. It was built using python and various machine learning tools. A convolutional neural network was built with tensorflow, and the deep learning model was trained on respective datasets for each possible prediction. The models were then saved and deployed using streamlit. Streamlit handles the frontend where users can decide to upload pre-existing pictures or take a picture in real-time using mobile devices and the image is then run through the respective model and teh predictions of the model are returned to the users to make information powered decisions about the livestock or crop Challenges we ran into A major challenge we ran into is the dataset to be used for training. Kaggle is one of the best sources of dataset and we were able to find relatively few graphical and picture based datasets on livestock diseases. The datasets for crop diseases were also few and more relied on tabular form of data for predictions, therefore it will be imperative to gather and source data for extended purposes. Another challenge is the performance of the dataset. While we were able to achieve appreciable values of accuracy of 80% and above, higher accuracy values will still be required which can be gotten with more time and more training which was not done due to timeframe. Accomplishments that we're proud of A major accomplishment we are proud of is being able to deploy the model for use publicly and in real time. Deploying deep model projects always serve as a challenge due to the heavy resources required What's next for AgriHealth There are a lot of things to be done to improve the project, however two of the most important of them are Addition of more livestock and crops Integration of chatbots (like openAI) to give Realtime feedbacks based on the prediction of the models <div