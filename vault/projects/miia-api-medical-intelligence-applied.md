---
slug: "miia-api-medical-intelligence-applied"
url: "https://devpost.com/software/miia-api-medical-intelligence-applied"
title: "MiiA API - medical intelligence applied"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 678
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/developer"
  - "user/patient_family"
---

# MiiA API - medical intelligence applied

> The system leverages AI technology to analyze data collected from facial recognition, wearable devices, and/ or IoT on a daily basis, and alert the caregivers if there are any identified risks.

[Devpost](https://devpost.com/software/miia-api-medical-intelligence-applied) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[sensor_fusion]] [[voice_speech]]
**domain** [[agriculture_food]] [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[developer]] [[patient_family]]

**stack** amazon-web-services, deeplearning, heroku, node.js, postman, restapi, vue

## How they structured the write-up

- inspiration
- what it does
- how we built
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for miia api - medical intelligence applied

## Body

GIF FitBit Testing server Postman Miia Collection Inspiration As our population ages, we will begin to have a lot of multimorbidities. The aging population will have higher rates of diabetes, hypertension, and other chronic ailments along with neuropsychological conditions. Seniors suffering from chronic diseases require regular health check-ups every 3-4 months for proper management of medications, vital signs, and lab values. These conditions impact the quality of life and ability for seniors to perform in everyday activities, thus increasing the need for caregivers to assist with daily routines on top of managing complex conditions. Furthermore, evidence suggests that caregivers enter their roles with little support and therefore carry high rates of mental and emotional health problems as a result. Now with the onset of COVID-19, the elderly’s ability to access usual medical care and mental support have drastically decreased, and the communication with caregivers is impaired. Seniors are advised to stay at home and may feel isolated from their family and friends, leading to struggles with mental health on top of existing feelings of hopelessness and possible grief from the loss of loved ones. Caregivers too may experience increased stress due to barriers in remote healthcare support. These problems all point to the need for a solution in developing communication channels between the seniors and caregivers for health management while making remote support and health care accessible. Mobile health (mHealth) interventions using smartphones have proven effective for monitoring mood and health symptoms, while also providing a platform for communication and support for mental health concerns. However, these applications are not always accessible to the elderly population. Finger sensitivity and mobility can be an obstacle for the elderly as it impairs their ability to interact with apps. Features such as larger font size, high contrast, and text to speech functionality are often neglected due to the lieu of modern design trends intended to appeal to younger audiences. Therefore, we designed our app, miia (Medical Intelligently Applied) to be accessible and usable by most seniors. Miia is an application that will help track and manage both physical and mental health conditions for the elderly population. For instance, we implemented a Chatbot function to ask seniors about mood and emotions, while also providing a means to input health measurements such as vital signs. The chatbot can be made to speak aloud, while the senior can utilize their voice which is then converted to text. Furthermore, our app has an additional function to track the mobility and activity functions of our users through drawing data from the built-in accelerometer, gyroscope, and other smartphone sensors. This will help us predict the activity and encourage exercise, and potentially prevent frailty and traumatic falls with seniors What it does The system leverages AI technology to analyze data collected from facial recognition, speech recognition, wearable devices, and/ or IoT on a daily basis (FitBit etc), and alert the caregivers if there are any identified risks. The platform also provides a way to facilitate communication between caregivers and care recipients, while aiding with health management to alleviate caregiver stress. How we built we have created a set of API's that have helped us a lot during our continues development of Miia and we are opening some of them to the community for their usage and see if they are usefull We mainly developed them using Node / Vue technologies depolying on Heroku and used python and flask for deploying BMI prediction and emotion prediction on AWS EC2 instance. Challenges we ran into Postman echo system is fairly new to us Accomplishments that we're proud of we are finding after the current implementation that Postman could help us out on automation testing our API's in the future What we learned there are still other access and end points that we need to open up but now with Postman we could see a centralized source of true and available to the rest of the developer community What's next for MiiA API - medical intelligence applied expand our API farm to offer more usefull tools to the developer community <div