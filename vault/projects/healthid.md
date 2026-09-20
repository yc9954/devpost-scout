---
slug: "healthid"
url: "https://devpost.com/software/healthid"
title: "HealthID"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 795
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# HealthID

> An all-in-one health tracker with a unique passport to personal health.

[Devpost](https://devpost.com/software/healthid) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** figma, firebase, flutter, mobx, react, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for healthid

## Body

Inspiration With Covid-19 affecting virtually every aspect of our daily lives, the need for keeping track of our physical and mental health is at its peak. Getting anywhere nowadays requires extensive temperature testing, medical paperwork, and so much more. Each team member has experienced firsthand the effects of confinement and isolation on their health, whether it was an increasingly sedentary lifestyle, or a deterioration in mental health. With that, we wanted to create an app that not only keeps track of a user's daily physical and mental health conditions but also would make such information as portable as possible so that online doctors and testing centers can receive the most up-to-date information about the user. What it does HealthID aims to streamline personal health tracking through a comprehensive health logging system. Users may fill out a short daily form to record various activities such as exercise or sleep as well as any physical ailments such as a fever or cough. They may also choose to record any updates in their height or weight. These entries are saved to the user’s account, making it easy to track health-related changes. Users can share this information with others through a custom generated QR code and link, which brings up a website displaying all the user’s logs that anyone can access. Through a quick scan, all this medical information is easily accessible. While seeing doctors remotely, doctors may check a patient’s log to view any possible lifestyle issues that could cause disease. How we built it Mobile App We created the mobile app with Flutter and used Firebase Authentication, Cloud Firestore, and Cloud Storage to save and retrieve data. For more efficient state management, we used the MobX and Provider packages to serve data throughout the app. Website The website was built with React.js and integrates our Firebase Cloud Firestore database in order to read a user’s logs. This site is hosted on Vercel. Our domain name is healthid.tech. Challenges we ran into Our team members are all relatively new to web development, so one team member had to spend a number of hours searching and testing possible solutions for building a website that could integrate Firebase. In the end, we’re grateful that we found a solution in React.js. One team member is relatively new to Flutter—this is their first hackathon :). Learning Flutter development is not an easy task, but they figured things out after hours of intense work. Accomplishments that we're proud of We’re proud that in the end, all of our health logging features were completely integrated with Firebase, and we have an easy-to-use system for viewing a user’s profile. Everything in the app, except for our possible future feature of requesting doctors, is fully integrated with an efficient backend. We’re also super proud of the fact that we helped a new team member learn Flutter development—they made a ton of progress and ended up creating some incredible pages. What we learned MobX - This is our first time using MobX in an app, and it was amazing to see how quickly we could set up a backend using observables, actions, and reactions. React.js - We’re all quite new to web development, but after reading through a ton of articles, we’re happy to have produced a clean website that’s integrated with Firebase and is unique to each user. Vercel - Our first time using Vercel to host a website—it’s GitHub integration is awesome. Figma - None of us have designed much with Figma before, but we ended up creating some great designs together. Generating a unique QR Code - Using a Google API, we figured out how to create custom QR codes linking to a user’s website portfolio. What's next for HealthID In order to keep user’s medical information confidential and build trust, we plan to add protective security measures to our app in the future. Additionally, to maximize the potential for users to regularly and seamlessly track their daily health, we hope to sync our app with existing health trackers such as Fitbit, Apple Watch, Garmin, etc. We hope to allow not only users, but doctors, too, to interact with our app by letting them provide in-app suggestions that our users can easily access. Along with that, we also hope to add features that allow the app to suggest specific food and diet suggestions, helping users more swiftly reach their health goals. Adding more interactive interfacing, such as health quests and points, in our app is something we look forward to. Lastly, we would like to add features that allow users to follow others and share health goals and food suggestions. We had a lot of fun making this app, and we believe it has the potential to change how people track their health. <div