---
slug: "covid-vaccination-b26vhd"
url: "https://devpost.com/software/covid-vaccination-b26vhd"
title: "COVID Vaccination"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 184
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
---

# COVID Vaccination

> The limited supply of COVID vaccination in all healthcare organizations and making sure two doses are given efficiently is a challenge. API's can help in keeping appointments and inventory up to date.

[Devpost](https://devpost.com/software/covid-vaccination-b26vhd) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]

**stack** .net, azure, elasticsearch, epic, netcore, sql

## How they structured the write-up

- covid and the lockdown have tested all of us. to end this, we have to make sure everyone is vaccinated.

## Body

COVID and the lockdown have tested all of us. To end this, we have to make sure everyone is vaccinated. We have created API's that can provide a real-time update on whether a dose is available, if you are eligible to receive it, scheduling an appointment for the second dose all by querying the EPIC . Getting data out of the EPIC systems was historically done using ETL's. There are only a few developers that can actually write API in EPIC because of propriety technology and certification requirements. Once we have all the necessary access to the system and knowledge about data, we created a collection of the API calls that are used to test and later was used by the scheduling application for integration. Getting a solution that is customizable and provide real-time updates from EPIC is something not done in our organization. Using ETL's is not always the best approach as you will introduce other complexity and miss the latest data from other systems. The application is going to evolve not only for COVID vaccination but for other regular vaccinations. (Flu). <div