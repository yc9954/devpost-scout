---
slug: "clinicconnect"
url: "https://devpost.com/software/clinicconnect"
title: "ClinicConnect"
hackathon: "Hack the North 2020++"
winner: true
words: 459
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/structured_db"
---

# ClinicConnect

> ClinicConnect helps patients find clinical trials and studies at nearby treatment centers to address their long term health conditions.

[Devpost](https://devpost.com/software/clinicconnect) · hackathon [[Hack the North 2020-]]

## Facets

**domain** [[civic_government]] [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[structured_db]]
  <sub>weak: geospatial, web_dom</sub>

**stack** dropbase, gmaps, html, javascript, node.js, postgresql, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clinicconnect

## Body

Map view Trial View Welcome New Account Autofill Email Inspiration Over the past several months, many of the major pharmaceutical and biotechnology companies have been working to develop vaccines for SARS-CoV-2, the virus causing COVID-19. One of the major barriers to evaluating these vaccine candidates is the inability for willing participants to find clinical studies that are going on near them. We noticed that this trend extended to many other disease states and therapeutic areas. For example, 20% of cancer therapy studies fail because of a lack of enrollment. What it does Our platform serves as a patient-facing clinical trial platform where patients can search for trials based on a variety of parameters including disease states, study phase, location, and patient demographics (i.e., PHI such as age, gender, etc.). How we built it The platform populates a Dropbase database using raw CSV files from clinicaltrials.gov (a research scientist-facing platform hosted by the government). It further calculates the distances between the user's location and all clinical trial sites to find the closest studies with Google Geocoding APIs. Finally, Dropbase allows us to generate a REST API for this data to be quickly accessed powered by PostgREST which powers our frontend. Our interface allows users to search through nearby trials and see information about the studies such as intervention type, physician contacts, inclusion/exclusion criteria, distance, and time to travel. They can then interact with our platform to send an automated email to the study contact to explore enrollment options. Challenges we ran into Processing data was quite a difficult element of our design. Given that much of the data is from clinicaltrials.gov and is submitted by individual study leads, the input data was largely unstructured. We utilized Dropbase to help us process this data by incorporating a variety of custom functions, sorting/filtering functions, and functions that deal with null data. Another challenge was designing the JavaScript frontend-backend communication. We utilized Dropbase's easy-to-use SQL interface and API support in conjunction with JS to connect form results to the database. Accomplishments that we're proud of We are particularly proud of having developed a platform that truly has the ability to drive value to society, but also to potential industry partners (i.e., pharmaceutical companies) that are looking to advance their trials. What we learned We learned a great deal about database structure and writing PostgREST queries, as well as using pandas to venture across lots of unstructured data. What's next for ClinicConnect We aim to extend the analysis to other forms of studies (e.g., behavioral studies). In the future, we believe that a partnership with the NIH (the host of clinicaltrials.gov) can allow for more streamlined communication between the Dropbase database and the raw data as well as provide our platform with credibility. <div