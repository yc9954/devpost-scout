---
slug: "velogger-log-inspector-for-velo"
url: "https://devpost.com/software/velogger-log-inspector-for-velo"
title: "Velogger: Log Monitoring for Velo"
hackathon: "Wix Make-A-SaaS Hackathon"
organization: "Wix"
winner: true
words: 736
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/government_staff"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Velogger: Log Monitoring for Velo

> Enhanced log inspector designed for Velo developers

[Devpost](https://devpost.com/software/velogger-log-inspector-for-velo) · hackathon [[Wix Make-A-SaaS Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[government_staff]]
**substrate** [[structured_db]] [[web_dom]]

**stack** google-cloud-function, javascript, velo-by-wix, wix

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- user feedback
- what's next

## Body

The log inspector displaying several type of log Logo Inspiration The idea for this project comes from my frustration with using Wix's native log monitoring tool (aka site's events). It's too plain and the interface is far from being developer friendly. So I took on the challenge to create an enhanced version of the site events for my own needs and then turn it into a SaaS so that other Velo developers can enjoy a better experience. The aim was to design a tool that user friendly yet powerful to provide meaningful insight to Velo developers. What it does This is a log monitoring tool dedicated to Velo projects. It allows Velo developers to inspect, filter and search their logs projects via an easy-to-use interface. The aim is to improve work efficiency and reduce debugging time while developing on Wix. Main Features Beginner-friendly UI Real-time : view logs as they happen on the website. History : load logs from a given past period. Logs filtering by severity, context (backend vs frontend), environment(live vs editor) and revision. Log searching via keyword. How we built it It is built on EditorX , Velo and a Google Cloud Function . It uses Wix's Monitoring SPI to collect logs. Logs are sent to a Google Cloud Function . It acts as a buffer between the SPI and Wix. A Wix endpoint processes all incoming logs: Logs are saved via Wix data and sent to Wix real-time messaging API to be viewed in real-time. Challenges we ran into Monitoring SPI SPI are relatively new on Wix and not (no) many examples are available online. I had to figure out how to use it by trial. Database growth The volume of saved logs quickly grows as I onboard new beta testers. We are now at more than 3 million logs and rising. At one point, I had to tweak the database queries in order to avoid repetitive timeout issues. There are still improvements to do but it's out of the current scope. Google Cloud Function scaling At the moment, the link between Wix users and the Google Cloud Function is configured manually. I know this could be automated but I'm not sure about the future of that component and might get ride of it. So I decided to focus on the MVP front end and do the configuration manually as new users sign up. In the future, that step will be either removed or automated so the signup experience will be smoothened. Accomplishments that we're proud of I know a few beta testers are already using the app daily. It's good to know that I built something that helps others in their day-to-day job. What we learned Technical knowledge It was my first time working with the monitoring SPI so I had to learn to work with it. I also had to sharpen my knowledge of Wix Data API in order to enhance my queries and avoid recurring database timeout. Project Management experience I conducted several user interviews with fellow Velo developers to understand their needs and confirm that we shared a common frustration with the current state of Velo Monitoring tool. Those user interviews are usually done by my clients. Having the role of project owner grants me new insight and experience User Feedback After the first round of user interviews, 2 features were added: Search by keywords One user needed the ability to search for a user ID in the logs so that he could quickly identify logs belonging to a given user activity. This led to the creation of the content filter . Time format Being European, I'm used to reading time in 24h format but an American user expresses the desire to display time in the am/pm format. This resulted in the creation of the time format configuration that changes how time inputs are displayed and how the log's time is formatted. For the next phase of development, I will add timezone management What's next After the hackathon, I'll do another round of user interviews to collect more feedback from new users. As said before, I'll automate the backend process and I'll add paid-pricing plans so that the cost of development and hosting is covered by users. I also want to create spin-off features such as an incident reporting tool link to the logs and an advanced logger Velo package to help develop to create meaningful logs. <div