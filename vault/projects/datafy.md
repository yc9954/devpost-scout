---
slug: "datafy"
url: "https://devpost.com/software/datafy"
title: "DriveGuard"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 281
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DriveGuard

> API to detect blood on the face

[Devpost](https://devpost.com/software/datafy) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]] [[web_dom]]

**stack** flask, keras, machine-learning, postman, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- what we learned
- use case of the api
- tech stack used
- how does the api work
- check out the machine learning model used:
- test the api on postman with a post request, api url:

## Body

Inspiration Every day several people lose their lives due to road accidents. Imagine a situation where there is no one nearby to help the needy ones. To overcome this we can use mobile applications that integrated with this API to detect blood and confirm the severity of the accident that can be later used as a report generator. What it does We can use this API to detect the severity of the accident by checking if the driver is bleeding We can use the API in CCTV cameras to identify if someone is bleeding Can be used for other face detection system What we learned I learned to deploy machine learning models and test the API on the postman, and also various python libraries Use case of the API We can use this API to detect the severity of the accident by checking if the driver is bleeding We can use the API in CCTV cameras to identify if someone is bleeding Can be used for other face detection system Tech stack used Python Machine learning model with Tensorflow Keras framework Python Flask framework for deployment Heroku for hosting the API Postman to test the POST request for the API How does the API work The API accepts only POST request as a JSON format: { "url": "Input the image URL here" } The response given by the API is also in JSON format with a boolean value for the key "Blood detected": { "Blood detected": 0 if No blood is detected, 1 if Blood is detected } Check out the machine learning model used: FaceBloodIdentifier . Test the API on postman with a POST request, API URL: https://faceblood-detection-api.herokuapp.com/ . <div