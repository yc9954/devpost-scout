---
slug: "us-state-professional-licenses"
url: "https://devpost.com/software/us-state-professional-licenses"
title: "US State Professional Licenses"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 260
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# US State Professional Licenses

> Have you ever wondered if your Doctor or Dentist is having a valid license? How about Plumbers, Nail Technician and Tow truck company? This project will help you answer those questions easily.

[Devpost](https://devpost.com/software/us-state-professional-licenses) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[civic_government]]
**user** [[clinician]] [[frontline_worker]] [[general_public]]
**substrate** [[regulation_legal_text]] [[structured_db]]

**stack** amazon-web-services, data.gov, dynamodb, lambda, python, sam

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for us state professional licenses

## Body

Professional License Inspiration We wanted to make US Government data more accessible to the public. Through the Data.gov initiative, each States release their own dataset for Licensing and Regulation. We wanted to check whether Professional and Business has a valid License. What it does It's an API endpoint where you can call and request data for your specific US States and Agency. It will return data about a Professional individual or a Business operating in a US States that need license. It will show whether a License is valid or not. How we built it The backend we used AWS Services. The entire system is serverless (API Gateway, Lambda, S3, DynamoDB). We wrote the code in Python and published it on Github here: https://github.com/kpx-dev/licenses Challenges we ran into The dataset from each US States is different, so there's a lot of manual parsing for each States. Even in the same State, data can be corrupted, missing header. There's also a lot of data so ingesting it quickly to our AWS DyanmoDB can take sometime because we want to be cost sensitive for this project. Accomplishments that we're proud of We were able to load most of dataset for California! What we learned Data provided by States can be bad, a lot of manual processing. We actually learned to work as a team remotely effectively through text message and Postman Team. The update to Postman Collection is live. What's next for US State Professional Licenses We plan to use AWS Datawrangler to manage the parsing instead of writing custom code. <div