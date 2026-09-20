---
slug: "job-explorer"
url: "https://devpost.com/software/job-explorer"
title: "Job Explorer"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 462
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
---

# Job Explorer

> Testing external adapters for every OCR job before deployment is very taxing on Chainlink Node Operators. The Job Explorer helps insure successful job runs and accurate data.

[Devpost](https://devpost.com/software/job-explorer) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[sensor_telemetry]]

**stack** api, linkpool, materialui, metrics, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for job explorer

## Body

Job Explorer - Settings Job Explorer - Standby Job Explorer - Success Inspiration Testing external adapters for every OCR job before deployment is very taxing on Chainlink Node Operators. OCR jobs are deployed very often without testing the bridge tasks, which will then result in bridge task errors and inaccurate on-chain answers. I thought that there should be a tool that could facilitate the debugging of jobs, thereby ensuring successful job runs and accurate data without any deviation. What it does The Job Explorer is a chrome extension that is dedicated to debugging and "exploring" OCR jobs and more specifically the adapter requests in each bridge task. The tool is useful in many cases: Debugging bridge tasks on a job: Instead of manually parsing the request data from a bridge task and creating a POST request to test the adapter's health, the Job Explorer will do all of the work for you. All you need to do is paste the OCR job in the text input field and it'll take care of the rest for you. New OCR job with no runs: Since OCR jobs need to be deployed on a certain number of nodes to get kicked off, Node Operators will be left guessing if all the adapters will work accordingly with the request data. The Job Explorer allows you to somewhat simulate the bridge tasks in order to confirm the functionality/accuracy of the adapters and the request data. Checking answer and deviation: Thanks to LinkPool's Metrics API, the Job Explorer is able to query the on-chain latestAnswer for OCR feeds. The Metrics API will give more insight to Node Operators and will open doors to many more possible features. How we built it The project was built using TypeScript, React, Material UI and LinkPool's Metrics API. Challenges we ran into Error handling was one of the challenges that I faced while building the tool. Time constraints were also a problem. Making the Job Explorer configurable for other Node Operators was also a challenge. Accomplishments that we're proud of I'm able to easily debug OCR jobs before deployment on a daily basis. This has saved me and others a good amount of time and effort. What we learned I learned not to underestimate the work needed and to not procrastinate as much as I did while working on the project. I think the tool could definitely be better polished and have more features. What's next for Job Explorer I would like to take some time to clean up some code and implement essential tests so that the tool is bullet-proof. I would like to add more features and data available from the Metrics API. The Job Explorer could also support other types of jobs, since it currently only supports OCR. <div