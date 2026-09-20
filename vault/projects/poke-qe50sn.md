---
slug: "poke-qe50sn"
url: "https://devpost.com/software/poke-qe50sn"
title: "Poke"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 419
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Poke

> A platform that reminds you to reach out to people you know. Stop struggling with spreadsheets of contact information and inconsistent phone reminders--just use Poke.

[Devpost](https://devpost.com/software/poke-qe50sn) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[cross_origin_web]]
**user** [[general_public]]
**substrate** [[structured_db]] [[web_dom]]

**stack** css, firebase, firestore, html, javascript, react, render, typescript

## How they structured the write-up

- target tracks
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for poke

## Body

About the Project Target Tracks most likely meme startup lowkey actually kind of good i'm just a chill guy Inspiration I’ve always had a hard time remembering to reach out to people I meet. After talking to my friends, I realized that most of them had the same problem. To address it, I had been using a messy spreadsheet to keep track of contact information, but it wasn’t the seamless solution I was looking for. Together, Alex and I decided to bring the idea of Poke to life. What it Does Poke helps users reconnect with the people they know by sending reminders. Users can choose to "poke" or reach out to a contact or "pass" to snooze the reminder for another time. It’s designed to make maintaining connections easy and engaging. How We Built It We built Poke using: Firebase for authentication and backend database services. Firestore as our database for storing user data and contacts. React for the frontend. HTML, CSS, JavaScript, and TypeScript for creating clean, responsive webpages. Render for deployment to production. The backend connects the front end to Firestore to store and retrieve data seamlessly. Challenges We Ran Into Firestore Read Limit : One night, I ran over the read limit for our free Firestore database, which significantly slowed down development. LinkedIn API : We wanted to allow users to sign in with LinkedIn and automatically query their connections. However, the LinkedIn API requires approval to use, which involves proving we are a legitimate business with a website, address, and LinkedIn page. The approval process also takes considerable time. SendGrid Integration : We wanted to implement reminder emails, but SendGrid requires a registered business email with a custom domain, which we didn’t have at the time. Accomplishments That We’re Proud Of Successfully setting up endpoint protection for our Firestore database to ensure data security. Allowing users to upload their contacts via CSV for a streamlined experience. Deploying to production on Render, making the app accessible to the public. What We Learned How to use Render for deployment. The importance and setup of endpoint protection for databases. How to integrate authentication into a React project effectively. What's Next for Poke Releasing the webpage to the public to collect user feedback. Implementing the reminder email feature to notify users about their contacts. Adding a feature to prioritize contacts with upcoming birthdays or significant events, so they appear at the top of the reminder list. Exploring ChatGPT integration to provide smart suggestions for reconnecting with contacts. <div