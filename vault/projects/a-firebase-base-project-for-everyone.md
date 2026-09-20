---
slug: "a-firebase-base-project-for-everyone"
url: "https://devpost.com/software/a-firebase-base-project-for-everyone"
title: "A Firebase base project for everyone"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 715
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# A Firebase base project for everyone

> I wanted to create a firebase base project and a postman collection with automated tests for it. Now I and probably other people have a nice structured base project to build their app on.

[Devpost](https://devpost.com/software/a-firebase-base-project-for-everyone) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]]
**user** [[educator_student]] [[general_public]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** css, firebase, javascript, react, redux

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for "a firebase base project"

## Body

The App base for everyone Inspiration I think, building an app can be very easy if you have the right resources. I'm Simon, a student, beginner in software development and a german citizen, so please forgive my probably bad English 😉. I always wanted to build my own base app for future app developments. A baseline that I can easily build on including all crucial functionalities like signup, login, creating a database entry, getting something out of the database, and more. I learned how to "React" with a tutorial by a YouTuber named Classsed at the beginning of the year 2020 and since practiced building an app. When I saw the hackathon announcement, I wanted to build a nice structured, easily extendable app with my own API and a React frontend. I will use this app structure for my own future company. Until now I only used Postman for single requests to test one endpoint manually, but when I started to build the app for the hackathon I knew I had to create something better. I always didn't like to manually test every single endpoint of my own API and especially things like copying the token from the login API response to other requests. So today, the 19th of January, I started to improve and automate my API requests in Postman. What it does As I mentioned earlier, the app and Postman workspace including one collection are meant to provide a good foundation for an app. The app offers a simple interface with a header, navigation bar, menu, pages, some of which already have functions and can be easily expanded, and a page structure that allows easy creation of additional pages. The Postman workspace contains a collection of requests that covers all API endpoints and makes it as easy as possible to use and extend by automatically storing tokens and document IDs in variables for further use in follow-up requests and prebuilt tests. The focus was not on the full range of all possible test scenarios, but on a clear, easily usable collection of queries. How I built it A lot of trial and error 😃. I started by learning React, continued with Redux in late 2020, and last but not least Firebase. In the process, I kept encountering errors, some of which were not directly googleable, as many things are also related to the app's own structure, etc. A small example of this is the Firebase emulators, which I only gradually got to work properly, although when I now look at the solution, I see how simple it actually was. The only problem is that this solution was not exactly summarized in one place. And so, when I saw the announcement for the hackathon, I set about building a base for future apps, incorporating all the solutions and things I learned. I started with a React app that I could run locally. I continued with the configuration of Firebase and the first functions for the API endpoints. I connected the local Firebase emulators to the React app and was able to test the rough functionality. After that, I started to transfer all necessary API requests into Postman and created my first (yes, in my whole life 😅) collection that I could run completely with a runner, including variables that are set and including tests. Challenges I ran into I already mentioned challenges, so no further boring details. But one positive thing was the easy way to implement API tests in postman. There were also challenges (e.g. Why can't I use pm.environment.name in the monitor? I had to trick by fetching the URL and seeing if it belonged to the production environment or the local environment.), but overall it was very easy to make everything work and test the whole API with one click of a button. Accomplishments that I'm proud of Actually, I'm proud of the whole project. I have learned several new programming languages and libraries in the last year and now I could apply all this new knowledge in one project. What I learned Javascript, React, Redux, Firebase, etc. What's next for "A Firebase base project" I want to use it, make it better, and build a real app for a future company with it. That would be really cool 😉 <div