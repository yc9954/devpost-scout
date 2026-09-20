---
slug: "find-my-health"
url: "https://devpost.com/software/find-my-health"
title: "Find My Health"
hackathon: "PennApps XII"
winner: true
words: 406
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
---

# Find My Health

> The simplest way to search for hospitals by distance, waiting time, quality of service, and condition or illness.

[Devpost](https://devpost.com/software/find-my-health) · hackathon [[PennApps XII]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]

**stack** flask, ios, linode, python, swift

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for find my health

## Body

Inspiration There is a lack of access to medical care in many areas of the United States. When patients are able to get access, they often experience long waiting times as well, causing a percentage of patients to leave without being seen or treated every year. We sought to target this issue by providing a unique tool that can help simplify the experience for patients to find proper access to health care when they need it. What it does Find My Health is a platform for people to quickly decide on the best hospital and medical care facility to use depending on condition, distance, statistics on waiting times of various facilities, as well as quality of care. Sometimes the nearest hospital is not the best and quickest way to get seen by a doctor, and we strived to fix that. How I built it The data was scraped from websites pertaining to national data and averages regarding waiting times at hospitals, as well as data pertaining to quality of care, location, waiting times by condition, etc using Python. A REST API was built using Python/Flask and hosted on linode. A native iOS front-end was built using Swift in order to display the data and engage users in a meaningful way. Challenges I ran into Data availability, missing data, and finding the best way to present it. Accomplishments that I'm proud of With all the hurdles working through the data, we managed to extract what we needed in order to provide a minimally viable product that can truly be useful to people who need the quickest way to an ER. We really focused on the design and user experience, as emergency situations often need simplicity and speed for easy decision making. What I learned The amount of data out there that you can just grab and use is truly amazing. Also sleep and blankets are precious, I miss my bed. What's next for Find My Health This can a huge impact on developing countries and can provide lots of insights on the lack of access to care in certain areas both foreign and domestic. We would also like to provide a platform for hospitals to report live waiting times in order to improve patient workflow and better understand when patient turnout increases. We would also like to provide analytics beyond emergency care facilities in order to truly improve access to medical care on a larger scale. <div