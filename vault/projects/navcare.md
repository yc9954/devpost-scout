---
slug: "navcare"
url: "https://devpost.com/software/navcare"
title: "Navcare"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 525
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
---

# Navcare

> Our way of improving the scheduling and travelling experience for Personal Support Workers to help mitigate the growing staffing problem in healthcare.

[Devpost](https://devpost.com/software/navcare) · hackathon [[Hack the North 2022]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]]

**stack** django, figma, google, google-maps, react

## How they structured the write-up

- inspiration 💭
- what it does 🙊
- how we built it 💪
- challenges we ran into 😵
- accomplishments that we're proud of 😁
- what's next for navcare 😎

## Body

Navcare Logo Login Page Schedule Section Design Map Section Design Inspiration 💭 With the current staffing problem in hospitals due to the lingering effects of COVID-19, we wanted to come up with a solution for the people who are the backbone of healthcare. Personal Support Workers (or PSWs) are nurses that travel between personal and nursing homes to help the elderly and disabled to complete daily tasks such as bathing and eating. PSWs are becoming increasingly more needed as the aging population grows in upcoming years and these at-home caregivers become even more sought out. What it does 🙊 Navcare is our solution to improve the scheduling and traveling experience for Personal Support Workers in Canada. It features an optimized shift schedule with vital information about where and when each appointment is happening and is designed to be within an optimal traveling distance. Patients are assigned to nurses such that the nurse will not have to travel more than 30 mins outside of their home radius to treat a patient. Additionally, it features a map that allows a nurse to see all the locations of their appointments in a day, as well as access the address to each one so they can easily travel there. How we built it 💪 Django & ReactJS with google maps API. Challenges we ran into 😵 Many many challenges. To start off, we struggled to properly connect our backend API to our front end, which was essential to pass the information along to the front end and display the necessary data. This was resolved through extensive exploration of the documentation, and experimentation. Next while integrating the google maps API, we continuously faced various dependency issues as well as worked to resolve more issues relating to fetching data through our Django rest API. Since it was our first time implementing such an infrastructure, to this extent, we struggled at first to find our footing and correctly connect and create the necessary elements between the front and back end. However, after experimenting with the process and testing out different elements and methods, we found a combination that worked! Accomplishments that we're proud of 😁 We made it! We all felt as though we have learned a tremendous amount. This weekend, we really stepped out of our comfort zones with our assignments and worked on new things that we didn't think we would work on. Despite our shortcomings in our knowledge, we were still able to create an adequately functioning app with a sign-in feature, the ability to make API requests, and some of our own visuals to make the app stand out. If given a little more time, we could have definitely built an industry-level app that could be used by PSWs anywhere. The fact we were able to solve a breadth of challenges in such little time gives us hope that we BELONG in STEM! What's next for Navcare 😎 Hopefully, we can keep working on Navcare and add/change features based on testing with actual PSWs. Some features include easier input and tracking of information from previous visits, as well as a more robust infrastructure to support more PSWs. <div