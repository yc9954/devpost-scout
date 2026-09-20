---
slug: "centivize-v5o4c1"
url: "https://devpost.com/software/centivize-v5o4c1"
title: "Centivize"
hackathon: "COVIDathon - Decentralized AI Hackathon"
organization: "SingularityNet"
winner: true
words: 1203
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/web_dom"
---

# Centivize

> Incentivizing smart healthcare and social good by strengthening relationships in virtual spaces.

[Devpost](https://devpost.com/software/centivize-v5o4c1) · hackathon [[COVIDathon - Decentralized AI Hackathon]]

## Facets

**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]] [[retail_commerce]]
**user** [[clinician]] [[developer]] [[educator_student]] [[patient_family]]
**substrate** [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** ai, alexa, algolia, api-medic, css, digitalocean, geofencing, google-cloud, google-colab, google-geocoding, google-home, google-maps, grpc, gunicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for centivize

## Body

Diagnosis-Based Post (iPhone) Search Results (iPhone) Profile Page (iPad) Landing Page (Website) NOTE: Video demo also accessible at https://centivize.tech/demo . Inspiration COVID-19 has made basic tasks such as shopping for groceries and scheduling a checkup with a doctor almost impossible for most people. Many individuals who are self-quarantining or otherwise unable to leave their houses lack a means of obtaining resources necessary for everyday convenience and health. This problem is especially harmful for patients with maladies other than COVID-19, since a lack of available doctors as well as their aversion to stepping outside and potentially contracting the virus often prevents them from obtaining items such as prescriptions and over-the-counter medications that are necessary to their survival. To combat this problem of patients’ non-adherence to treatment while simultaneously encouraging social good, we set out to create Centivize. Through Centivize, we hope to use AI/ML, blockchain, and technology in general as a means of transforming careers and improving lives. The fields of medicine and social good have recently become prominent AI verticals, and we hope to expand on current efforts to autonomously and intelligently improve lives. What it does Centivize is a PWA (progressive web application) designed to strengthen community relationships in virtual spaces by connecting volunteers with individuals who possess conditions less critical than COVID-19 but still cannot be overlooked. In most communities, there are people who are in perfect health and want to help but don’t know how to. Our platform connects these two extremes, serving as the middleman between healthy and sick community members. People who cannot go to a doctor for diagnosis and treatment can use the app to obtain a detailed treatment plan. With this knowledge, they can post that they need a specific medicine or item, and volunteers can fulfill those tasks. On the Centivize dashboard, volunteers see a curated list of tasks they can fulfill. Internally, our NLP model uses transformers to determine this list of recommended posts by calculating a similarity score between a given task and past tasks that a given volunteer has fulfilled. These tasks can also be sorted by distance, since we use Google geocoding as well as the distance feature of Radar.io’s JavaScript SDK to store a geographical location object for every Centivize user. We also enable smart notifications with Radar.io geofences; a 15-mile radius geofence is assigned to each post, and the creator of the post is notified when users that upvote or respond to that post enter their geofence. However, any diagnosis-based healthcare service requires feedback and approval from medical professionals, and Centivize facilitates this with ease. Doctors can register on the Centivize platform with their resume and medical credentials, and once their proficiency is authenticated, they can edit posts related to recommended treatment plans and mark certain diagnoses or treatment posts as approved. Finally, users can upvote posts, and the total crowdfunded money associated with a post is awarded to the volunteer that fulfills the task. This incentivizes volunteers to help their fellow community members. How we built it After a few hours of wireframing, conceptualizing new features, and creating tasks, we divided ourselves into ! frontend, 1 backend, and 1 AI/ML developer and started working. Vignav worked on creating the Firebase/Google Cloud Server backend while also developing the diagnosis algorithms and making them compatible with Alexa and Google Home via Voiceflow as well as implementing the RadarJS SDK code, Mason designed the UI/UX using React.js, and Satyajit developed the recommendation and summarization ML algorithms. Vignav also worked with mentor Artur Gontijo to publicly release the models on SingularityNET and with Dr. Anton Kolonin to integrate Centivize's recommendation system with the Aigents platform. Challenges we ran into One of the main challenges we faced was that none of us had much prior experience with blockchain. While we were able to build a rough blockchain MVP, due to the hackathon’s time constraints, we were not able to integrate this functionality with the rest of our app, so we decided to implement a centralized upvote-based model and finish implementing a blockchain system after the hackathon as a means of scaling Centivize’s services. We currently have a Ethereum-based blockchain system, but it is not integrated with the rest of our app. Our blockchain system not only incentivizes social good with cryptocurrency but also maintains privacy of patient health data. In addition, we are currently working with Dr. Anton Kolonin to integrate our blockchain system with the Aigents reputation system in order to provide personalized recommendations of unfulfilled tasks to volunteers. Paired with Aigents, Centivize can provide accurate and tailored recommendations of tasks to volunteers and will learn to make better recommendations as more and more users join Centivize and provide the Aigents model with more data to train on, thereby increasing the chance that a volunteer completes a task recommended to them and thus fostering greater social good. We also had challenges with uploading the AI models to Google Cloud. One of our models, the summarization transformer, was larger than the 2 GiB memory limit for a cloud function. This caused many problems and we ended up deciding to implement the model with Google’s AI Engine in order to use it in our platform. Accomplishments that we're proud of We're proud of the unique way in which we were able to combine and build off of research from various sources and fuse them into one final product. It was really exciting to see all of our features come together and for us to successfully transform something that has so far been primarily an untested, theoretical concept into an innovative working product. We're really proud of everyone's dedication to the project and determination to tackle this problem with a revolutionary solution. In addition, our summarization and similarity score ML models are available on SingularityNET. We worked with Artur Gontijo to release our models on the SingularityNET blockchain to enable their public use; it will soon be exposed on the SingularityNET DApp for purchase using AGI tokens. The code for the SingularityNET service is accessible at https://github.com/rvignav/snet-centivize . What we learned We entered this hackathon with absolutely no knowledge of how to build centralized upvote-based PWAs, and after a lot of hard work (and online tutorials), we finished Centivize. Working with vast amounts of ML training algorithms, medical API data, and more made this project really fun! What's next for Centivize For the second iteration of our smart diagnosis feature, we plan to integrate our transformer-based summarization algorithm, which converts the long paragraphs of treatment information that patients currently have to read into a brief list of necessary steps to obtain treatment, into the Centivize app. While we already developed the ML model, we were not able to convert it into a Google Cloud function because it exceeded the 2 GiB memory limit, and we aim to use the Google AI Engine or the SingularityNET Python SDK as a means of deploying this algorithm in our app. Most importantly, Centivize’s diagnosis and blockchain solutions extend far beyond the scope of COVID-19. While our work is disruptive in fostering effective community interaction during these unprecedented times, our technologies can be applied to various other scenarios and industries that aim to strengthen relationships in virtual spaces. <div