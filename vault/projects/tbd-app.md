---
slug: "tbd-app"
url: "https://devpost.com/software/tbd-app"
title: "NLB"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 545
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/financial_record"
---

# NLB

> Life is busy, sometimes we forget things. Let NLB help you out. Never forget what to buy again. Bill splitting for large groups made easy. Made by roommates, for roommates (and family and beyond)

[Devpost](https://devpost.com/software/tbd-app) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]] [[retail_commerce]] [[transportation]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[financial_record]]

**stack** apple-kit, computer-vision, firebase, google-gemini-api, ios, ocr, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nlb

## Body

logo login/signup Home screen - location and list to get adding items to list screen Notification when you have items nearby adding/viewing group members split bill initial screen assign items to bill get total owed parse receipt Inspiration We often have incidents where we remind friends, family, or even ourselves to pick up groceries or some other item, and in our busy lives these small errands can end up being forgotten and put off over and over. Theres also been so many times that among a group of us, we have had to split a large bill requiring some manual calculations to be done that could have been automated, saving time. What it does That is why we made NLB (Nothing Left Behind). NLB is a location-based reminder app that notifies you when you're near stores with items on your shared shopping list, ensuring you never forget to pick up what you need while you're already out. It also features AI-powered receipt scanning that instantly extracts items and splits bills among group members, making it the ultimate convenience tool for roommates and families managing shared expenses. By adding members to a group, users can have a shared list of items needed to buy. Using the members’ locations, NLB knows when these items are nearby and can be picked up quickly. NLB relieves the user of needing to remember these small tasks and sends notifications to remind the user as they’re driving, all while keeping a combined and updated list for every member of the group. In addition, if you need to split a grocery run with members in your group, NLB allows an easy approach to uploading a receipt, assigning items to members of your group, and getting the total each person owes quickly. How we built it Built with SwiftUI, Firebase (Authentication & Firestore), CoreLocation for geofencing, Vision framework for OCR, and Google Gemini AI for intelligent receipt parsing. Challenges we ran into A big challenge we ran into was the receipt scanning, as it wasn't parsing properly for a while. Initially we were just using the vision framework for OCR and attempting to list the items from there, however this kept running into errors which is when we thought of integrating google gemini's API. Since the text was being recognized properly, our only issue was making it into a list, which is where prompting gemini with the recognized text simplified the process. Accomplishments that we're proud of We are proud of solving a problem that we have personally faced among our friends and family. The app is intuitive and easy to set up and understand, and we can see ourselves and others making good use of it. Technically speaking, being able to implement such an intuitive app in a 24 hour window with a tech stack that we had never worked with before was something that we are really proud of. What we learned Technical Skills - Swift, Firebase, Authentication, OCR, Computer vision Non Technical Skills - worked with iterations in an agile way, move fast, understand a problem from a consumer standpoint and figure out a solution for it and implement it. What's next for NLB automated payment link (venmo/zelle) voice notifications so that a driver doesnt look at their phone <div