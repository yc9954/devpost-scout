---
slug: "kyt-know-your-traveler"
url: "https://devpost.com/software/kyt-know-your-traveler"
title: "KYT: Know Your Traveler"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 408
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "substrate/medical_record"
  - "substrate/video_visual"
---

# KYT: Know Your Traveler

> A privacy-focused digital health passport that helps you to securely store all your health records and enables you to validate against COVID-19 without revealing any of the underlying health data.

[Devpost](https://devpost.com/software/kyt-know-your-traveler) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[health_clinical]] [[labor_employment]]
**substrate** [[medical_record]] [[video_visual]]

**stack** azure-app-services, azure-cognitive-services, azure-face-api, cosmosdb, dart, express.js, firebase, flutter, imagevision-facedetection, javascript, node.js

## How they structured the write-up

- background
- problem
- what it does
- core technologies
- challenges we ran into

## Body

welcome register login upload home valid test details invalid test details qrcode settings edit profile about report a bug Background The world is facing unprecedented global health, economic, and social emergency due to COVID-19. However, there is a renewed hope with the accelerated vaccine development and pilot program launches. Economy, business, and work have to continue and catch up to their usual pace—and all countries together have to find ways to combat the unprecedented rise of unemployment. Alongside, as the world becomes more and more reliant on technology, we believe it is time to digitize a person’s health data and make it accessible in a contact-less approach—a one-stop unique digital health passport. Problem COVID-19 test/vaccine reports will be a mandatory requirement for traveling or going to large workplaces/public gatherings. But is the go-to way of doing things the ideal way? What it does The KYT mobile app is a privacy-focused digital health passport centered around COVID-19 which helps you to securely store all your important health records and enables you to validate against the virus without revealing any of the underlying health data. A user can add test results to their profile by uploading their original report. The uploaded picture is validated by the KYT API which is powered by Azure technologies. And, if the reports are valid, it creates a record for the user on their uniquely assigned KYT Number. The user can then simply show their unique QR Code which will verify them based on the verified medical records they have added to their profile. Alternatively, travel, tourism, and workplace organizations can use the user’s KYT Number using our API endpoint to validate their medical status—without actually revealing any of the underlying data. Core technologies Our app is powered by Azure technologies. We utilize the Read API and the Text Analytics API, along with Google Cloud NLP, for our medical report verification system. The user's profile photos are validated using the Face API; the user records are created on MongoDB using a CosmosDB wrapper. We also utilize Firebase Authentication and Cloud Storage for our auth system and storage bucket. Our API is hosted by Azure App Services. Challenges we ran into Going about the two endpoint Read API system was a challenge, and we had to implement a recursive function to solve it. Another challenge we faced was getting the original date from the uploaded medical record, which we solved by using various RegEx expressions. <div