---
slug: "wemindyou-app-emotional-well-being-of-kids-during-covid-19"
url: "https://devpost.com/software/wemindyou-app-emotional-well-being-of-kids-during-covid-19"
title: "WeMindYou App - Emotional Well-Being of Kids during Covid-19"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 1166
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# WeMindYou App - Emotional Well-Being of Kids during Covid-19

> A digital workflow app to identify Emotional Well-Being of Kids through facial analysis & psych questionnaire, empower them with meditation/yoga techniques & verify improvement using neural correlates

[Devpost](https://devpost.com/software/wemindyou-app-emotional-well-being-of-kids-during-covid-19) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[elder_child_care]] [[mental_health]] [[scientific_research]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** azure, bci, c#, emotion, neuroscience, onedrive, outlook, powerbi, psych, quickbase

## How they structured the write-up

- inspiration
- what it does
- how we built it (detailed technical workflow)
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for wemindyou app - emotional well-being of kids during covid-19

## Body

WeMindYou App Title WeMindYou App - Dashboard WeMindYou App – Mobile Dashboard WeMindYou App – Facial Emotion Metrics WeMindYou App – Neural Emotion Metrics WeMindYou App – Kids Demographics Charts and Maps WeMindYou App – Power BI Integration WeMindYou App – Adolescent Registration Form WeMindYou App – Psych Questionnaire Intro to Ramakrishna Math and Mission Service activity of RKM Chennai at Meyyur Rural Unit The Problem during Covid-19 Lockdown Service during Covid-19 Lockdown A time-tested traditional preventive method Transforming the traditional method for Covid-19 era WeMindYou App – Workflow Diagram WeMindYou App – Introduction & Workflow WeMindYou App – Why Quick Base Platform WeMindYou App – Architecture with Quick Base WeMindYou App – Table Relationship Diagram Guided Meditation Yoga Training Meditation with EEG Headset References Inspiration India has the largest child population in the world with 472 million children. Covid-19 lockdown has significantly impacted 40 million children from poor families. These children come from marginalized families affected due to poverty, social inequality, alcohol addiction, education and digital divide. Many organizations during the lockdown provided necessities like free food and clothing, basic health-checkup to satisfy the essential needs of these under-privileged kids. However, a growing number of concerns related to emotional health such as anxiety, stress, loneliness of these children have accelerated due to the lockdown. We at RKM MediaLab, felt the need to monitor the emotional health of children using scientific methods, and go for a time-tested preventive intervention that aids in their overall well-being. In association with Ramakrishna Math, we collaborated with one of their rural child welfare units for a pilot experimental project to gauge the child’s emotional wellbeing. We developed an app called “WeMindYou App” intended for rural unit coordinators who run this emotional well-being program for kids within their unit. What it does WeMindYou App provides a digital workflow to identify the Emotional Well-Being of children through facial analysis and a subjective psychological questionnaire, empower them with time-tested integrated body-mind training techniques like meditation/yoga and finally verify the improvement in their emotional well-being using neural correlates. This app is intended for rural community coordinators who manage this well-being program for under-privileged children. The App provides the following workflow a) Registration of new children into this emotion well-being program b) Filling-up of subjective questionnaire (Loneliness scale & Anxiety Scale) c) Populating the facial emotion metrics into WeMindYou App derived from cloud emotion recognition app d) Uploading Videos for training program and updating the training calendar e) Populating the neural emotion metrics into WeMindYou App derived from Brain Computer Sensor f) Provides detailed charts, reports and analytics for interactive visualization of various metrics g) Maintain a tasklist update of the entire workflow using Kanban system How we built it (Detailed Technical Workflow) a) First, the coordinator registers a new child with demographic details using a Quick Base custom form. A photo of the child is taken and uploaded to Azure cloud using Quick base pipelines with webhooks for requests. The emotion recognition system (Cognitive Face API) analyzes the photo and outputs emotion indexes, which are then parsed using regular expressions in text channel applied with jinja logic. The emotion indexes of each child is populated in the Facial emotion metrics table. A Slack & Email notification is sent to the coordinator once the child registration process is completed. b) From now on, the child’s emotions are observed using the video feed during remote classes. The generated emotion indexes averaged throughout the day give us a more accurate portrayal of the child’s emotions. The emotion indexes from Azure Face API (identify people and emotions in images) are synced to Google drive with Quick Base Sync folder at a scheduled time and then copied to the original table using Quick Base automation. c) In the third stage, the coordinator utilizes a research-based Anxiety and Loneliness Scale questionnaire with an inherent unique reverse scoring system calculated using Quick Base formula language. d) In the Fourth stage, coordinator uploads relevant meditation/yoga training program videos on Microsoft OneDrive embedded within the App. A training program implemented on Outlook calendar embedded within the App helps the coordinator organize the programs. e) Finally, to verify the efficacy of the training, EEG headsets are utilized to capture emotion indexes which are then populated in the Neural Emotions Metrics table within Quick Base. f) At any point of time, using the built-in Kanban system, the co-ordinator will be able to assess the progress of the child. g) Visualization of Data is implemented using built-in Quick Base charts and reports for facial and neural emotion metrics. An animated brain activity map and brain visualization of the child with highest negative emotional index enables the co-ordinator to give special attention to the suffering child. Advanced interactive charts implemented in Microsoft PowerBI are also embedded in Quick Base with connectors. Challenges we ran into a) Developing an app that utilizes disparate systems (low code platform, neural correlates measurement, emotion recognition), leads to integration difficulties within the existing systems. In those cases, we had to resort to iPaaS (or) RPA to automate the workflow. b) Within Quick Base, we were not able to update/create records in connected tables via pipeline. So, as a workaround, we had to copy from the connector table to the main table. c) The OpenStreetMap utilized within Quick Base contain limited addresses within rural India, this leads to maps reporting incorrect locations for rural areas. d) Certain UX features in Quick Base that we needed for the dashboard are still in the Beta stage e) Discussion of emotional health (mental health) especially among children in South Asian countries is a taboo topic and getting acceptance for testing among families of rural communities is a greater challenge Accomplishments that we are proud of a) Making an multi-disciplinary research idea into an App within a short span of time utilizing Quick Base nocode functionalities was the biggest accomplishment b) Adding interesting and interactive charts with PowerBi and embedding it within Quick Base App using PowerBI Connector c) Utilizing multi-disciplinary technologies to address a current critical issue especially affecting under-privileged children during this challenging time of Covid-19 lockdown What we learned a) Learned basic neuroscience and BCI, understood about EEG headsets and their API access b) Learned about facial emotion analysis using various AI cloud solutions c) Learned in depth the strengths of zero/low code platforms d) Experience in social connection with rural community children and addressing their issues What's next for WeMindYou App - Emotional Well-Being of Kids during Covid-19 a) First and foremost is use a continual multi-modal approach for higher accuracy by deploying Emotion recognition using Neural correlates with Ear EEG, Face and Gait analysis with Kinect depth cameras, Bio-sensing with wearable devices b) Implement seamless workflow and maximum automation within the App c) Ensure app can handle multiple rural units d) Implement multi-lingual design and ensure provisions for accessibility e) Ensure that technology is being utilized for social good causes and extend the app further to better service the societal needs <div