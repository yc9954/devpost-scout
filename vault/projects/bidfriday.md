---
slug: "bidfriday"
url: "https://devpost.com/software/bidfriday"
title: "BidFriday"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 908
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# BidFriday

> Simplify and automate the bidding process for your projects.

[Devpost](https://devpost.com/software/bidfriday) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**domain** [[health_clinical]]
**substrate** [[structured_db]] [[web_dom]]

**stack** javascript, node.js, vue

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bidfriday

## Body

A simple UI to request details on products vendors offer. Invite vendors to submit bids for your requests. Get an overview of prices offered for by different vendors. See details of all items received across all vendors in one place. View details from a bid in an easily accessible clean format. See items which were added after bids were submitted. BidFriday tracks changes to item details and highlights them for owners and vendors. Use Monday to manage your requirements from one place. See details of all bids submitted for your requests. Inspiration It is meant to address a pain point I experienced while working as an interior architect. In course of doing the interior (design and build) for a client the workflow would involve developing a design, preparing a bill of quantities and distributing the quantities to different vendors (based on their specialties) to source the material or services. eg: supplying furniture, designing HVAC systems, supplying glass etc. However very often the design would change in the middle of the process and the task of redistributing the updated quantities would turn into an overwhelming book-keeping effort. Vendors would often submit quotes on outdated quantities and the back and forth communication spanned across different specialties would run into long chains of emails and an overall coordination nightmare. The task itself (of sending the updated quantities) would often be mundane and it felt like a large part of the process could be automated. Besides the benefits of ease of updates it would also minimize errors in the process. The format was also so standard that the same templates were used across different projects. What it does It's a platform to coordinate the bidding process on a list of required materials and/or services. Projects owners can create a list of items that needs to be sourced for a project and invite vendors to bid on them by sharing a link. The link allows vendors to submit bids on the items and update with changes if necessary. Instead of a stream of email back and forth with attachments the participants can view the most up-to-date versions of the item lists and corresponding bids on the application. As the project requirements change they can update the list in one location and the updates would be rolled out to interested vendors who can then update their bids. The application smartly tracks the changes in the the requirements and highlights the updates to be easily viewed by the project owners and bidders. The dashboard view allows the owners to view bids received and helps them compare and analyse them to make sure they get the best deal. How I built it The application is a Monday app with item lists being created from Monday boards. It reads and curates the data in a format conducive to track changes in the item list as the project progresses. The lists can be publicly shared to vendors who can bid on the item lists without necessarily needing a Monday account. The information submitted by bidders is collated and presented in a concise dashboard within the Monday board for the project owner. The app also meaningfully tracks the bids for the versions of the item list for which it was submitted and it can notify the relevant participants if any updates are needed. The app is built as a nodejs web project with the UI based on a vue frontend. MongoDB is used as the database with the front and backend connected via an express server. Challenges I ran into The scheme required for meaningfully tracking changes as the item list changes turned out to be a interesting challenge. The final outcome turned out to be pretty good after lots of trials and errors. It is able to track the changed parts in a very neat way so less time can be spent in trying to spot the differences between different versions. The overall UI was also a very challenging part. There's a lot of information coming from different sources into the dashboard. One part of my project would have worked a lot better if a Monday template could be shipped with an app. But I'm keen to pitch the template and see if it could be a part of the standard templates offered. The bidding process and format is pretty generic and I'm sure it would be useful across a lot of practices/workflows. Accomplishments that I'm proud of The problem I'm seeking to address has been a particularly sore pain point in the entire workflow. I am happy to have been able to build a system which I think can meaningfully address the problem. As mentioned earlier it's doing a great job to tracking changes which I think is very useful when running on tight deadlines. What I learned I had to setup multiple authentication systems to manage separate access for different kinds of users. That was a new challenge for me in terms of developing web apps. What's next for BidFriday My experience with the problem has been from an architecture design point of view. However I feel the workflow is common across a lot of practices. The process described could be used to procure anything - from office stationery to hospital supplies. I would love to gather feedback from others who may use the app and improve to make it fit their workflows. Website Monday App Link Short Video Detailed Video Setup the Monday Board <div