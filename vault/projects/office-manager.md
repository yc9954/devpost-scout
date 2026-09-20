---
slug: "office-manager"
url: "https://devpost.com/software/office-manager"
title: "Office Manager"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 703
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Office Manager

> Office Manager connects workers in hybrid in-office/remote models with the desk that will allow them to do their best work and bond with their teammates, from the tool they're already using everyday.

[Devpost](https://devpost.com/software/office-manager) · hackathon [[Codegeist 2021]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[labor_employment]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** atlaskit, forge, love, react, recoil, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for office manager

## Body

GIF Our first mock-up done with our beloved Escalidraw On the main page, you can see who's in office today (or tomorrow if your change the date in the calendar) Book your day and chose your desk. Edit your office map Inspiration Remote and hybrid work models are on the rise in this soon-to-be post pandemic times (fingers crossed). Offices and the way they're used by staff are changing: instead of primarily needing space for focused solo work and a spot for everyone, workers will show up at the office with the intention of collaborating with teammates and the company will want to optimize office space costs. With Elements Office Manager , we aim to solve one of the most common challenges with flex offices: connecting workers with the desk that will allow them to do their best work and bond with their teammates, every time they come into the office. We believe that booking your spot should be a pleasant, integrated experience, and that because your company runs in flex office mode you shouldn't rush to the office in the morning to find a desk. What it does As member of the team, I can schedule my presence by selecting the date I will be in the office. In addition to that I can also reserve my workspace from the list of available desks. As a workspace manager I will have an floorplan editor where I can configure the desks in the office and their arrangement. The edit allow 45° rotations of the desks. A description can be added to list, for example, all the available accessories on this desk (mouse, screen, etc...) In a nutshell: book your desk draw your office map ease the management of who's physically in the office How we built it Office Manager uses: Forge modules (project page ); Custom UI; And HTML Canvas for the office editor. Challenges we ran into Clearly the office editor was the most complex part. The editor itself + magnet part + rotation + rotation & magnet. We had to go back to trigonometric math and transformation matrix; that's not something we do often when developing Jira add-ons! Retrospectively, we wouldn't do it the same way. It was really fun to do but unfortunately, it's now very complex to add some features to the map. We would have loved to add the profile picture of the people who already booked a desk and have in a glance an overview of who will be in the office and what desk they chose. Also at Elements we decided to try to build several apps for Codegeist and explore a number of different ideas. We faced a variety of issues while building multiple apps, and some of them didn't make the cut to be submitted for the competition. We thought it would better to assemble all the issues and remarks we had into one single feedback, available here Element's Feedback on Forge . Accomplishments that we're proud of The editor :D ! Even if it's not as functional as we expected, it was a great challenge and we are quite proud of it. It shows that with Forge it's possible to do complex developments. What we learned We were pleasantly surprised to find out that Forge allows you to do complex development. When we first had the idea to do the map editor, we didn't have any idea how we could build it. We doubted that Forge would allow it to work. We also learned that Office management can be a quite complex topic. We talked with some administrative colleagues, and their needs or ideal solution can differ a lot depending on who you talk to. What's next for Office Manager The next step would be to update the map editor to make it more user friendly, like adding the possibility to choose the desk directly by clicking on the map. Also, we would like to add the possibility to propose several maps, like several floors, or open space, depending on your office configuration. We could also think of meeting room with several user associated to the booking. Even with its limitation, Office Manager is a tool that we will definitely use internally! <div