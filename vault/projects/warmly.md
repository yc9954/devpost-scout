---
slug: "warmly"
url: "https://devpost.com/software/warmly"
title: "Warmly"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 541
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Warmly

> Use AI to never send a cold email again.

[Devpost](https://devpost.com/software/warmly) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[legal_justice]] [[media_journalism]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** javascript, nltk, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for warmly

## Body

Inspiration Only 3% of cold emails receive responses. These responses can range from "Yes", "No" to "Hell No". I know this because I've been doing enterprise sales for the past 3 years. All the sales experts recommend taking time to research your prospect and compose a very personalized message that is full of context, mutual interest, and a compelling reason to connect. The problem is that it can take nearly 20 - 45 minutes to send one great email. What it does We built a chrome extension that creates personalized emails in seconds. Warmly will search the web for blogs, news or related published content. It will then score the search results based on contextual relevance and creates a personalized message. This message can be copied and paste into an email client. Voila! A personalized message in seconds. How we built it We built the google chrome extension in javascript using gmail.js, an open source framework. The backend was written in python using NLTK and hosted on Azure. Challenges we ran into Summarizing articles and scoring relevancy is hard, but creating a consistent personalized message is extremely challenging. In order for it to consistently work, we had to train our AI system for StudyTree (Ethan's startup). To overcome this challenge, we will allow users to input more information so Warmly can learn how to better warm cold email. While using AI to create a unique personalized message is the goal, often times it is simply not possible due to lack of data. In these scenarios, we supply the end users summary, keywords, quotes, and mentions about the target which enables them to create their own message. AI + Human still drastically reduce research and personalization from 20 minutes to only <2 mins. Accomplishments that we're proud of Emails response rates jumped to 25% when mutual interest was added via Warmly. All of our team members brought something different. Chris wrote the chrome extension. Brian, Leon, and I (Ethan) wrote the backend and AI system. Larissa helped connect us with PR firms in NYC that are interested in piloting our technology. We had a mix of technical and nontechnical teammates that made Warmly a reality. For the past few weeks, I've used warmly to connect with investors regarding my startups Series A. I now have partner meetings with a number of VCs. Literally, we are using AI to raise a Series A. What we learned Since Warmly only workes when there is mutual interest, the technology will cut down on overall spam emails as we scale. After speaking with both decision makers who receive cold emails and vendors of technologies, we have learned that both parties want to connect with each other when interest and goals align. What's next for Warmly New UI to make it fresh and clean for TechCrunch Disrupt. Warmly will be free for anyone to use but we will monetize B2C via a subscription with premium features. We will also allow for enterprise customers access via B2B options. These customers will be PR firms, journalist, lawyers, and large sales teams. A few premium features that have been requested by PR firms. 1) Upload CSV document of emails and create personalized messages. 2) Real-time updates 3) Training Warmly <div