---
slug: "timezone-assistant"
url: "https://devpost.com/software/timezone-assistant"
title: "TimeZone assistant"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 465
team_size: 8
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/supply_logistics"
---

# TimeZone assistant

> The TimeZone assistant app helps JSM agents to personalize communication with end users by showing the reporter's timezone, current time, and the time difference while allowing scheduling replies.

[Devpost](https://devpost.com/software/timezone-assistant) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[supply_logistics]]

**stack** forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for timezone assistant

## Body

Inspiration Supporting end users is not only a matter of time but also a matter of building a relationship with a person. The personal touch is important. While talking to our JSM agents, we noticed that sometimes they have to go as far as checking linedin profiles to understand reporters' locations to be able to personalize the message or schedule a call with them. Why don't we conveniently show the reporters location? Another point was about marketing best practices: why do marketers care when their emails are delivered while support agents are fine with sending a reply in the middle of the receiver's night? This is how the idea for TimeZone assistant app appeared. What it does For JSM: Shows time and time zones of the reporter (in case of having a portal account) and the agent to support agents Shows time difference between the reporter’s and the agent’s time zones Shows part of the day (night, day, evening) Provide an ability to schedule comment/reply to the reporter. Adds a greeting appropriate for the scheduled time of replying. How we built it This is our first Forge app. We used only React + Forge. The process went pretty smoothly. Challenges we ran into Setting up the development environment. Forge tunnel was not suitable for us, because we wanted to have full control over webpack configuration and have a hot reload during development. In order to do so we had to mock Jira api responses and develop outside of Jira iframe. Then indicate /build directory in the manifest, run build script and forge tunnel to test it in the iframe. Another challenge was to post comments on behalf of the user. Unfortunately, we encountered auth problem and did a compromise and decide to post them on behalf of the app. It would be great if performing actions on behalf of the current user will become possible in the future. Autoscaling for dynamic content is not available, we had to reserve some space for the content appearing dynamically (scheduling comments). This problem has not been resolved yet. Accomplishments that we're proud of The scheduler has been done by using Forge, similar functionality in our Connect apps required at least 2 external services. What we learned Forge is pretty cool :) It requires a little bit more effort to set up the environment, but on the other hand provides us with useful functionalities like CLI, scheduled and web triggers. It also seems like Forge offers more extension points and it's easier to manage them in the manifest file (which we like a lot) than it was in Atlassian-connect. What's next for TimeZone assistant Lots of space for improvements: Configuration with time format, daytime icons Configuration with templates for responses Showing the list of scheduled events and others <div