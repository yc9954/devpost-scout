---
slug: "encountable"
url: "https://devpost.com/software/encountable"
title: "encountability"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 509
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# encountability

> friends don't let friends forget to pay each other what they owe!

[Devpost](https://devpost.com/software/encountable) · hackathon [[Hack the North 2023]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** cockroachdb, css3, flask, html5, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for encountability

## Body

Inspiration Have you ever gone on a nice dinner out with friends, only to find that the group is too big for your server to split the bills according to each person's order? Someone inevitably decides to pay for the whole group and asks everyone to pay them back afterwards, but this doesn't always happen right away. When people forget to pay their friends back, it becomes somewhat awkward to bring up... Enter Encountability, our cash transfer app! What it does Encountability was created as an alternative to current cash transfer mechanisms, such as Interac e-transfer, that are somewhat clunky at best and inconvenient at worst - it sucks when the e-transfers don't arrive immediately and you and the person you're buying stuff from on Facebook Marketplace have to stand there awkwardly shuffling your feet and praying that the autodeposit email arrives soon. You can add friends to the app and send them cash (or request cash of your own) just by navigating to their profile on the app and sending a message in seconds! The app also reminds you of money you owe to any friends you might have on the app, ensuring that you don't forget to pay them back (especially if they shouldered everyone's bill last time you went out) and you spare them the awkwardness of having to remind you that you owe them some cash. How we built it We built the backend in Python and Flask, and used CockroachDB for the database. The RBC Money Transfer API was also used for the project. For the frontend, a combination of HTML, CSS, and Javascript was used. Challenges we ran into The name Encountability is a portmanteau of "encounter" and "accountability"; this was because we originally envisioned an RPG-style app where dinner bills that needed to be split could be treated like boss monsters and "defeated" by gathering a party of your friends and splitting the bill amongst yourselves easily. Time constraints were in full force this weekend, and we had to cut down on some of our more ambitious planned features after it became evident that there would not be enough time to accomplish everything we wanted. There were some difficulties with learning the techniques and tools necessary to integrate frontend and backend as well, but we pushed through and created something functional in the end! Accomplishments that we're proud of Despite the hurdles and the compromises (and the time constraints... and the steep learning curve...) we were able to create something functional, with a prototype that shows how we envision the app to work and look! What we learned databases can be fiddly, but when they work, it's a beautiful thing! Sanity Walks™ are an essential part of the hackathon experience so are 30-min naps What's next for encountability We'd like to connect it to bank accounts directly next time, just like we originally intended! It would also be nice to fully implement the automatic transaction-splitting feature of the app next time, as well as the more social aspects of the app. <div