---
slug: "mike-ai"
url: "https://devpost.com/software/mike-ai"
title: "Mike.ai"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 927
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Mike.ai

> Mike.ai is a stroke prediction quizzer that uses machine learning to predict the likelihood of a stroke occurrence based on user's responses to the quiz.

[Devpost](https://devpost.com/software/mike-ai) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[structured_db]]

**stack** asp.net, azure, c#, core, machine-learning, sendgrid, smarteraspnet, xamarin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mike.ai

## Body

WelcomePage QuizPage PredictionPage Inspiration On December 28th, 2018, I received the shocking news that my Dad was hospitalized having got Stroke, this news was like none I have ever received, it was unimaginable because we have no prerecorded family history of this ailment. This ushered my family into a difficult phase. Asides from the enormous expenses that come with managing Stroke, the discomfort it brings can be extremely emotionally draining for the patient and the caregiver(s). On several nights, my dad was rushed to hospital and taken to emergency wards to prevent a recurrence of a stroke crisis, a recurrence can be severe as he is already a Stroke patient. In general, we had to face a lot of financial challenges and at the same time made efforts to ensure we kept being joyful. My family’s experiences in these last three years kept me pondering on how I can contribute to the mitigation of occurrence for such a deadly disease that has the ability to steal amazing moments from a family. Indeed, it is really not an experience you would want your loved ones to witness and in extension; humanity. This led me to think of building a solution that could help create more awareness and a need for medical checkups on the part of people. The aim is to mitigate the occurrence of Stroke; the second deadliest disease in the world. What it does Mike.ai is a stroke prediction quizzer that uses machine learning to perform predictions based on user's responses to some quiz questions. Launching the app will introduce the question pages, a set of 11 questions, targeted at some personal information and lifestyle factors. The answer provided by the user is passed to a custom machine learning model trained from a dataset of over 5000 stroke data found on Kaggle. The model makes predictions of a stroke occurrence or not. If there's a likelihood for a stroke to occur, the user can send a stroke prediction report to his/her email. If there's no likelihood of a stroke, the user can start the quiz afresh or choose to exit the application. How we built it The following were the steps employed to achieve this project: Requirement planning was carried out by the team. We brainstormed on the fastest possible approach to communicate our idea as a product and also come up with something simple. In the end, we came up with a wireframe to guide our thoughts. A product design was created using Figma to guide the app development. Here's the design link Next in line was to train a custom machine learning model for predictions. Datasets for model training were gotten from Kaggle and Azure machine learning was used for the training. The trained model was downloaded and integrated into a REST API built with ASP.NET Core. Also, the email service was achieved on the backend by integrating SendGrid API. The backend layer of the app was further hosted on Smarter Aspnet remote server after series of testing locally via Postman. It's important to note that the layered architecture was employed in writing the backend services. The mobile application was built using Xamarin following the product design as a guide. Integrating to the backend through the REST API was achieved on this mobile (Android) layer of the application. Series of testing on a physical device occurred before the final compiling of the app's apk. It is important to note that the repository, unit of work, and MVC design patterns were employed in writing this application (mobile and backend). Also, dependency injection was employed to achieve a loosely coupled solution amongst a host of other best practices to achieve a maintainable, scalable and testable codebase. I couldn't write unit tests though due to the brevity of time. Challenges we ran into The major challenge was the accuracy of the trained model. This is because we aimed at achieving an accuracy of at least 95% confidence limit but this wasn't the case because of the non-linear regression or logarithmic regression nature of the datasets. We, however, achieved an accuracy of 85% for predictions. Accomplishments that we're proud of We take pride in the doggedness of bringing an idea once conceptualized in 2018 to reality in 2021 through this hackathon. Most importantly, we take pride in the impact this product would have on persons, particularly hypertensive people as a check for carefulness and strict attention to their health to avoid the occurrence or re-occurrence of a stroke crisis. What we learned We learned to integrate machine learning into an application as this is the first experience to make such happen. Though it was not possible to achieve the integration directly on Xamarin, as a best practice on separation of concern, we think it is cool we achieved integrating a machine learning feature to an application using Azure machine learning by first integrating the trained model into a REST API before further consuming the created REST API on whatever client of choice. Also, I had to conduct tons of research to perform the model integration into the REST API. I think the official documentation on this needs to be improved or updated for proper and easy guidance to developers trying to achieve such integrations. In the meantime, I hope to come up with an article on this observation and share some code snippets via Gist. What's next for Mike.ai We hope to refine the model for improved accuracy and commence efforts for further development of features with a target to provide a quality solution to the market. <div