---
slug: "classie-ticketclassifier-machine-learning-model"
url: "https://devpost.com/software/classie-ticketclassifier-machine-learning-model"
title: "Classie-TicketClassifier (Machine Learning Model)"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 506
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# Classie-TicketClassifier (Machine Learning Model)

> Intelligent email classification model, categorizing to a predefined set of ticket classes or work queues.

[Devpost](https://devpost.com/software/classie-ticketclassifier-machine-learning-model) · hackathon [[Power Up Automation]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** .net, azure, machine-learning, multi-class-neural-network

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for intelligent activities - document and text translation

## Body

Inspiration As a company gets bigger and bigger there is a proportionate need to create larger teams to support various services across different departments. This is because, ultimately, your goal to make your customers happy with quality service, real-time support, and easy-to-use productivity tools for your agents; a system that provides an opportunity to grow your business and take on new challenges. But, perhaps your current ticket management system can no longer stand up to the number of tickets your agents receive on a daily basis. That is an old news! What if you can harness the power of machine learning in order to create really advanced intelligent APIs? Because right now we already have the power to implement better email triaging system using machine learning, augmenting agent's capabilities in triaging help tickets! What it does Email ticket classifier This is an email classification experiment to assign an email to one or more class(es) of predefined set of classes or work queues. For the input, you only have to provide the email subject and the email description. Then the output it would provide is the predicted case subject, case type and queue name based on what it has learned from the model. Activity Parameters How I built it The project was built using the following technologies. Visual Studio with .NET Framework 4.6.1 Azure Machine Learning Studio - Multi-class neural Network Challenges I ran into As with most machine learning problems, challenges in cleansing data by far the most common. Also this is really the one of the most crucial part since this will ultimately dictate most of the accuracy and reliability of the trained model. The more data, the more the results are trained properly and the more it can predict the results on the test data. Next in line would be selecting the most optimal algorithm for a particular use case which may vary among different problems. Skewed or unbalanced data. This also includes making sure that the data is free from bias brought about by unbalanced data. The experiment requires lots of training iterations to finally optimize the weights of the parameters in each hidden layer and find the most optimal value learning rate. Selecting the right features to for the training is proved to be one of the most critical decisions as well. Accomplishments that I'm proud of Creating MORE AND MORE VALUE out of products that’s already providing the best value! I'm really proud to have developed another channel for this wonderful solution/API to be utilized. One in which the automation community can get the hands of and build really intelligent automation workflows that can accelerate businesses' journey to digital transformation. What I learned I learned a lot about how and when each types of ML algorithms can be used for different machine learning problems be it predictive (regression), classification, clustering, anomaly detection, etc. What's next for Intelligent Activities - Document and Text Translation Ability to do asynchronous retraining on the model with an updated dataset. More intelligent activities to come! <div