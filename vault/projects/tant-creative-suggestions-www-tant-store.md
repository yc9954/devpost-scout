---
slug: "tant-creative-suggestions-www-tant-store"
url: "https://devpost.com/software/tant-creative-suggestions-www-tant-store"
title: "Tant, creative suggestions – www.tant.store"
hackathon: "Junction 2016"
winner: true
words: 577
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/web_dom"
---

# Tant, creative suggestions – www.tant.store

> Tant offers you tailored clothing suggestions via Zalando based on your Deezer preferences and Instagram activity.

[Devpost](https://devpost.com/software/tant-creative-suggestions-www-tant-store) · hackathon [[Junction 2016]]

## Facets

**substrate** [[web_dom]]

**stack** azure, css, deezer, go, html, instagram, javascript, zalando

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for tant, creative suggestions – www.tant.store

## Body

Welcome 3-field form Login to Deezer and/or Instagram Apparel choices Tailored preferences Redirect to Zalando Inspiration Everyday we define ourselves from the rest with our actions, choosing particular outfit over another or listening to certain kinds of music. We wanted to optimize the already existing recommendation systems to help users find the clothes and outfits their points of reference are wearing. What it does Tant suggests tailored clothing offers to its users by analysing their presence in Deezer and Instagram. The app is integrated with Zalando’s Shop API to facilitate the purchase of the desired clothes. The onboarding to the app is very simple since it consists of a 3-field form (gender, age and country) and the login to either the user’s Instagram and/or Deezer account. When the user is ready to run Tant, our algorithm calls Zalando’s Shop API to scrape all the brands in stock, then analyses the shopper’s presence on the previously mentioned platforms and returns the most suitable pieces of apparel. How I built it To build Tant, we’ve chosen Zalando’s Shop API, Deezer’s API and Instagram’s API to develop our core service. Go has been adopted as backend language using BeeGo as the preferred framework since it helps us cut down the developing time. The development of the frontend has been carried out using HTML, CSS and JavaScript as core languages. Radix has been kind enough to offer us the domain tant.store for free but the site is hosted in our own server. To browse the web, we’ve used Azure Cognitive Services as search API to fetch all the information regarding the artists. Challenges I ran into We ran into several challenges while developing and deploying the project. The fact of linking 2 different concepts (music and clothing) supposed a series of product design challenges until we reached the final breakthrough. On the one hand we had a trouble with Deezer’s authentication library that didn’t work properly with Go’s OAuth. On the other hand, Instagram forces you to verify the application you are willing to develop, this implies a series of limitations regarding the calls to their API. In order to solve this issue we had to hack our way by using less elegant ways of achieving our goals, bypassing their sandbox environment as much as we could. Accomplishments that I'm proud of We are very proud of the fact of being able to link 2 concepts that might seem so distant conceptually speaking and blend them seamlessly in one product that is ready to use as it is. We’re also happy because we’ve been able to integrate every API under the same umbrella. What I learned Although the rest of the team has previous experience in hackathons, this has been my very first one. I've had the chance to develop a product from scratch, getting to know the different parts of the process and being able to hone my product development skills. What's next for Tant, creative suggestions – www.tant.store We want to keep Tant as a standalone app and engage in conversations with both Deezer and Zalando to improve the service we’re offering to our users. Refining the current version of the algorithm to eliminate false positives and improve the results displayed at the moment. Next stages of development would include implementing a social feature to share outfits and music preferences allowing us to build a larger and richer graph that would greatly improve our recommendation system. Website: www.tant.store <div