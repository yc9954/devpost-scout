---
slug: "swapper-8u4rq0"
url: "https://devpost.com/software/swapper-8u4rq0"
title: "Swapper"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 510
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Swapper

> Platform for facilitating exchanging, lending, or borrowing local items

[Devpost](https://devpost.com/software/swapper-8u4rq0) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** go, ravendb, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for swapper

## Body

Home Page Conversations Page User Page User Reviews Item Page Inspiration We are both passionate about full-stack development and thought that the track proposed by RavenDB would not only be a fun challenge, since we're both college students we often have old items we're not using anymore like textbooks that we don't need anymore and would like to give to someone in need. We build this in hopes that this project could benefit or inspire people our campus community to reduce waste. What it does The platform filters items posted by users based on distance from the user's selected region. User are able to specify different filters and categories of items to ensure they are matched with items most relevant items to their needs. The facilitation of item exchanges is promoted by our messaging feature which allows users to coordinate and exchange items after messaging through the item page. Each user and items have separate pages where they can be rated by other users to promote trust worthy people on the platform. Furthermore, we ensured that we had safe and secure user authentication, protected user messages, and made sure users could not specify the exact address of products so that their home location would be protected. We also allow users to upload their own profile pictures which will show up elsewhere on the app which we forgot to highlight in our demo. How we built it We utilized RavenDB's Go client and gin to create our projects backend. We also utilized React and Vite on the frontend to provide a nice user interface. Challenges we ran into Programmatically creating spatial indices with RavenDB in Go, which we were able to figure out after some help from the support team. Another big challenge was styling our front-end. Although we both enjoy full-stack development, We would both consider our strengths to lie more in the backend and frontend state rather than the actual css/html design portion of the frontend. This is something we worked through and had to spend a fair bit of time polishing and is something we are pretty proud of! Accomplishments that we're proud of We both are super proud of the UI we were able to come together and design and create together, since we both haven't done much design work before. What we learned We learned that especially in a hackathon, usually your first step is going to be making a bad looking UI then over time polishing it up in an incremental fashion after you have the core features completed. We also learned a lot about efficient filtering in RavenDB and using spatial indicies. We also learned how to support messaging between users, and optimization of the queries with grouping. What's next for Swapper We'd like to set up automation around reminding people to return items that are lended out to them by a specified return date so that other users of the platform and get a chance to use them. We'd like to integrate this through sending out emails to our users and more. <div