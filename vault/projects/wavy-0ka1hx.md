---
slug: "wavy-0ka1hx"
url: "https://devpost.com/software/wavy-0ka1hx"
title: "Wavy"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 517
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
---

# Wavy

> Wavy is the smart partner for your heart health, by connecting everyday wearable devices and smart home speakers.

[Devpost](https://devpost.com/software/wavy-0ka1hx) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
  <sub>weak: web_dom</sub>

**stack** alexa-skills-kit, amazon-alexa, amazon-dynamodb, amazon-web-services, aws-lambda, fitbit, html5, javascript, tensorflow

## How they structured the write-up

- inspiration
- 50 word elevator pitch
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wavy
- n.b.

## Body

Wavy, the smart partner for your heart Check out the presentation right here, check out the website with demos here and if you can only watch one... we recommend this one. Inspiration Heart disease affects millions of lives worldwide and is the number one cause of death in the United States. People suffering from the category heart failure, especially elders, have to deal with it mostly alone. They become afraid something might happen and no one will be able to help them. Among elderly, heart failure is a big factor in getting admitted into hospital care. It also takes a lot of time, effort and specialist devices to monitor the progression of heart failure. Isn't there anything that can be done using recent technological advances? 50 word elevator pitch Wavy is the smart partner for your heart, by connecting everyday wearable devices and smart home speakers. Wavy learns to understand your heart and even gives customized alerts by analyzing and predicting your behavior. Through Wavy's connected integration, every person with heart failure is looked after, no matter their age. How we built it A heart failure patient wears a fitbit or other smartwatch device. Using API connections we stream that data to the cloud with AWS Lambda services. The data is stored in a DynamoDB and also put through our TensorFlow neural network detecting and monitoring the patients heart data for any deviations. That data is made available to Amazon Alexa in near realtime, so in case strong deviations occur (based on what is normal for that person) Alexa can take action. She can for example unlock IoT doorlocks in an emergency. Challenges we ran into The biggest challenge was retrieving and cleaning the data so it can be processed by a predictive algorithm and displayed properly in the app. Another one was getting the hang of Amazon Alexa, none of us had experience with building Alexa Skills before this hackathon. Accomplishments that we're proud of The feedback from our test panel of heart patients was amazing and a very humbling experience. This is actually one of the first projects where we all applied our prior skills and knowledge to such a high impact social problem. The fact that we can actually give people their sense of safety back using AI and cutting edge but affordable technology makes us very proud and humble. What we learned The technology to make this kind of impact does not have to be expensive. Using AI we can actually make connections and derive underlying symptoms of heart failure. Technology has become so advanced it actually becomes easier to use and integrate with everyday life (fitbit, Alexa). There is a really big unmet demand for the Alexa Emergency feature. What's next for Wavy We'd very much like to build the Alexa Emergency function with the help of Amazon developers. We think it really will save lives. Even if it's just one, isn't it already worth it? See our presentation below for our future plans. N.B. Everything about Wavy has been built during the current hackathon, Wavy did not exist before then. <div