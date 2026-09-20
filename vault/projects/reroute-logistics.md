---
slug: "reroute-logistics"
url: "https://devpost.com/software/reroute-logistics"
title: "Reroute"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 379
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/structured_db"
---

# Reroute

> Local reworks for rejected freight by trusted warehouses

[Devpost](https://devpost.com/software/reroute-logistics) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**domain** [[finance_payments]] [[supply_logistics]]
**substrate** [[structured_db]]

**stack** firebase, gatsby, quickbase, react, stripe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reroute

## Body

they could sure use a reroute... our quickbase architecture freight carrier dashboard warehouse dashboard Inspiration Over $35 billion was spent dealing with rejected freight in 2019. Currently, freight carriers can do one of two things when a customer rejects their shipment: 1) they can return the truck home and lose an additional $4,000-$6,000, or 2) call around to local warehouses near the customer and try to get the load reworked. Most "local warehouses" do not advertise themselves very well, but desperately want more business. Finding local warehouses can be very time consuming and our goal is to help them connect with freight carriers. What it does Reroute allows freight carriers to broadcast their rejected freight issues nationwide and receive price estimates from local warehouses. Carriers who use local warehouses to rework their damaged freight save thousands of dollars versus returning shipments all the way home. How we built it The frontend is a static ReactJS app built by gatsby served by an NGINX webserver. Our payments are processed via the Stripe API and a NodeJS with Express server running on the same box as the webserver. The backend is a quickbase app with four tables: Freight Carriers Warehouses Bids (Price Estimates made by warehouses) Reroute Cases (Issues posted by freight carriers) Challenges we ran into Our original solution was built using firebase's NoSQL realtime database, but we ran into issues scaling that to real customers and had to fall back to our old method of emailing/phone calls. We hope to have more success using a more stable platform (Quickbase) as our backend. Accomplishments that we're proud of We were able to build our Quickbase App incredibly fast, it literally took an afternoon of poking around in it to get it on par with our current firebase solution. What we learned We originally tried to build our app from scratch, but realized our value-add was not in our tech, but in our relationship with customers. So, we are excited to move our backend to a low/no-code solution to have more time for dealing with customer support and growing the business. What's next for Reroute We are testing our software with a single freight carrier right now, but we are excited to grow and increase our coverage across the US. <div