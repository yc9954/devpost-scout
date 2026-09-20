---
slug: "vac-alert"
url: "https://devpost.com/software/vac-alert"
title: "VacAlert"
hackathon: "Hack the North 2020++"
winner: true
words: 970
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# VacAlert

> A personalized Vaccine Tracker tool to turn the tides against Covid-19

[Devpost](https://devpost.com/software/vac-alert) · hackathon [[Hack the North 2020-]]

## Facets

  <sub>weak: realtime_stream</sub>
**domain** [[civic_government]] [[developer_tools]] [[elder_child_care]] [[labor_employment]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** angular.js, cockroachdb, dropbase, firebase, google-cloud, ibm-cloud, kubernetes, loopback, node.js, vonage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vacalert

## Body

VacAlert is your trusted friend while you wait to get vaccinated against Covid-19. Answer a few questions to get started. You get an estimate on where you expect to get the vaccine. You can subscribe to real-time alerts while you are waiting for the vaccine. You get a SMS alert on updates that may impact your timeline to immunity. Get a sense of what is going on in the vaccine rollout. Using the Locator, you can quickly find a vaccination location near you to make an appointment. Check direction to your appointment on the Map. Set a reminder for your vaccine appointment. You get alerts for your appointment. Congratulations! You are now fully immunized against Covid-19. Inspiration Covid-19 has wreaked havoc across the globe. With vaccines approved for use in Canada and other countries, we finally see light at the end of the tunnel. It is time to get the population immunized against the deadly virus. However, since the vaccines are in short supply , people will be vaccinated at different times depending on their risk level. While the first vaccines are being rolled out to priority groups such as frontline health care workers and the elderly in senior homes, the general public is still confused about when and how they will get the long-awaited vaccine shots. For many people, it is difficult to constantly check for updates to the vaccine rollout. The question is, “When is my chance to get the vaccine?” This application will send you instant personalized alerts and frequent updates on what is going on, based on your age, occupation and other criteria. In this way, you will not miss your chance to get immunized at the earliest opportunity! This tool will help streamline the steps you take from alerts to full immunity. When everyone takes their vaccine shots as planned, the society will win the fight sooner against Covid-19. What it does VacAlert is tailored to individual users who are waiting to take the vaccine based on their priority profiles. They will receive relevant alerts and stay up-to-date on changes that impact their timeline to immunization, such as approval of new vaccines and increase of supplies from manufacturers. The users can use the app to schedule their appointments to receive their vaccine doses. This app aims to be a one-stop solution for individuals to keep track of what is going on from alerts to full immunity against Covid-19. The key features include: A simple questionnaire to estimate your priority and time to wait before you can get vaccinated. The estimates are based on official guidelines and data provided by national and provincial governments. We adjust the datasets to improve the estimates based on changes that affect the rollout plan. A vaccine map for the user to gain insights into the rollout plan such as the number of doses that have been administered in different provinces. Relevant Covid-19 alerts are sent to you via web notifications, e-mails or SMS messages. A convenient locator to find the vaccination centres near you to make an appointment when it becomes available to you. An easy-to-use scheduler for you to set a reminder for your appointment to receive the two doses of vaccine. How we built it We built the web application with responsive design using Angular and Material Design guidelines. We used IBM’s award-winning LoopBack 4 framework to quickly scaffold our REST API server. The Angular front-end calls this backend API server through OpenAPI 3.0 standards. Using DropBase’s simple-to-use API, we efficiently processed a large amount of web scraped data and loaded them quickly into our database for our live insights. We used CockroachDB as our database, which was fast to deploy but very robust on GCP and load balanced using HAProxy to yield the benefits of Distributed SQL. We sent instant SMS alerts using the Vonage API, which is a powerful tool to implement SMS messaging in web applications. We sent push notifications to the users using Google’s streamlined Firebase Cloud Messaging (FCM) API, which is robust and easy to use. We used IBM Cloud to deploy and host the server components of the application. We were able to package both our client web application built with Angular and REST API server using IBM’s LoopBack 4 Framework into Docker images and stored them in the IBM Cloud private container registry. We then successfully deployed these images into Kubernetes. Architecture Deployment Dropbase Challenges we ran into We struggled to quickly learn the APIs in order to integrate them into our application. Luckily the sponsor APIs we chose are easy to use with good documentation. We brainstormed on various ideas. We settled on the best design option given the time available and worked relentlessly towards our goals. Accomplishments that we're proud of We used the right tools and libraries to build a compelling web application based on Material Design and OpenAPI standards. Our application benefited from the diverse set of APIs we used. We successfully achieved all our design objectives. What we learned Working with Angular PWAs and Service Workers to subscribe to Push Notifications. Utilizing CockroachDB to quickly create a robust and scalable database through Distributed SQL. Implementing SMS messaging with Vonage’s SMS API and Node.js SDK. Using Google’s Firebase Cloud Messaging (FCM) API to send web notifications. Using DropBase’s API to streamline web scraping processes to easily extract and process data. DropBase custom pipeline function is powerful as it can verify the web scraped data in case of unexpected changes to the data source format. Using IBM Cloud tools to deploy packaged Docker images into scalable Kubernetes clusters and deploying them to IBM Cloud. What's next for VacAlert Expand the coverage to other countries based on their specific rollout plans. Add more data and insights into the Vaccine Map. Making our app available in mobile app stores. <div