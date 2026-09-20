---
slug: "team-registration-ctr1qh"
url: "https://devpost.com/software/team-registration-ctr1qh"
title: "Rate My Drivers"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 303
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Rate My Drivers

> Introducing Rate My Drivers, an application that helps minimize auto insurance costs for both drivers and businesses, as well as improving driver experience.

[Devpost](https://devpost.com/software/team-registration-ctr1qh) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[accessibility]] [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, html, java, javascript, python, swift, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rate my driver

## Body

Inspiration We know that it can be hard to make ends meet sometimes, so our application helps minimize costs for drivers and businesses when it comes to auto insurance. What it does By utilizing a beacon/camera device placed in the dashboard of the car, we can record the driver and monitor the driver's eye motions and facial behaviors throughout the trip using Python and OpenCV. A grade is then calculated for the trip using the data from our image recognition model. This is then sent to a MongoDB, which keeps track of the history of each driver's grades for each of their deliveries. To effectively display this information to employers, we created an application using Next.JS to display the grades of each driver and the average. How we built it By utilizing a beacon/camera device placed in the dashboard of the car, we can record the driver and monitor the driver's eye motions and facial behaviors throughout the trip using Python and OpenCV. A grade is then calculated for the trip using the data from our image recognition model. This is then sent to a MongoDB, which keeps track of the history of each driver's grades for each of their deliveries. To effectively display this information to both the drivers and employers if businesses were to use this product, we created an application using Next.JS to display the grades of each driver and the average. Challenges we ran into Sending Open CV information to mongoDB. Accomplishments that we're proud of Successfully built image/behavior-recognizing model What we learned Gained more expertise in machine learning, databases, and Next JS What's next for Rate My Driver There are many drivers with slightly misaligned eyes and impaired vision, and we hope to one day be able to fairly and accurately serve those with these physical disabilities. <div