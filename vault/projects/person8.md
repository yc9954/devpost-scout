---
slug: "person8"
url: "https://devpost.com/software/person8"
title: "Person8"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 413
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Person8

> A Lifeline for Digital Nomads

[Devpost](https://devpost.com/software/person8) · hackathon [[MongoDB World Hackathon]]

## Facets

**domain** [[finance_payments]] [[housing_homeless]] [[labor_employment]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** blockstack, clojure, lightning, mongodb

## How they structured the write-up

- solution
- implementation with blockstack and lightning
- what's next for person8

## Body

Sign in to the app from any device through Blockstack Review personal identity information encrypted in Blockstack's Gaia Click to reveal identity documents Share documents via SMS Request emergency funding via the Lightning network Social Impact Person8 helps homeless youth restore and maintain their identity. There are 8000 homeless individuals just in San Francisco, the second highest homeless density in the United States. A growing number of them are youth: One in ten young people in America experience some form of homelessness in the course of a year. Most have a mobile phone , typically being their primary computer device. It is an anomaly to find a homeless person who has all their identity documents. To get them properly connected to homeless services, they need their birth certificates, social security cards, health insurance records, and other documents. Many homeless people don’t have those documents. Solution Person8 provides a digital footprint that can’t be deleted, lost or stolen. It keeps a copy of their identity documents and other key information, hosted securely online through Blockstack so a missing phone won't become a crisis. The individual will have access to their own records and have control over who can see it. For homeless without a mobile device, their identity profile will also be universally accessible for them, through for example public computers like those found at the libraries. A homeless service worker approaching someone on the street will be able to find their identity records without having to bring them into an office and locate a physical file folder. Person8 can be used to request emergency funds via Lightning. The owner can generate a Bolt11 invoice in the app and send it via SMS to their patron. Implementation with Blockstack and Lightning Person8 is implemented as a serverless React based SPA in Clojure targeting Javascript (ClojureScript). It uses Blockstack for authentication and encrypted data storage, and Lightning / Bolt11 for funding requests. The application applies mobile-first Material Design but is responsive to also provide a decent experience on any size computer display. What's Next for Person8 We hope to raise funds from social good arms of local companies and set up a team at the San Francisco brigade of Code for America . We’d like to co-develop the app in participation with homeless youth, with the side effect of introducing them to product development, which may open up further opportunities and inspire them to a path forward. Support us with a slice on Pietron! <div