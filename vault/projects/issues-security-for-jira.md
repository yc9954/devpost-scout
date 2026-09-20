---
slug: "issues-security-for-jira"
url: "https://devpost.com/software/issues-security-for-jira"
title: "Issues Security for Jira"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 396
team_size: 6
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Issues Security for Jira

> Allowing users to use online signatures on Jira Cloud issues with personal contactless cards.

[Devpost](https://devpost.com/software/issues-security-for-jira) · hackathon [[Codegeist 2020]]

## Facets


**stack** forge, heroku, java, javascript, jira, microservices, react, reactnative, spring, thymeleaf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for issues security for jira

## Body

Forge - Register account Spring Boot Authentication Server - Register form Mobile App - Login Screen Mobile App - Register device and card Forge - Sign issue Mobile App - Requests list Mobile App - Completed sign issue Forge - Completed sign issue Inspiration Jira Cloud lacks in securing issues with elements, such as online signatures. Currently, our company Transition Technologies PSC, in order to migrate from Jira Server to Jira Cloud would need such a feature. On Jira Server, we managed to solve this problem by custom development. We also wanted to test out the newest Forge technologies and check it's compatibility with other external micro services, such as the ones created in Spring Boot and mobile applications (such knowledge could be useful in the future). What it does Our system allows your Jira Cloud's users to register into our independent Spring Boot application, and later with such account, to sign Jira issues, using our mobile app and contact less card. After you install our Forge application in your Jira Cloud instance, you must do the following steps: You must authorize our Forge app on your Jira Cloud. On issue view, users will first need to register in our Spring Boot application.. Continue registration by logging on mobile app, and providing contactless card (you must have NFC module). Beware: you can register only one device and one card per account! Going into your Jira Cloud issue, and sending requests for signing issue. Approving request by logging on mobile app. And that's it! Your issue is signed! How we built it Our system is composed of 3 elements: Spring Boot application, deployed on Heroku. Mobile application on Android (in the future, iOS), written in ReactNative. Forge application. Challenges we ran into Connecting 3 separate, independent micro services, which depend on each other, creating one system. First experience with new Forge technology. Accomplishments that we're proud of We can show our company the possibility of migrating from Jira Server to Jira Cloud, by providing the same level of security, as it is currently created, in our addon. What we learned We learned the basics of Forge, and we improved our current abilities. What's next for Issues Security for Jira Our system is in alpha version. There is a lot of space for improvements, such as: Improving security measures. Better user experience. Multi platform. iOS mobile application. <div