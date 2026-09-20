---
slug: "quicq"
url: "https://devpost.com/software/quicq"
title: "QuicQ"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 575
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# QuicQ

> Allow customers and organizations alike to make informated customer service decisions, using Computer Vision and Genesys's API.

[Devpost](https://devpost.com/software/quicq) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** bulma, flask, genesys

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for quicq

## Body

Dashboard for customers to view real-time customer support data and to make informed decisions. Computer vision line detection model at work! Organization dashboard providing robust analytics and metrics. computer vision Inspiration We can make customer support so, so much better, for both customers and organizations alike. This project was inspired by the frankly terrible wait times and customer support information that the DriveTest centres across Ontario have. What it does From a high-level, our platform integrates analytics of both in-person and online customer support lines (using computer vision and Genesys's API, respectively), and uses those to provide customers real-time data for which customer support channel to utilize at a given time. It also provides organizations with analytics and metrics to be able to optimize their customer support pipelines. Speaking about the internals, our platform utilizes computer vision to determine the number of people in a line at any given moment, then uses AI to calculate the approximate waiting time for that line. This usecase is meant for in-person customer support interactions. Our platform also uses Genesys's Developer API (EstimateWaitTime) to calculate, for any given organization and queue, the wait time and backlog of customer support cases. It then combines these two forms of customer support, allowing customers to make informed decisions as to where to go for customer support, and giving organizations robust analytics for which customer support channels can be further optimized (such as hiring more people to serve as chat agents). How we built it OpenCV along with a custom algorithm for people counting within a certain bounding area was used for the Computer Vision aspect to determine the number of people in a line, in-person. This data is sent to a Flask server. We also used Genesys's API along with simulated Genesys customer-agent interactions to determine how long the wait time is for online customer support. From the Flask server, this data goes to two different front-ends: For customers: customers simply see a dashboard with the wait time for online customer support, as well as the wait times at nearby branches of the company (say, Ontario DriveTest centres) – created using Bulma and Vanilla JS For organizations: organizations see robust analytics regarding wait times at certain intervals, certain points in the day, etc. They can also compare and contrast online and in-person customer support analytics. Organizations can use these metrics to optimize customer support to reduce the load on certain employees, and by making customer support more efficient for customers. Challenges we ran into Working with many services (Computer Vision + Python, Flask backend, Vanilla JS frontend, Vue.js frontend) was a challenge, since we had to find a way to pass the data from one service to another, reliably. We decided to fix this by using a key-value store for redundancy to ensure data is not lost through numerous layers of transmission. Accomplishments that we're proud of Creating a working product using Genesys's API! What we learned The opportunity that lies within the field of customer support and unifying both online and in-person components of it. Also, the opportunities that Genesys's API holds in terms of empowering organizations to make their customer support as efficient as possible. What's next for QuicQ We wanted to use infrared sensors instead of cameras to detect people in a line in-person, due to privacy concerns, but we couldn't find infrared sensors for this hackathon! So, we will integrate them in a future version of QuicQ. <div