---
slug: "medic-android-app"
url: "https://devpost.com/software/medic-android-app"
title: "Medic Android App"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 317
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Medic Android App

> Medic App helps you to search the usage of the medicine just by pointing the camera on it. It also shows some helpful stuff like your BMI and current Covid cases.

[Devpost](https://devpost.com/software/medic-android-app) · hackathon [[Cloud Native Hackathon]]

## Facets

**substrate** [[video_visual]]

**stack** covid19, firebase, firebase-auth, google-web-authentication, react-native, rncamera

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for medic android app

## Body

Inspiration Our inspiration to execute this idea and to built this Medic android app came from our personal day to day life experiences, as we have a lot many medicines in our medical kits and often get forget that which medicine of what use. And personally we think that it happens with almost everyone. So keeping this in mind we decided to create something that helps people to identify the medicines and can keep updated their medical kits instead of just throwing out or going out to the medical store to ask the same about the medicines. What it does Medic App helps you to search the usage of the medicine just by pointing the camera on it. It also shows some helpful stuff like your BMI and current Covid cases. How we built it We first created a camera screen. Tried clicking a picture with it. Stored the pic in cache. After clicking the picture we extracted the text or string from it. and finally returned the usage of the medicine. and also - in addition to this we added a feature for the user to track their BMI(Body Mass Index) just by putting their weight(Kg) and their height (cm) and added Covid-19 active and confirmed cases, deaths and recoveries of India. Challenges we ran into Challenges we have faced are- Couldn't find any free medicine API that provides the usages of the medicines. So right now for this this project we have used Firebase Firestore to store the data of medicines. What we learned How Google Auth web API and Firebase Auth works. And learned about storing and fetching the data from the Firestore. Learned how RNCamera works. What's next for Medic Android App Right now we just added few medicines and their usages in the Firestore but in future we can add more medicine data to it and can improve the scanning feature. <div