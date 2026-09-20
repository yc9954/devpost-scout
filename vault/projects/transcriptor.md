---
slug: "transcriptor"
url: "https://devpost.com/software/transcriptor"
title: "Transcriptor"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 242
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
---

# Transcriptor

> This is a simple tool to transcribe all your developer/business meetings on zoom. With this, you will never have to remember all the details/ make simultaneous notes and you can focus on the meetings.

[Devpost](https://devpost.com/software/transcriptor) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** api, ibm-cloud, node.js, postman, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for transcriptor

## Body

Sample Zoom Meeting Sample Audio Test Inspiration With this pandemic going, people have been working from home and have a lot of day-to-day meetings, which exists along with family engagements. Sometimes we are distracted , or maybe not in a fully concentrated mode to focus. This leads to missing out on some key details / or misunderstanding of information. This tool solves the problem by transcribing your meetings in texts , so you never miss out on anything and can focus/ read through the meetings whenever you are ready. What it does This basically is a simple webapp one can use to transcribe your live/prerecorded meetings on zoom and save them as text (or any other file format preferred) along with a meeting headline and other details for later reference. How we built it I used Nodejs as the main server language, and React for frontend components. I am using IBM cloud speech to text API for conversion to notes. Challenges we ran into Integrating Zoom SDK in the webapp. Testing the IBM Cloud API Connecting to Zoom meetings from within the web app What we learned Using IBM Cloud Service for speech to Text conversion Integrating Zoom within the Webapp Working with Postman API What's next for Transcriptor Polish the Project, and optimizing the code for both offline and online usage. Enabling it to be useful for other meeting platforms like GoogleMeet. Explore other more efficient ways for speech-to-text conversion. <div