---
slug: "buzz-up"
url: "https://devpost.com/software/buzz-up"
title: "Buzz Up"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 709
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Buzz Up

> Buzz Up helps to find and connect to local Buzz in your locality for small unofficial events and discussions like Cricket Match on Sunday or Christmas Party in the Society.

[Devpost](https://devpost.com/software/buzz-up) · hackathon [[MongoDB World Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[general_public]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** android, android-studio, azure, geofencing, google-cloud, java, javascript, mongodb, mongodb-mobile, mongodb-stitch, serverless

## How they structured the write-up

- special features
- walkthrough
- mongodb products used
- extra tech stacks used
- team

## Body

Buzz-Up Demo link - https://www.youtube.com/watch?v=vi2PKOwkEqo Buzz Up is a Social App which lets like-minded people come together for a local Buzz around them. How often is it that we want to organise a cricket match on Sunday or host a house get together party for all your local folks or maybe just a simple elClassico Screening in the local bar? We often tend to be limited about knowledge of such local events. Buzz up lets you know about all the Local Buzz happening around you. It has been fully powered with MongoDB Stitch and MongoDB Mobile with Sync to get the best of Serverless, Geofencing and Synchronisation into your app. Special Features The chat system is fully built over MongoDB Mobile with sync. All the local Buzz' are synced to your local db and can be accessed even when internet goes out. Google Maps and Places API have been integrated to support real time location features and travel to the Buzz. Trigger have been used for both Chat system and Email Notifications for new trending Buzz around the user. The backend is completely powered by MongoDB (Stitch and Mobile) only. Walkthrough It starts with a login screen, asking for Google Login. Once logged in, It will show you the Top Trending Local Buzz in and around you, typically upto 2 miles. These Buzz have been ranked based on User popularity and user engagement. We can add a New Buzz by clicking the plus icon on the bottom right. It will ask for a Buzz Name (which should be a single word hashtag), the Date till which the Buzz should be active and the location of the Buzz happening nearby. We can set the location to Current User's location, or pick one from Google Maps. When created, it will be directly synced to Atlas and your own local device. By any chance, if your net connection breaks down, Buzz up will still allow you to create a new Buzz and will sync automatically. It allows you to check your own hosted Buzz' in the profile section, which even works when you are offline. You can click on any Buzz, and it will open up a chat room for that particular Buzz. This chat system has been also fully developed using MongoDB Mobile, with appropriate optimisations, to harness the power of Sync. Let's add a new message by another device now and see how long does it take to appear. You can discuss, chat and get to know each other, without your private details such as email or phone number being leaked to the public. Additionally, each Buzz has its own information page, where you can check who hosts the Buzz and till when would it be active. Each information page also provides you with a "Go to location" button which will open up Google Maps for you to visit the Buzz location on the event date. The owner or host, can also modify the information of their Buzz which will be reflected as soon as you have a working internet connection. In the end, each user would be subscribed to the Buzz Up mailing list. Users can get an automated email when a new Buzz goes trendy around them, or could get a listing of such Buzz on say, every friday. This has been done by using Stitch Triggers and Azure Logic Apps. Setup Git clone the repository. Import the stitch app in folder stitch-app . Create a new file secrets.xml in the path - path_to_repo/app/src/main/res/values and add 3 strings as follows - <?xml version="1.0" encoding="utf-8"?> <resources> <string name="initialiseClient">Your Stitch App ID</string> <string name="serverAuthCode">Google Web App Client ID</string> <string name="googleApiKey">Google API Key for GMaps and PlacesAPI</string> </resources> Keep in mind to also generate an Android App cred in Google with your SHA1 key for Login. Open the app in Android Studio and build. MongoDB Products Used MongoDB Atlas - For mainting the database on Cloud and integrate with Stitch. MongoDB Stitch - Mainly for Geofencing queries, auth and servcies. Mongodb Mobile with Sync - For every other Backend Operation. Extra Tech Stacks used Android Studio Google Cloud Apis - Maps and Places API Microsoft Azure - Logic App to send customised Email Triggers Team Shrey Batra and Nishtha paul <div