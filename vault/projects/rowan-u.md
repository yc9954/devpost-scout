---
slug: "rowan-u"
url: "https://devpost.com/software/rowan-u"
title: "Rowan U"
hackathon: "Alexa Skills for Students – Powered by AWS Educate"
organization: "Amazon"
winner: true
words: 416
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Rowan U

> Get information about Rowan University and Glassboro NJ

[Devpost](https://devpost.com/software/rowan-u) · hackathon [[Alexa Skills for Students - Powered by AWS Educate]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-alexa, amazon-web-services, mysql, python

## How they structured the write-up

- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for rowan u
- try it out

## Body

What it does Rowan U provides information for all aspects of your college experience at Rowan University, from before you apply through graduation. Before you apply to Rowan, try Alexa, ask Rowan U when is the next open house? After you move in to your freshman dorm, ask What is there to do in Glassboro? If you are hungry, try asking How long is the line at Jersey Mikes Subs? or Find me free food on campus If you want to work out, ask How busy is the rec center? or When is the next baseball game? Stay up to date about events on campus. Ask What is the next Rowan After Hours event or When is the next movie night? It can even help until graduation day. When is finals week? or What time does the library close? How I built it I used the Alexa Developer Console to create the voice intents. My program is hosted on AWS Lambda with the ASK SDK for Python . My skill utilizes a number of public APIs to provide information. • To access the wait for food my program is utilizing the Tapingo API . • My program searches the Proflink website to find events on campus, as well as finding free food. • Rowan University lists how busy the gym is on their website . I am feeding this data to my Alexa skill. Challenges I ran into Originally I had trouble creating the GUI for the Echo Show and Alexa apps. However, once I found the ASK SDK it made the process much easier. I was able to just pass the title and image to the sdk and it generates the layout for me. Accomplishments that I'm proud of I'm proud that I developed an application that provides easy to access information about Rowan. The school has a number of apps all of which provide information about the school. Between ordering food, checking my grades, and finding events, I have at least 5 "rowan apps" on my phone. This Alexa skill allows me to access of the information in one place. What's next for Rowan U I plan on expanding my Alexa skill to other universities. This could be useful to all college students, no matter which school you go to. Many schools also use CampusLabs for planning events, so it would be easy to support other universities. Try it out Tell your Alexa device to "Open Rowan U" or watch the demo video <div