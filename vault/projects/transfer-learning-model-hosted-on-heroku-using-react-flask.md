---
slug: "transfer-learning-model-hosted-on-heroku-using-react-flask"
url: "https://devpost.com/software/transfer-learning-model-hosted-on-heroku-using-react-flask"
title: "Transfer Learning Model hosted on Heroku using React & Flask"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 538
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Transfer Learning Model hosted on Heroku using React & Flask

> Transfer Learning Model using RoBERTa/LSTM built on PyTorch, trained on the IMDb dataset hosted on Heroku using React and Flask.

[Devpost](https://devpost.com/software/transfer-learning-model-hosted-on-heroku-using-react-flask) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** flask, heroku, javascript, python, pytorch, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for transfer learning model hosted on heroku using react & flask

## Body

Inspiration We got to know about Transfer Learning through the fast.ai course by Jeremy Howard, who in his course has emphasized the importance and usage of Transfer learning. Transfer learning uses pre-trained models on large datasets, extracts the features from them, and then uses it to solve similar problems using similar datasets. Rather than training a model from scratch, it allows the user to use the features extracted during a task and use those learned features to tackle another problem of a similar type. What it does We have used Transfer learning on a customized pre-trained RoBERTa model to train it on the IMDb Movie Review dataset first. The model is then saved, and the learning is then transferred to another model having exactly the same architecture. The new model is now trained on the IMDb Movie review dataset and the performance is compared to the first model. In the final step, we have created a Web Application using React and Flask, which deploys this model on a web application making it user-friendly. The web application has been hosted using Heroku. How we built it For the first part, we used Facebook's pre-trained RoBERTa model and downloaded the respective weights for the architecture. This pre-trained model was then customized using a few additional layers. For the pre-training part of our tutorial, the weights of the RoBERTa model were frozen and the model was pre-trained so that only the weights of the additional layers were updated. The weights were then transferred, and the model was fine-tuned on the same IMDb movie dataset and showed an improved performance than before. Challenges we ran into A major challenge we ran into while building our project was to find two similar datasets to validate the exact performance of Transfer learning. Since we could not find two similar datasets, we decided to transfer the learning from the same dataset and then fine-tune the model to show the improved results. Another problem we faced was during the hosting of our project. Heroku allows a maximum size of 500Mb to be hosted for free. Since the RoBERTa model's saved weights alone racked a total space of 900Mb, we had to shift to smaller LSTM Architecture for the demonstration purpose of hosting. As for people who have access to better hosting services, the steps for hosting would remain exactly the same as we have shown here. Accomplishments that we're proud of What we learned While working on the project we gained quite a lot of knowledge about the following: RoBERTa model for NLP Transfer Learning The necessity of having a similar dataset to apply Transfer learning, we tried to implement it on the SST2 dataset but due to the difference in length of reviews, the model failed. Hence having similar datasets is quite necessary Training Deep Learning models using PyTorch Flask Create a basic front-end using React Hosting web-applications on Heroku What's next for Transfer Learning Model hosted on Heroku using React & Flask We would like to explore the working of Transfer learning on similar datasets, to look into more of the challenges it might impose. We would also explore other free hosting solutions which would allow us to host large deep learning models. <div