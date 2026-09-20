---
slug: "medical-intelligence-applied"
url: "https://devpost.com/software/medical-intelligence-applied"
title: "medical intelligence applied"
hackathon: "AWS Data Exchange Challenge"
organization: "Amazon"
winner: true
words: 1462
team_size: 12
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# medical intelligence applied

> Two-way health management platform for seniors and caregivers

[Devpost](https://devpost.com/software/medical-intelligence-applied) · hackathon [[AWS Data Exchange Challenge]]

## Facets

**mechanism** [[sensor_fusion]] [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-athena, amazon-cognito, amazon-dynamodb, amazon-ec2, amazon-lex, amazon-marketplace-web-service, amazon-ses, amazon-web-services, amplify, android, figma, lambda, vue

## How they structured the write-up

- overview
- inspiration
- how to use miia
- what it does
- main features
- how we built it
- challenges we ran into
- what's next for miia!

## Body

Software architecture (dashboard) Health check bot Search bot Email search results Dashboard login Dashboard home Dashboard user profile emotion prediction BMI prediction Login Signup Data visualisation dashboard Voice chat Text chat Overview Here are some quick links to some of the resources we developed while creating our project: 💡 • Website 📐 • Wireframe 📱 • Figma Prototype 📕 • Documentation Inspiration As our population ages, we will begin to have a lot of multimorbidities. The aging population will have higher rates of diabetes, hypertension, and other chronic ailments along with neuropsychological conditions. Seniors suffering from chronic diseases require regular health check-ups every 3-4 months for proper management of medications, vital signs, and lab values. These conditions impact the quality of life and ability for seniors to perform in everyday activities, thus increasing the need for caregivers to assist with daily routines on top of managing complex conditions. Furthermore, evidence suggests that caregivers enter their roles with little support and therefore carry high rates of mental and emotional health problems as a result. Now with the onset of COVID-19, the elderly’s ability to access usual medical care and mental support have drastically decreased, and the communication with caregivers is impaired. Seniors are advised to stay at home and may feel isolated from their family and friends, leading to struggles with mental health on top of existing feelings of hopelessness and possible grief from the loss of loved ones. Caregivers too may experience increased stress due to barriers in remote healthcare support. These problems all point to the need for a solution in developing communication channels between the seniors and caregivers for health management while making remote support and health care accessible. Mobile health (mHealth) interventions using smartphones have proven effective for monitoring mood and health symptoms, while also providing a platform for communication and support for mental health concerns. However, these applications are not always accessible to the elderly population. Finger sensitivity and mobility can be an obstacle for the elderly as it impairs their ability to interact with apps. Features such as larger font size, high contrast, and text to speech functionality are often neglected due to the lieu of modern design trends intended to appeal to younger audiences. Therefore, we designed our app, miia (Medical Intelligently Applied) to be accessible and usable by most seniors. Miia is an application that will help track and manage both physical and mental health conditions for the elderly population. For instance, we implemented a Chatbot function to ask seniors about mood and emotions, while also providing a means to input health measurements such as vital signs. The chatbot can be made to speak aloud, while the senior can utilize their voice which is then converted to text. Furthermore, our app has an additional function to track the mobility and activity functions of our users through drawing data from the built-in accelerometer, gyroscope, and other smartphone sensors. This will help us predict the activity and encourage exercise, and potentially prevent frailty and traumatic falls with seniors. How to use miia Miia can be used through signing in with gmail or by creating a new account. Once you've logged into miia you're greeted by the main dashboard that provides an overview of your profile along with several different tabs. Here users can chat with miia, sync wearables, and receive diagnostic reports from health checkups. The current functionality of the application is limited to conducting conversations with the chatbot while also completing facial recognition scans that detect mood and BMI. Nonetheless, our current Figma prototype serves as a better representation of the app's final functionality and design. In contrast to the web application, the prototype is developed for mobile devices to better serve the elderly through prioritizing convenience and mobility. The prototype itself is fully interactive as users have the ability to click, scroll, and drag through both caregiver and patient interfaces. What it does The system leverages AI technology to analyze data collected from facial recognition, speech recognition, wearable devices, and/ or IoT on a daily basis, and alert the caregivers if there are any identified risks. The platform also provides a way to facilitate communication between caregivers and care recipients, while aiding with health management to alleviate caregiver stress. Main features Health data collection Daily health monitoring We ensure the health data collection process is easy to follow by having the whole health check-up process guided by our AI chatbot miia, which include the following: AI chatbot - collect health data unavailable in facial and speech recognition/ wearable devices. Facial recognition - facial image taken for analysis of emotions, and BMI Elderly focus design We have conducted phone interviews and user tests with seniors to ensure the app is simple and easy to use. Voice control - elderly users can choose to interact with chatbot by voice or text AI Chatbot to stimulate human-like interactions Enlarged text and other accessibility features Data visualization for caregivers The caregivers' interface is specially designed by our designer and incorporated feedback from two medical professionals in our team. We ensure the app is useful and meets the needs of caregivers. Data analytics dashboard - show key metric of elderly over one month Detailed health reports of elderly - details of each health parameter Medicare provider search If medical follow-up is required, caregivers and/ or seniors can ask our search bot for the Medicare providers in their living area to schedule an appointment. How we built it Software • Frontend development using vue for the caregiver dashboard and Android studio for Android app. • AWS amplify - develop and deploy Android app • Amazon lex - developing chatbots for daily health check-in and Medicare provider search • Lambda - collect values from Amazon lex • Amazon Athena - providers search and create graph visualization • Amazon Cognito - authentication and access • Amazon DynamoDB - Database • Amazon EC2 - deploy machine learning models • Hosting and CICD setups using Netlify and Heroku and GitHub. • Google Colab notebooks to execute heavy GPU workloads and ML Algorithms. • Invision for developing WireFrames • Figma for creating the prototype • Slack for Internal Communications & Google Drive for Documents, Images, etc. Machine learning We collected datasets from various sources such as Kaggle, JAFFE and IMFDB and trained the machine learning model for a couple of tasks: the identification of emotions from facial expressions, identification of BMI from face images, identification of emotions from speech, and detection of falls from phone sensors. Determination of cardiovascular disease risk is also achieved by reviewing cohort studies and results in medical journals. After training the model, we deployed a demo of the emotion prediction model, BMI prediction model, and cardiovascular disease risk using Heroku service. Challenges we ran into There is not much documentation for AWS, and we had a hard time debugging the chatbots, Cognito and EC2. It is also challenging for us to collaborate in AWS. It is difficult to find quality labeled data for training machine learning models, which in turn affects the accuracy rate. Given that this is a remote hackathon, we were also unable to test connections with wearables. While there is the flexibility to use the app without external sensors, we plan to integrate with multiple wearable devices and platforms in the future. What's next for miia! New features Health data collection Speech recognition - speech recorded and analyzed for emotions and mood Phone sensors - monitor activity to encourage exercise and detect falls Wearable devices/ sensors - measurements including but not limited to blood pressure/ heart-rate/ sleeping pattern/ activity Activity monitoring Users can opt-in to allow monitoring of activity in the background. Exercise has been shown to help alleviate symptoms of depression. Since low activity may be one potential symptom of depression, a notification can be sent to senior users to help guide them through simple exercises (yoga, walking). These exercises can also help decrease fall risk. In-app communication To facilitate communication between caregivers and senior users, the app supports messages, calls, and video calls. Seniors can also ask our chatbot miia to initiate a call with their caregivers. Voice control - elderly users can choose to call or message their caregivers with the help of chatbot Elderly users can highlight a region or ask the chatbot to send a particular section to their caregivers for clarification Reminder system for seniors Visual and sound alerts can be snoozed until the elderly login and complete the health monitoring daily Alert system Alert system for identified issues - caregivers can set threshold values according to elderly's condition; red warning symbols and notification pop up when value above/ below normal Join us! We are planning to bring the project to the next stage. Shoot us a message if you're interested! <div