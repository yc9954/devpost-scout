---
slug: "sequoia-tgnryh"
url: "https://devpost.com/software/sequoia-tgnryh"
title: "Sequoia"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 749
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
---

# Sequoia

> An SMS-based platform made to help hospitals handle the burden of exponential patient influx by remotely connecting users to healthcare providers for triage

[Devpost](https://devpost.com/software/sequoia-tgnryh) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[general_public]] [[patient_family]]

**stack** digitalocean, flask, geojson, python, twilio, waitress

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sequoia

## Body

Provider opening screen Enter triage Triage shows user text messages collected through SMS Scrolling down Language on provider side is adjustable Translated to mandarin Scrolling down Back to english, select a triage level Submit Triage decision has been submitted and sent back to user Click to receive next user in the queue Enter resource log Log hospital resources User text messages - submit zip code User text messages - questionnaire User text messages - describe symptoms in detail Triage message returned to user - lists 3 hospitals of the appropriate care level Inspiration During the COVID-19 pandemic, a key message has been to "flatten the curve." In this strategy, it is necessary to shift patient populations visiting hospitals to prevent the healthcare system from being overwhelmed. However, how do you "flatten the curve" when you exhibit COVID-19 symptoms? Although there is has been a global effort to combat the pandemic, COVID-19 is unfortunately still able to overwhelm the health care system. As the pandemic worsens, people are going to the wrong health centers - going to the emergency department in place of self-isolating for mild symptoms - and overloading health providers to a degree that is exponential in severity. We found that this issue - the overloading of hospitals due to COVID-19, is a huge problem, one that could be solved by a triage system supported by remote providers who are located a distance from pandemic hotspots. There is a great need for physician-made decisions to triage patients and direct them to the appropriate level health center, and a system offering communication between a user and provider through remote means would solve this, both alleviating the load of providers at the front lines of the pandemic, and preventing continued overloading of the system by patients coming to hospitals unnecessarily. What it does Sequoia is a two-way system between a user and health provider. A user experiencing COVID-19 symptoms is able to provide details regarding COVID-19-related symptoms via SMS, send their messages to a triage, and receive a recommendation from a remote physician on next steps, which include whether to seek testing, see a specific level (1-4) of hospital, check in again after a marked number of hours, or stay at home. For recommendations involving testing locations or hospital levels to be sought out, our system texts the user a list of the 3 nearest hospitals at the appropriate triage level that have availability. As a result, Sequoia allows remote providers to distribute the load for hospitals already overloaded by the pandemic. This system is highly accessible and easy to use for users, who communicate via SMS, and providers, who triage users in a web app. How we built it Sequoia utilizes Twilio for programmatic SMS and Flask / waitress for a web server, running on a DigitalOcean droplet. To support large volumes of users, Sequoia uses a queue-based system to match a specific provider with a user to triage, and a secondary producer-consumer thread system for off-main-thread querying of web-based GeoJSON APIs. In addition, Sequoia uses an extensible and adaptable weighting system to match each user with a health care center, based on available resources, distance, and care level. Challenges we ran into Some initial challenges we faced included finding a list of hospitals spanning the nation that were ranked by triage level and marked by zip code. We were able to solve this by asking experts, who directed us towards hospital records in the CMS. Accomplishments that we're proud of We are proud of both sides of the two-way communication line! User data is sent to the electronic triage with great ease and speed, making for a solution that would benefit both users and providers during any setting with hospital overloading. We are also proud of receiving positive feedback from experts in medicine, informatics, medical technology, and engineering. We interviewed a diverse group of people for feedback and were pleased to hear that we chose a problem with a great need, and developed a solution that efficiently combined medicine and technology. What we learned We learned how to implement the Twilio API, a powerful tool that brings great accessibility to users. We learned much more about hospital systems, before and after the pandemic, hospital triaging, and the COVID-19 pandemic at large. What's next for Sequoia Next, there are several add-ons that would enhance adoptability of our service. These include verification of physician licensing within each state or across state lines and multi-provider verification for each triage decision. <div