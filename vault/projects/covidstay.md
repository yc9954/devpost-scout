---
slug: "covidstay"
url: "https://devpost.com/software/covidstay"
title: "COVIDStay"
hackathon: "Pandemic Response Hackathon"
organization: "Datavant"
winner: true
words: 604
team_size: 13
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/patient_family"
---

# COVIDStay

> Connecting First Responders to Accommodations

[Devpost](https://devpost.com/software/covidstay) · hackathon [[Pandemic Response Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[disaster_emergency]] [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**user** [[frontline_worker]] [[patient_family]]

**stack** appian

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for covidstay

## Body

Connecting First Responders to Accommodations Inspiration When we learned that a local emergency management organization in New York was considering options for accommodations of key staff who were at high risk (e.g. medical staff) or had been advised to quarantine, IEM technologists started brainstorming a system that could support registration and tracking of individuals either working as frontline COVID-19 responders or individuals working in high Coronavirus spread area who want to distance from immediate family and others due to their higher contact risk stemming from treatment of multiple sick patients. Moreover, if any of these people develop symptoms and test positive for COVID-19 and have to self-isolate themselves, COVIDStay can track them. This rationale does not necessarily apply only to healthcare workers (HCW) on the front lines, but first responders, emergency operations center personnel and others. These individuals fighting the front line battle against this pandemic have an understandable need to physically separate from loved ones and friends, but also need a safe, comfortable refuge that has amenities such as wifi, laundry, food, sundry and other services available. For people who test positive and have to self-isolate it is imperative and mandatory that the disease is reported so the local health departments take preventive measures. COVIDStay allows tracking of these individuals. What it does COVIDStay allows either an individual or a staffer acting on their behalf to create a credentialed account, answer questions allowing the system to determine whether they are eligible for self-separation accommodation, assign them to a hotel room, monitor the inventory of hotel rooms available, and track the arrival and departure of the qualified individual. Initial qualification and subsequent tracking is essential to minimize risk of introducing sick guests to the hoteling accommodations and to properly quarantine them medically if they get sick during the course of doing their essential mission. How I built it Our team has a lot of experience with developing complex applications very rapidly using the Appian BPM platform. Using this platform and toolkit, we were able to construct a full-featured application in a very short time. Challenges I ran into We would have liked to integrate the tool directly with hotel reservation systems to keep available room inventory up to date. While we determined the requirements that would be necessary to integrate with a GDS system such as SABRE, we were not able to complete the integration in the allotted time. Accomplishments that I'm proud of Our team produced a robust prototype on a platform that is FEDRAMP, SOC-3 and HIPAA compliant in a three-day window. What I learned Modern technology platforms really provide a big advantage in rapidly producing secure, scalable applications that deliver a great user experience. What's next for COVIDStay Next steps for this app would include live feeds for hotel room availability, as well as possibly adding a module to address additional core services such as delivery of prepared food, health monitoring/testing, or other personal amenities. In addition, a scheduler with optimizing functions would help if support for hoteling essential workers needed phasing or shifts over time, based on additional measures that would further reduce risks outside of their front-line mission. Additional integrations could inform local health departments of any COVID-19 confirmed cases residing at the hotel. Additional development can continue with a small, focused development team of 1-2 technologists, supplemented by in-house subject matter experts with extensive experience in the hospitality industry to provide needed functional input. Development of releases would proceed using sprint cycles of 7 days to allow customization for local area considerations where deployed. Scalability would be addressed by allocating additional cloud resources to the existing deployment. <div