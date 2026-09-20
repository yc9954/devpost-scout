---
slug: "teamfromportugal"
url: "https://devpost.com/software/teamfromportugal"
title: "PathOut"
hackathon: "GlobalHack VI"
winner: true
words: 387
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/social_worker"
---

# PathOut

> A single, holistic platform to create a path out of homelessness

[Devpost](https://devpost.com/software/teamfromportugal) · hackathon [[GlobalHack VI]]

## Facets

**domain** [[housing_homeless]] [[labor_employment]]
**user** [[social_worker]]

**stack** outsystems

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pathout

## Body

Inspiration Every organization, and every service they provide, all work towards one unified goal: end the chronic cycle of homelessness by ensuring every individual has a way out. So why not create a platform with that goal built in from the start? What it does PathOut is a HMIS whose goal is to give every individual a path out of the homelessness cycle. Starting with a coordinated entry system where a case manager can enter relevant data about the client and assess their priority (based on the VI-SPDAT), PathOut then allows case managers to determine their client's individual needs based on four key service areas: housing, education, health, and employment. Then, a case manager finds specific services offered across a city's CoC organizations based on that client's needs, and they add the service to the client's "path out of homelessness." This path is a holistic visualization of client needs for any case manager -- regardless of organization -- to understand, better enabling coordination of services across CoC members, and a progress tracking for clients that provides a clear, simple path out of homelessness. How we built it We created a Rest API from the sample data, which we created logic to match organization qualifications to the data we enter into the intake form. This made it so the only services displayed were things the client actually qualified for. We then organized these services into the client needs they address, and finally laddering all needs up into four categories -- housing, health, education, & employment -- with housing always being displayed as a priority. Challenges we ran into Initially we had a bunch of assumptions about case managers to help design our platform, but after some user interviews we ended doing some major redesigns to create the optimal flow. We also had challenges in...(????) Accomplishments that we're proud of Building the Rest API from the sample data and sharing it with the rest of the participants. What we learned The homelessness issue is incredibly complex. There is no "one-size all" solution, so we had to learn to focus on one specific aspect of the issue while keeping in mind the whole context of the situation. What's next for PathOut Building a system that would pull data from multiple organizations systems that would seamlessly feed into our system. <div