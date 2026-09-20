---
slug: "m-gap-irp4ev"
url: "https://devpost.com/software/m-gap-irp4ev"
title: "MaintainGAP"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 648
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MaintainGAP

> A 3 in 1 automated screening system built in Postman's Public Workspace for safety and security purposes in public premises.

[Devpost](https://devpost.com/software/m-gap-irp4ev) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[health_clinical]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** flask, opencv, postgresql, postgrest, postman, python, sendgrid, tenserflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for m-gap

## Body

Postman Workspace Website screenshot 1 Website screenshot 2 Inspiration 2020 has been a testing year for all of us. Going outside your home now means securing your mask, frequently reminding yourself of the term “social distancing” and getting your temperature checked as soon as you enter any public premise. We have devised a solution for all industries and crowded areas where security and safety issues are a concern. By developing an economical and automatic system that is capable of measuring the body temperature of a person combined with Face-Mask Detection and Facial Recognition, a company will be efficient in carrying out an additional screening before the employee with initial/potential symptoms could enter the location. What it does M-GAP does the following things:- i) Measure body temperature (initial COVID symptom). ii) Detect mask equipment. iii) Perform facial recognition. iv) Generate an alert according to the favorability of the outcome. v) Monitors and records each detail about an individual for future use minimizing manual work. All the functions listed above are performed by generating API Requests through POSTMAN. How we built it Using all request methods- Post , Get, View, Put , Patch , Delete , etc _ in the Postman Public Workspace. The web application creates and utilizes API's built in Flask, a web framework built atop Python and WSGI by sending requests from Postman. The project utilizes OpenCV and Tensor Flow open source libraries to perform Facial Recognition and Face-Mask Detection. The whole solution performs the functions by taking input as query parameters or in multipart/form-data and in json files. The team designed its database using PostgreSQL and have tried to establish a connection with Postman using _Postgrest . Additionally, we have incorporated Authorization using Sendgrid API Key in order to generate an automated reply from the business email using test scripts and snippets . The working of the solution involves two processes - registration and verification but in between there are a variety of API connections made which are successfully working with the use of Postman. Challenges we ran into The project in itself was a challenging task to complete as we were not previously familiar with Postman Collections. We are new to implementing facial recognition and face-mask detection. A separate study for postman was a tough assignment. We had to continuously test and debug our solution while using Postman which was a demanding task. We referred all the resources offered for the hackathon and learnt how to execute API's in a workspace. All the sub-components on Postman like Pre-request Scripts, Headers, Authorization became a challenge for us to learn and execute. Accomplishments that we're proud of We are proud to have completed the project in a limited time frame with full efficiency by testing it multiple times. We are elevated to delete, put, patch, lock and unlock method requests using postman and feel lucky to learn the same. Additionally, we have tried to keep a user-friendly interface design on a complex back end with two highly accurate machine learning models deployed which is in itself an accomplishment. What we learned The journey of building the project was a great learning experience for the team as we had the first time collaborated to build a project together. Furthermore, the team gave in exceptional efforts to learn and implement machine learning algorithms and Postman for the execution of API's into the project idea. We learnt about the Postman Public Workspace and how efficient it is for collaborating in teams. Also, all the features from creating API's to mock servers and monitoring, the team put in effort to make the maximum use of all functionalities offered by Postman. What's next for M-GAP Implementing our web application into a hardware device is a future update we would be working on and would be looking to build more API's and incorporate new features apart from Facial Recognition and Face-Mask detection. <div