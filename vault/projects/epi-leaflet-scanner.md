---
slug: "epi-leaflet-scanner"
url: "https://devpost.com/software/epi-leaflet-scanner"
title: "ePI Leaflet Scanner"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 855
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# ePI Leaflet Scanner

> An iOS mobile app powered by Blockchain. We connect the patients with the pharmaceutical companies, by helping them read medical leaflets easier and more efficiently.

[Devpost](https://devpost.com/software/epi-leaflet-scanner) · hackathon [[HackZurich 2021]]

## Facets

**domain** [[civic_government]] [[health_clinical]]
**user** [[government_staff]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** firebase, infura, remix, solidity, swiftui, web3swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for epi leaflet scanner

## Body

Scan, Zoom, Find, Read Architecture Overview Every leaflet can be added in multiple languages Scan the QR-code from the package Zoom-in if the font size is too small Zoom-out Don't waste time scrolling, find what you need easier Advantages Inspiration Every year more than 500km of leaflets are produced by pharmaceutical companies. However, most of them end up in the trash, which is really bad for the environment. The only solution to mitigate that problem is to introduce digital leaflets, however, their protection is very challenging. If we store a digital leaflet on a centralized server, it doesn’t matter how well protected it is, there is always a chance to be hacked or manipulated without the knowledge of the company producer. This is caused because of insufficient transparency in the processes. What it does Our team has developed an iOS mobile app, which is connected to Blockchain smart contract in order to provide full transparency and immutability of the process. Whenever a new medical leaflet is created, the “Health authorities/Regulators”, which approve it can vote inside a smart contract which is deployed to Etherium. That makes the entire voting process accessible to the end-users( the patients). Let’s imagine that they vote for the approval of a new Covid Vaccine in Europe. If the vaccine is approved, the first smart contract will upload its pdf leaflet to a centralized server like Firebase or AWS, and will produce a SHA256 digest which will be uploaded to a second smart contract that is connected to an iOS app. We need 2 smart contracts, because the first one is accessible only from the pharmaceutical company and the health authorities, unlike the second which is accessible only from the patients. The end users/the patients will download our app on their mobile phones and will be able to scan a QR code from the package of their medicaments. The app will then fetch the data from the server and compare its hashed value with the hashed value deployed on the smart contract. If they match, that means the leaflet was approved, if they don’t, that indicates a problem. Common problems might be either the health authorities haven’t approved it, but the medical company has begun to sell them or a malicious hacker has modified the leaflet from the server. Both issues are resolved in a matter of seconds, because the end-users will be able to read only approved leaflets. Not-approved ones will be hidden to avoid any potential health threats. Due to the lack of time, we couldn’t develop a User-Interface for the health authorities to interact with the first smart-contract, but in the video, we demonstrate how it should work. If you find it challenging to convince every health authority in every country to use a smart contract, you can always use it internally inside the pharmaceutical company. That will provide more visibility in the process of creating and updating a medical leaflet. Advantages for the users: Easy to use interface Multi-language accessibility Easy to read leaflets (Zoom-in, Zoom-out) Easy to navigate leaflet (Search for key words) How we built it The application was build using Xcode and SwiftUI, where we use the iPhone camera to scan the QR code and compare the data from Firebase and Etherium. The connection to Etherium is done via Web3Swift and Infura Gateway. The Smart contracts are build using Solidity and Remix. The pdf versions of the leaflets are stored in Firebase. Challenges we ran into The biggest challenge we faced during the development process was connecting the iOS app to Etherium. This was done using a framework called Web3Swift, however, we are building the app using SwiftUI which was not compatible with the current version of Web3Swift. We chose to use SwiftUI because it provides opportunities to deploy the app also for iPad and Mac, which is very good since it is not limited to only iOS. In order to resolve the problem, we had to manually debug the library which caused many hours of work. However, if we hadn’t debugged it, the whole idea would have gone wrong, because if we don’t compare the hash saved on Etherium with the pdf file stored in Firebase, the idea would have been a simple digital leaflet without any protection. Accomplishments that we're proud of After searching in Google for similar projects, we couldn’t find any examples. That became our main motivation for the Hackathon, to develop something new, which has not been engineered yet. We are really proud of the results, because we have achieved our goal and have delivered a fully protected multi-language digital leaflet using blockchain and mobile app. What we learned We have learned how to connect an iOS mobile app to Etherium and how to securely protect digital information/files by hashing them and compare the resulted digests with their digital records stored on servers and their corresponding hashes stored on Etherium. What's next for ePI Leaflet Scanner Next step is to hear the feedback from the Jury and if the idea is accepted, develop an Android prototype in order to make it accessible to as many users as possible. <div