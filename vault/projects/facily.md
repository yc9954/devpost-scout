---
slug: "facily"
url: "https://devpost.com/software/facily"
title: "facily"
hackathon: "Junction 2016"
winner: true
words: 767
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/sensor_fusion"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# facily

> Getting problems fixed with a single picture.

[Devpost](https://devpost.com/software/facily) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[provenance_signing]] [[sensor_fusion]]
**domain** [[labor_employment]]
**substrate** [[video_visual]]

**stack** android, apache, azure, django, ionic, ios, python, sketch, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for facily

## Body

Employee: Incident Overview Employee: Report Incident Employee: Select topic Employee: Add details Worker: Overview Worker: Incident location Worker: Navigation Inspiration We all know this situation: You have an important presentation and the beamer is not working. Nowadays you pick up the phone and call up the facility worker or write an email. After a while the guy will eventually show up, analyse the problem, go back to get some additional tools and finally solve it. In the mean time you and 10 other people are waiting without knowing what is going on... Reporting and tracking incidents should be easy and efficient, everyone wants them to be fixed asap. There are many powerful tools that try to solve those problems, but they all lack one important thing: Simplicity. What it does Facily enables employees to create a service request by taking a single picture, the software will take care of the rest. By combining a powerful machine learning driven backend and UX optimized user facing apps, the system we are offering brings your incident reporting to the next level. The system uses machine learning to automatically classify your request and assign it to the best suited service worker. Context information (e.g. sensors and historic data) allow us to automatically determine the urgency of an issue, as well as provide smart suggestions to both the employee and the service worker to fix the problem asap. Guided by these suggestions an employee will be able to do simple tasks and sometimes even resolve his problem before an issue is generated. How we built it Both user-facing apps, are built with Ionic 2 and therefore support Android and iOS. The main goal for the employee app is to create a straight forward reporting process, that's why we decided to build it like a conversation. By leveraging machine learning and context information, the user's input is kept to the bare minimum making it very straight forward and fast to report the incident. The worker app provides the user with the needed context information to keep the round trips between service location and storage rooms to the bare minimum and empower the service worker. Both apps communicate through a horizontally scalable python Django backend hosted on Microsoft Azure and use the latest machine learning algorithms to classify incidents and provide the needed context information. Challenges we ran into Besides the usual coding issues, our main challenge was to keep focus on our initial goal: A simple solution for the user with a great user experience. The temptation was big to try to integrate every sensor available and display it to the user. But the key to success is to do one thing, and do it well. Once the app is working as intended, new features can still easily be added. But it's important to stay focussed on the task at hand. Keep it simple, stupid! Accomplishments that we're proud of The user interface is very intuitive and fun to use. Using machine learning to classify images as well as learn from the context information to automatically create tasks. Another interesting aspect is that the system can automatically train itself by using the pictures and data provided by the users. What we learned It is important to define the main goal of the app early. We spent quite some time even later during development to resolve differences of opinion about some aspects of the app, even though we had discussed them before at some point. What's next for facily There are many more ideas we could not implement because of the limited time. The user facing app will remain approximately the same too keep its simplicity. However, the worker app, as well as the backend, can be easily extended. Some ideas we had include: Detect duplicate issues and combine them automatically Give suggestions of parts to take for the service worker based on topics Detect urgency based on environment Customers involved/nearby => critical A lot of people near asset => urgent Multiple duplicate issues => high Assets can be marked as important Anomaly detection to find issues A desk has been unused for a week Printer did not connect during working hours Asset has not been used for an unusual amount of time Train new assets by using pictures taken by employees Allow employees to give a signature on the device Natural language processing to analyze written requests. Admin Panel to see overall performance measurements The appetite for efficient facility service solutions is huge, so our next step is to create a business plan, find possible investors and partners to promote the solution. <div