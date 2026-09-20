---
slug: "globby"
url: "https://devpost.com/software/globby"
title: "DayTrip"
hackathon: "Google Maps Platform Hackathon"
organization: "Google"
winner: true
words: 744
team_size: 7
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# DayTrip

> Planning an amazing DayTrip in seconds. wherever you are, whenever you want to start your day, we will help you choose the best places to visit around you, and help you navigate to every step

[Devpost](https://devpost.com/software/globby) · hackathon [[Google Maps Platform Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]
  <sub>weak: financial_record</sub>

**stack** expo.io, figma, github, google-auth, google-directions, google-distance-matrix, google-geocoding, google-geolocation, google-gmail-oauth, google-maps, google-nearby-places, google-places, heroku, mongodb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for daytrip

## Body

Using Expo Client App (Expo Go) and scan this QR code Onboarding - splash page Last page of flow - summarize your day before starting navigation Product Vision Problem Statement User Needs Product Goals User Persona Main References Insights from references Insights from references Insights from references Insights from references Insights from references Inspiration We are a group of five young people, and we all love to travel. Problem is, with spontaneous travelers like us - planning a day trip in an unfamiliar place could be exhausting. There are so many different apps, Facebook groups, and websites for recommendations and reviews, and we often get lost, and plan our day in an ineffective way. That's why we immediately thought of helping travelers like us to plan an effective personalized yet time saving trips . What it does Our app uses Google's recommendations and reviews, and allows the users to choose four different activities (breakfast, activity, lunch and final attraction) around their location. After choosing, users can see a short summarize of their expected day trip and start navigating via Google Maps. Bottom line - one place that gathers for you the best recommendations, and plans the best, time saving day trip. How we built it DB: MongoDB. Server: NestJS. Client: React Native. Firstly, we integrated with Google cloud platform, explored the API until we fully understood its capabilities, response data and limitations. Secondly, we designed our app architecture including frontend, backend and DB. Only then, we started building the main components by our design system such as buttons and other global styling to make sure we can reuse our code easily. The next step was to built the main flow and logic which are the heart of the app. In addition, we integrated with OAuth and developed the sign-in with google option to make sure our users are also Google users. Lastly, we did a full QA cycles and tested all the edge cases in order to make sure our app is production ready and can work worldwide. Challenges we ran into React Native development: Developing for both Android and IOS platform has risen up some difficulties since there are some things that work and one platform but not on the other. We overcame this difficulty by running both emulators while developing to make sure our app is platform agnostic and can run smoothly for everyone. ** Time limitations One of the hardest challenges was planning sprints and prioritizing the tasks. Our vision for the app is extremely broad so we had to decide on what features to focus first and what to leave for V2. UX Challenges: . We faced many UX dilemmas. Things like - how to let the user see their chosen activities on a map, yet allowing them to choose another activity at the same time. How to do the quickest onboarding possible, yet allowing users to change their default choices if they want to. In the end, there were no shortcuts. Thorough market research, competitors research and reviewing similar references from leading apps was the only way to solve these problems. Accomplishments that we're proud of We did a full thorough process of specification of the problem, opportunities, user research, user interviews, market research, built user persona and user journey. It took us a lot of time, but it helped us to fully understand the needs and the solution that people will use. From the dev perspective, even though we faced a tight schedule, we managed to produce a well-written code which follows the best practices and code reuse principles. Moreover, we built a scalable infrastructure which would allow us or other developers to easily extend the codebase. What we learned We discovered the great world of Google Cloud platform and Google maps API in particular. In addition, we improved our teamwork and our team management. What's next for DayTrip The next major thing we aim to accomplish is the navigation flow. The app allows the user to navigate via google maps, outside of the app itself, but we think that a better user experience would be staying in the same app through the day. In addition, we want to add further customization for different users. The app currently allows users to plan a day trip for the current day, only by walking. In the future, we want to allow users to travel also with local buses or by car, and to choose their preferred experiences in advances. <div