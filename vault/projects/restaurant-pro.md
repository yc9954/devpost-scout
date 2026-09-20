---
slug: "restaurant-pro"
url: "https://devpost.com/software/restaurant-pro"
title: "Restaurant Pro"
hackathon: "HubSpot Themes Challenge 2021"
organization: "HubSpot"
winner: true
words: 343
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Restaurant Pro

> Designed for quickly creating a beautiful restaurant website that will put your restaurant at the top of local search results via it's integrated Schema.org markup and performant architecture.

[Devpost](https://devpost.com/software/restaurant-pro) · hackathon [[HubSpot Themes Challenge 2021]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[video_visual]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** css, hubl, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for restaurant pro

## Body

Quickly create an online menu with tons of customizability Easily add multiple locations to the Google Maps embed Get your restaurant website up and running in no-time with Restaurant Pro Inspiration Our designer came up with the idea of making a giant hot pocket the size of a burrito and started making a fake brand/company for it. Fast forward a few months and we have an entire HubSpot Website theme for Pizzarrito, our fake restaurant/drive-thru we hope someone will make a reality for us someday 😆 What it does We tried to integrate as much of the restaurant specific Schema.org markup into our modules as possible with the goal being that the restaurant that uses this would rank the highest in their area in local search results. How we built it We used the HubSpot Boilerplate theme as our base and went from there. Page load performance was a priority for us since this is an image heavy website design. In order to combat slow image loading, we made sure that all of the "background" images were actually using <img> tags. This enables us to take advantage of native lazy loading and srcset which automatically loads the right size image based on the device size. We also coded the entire theme without jQuery, woot! Challenges we ran into The biggest challenge by far was making time for our HubSpot theme in the face of our client work. Agency life, am I right? What we learned Using the design manager is so much quicker to create modules compared to using the CLI locally. Also was the first time using the language switcher and making translations for a page in HubSpot, a really great feature! What's next for Restaurant Pro Completing a WordPress version of the theme for those customers that might have both WordPress and HubSpot pages and incorporating additional Schema.org markup for more of the modules. Additionally, we would love to include eCommerce like functionality using the new HubSpot payments feature so people can order ahead and pickup their order in person. <div