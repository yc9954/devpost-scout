---
slug: "standby"
url: "https://devpost.com/software/standby"
title: "Standby"
hackathon: "Square Developer Hackathon 2023 "
organization: "Square"
winner: true
words: 378
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
---

# Standby

> Standby makes it easy to fill the appointment slots that open up due to cancelations. One sector, 1.5 million beauticians in the US, suffers a 30% cancelation rate leading to billions of lost revenue.

[Devpost](https://devpost.com/software/standby) · hackathon [[Square Developer Hackathon 2023]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[finance_payments]]

**stack** firebase, ios, square, swift, swiftui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for standby

## Body

Standby App List of open Appointment Slots Add a new open slot and notify customers List of customers Customer views open slots and can take or decline Inspiration My service providers, and those of friends, have often complained about dealing with cancelations. This has reached a point where some are instituting cancelation fees. However I, and many I know, are flexible when it comes to when we can get the service, such as a haircut. In researching the topic, I found that cancelations are rampant in the industry, and costs tens of billions of dollars in lost revenue. But it is time consuming to reach out to clients to find one to fill an opening. What it does Standby is a mobile app and service that allows service provides a simple way to notify clients about appointment slots that open up on their calendar. Clients can decline or attempt to claim a slot when it opens. Standby is a subscription service, paid by the service providers using Square Subscriptions. How we built it I created an iOS app using Swift and SwiftUI. I integrated Firebase for the backend, and integrated the Square iOS library for card tokenization. I also wrote a layer to communicate with Square for creating identities, payment instruments, and subscriptions. Firebase is used for authentication, data storage, and notifications. Challenges we ran into Distilling the problem into a simple interface for both the service providers and the clients took a lot of iteration. I had problems integrating the Square iOS tokenization framework using the Swift Package Manager. I had to revert to embedding the library directly into the app. There was quite a bit of work writing a layer to communicate with Square and translate responses to my models. Accomplishments that we're proud of I believe this will be a useful service for a large industry, and the app I was able to build provides a solid MVP to demonstrate its usefulness. What we learned I learned how to integrate Square Subscriptions into an app, and quite a bit about some issues in the services industry. What's next for Standby Standby needs some vetting within the industry, and a few features need fleshing out, but those will be driven by feedback from potential clients. <div