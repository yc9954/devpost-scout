---
slug: "gaitorade-jq937f"
url: "https://devpost.com/software/gaitorade-jq937f"
title: "Gaitorade"
hackathon: "PennApps XII"
winner: true
words: 355
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
---

# Gaitorade

> Walk with confidence

[Devpost](https://devpost.com/software/gaitorade-jq937f) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]]

**stack** java, myo, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for gaitorade

## Body

Inspiration We wanted to develop a product that would make an impact to the health care system and attack some of the common problems people face these days. What it does Our product Gaitorade, does the analysis of how a person places his/her foot while standing/walking. ( gait analaysis). It maps the pressure points over a person's foot sole and has many applications in the field of health care. For now, along with the plantar analysis, it detects the presence of Parkinson disease where the legs of patient are effected. Gaitorade software also allows the user to message directly to the doctor to notify him about the progress in healing. How I built it Myo was worn in legs for the development in this project. Myo is generally used for gesture detection tasks and it is worn in hands. We broke the convention and wore it in legs to demonstrate its capabilities in the health care domain. Challenges I ran into As the Myo has been developed for gesture detection tasks, most interfaces to Myo give an access only to the data after some basic detection APIs. As we had changed the way Myo has been used, we had to start the development from scratch and hack into Myo to get the raw sensor values from hardware and then do the filtering and processing tasks to get our output. Accomplishments that I'm proud of Our product can accurately detect and measure the few stances planned by us and has shown promising results for the further development to cover other positions as well. It can also detect the presence of Parkinson disease in the user. What I learned Nor me or my team had worked on EMG sensors before and learning to operate it so well in 1 day and then using if for a noble domain was a wonderful experience. What's next for Gaitorade This product has infinite scopes open ahead. The future tasks include learning algorithms for detection of detailed foot placements and walk patterns, auto-detection of few of the common diseases/issues, and usage of on board IMU for various fitness tracking tasks. <div