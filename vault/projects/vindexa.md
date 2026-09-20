---
slug: "vindexa"
url: "https://devpost.com/software/vindexa"
title: "Vindexa"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 801
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Vindexa

> Extract rich insights from videos, seamlessly translate videos into multiple languages, explore visual emotions and sentiments all on one interactive portal. Powered by Microsoft's video indexer APIs

[Devpost](https://devpost.com/software/vindexa) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** .net, app-service, azure, azure-cognitive-service, azure-datalake-storage, azure-media-services, azure-sql-database, azure-vide-indexer-api, c#, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vindexa

## Body

Vindexa graphs Demo thumbnail Inspiration This project was inspired by the desire to connect people despite their language barriers. Later on, we were also inspired by the prospect of giving people insight into human emotions and sentiments based on their facial expressions and tone of voice. What it does Vindexa accepts videos from users and then carries out extensive indexing operations using Microsoft Video Indexer APIs. The result of this indexing includes the following: Closed captioning of the video Translating the captions into any of the 54 available languages. Ability to edit video transcript Ability to download transcript Ability to assign names to recognized faces Identification of celebrities Count of number of people in the video Identification of faces in the video Identification of key topics discussed in the video Identification of named entities (locations, people, things) and keywords Identification of emotions and sentiments displayed in the video Identification of brands and written text in video Detection of scenes and keyframes for editing Graphical display of the trend in emotions and sentiments in the video How we built it The Video indexing capabilities were implemented by using Microsoft Azure's Video Indexing APIs. In order to gain access to the APIs, we had to register on the video indexer developer portal and get subscription keys. We were then able to get access tokens using the authorization API. This gave us access to the Operational APIs that included services such as Indexing videos, creating projects, and so on. You can check out the catalog of APIs here . In order to make the most of the application, we needed to upgrade from a trial account to a paid account, so that we could get some of the features to work. We built the backend using .Net core, while the front end was built using Javascript, HTML, and CSS. We stored the videos being uploaded from the platform into Azure storage and their corresponding URLs into a SQL database. We then passed the URLs of the videos to the Indexer API to perform the indexing operation. The results from the indexer API were gotten by calling the player widget, insight widget, and index API. The widgets contained the extracted insights, the original video, and other metadata including the transcript and rich customizations that the user can easily take advantage of. While the index API returned the video insights JSON, which we used to plot the video sentiment and video emotion charts. We wanted a way to show the numerical insights that were extracted which included the sentiment scores and emotion weights. We tried Power BI but we changed our approach because Power BI would require users to have a license. So, we decided to use amCharts - a javascript library for making dynamic charts. This presented a learning curve, but we were able to pull it off. Challenges we ran into Video indexer APIs were unavailable at random times because the service was undergoing maintenance. We were unable to save or edit projects using both the API and the editor widgets. We reached out to ask questions on stackoverflow but the solution provided did not work, so we focused on optimizing the features we had gotten to work. This issue also prevented the video editing widget from working. Deploying the web app to azure was a minor challenge. But we figured out that it was because of the configuration of the App service that we chose. Once we changed it from a Linux hosted plan to a Windows plan, it worked like a charm. Understanding the documentation for some of the indexer APIs. Some of the documentation on the APIs are outdated, while some are just non-existent. We believe this is because some of the services are still in preview and there is nothing we could do about that. We had to learn javascript to implement the styling and functionality of the application. We ran out of Azure credits 2 weeks before the submission deadline. Thus, we had to create a new subscription, re-create all our resources again, and update our code accordingly. We implemented the streaming feature and got it to work with OBS studio, but it was too costly for us to keep running. This was a huge blow to us as this was meant to be our icing on the cake. We had to divert our attention to other features. Accomplishments that we're proud of Learning Javascript on the job. Getting amChart to work with our saved data. What we learned How to use azure media services for indexing and editing videos Javascript Learning how to implement streaming and auto-captioning with Media service APIs. Video editing with OpenShot What's next for Vindexa Implement Live streaming for Video Indexer. Implement an account-based system for the Video Indexer. Implement the edit feature. <div