---
slug: "bone-health-tracker"
url: "https://devpost.com/software/bone-health-tracker"
title: "Bone Health Tracker"
hackathon: "AWS Health AI Hackathon"
organization: "Amazon"
winner: true
words: 653
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Bone Health Tracker

> 1 in 3 women over the age of 50 years and 1 in 5 men will experience osteoporotic fractures in their lifetime. Bone Health Tracker will help them monitor their bone health and track their treatments.

[Devpost](https://devpost.com/software/bone-health-tracker) · hackathon [[AWS Health AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[transcript_audio]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** amazon-web-services, chart.js, go, html, javascript, machine-learning, python, sqlite, svg

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bone health tracker

## Body

The key metrics from Bone Mineral Density(BMD) scan report is automatically detected by Bone Health Tracker. Skeleton visualization shows the status of bones from your latest report according to WHO classification. Dynamic Chart keeps track of the T-scores from your BMD reports and helps you monitor the progress of your treatment. Inspiration When I was 32 years of age I was told that my bones were like that of an 80 year old due to a health disorder called Osteoporosis. Osteoporosis can make our bones fragile and likely to break. 1 in 3 women over the age of 50 years and 1 in 5 men will experience osteoporotic fractures in their lifetime. It is likely that your parents and grand parents are already suffering from Osteoporosis. Osteoporosis is identified using a Bone Mineral Density(BMD) scan test which gives scores for our bone density and is compared with the known scores from the healthy individuals of same age. I was told that these known scores does not include all races, ethinicities and are generally unreliable for those with pre-existing diseases. This makes it difficult for providing proper healthcare, Even more so for outliers like me. I'm attempting to change that with Bone Health Tracker. What it does Bone Health Tracker classifies the Bone Mineral Density(BMD) scan test report using Amazon Comprehend Medical to display the reports with visualizations to better understand the bone health and to monitor the progress of bone health treatments . Healthcare providers currently have to manually compare the BMD reports of their patients every year to analyze the treatments, With Bone Health Tracker's dynamic chart feature they can now do it automatically and even patients can track the progress of their treatments. Skeleton visualization helps to easily understand which bones are affected by Osteoporosis, Osteopenia even by those without prior medical training . BMD scan test reports without any personal information can be submitted for the research of bone health and treatments for bone health diseases. No Protected Health Information (“PHI”) is collected during the entire function of Bone Health Tracker as only assessment section of the BMD scan test report is needed. How I built it I built by first writing a middleware to communicate with AWS services like Amazon Textract and Amazon Comprehend Medical. Then I built a parser to format the data returned by Amazon Comprehend Medical into BMD reports. I built routines to store the reports locally in the client and I built front-end to manage the report upload, visualizations and report submission with necessary routines for security. Frontend & Backend: HTML, JS, Go Middleware: Amazon Textract and Amazon Comprehend Medical machine learning service via Python. Database: Sqlite3 with Readers-writer lock pattern for concurrency. Challenges I ran into Amazon Comprehend Medical machine learning doesn't have default support for Bone Mineral Density scan test reports, So I had to figure out how to use the structured data returned by Amazon Comprehend Medical for constructing the BMD reports. Accomplishments that I'm proud of I wrote a custom parser to parse the structured data returned by Amazon Comprehend Medical as there was no default support for BMD scan reports during the development of Bone Health Tracker. The parser can handle data of all supported bone sites in a BMD scan test report irrespective of its format i.e. Standard BMD report (or) Medical transcription. Bone Health Tracker doesn't collect any personal information to function. The BMD report data is stored locally in the client, Protecting the privacy of its users . What I learned Amazon Comprehend Medical is accurate and has very low latency, Along with Amazon Textract real-time health AI solutions can be built at scale to augment the healthcare infrastructure. What's next for Bone Health Tracker To work with Amazon Comprehend Medical team to add default support for Bone Mineral Density scan test reports and to add support for other bone health diseases in Bone Health Tracker. <div