---
slug: "priovax"
url: "https://devpost.com/software/priovax"
title: "PrioVax"
hackathon: "Hack the North 2020++"
winner: true
words: 997
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/structured_db"
---

# PrioVax

> A solution to help facilitate local vaccine distribution and prioritize at-risk groups.

[Devpost](https://devpost.com/software/priovax) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[scientific_research]] [[supply_logistics]]
**user** [[general_public]] [[patient_family]] [[researcher]]
**substrate** [[structured_db]]

**stack** dropbase, express.js, firebase, gcp, javascript, node.js, numpy, pandas, python, react, sklearn, vonage

## How they structured the write-up

- inspiration
- what it does
- technologies used
- how it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for priovax

## Body

Sign Up Page Clinic Dashboard (without data upload) Admin Dashboard (work in-progress) - to append new ML data set Add a single new patient to database Import patient data csv Clinic Dashboard (with data upload) Patient Vaccine Notification (SMS) Data Processing Inspiration With the recent news about the distribution of COVID-19 vaccines in stages, our team was inspired to develop an application to help facilitate this process within local communities. One of the challenges that we are currently facing regarding vaccine distribution is the enormous amount of pressure placed on provincial governments and local healthcare organizations to administer vaccine doses to qualified residents as soon as possible. Our project is able to help medical professionals identify, prioritize and contact high-risk patients at the click of a button by uploading their clinic/hospital’s patient records onto our database. Having a safe and efficient rollout strategy can help save lives. By identifying and prioritizing at-risk groups using our ML algorithm, we aim to help mitigate future fatalities and strive closer towards eradicating the virus and moving forward in our day-to-day lives. What it does 1. Vaccine Prioritization for Hospitals and Clinics: Hospitals and clinics may simply upload their existing patient data (CSV) or create new entries within their web portals, and receive priority values for all of their patients based on our machine learning algorithm. Following this calculation, the app automatically sorts all patients according to their priority of receiving vaccines. 2. Mortality Prediction: Using key factors such as the person's age, gender and pre-existing health conditions, our Machine Learning model calculates the patient’s probability of death due to COVID-19. This decimal value between 0-1 constitutes their priority value. 3. Patient Notification: Based on their prioritizations, patients will receive alerts via SMS to schedule their vaccination appointments with their registered hospital or clinic. 4. Scheduling (work-in-progress): With access to patient data, prioritizations and the notification system, our app can seamlessly integrate a system that manages the scheduling process for hospitals and clinics, all done through their web portal. Technologies Used Front-end development: React. Back-end development: Node.js, Express. Machine Learning: Python, Pandas, Numpy, Sklearn / (Fast.AI) Cloud: Google Cloud Platform, Firebase. Database: Dropbase, Firestore. Communication with patients: Vonage API. How it works Front End: Our clinic facing web application is built on React with UI components and styling coming from Material UI. The front-end application brings together almost all of the major cloud services we utilize including Firebase, Google Cloud, and Vonage. The front-end features an email/password signup and login, patient record creation form, bulk csv upload component and actions to fetch prioritization data and notify patients through Vonage. The primary data table component hooks into Firestore onSnapshot method allowing it to reflect changes in the Firestore db in real time. Back End: We stored our patient data in a Firestore db with a collection of patient records associated with each clinic user. Sign up, authentication and storage account data are all handled using the firebase auth sdk. Using both Google Cloud Functions and Firebase Cloud functions we created endpoints to trigger generation of prioritization data from our ML model and trigger SMS notifications through Vonage respectively. Machine Learning: We obtained case-by-case data of patients who were tested positive for COVID-19. The input parameters include their age, sex, and prior medical conditions, and the output is death/recovery. This is used to train a logistic regression model that is ultimately able to take in the parameters of any individual and output the probability of death due to COVID. Additionally, we trained a deep neural network for comparison, and found that performance between the two models are similar (based on precision/recall scores). Dropbase Pipeline: Through Dropbase, we were able to import raw data using CSV files and complete data processing using pre-built and custom data transformation functions. After processing, we were able to export the data and set up a live database and a Rest API. We set up a Dropbase pipeline specifically to clean ML data sets (i.e. removing unnecessary columns), which are then stored in our live Dropbase DB. This provides us 2 major advantages. First, whenever we want to retrain our ML model, the cleaned data set can be automatically fetched from Dropbase DB. Second, whenever we want to add additional datasets, it can easily be done from our React front-end by making a POST request to Dropbase DB. Challenges we ran into One of the biggest challenges we faced early on was obtaining the data set to train our machine learning model. The vast majority of publicly available COVID-19 data sets are too simplistic and are targeted towards epidemiology studies. More elaborate patient data are typically restricted to researchers authorized by the government and hospitals. We had to dig really deep to find a peer-reviewed research paper that shared their data set that included informative case-by-case data. Another big challenge we had was deploying our predictive model via Google Cloud Functions. Since testing of a production function often requires lengthy redeployment, finding and eliminating bugs related to authorization keys, environment variables and request shaping can often be tricky and time-consuming. Fortunately, with the help of a mentor we were able to slow down and debug more methodically between deploys ultimately narrowing us down to the root of the problem Accomplishments that we're proud of Rapid prototyping using firebase and material UI Bringing together a variety of different technologies and services into one cohesive product What we learned How to deploy a machine learning algorithm using Google Cloud Functions How to interact and work with a variety of languages and services (e.g. Python for Machine Learning and Cloud Functions, JavaScript/React for the Web App) How to leverage Firebase SDK’s for rapid prototype development (Auth, Firestore, Cloud Functions) What's next for PrioVax Training our ML model on larger data sets using Dropbase. Providing advanced scheduling features for vaccination appointments with easier two-way communication and better automation. Provide more avenues for contacting patients through Vonage such as messenger and whatsapp messages. <div