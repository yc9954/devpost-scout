---
slug: "zzzyield"
url: "https://devpost.com/software/zzzyield"
title: "zzzyield (Team: EDIHealth)"
hackathon: "Junction 2016"
winner: true
words: 667
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# zzzyield (Team: EDIHealth)

> Increase employee productivity, health and happiness through better sleep. Measure, motivate, track, regulate.

[Devpost](https://devpost.com/software/zzzyield) · hackathon [[Junction 2016]]

## Facets

**domain** [[finance_payments]]
**user** [[social_worker]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]
  <sub>weak: regulation_legal_text</sub>

**stack** android, atmel, azure, bluetooth, casambi, css3, deezer, git, html5, i-beacon, mesh, mysql, oauth2, oura

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zzzyield

## Body

Logo of zzzyield Casambi programmable lights for environment regulation Smart Paulig Muku coffee cup alerting user on how much coffee and when to drink, and also if additional activity is needed. Ōura ring used for sleep and activity tracking Testing how productivity increases after sleeping at workplace Coffe mug knows how much You need to drink today The third Raspberry pi has been sucessfully conquered! The whole team working Overall flow Profit! (Business model) Big picture Inspiration Everyone has had the experience when there was not enough sleep the night before and the productivity is basically non-existant. A lesser known fact, is that based on research ~40% of adults don't get enough sleep (<7h), even though their subjective feeling is that they do and could be productive. It has been calculated, that the lost productivity because of this false assuption in the USA alone leads to annual losses of 63*10^9 USD. Also, a stressful day at work, or too much coffee while working can lead to problems sleeping at night resultin in a vicious cycle: Less sleep means lower productivity Lower productivity means more stress and higher coffee consumption Which again lead to difficulty sleeping and less On the other hand there is research that specially tailored environment can help sleep better, and that better sleep leads to better productivity - even if because of sleeping there is less time for work. Also well rested people take much better and safe decisions, and less risk means less insurance claims benefitting insurers and reducing insurance costs for clients. What it does is a system for employers which helps employers become more productive by sleeping better - it manages their coffee intake for the times they need to be awake and limits it before sleep. Also it manages the environment, such as lighting and music based on sleep and activity patterns. The specific environmental changes are triggered by proximity of the special Ōura ring, which also monitors the sleeping patterns and activity of employees. Our product also tries to rise awareness among employers, that it is better to let an employee take a nap than be unproductive, but awake. How we built it First, we gathered data from Ōura ring API, which is then analyzed and stored on Azure web platform. Each user have assigned ring and when they come close to specific devices, such as smart coffee mug, smart ligthing or raspberry pi with speakers these devices react according to the sleep quality and activity of the person, by either congratulating, suggesting caution or strongly suggesting to slow down and sleep. Coffee mug receives images from android application, which gathers data from Azure web application. Smart ligthing and sound are controlled by raspberry pi, which also gets the data from Azure web application and identifies the specific user through bluetooth signal and its strength. Challenges we ran into Connecting raspberry pi to wifi - at first we didn't have monitor/keyboard Installing windows for Atmel development tools required to fix problems with smart lighting Forgot that PHP does not detect isset() if the value is equal to zero Sleep One of Ōura rings didn't log the activity information because the person slept at a place without internet ... Accomplishments that we're proud of Integration of many different techonolgies and hardware Fixing several bugs with smart lighting system Designing website that looks nice also on phones and tablets Learning to use Azure ... What we learned Azure Ōura ring API Paulig Muki API Tracking Bluetooth devices and their distance in python 3D printing committing to GIT regularly ... What's next for zzzyield Additional environmental feedback devices should be added (e.g. smart heaters, other lamps etc.). Also better analysis of Ōura ring data should be done in the long term, possibly by applying machine learning/deep learning algorithms. Long term tests of the productivity and impact on health and employee satisfaction should be done. The team will be evaluating the future prospects of this technology and possibly look for interested investors. <div