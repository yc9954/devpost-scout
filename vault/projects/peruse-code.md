---
slug: "peruse-code"
url: "https://devpost.com/software/peruse-code"
title: "Peruse Code"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 496
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
---

# Peruse Code

> Peruse Code makes it easy to read code online so you can write better code!

[Devpost](https://devpost.com/software/peruse-code) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]] [[educator_student]] [[general_public]]

**stack** amazon-dynamodb, javascript, node.js, postman, python, react, serverless

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for peruse code

## Body

Annotate and make comments on files a repo Share your editor on your socials Use our rich editor to add coments and notes Save your faves! Use the chrome plugin Inspiration “Indeed, the ratio of time spent reading versus writing is well over 10 to 1. We are constantly reading old code as part of the effort to write new code. ...[Therefore,] making it easy to read makes it easier to write.” ― Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship Whether it was internal code reviews, trying to understand the code from a tutorial about that shiny new framework you wanna learn or simply just to peek under the hood of your favorite open source project. We as developers spend a huge chunk of time reading code and a lot of this code is stored and hosted on Github. Peruse Code makes it easy to read code online so you can write better code! What it does Peruse Code - turns your favorite Github reposistory into a easy to navigate code editor online Peruse Code comes with a nifty note feature that allows you to annotate individual files and add additional comments, input and feedback. You can also save your favorite repos and access them from either your computer or on the go using your mobile phone. We've also written a chrome extension that simplifies viewing repos and saving them on the fly in your browser! Check it out: Install Peruse Code Chrome Plugin How we built it Frontend - our frontend is written entirely React and a service worker to allow for PWA functionality - so you can install the app in your home screen and use it as a mobile or desktop app. The backend is a microservices architecture built with Serverless, mostly node and sprinkles of python code. We use DynamoDB to store data - we choose this because of the scalability and low latency it offers. Use the public workspace to test the API and how we use Github: View Our Workspace Challenges we ran into We had so many more ideas and features we wanted to pack into our initial release but with the limited time of the hackathon we had to streamline our feature roadmap. Accomplishments that we're proud of We put together a really good workspace on Postman We put together a good initial release - just in time! Our chrome plugin got approved as well We became users of our own product at least What we learned We had to learn a lot about the Github API, It's authentication methods and we used Postman a lot for API discovery and testing before writing any code. What's next for Peruse Code We have a list of features we wanna add in the next release - we've also created a project roadmap that we intent to follow but feedback from people might help us shape the app to be useful to more than just us! <div