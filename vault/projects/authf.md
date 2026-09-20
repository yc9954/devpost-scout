---
slug: "authf"
url: "https://devpost.com/software/authf"
title: "Faceable"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 518
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Faceable

> Facial multi-factor authentication for web apps, using Face API of Azure cognitive services.

[Devpost](https://devpost.com/software/authf) · hackathon [[Azure AI Hackathon]]

## Facets

**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** .net, azure, c#, cognitive-services

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for faceable

## Body

Inspiration I have already worked on other projects with Azure Face API, but I saw something that had not yet been exploited in facial recognition, which was used as an authentication system, since using mobile apps or SMS makes the user dependent on having a device, being that it is safer from our perspective of "what you have" to "who you are". What it does Faceable is a system that allows you to authenticate to a website by means of your face, after registering with a username and password, you must register your face, and to access the app, the system always forces the user to enter their access and show their face to confirm that the person is who they say they are and access the app. In addition, it allows you to configure the percentage of precision to access (the higher the percentage, the more secure) and everything goes directly to the Face API, without storing the users' images (more privacy). Finally, this demo has a forum, just to test access through authentication, developed using C # with MVC framework and published on Azure. How we built it I did it using .NET, specifically C # with MVC framework with the Visual Studio IDE, and an Azure App Service was created for the demo, while the database is in Azure SQL Database (we think that for testing purposes it is reasonable) and the Azure Face API cognitive service for facial recognition. To control that only users who showed their faces can access the app, we created a very simple MVC attribute that only allows access to pages if the user has fully logged in. Also taking advantage of gesture recognition, the user who wants to enter must smile. Challenges we ran into The biggest challenge is preparing for users who don't have such good cameras for facial recognition (cell phones, old computers, etc.), so I thought it best to let the users themselves set a minimum percentage of accuracy (between 75% and 95%), and that the system will send directly to recognize or register the face, without saving a single image in Blob Storage so that users from the beginning have control of their own information. Accomplishments that we're proud of Take the use of the Face API to a more natural and simple theme for all users, that is, that this great Azure service can be used by the entire community in a simple way, which I think is my greatest achievement in this project. What we learned I learned more about the Face API, although I had already worked with this cognitive service, I took advantage of reading all the documentation, but also understanding and working exploiting an area such as multi-factor authentication (MFA) with non-technical users who could take full advantage of this technology. What's next for Faceable I want to promote and create Faceable as a service, which allows any website to implement multi-factor authentication (MFA) in a simple way, without further technical knowledge, and that for users is a secure system that maintains their privacy and control over their data. <div