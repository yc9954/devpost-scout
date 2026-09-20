---
slug: "presence-and-working-time-monitoring-by-gps"
url: "https://devpost.com/software/presence-and-working-time-monitoring-by-gps"
title: "Presence and working time monitoring by GPS"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 621
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
---

# Presence and working time monitoring by GPS

> With this App, Monday.com can help project managers to remotely monitor presence and working time of employees or subcontractors on sites, using the GPS of their smartphone.

[Devpost](https://devpost.com/software/presence-and-working-time-monitoring-by-gps) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[education]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]]

**stack** azure, javascript, node.js

## How they structured the write-up

- what our app does
- how it works and how we can implement it in a monday.com account
- inspiration
- impact
- how we build, what we learned and challenges we faced
- what's next for presence and working time monitoring by gps

## Body

Validation screen on smartphone Creation of a new site in Ubiqod backend Example of recipes applied to a board in Monday.com Email received by the assigned person What our app does Our App tracks time of people on site, using the GPS of their smartphone to prove their presence at the expected location. Users can create missions or job tasks (items) directly into Monday.com, and they will be able to follow the progress of the mission in real time. The whole process is automated, from sending the mission details to the assigned person to the departure from the site. How it works and how we can implement it in a Monday.com account When project managers want to launch a mission, they have to follow the following process: Create an item containing: A Ubiqod site number An assigned person (who will receive the email, can be a Viewer) A deadline The name field is used to describe the mission to carry on (ex.: clean the building) Trigger the sending of the mission by email (depending on the recipe): Manually with a status update Scheduled depending on the deadline (ex.: at 8pm the day before the mission date) A free Ubiqod account is requested in order to manage sites and run the integration (oauth process with Monday.com when adding the recipe). The workers receive an email with a unique link. When they arrive on site, they click this link, and they can "clock-in" and "clock-out" with a mobile web interface (no app required) While doing so, the system check their GPS position, and compare it to the position of the site. In case of mismatch, an alert is sent to Monday.com (update in the item). Inspiration Skiply is tracking on site presence of tens of thousands people working for the largest facility management companies in the world (including ISS). Unitl now, we did it mainly with IoT. But with the COVID crisis, our customers asked us to find contactless solutions, or solutions that are usable with personnal devices. We realized that Monday.com, combined with our site and position management tool, could provide a very good tool to monitor, visualize and manage service requests and to track the working time. Impact With the crisis, tracking remote activities became one of the biggest challenge in many sectors (Facility Management, Industry, Maintenance, Medical Care Services...) Everyday, we receive requests from companies who are looking for reliable and simple solutions to check that the job is done on time by remote workers. It can be for the maintenance of an elevator, or even to be sure that the nurse went at school on time to pick up the kids. For us, this App is a very simple solution, universal, and adapted to every type of workers (especially those who will never connect to Monday.com). Regardless of the issue of the challenge will be, we plan to promote it widely. How we build, what we learned and challenges we faced We never used Monday.com API before. So, even if we were really familiar with the tool, we had to learn. We followed all the technical webinars, asked for the feedback of the Monday.com team... We are active on the community site. We really enjoyed participating as a team. Of course, we had a good background, especially in Node.js, that helped to build a robust and secured solution. The main challenge was to propose a simple solution that can be use by anyone, not only by people that are familiar with IT tools. What's next for Presence and working time monitoring by GPS We want to implement the site management system inside Monday.com. Today, it can't be done because the Monday API can not access the location file. <div