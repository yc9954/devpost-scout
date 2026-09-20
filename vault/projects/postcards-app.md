---
slug: "postcards-app"
url: "https://devpost.com/software/postcards-app"
title: "Postcards App: personal push notifications with an API call"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 857
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Postcards App: personal push notifications with an API call

> Turn your phone into an IoT alarm with a simple API call

[Devpost](https://devpost.com/software/postcards-app) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** android, firebase, kotlin, node.js, postman, typescript

## How they structured the write-up

- inspiration
- what it does
- use cases
- sample use cases collection
- how we built it
- challenges we ran into
- tech stack
- accomplishments that we're proud of
- what we learned
- what's next for postcards app

## Body

Home screen API key and instructions Get key and instructions on email Send push notification Caught pokemon types Inspiration Ever leaked an API key in a public workspace, and got email spammed by Postman? Did your Postman monitors go haywire in the middle of night, but you were fast asleep and missed the alert? You're not alone. Lot of companies like Postman use email for alerts, due to its ubiquity and ease of use. But email notifications have some drawbacks: We get a lot of emails. Important mails can end up in promotions or spam folders. Email apps have an uncharacteristic alert sound. All emails sound the same. You may be asleep. Missed emails can cost your business. Keeping track of such alerts can be a stressful task, as one needs to look at every incoming email alert. We faced this problem at work, where we need to respond to e-commerce purchases on our app. We wanted a platform which is reliable, programmable and simple to use. Push notifications fit the bill, but not every developer can have a personal app for their notifications. Postcards app is an elegant solution to this problem. What it does Postcards is Twilio for personal push notifications. You can turn your phone into an IoT alarm with a simple API call. You can send postcards How it works Install app to get API key. No sign up required! You can optionally get API key and instructions delivered to your email. Send Postcard using the REST API. The API key uniquely identifies your device. Get the alert on your phone! Use cases Any place where rapid human action is required, in response to a computer event. Server meltdowns. E-commerce purchases. Your personal burglar, fire, zombie or radiation alarm. If you are an indie or small developer, this will help you do things that don't scale . Get alerted in real time and do behind the scenes manual work. Tl:dr- the limit is your imagination. Sample use cases collection Look at the sample use cases collection in this workspace for examples. Pokemon catcher bot We've converted PokeAPI into a Pokemon catcher bot using Postman monitors! Every hour, the bot encounters a random Pokemon. You have a 40% probability of catching the Pokemon. If you are lucky, you'll get a Postcard notifying about your successful catch! Pokemon type visualizer After building your dream team, are you looking to challenge the Elite Four? Know your odds by finding what types of Pokemon you have! This uses the GET API to fetch all postcards, and displays them using Postman visualizer API. Server latency alert Compliment your Postman latency monitor with a Postcard notification! The test script sends a postcard every time latency is higher than 1000 ms. How we built it A Firebase Cloud Messaging (FCM) token and API key is generated when user installs the app. User uses the key to access Postcards API. For example, user can send a postcard notification or get a list of his existing postcards. The postcards API is hosted on cloud functions. Cloud function validates data and calls FCM API to send push notification. The data is also saved in Firestore database, so user can view it. API documentation is hosted in a Postman public workspace. Twilio Sendgrid is used to send API key and workspace link to user's email. Challenges we ran into Platform fragmentation : We wanted the app to make a customized notification sound. This requires native device APIs, which are different for iOS and Android. I decided to use Android over React Native due to this reason. Android API compatibility issues : The notification API changed in API 26 (Oreo), where notification channels were introduced. This means version specific code for needed for older and new Android versions. Tech stack Firebase cloud messaging (FCM): For push notifications Firebase cloud functions and Node.js: For compute Firestore database Android app: Kotlin, MVVM, Retrofit Postman public workspaces for API testing and documentation Twilio Sendgrid for email Postman features used Public workspace, collections and requests (GET, POST, PUT, DELETE) API : Holds OpenAPI 3.0 documentation Environments : Contains API key and endpoint Mock servers and test scripts : To check for API uptime, and for Pokemon and latency examples. Visualization API : For Pokemon example. Used to display Pokemon count per type. Pre-request script : To generate random number for getting random Pokemon. Accomplishments that we're proud of Postcards solves my own problem of missed email alerts. Hopefully the community can also find it useful. Built and launched my first open-source SaaS. What we learned Postman public workspaces are a complete and much better replacement to self-hosted swagger pages. It's an integrated platform for API development, testing and collaboration. Firebase is a great platform for rapid app development. What's next for Postcards App Provide support for older versions for Android. iOS app. Explore monetization options like Google Ads and GitHub sponsors. Monetization can be tricky because the app is free and open source. Start a Discord server and build a developer community around Postcards. Build a nice website for the app. Launch on Hacker News and Product Hunt. <div