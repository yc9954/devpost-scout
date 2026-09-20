---
slug: "healthcare-assistant"
url: "https://devpost.com/software/healthcare-assistant"
title: "Healthcare Assistant"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 288
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Healthcare Assistant

> Get all the healthcare service APIs in one place.

[Devpost](https://devpost.com/software/healthcare-assistant) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[web_dom]]

**stack** drchrono, here-geocoder, postman, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how to use it
- accomplishments that we're proud of
- what we learned
- what's next for healthcare assistant

## Body

Postman Workspace Website Homepage Inspiration Requirement for online healthcare services increasing day by day in the post-COVID world Lack of applications/websites addressing the end-to-end needs of the doctors and the patients Scarcity of information around development tools and helpful APIs Need of a workspace/collection providing all the healthcare-related APIs in one place What it does Postman Workspace Provides the developer with all the healthcare-related APIs supplied by DrChrono Contains executed examples for all the APIs, specifying the required inputs and the corresponding request formats Includes Google Maps and HERE Maps API to geocode addresses into corresponding latitude and longitude Healthcare Management App Allows the doctors to message patients, view patient profiles, visualize patient globally Enables the patients to visualize doctors across the globe and book appointments with them anytime Uses a subset of APIs from the constructed Postman workspace How we built it Workspace is created using the DrChrono and the HERE Maps API collection Website is developed using React JS and Material UI How to use it Fork the public workspace Select an existing environment(for example, Healthcare Assistant - Development ) or create a new one Get the OAuth 2.0 Access Token by following this link Update the ACCESS_TOKEN environment variable with the obtained access token Modify requests if needed and play with the APIs !!! For using the geocoding APIs, obtain the Google Maps API key or the HERE Maps API key, and add its value to the corresponding environment variables Accomplishments that we're proud of Created my first Postman Workspace What we learned Geocoding Addresses on a Map Utilizing healthcare APIs Using Postman environment variables Employing Postman tests to monitor the collections What's next for Healthcare Assistant Update the workspace with other healthcare-related APIs <div