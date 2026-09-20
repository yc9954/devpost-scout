---
slug: "shizo"
url: "https://devpost.com/software/shizo"
title: "Shizo"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 484
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/housing_homeless"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Shizo

> Shizo is a metaverse map based on the physical world's map where you can buy and sell digital roads and lands and change their appearance.

[Devpost](https://devpost.com/software/shizo) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[housing_homeless]]
**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** golang, near, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shizo

## Body

Inspiration With the growth of the Metaverse, it would be necessary for this digital world to have a map just like the physical one. While there are many Metaverse platforms out there, we still don't have a super convenient map. What it does It's a digital map where everything is selectable (from roads to parks, and even each individual building) and users can mint them as NFTs. Users can update the appearances of their lands. For instance, they can change the building's color or the road's name and these changes would apply immediately to the map. New names would be searchable allowing other users to find other's properties on the map easily. In addition, each owner can add a "YouTube Embedding" or a "Link to External Website" to their land. For instance, if a user has created a VR experience of their property, they can show a preview of that in the "YouTube Embedding" and can link the VR experience via "Link to External Website". No need to mention that users can also set a price for each of their properties to sell it. How we built it Shizo has 4 main parts: On the user interface level, we created a DApp using React that enables users to buy/sell lands. They can also set a price and change lands' data and appearance. We took a snapshot of the physical world's data and use it to generate our own map from scratch. Since there's no need for a third-party map service, users have the complete freedom of changing any data of their lands on Shizo. We created a backend that is written in Golang for serving map tiles and also caching data. We also took advantage of using ElasticSearch for indexing and caching addresses and names to build Shizo's search engine. Challenges we ran into Coming with no background in web3, developing for NEAR was pretty easy. We expected that developing a DApp would be the most difficult part of the whole process and we were surprised to realize it wasn't hard at all! This aspect of NEAR saved us a lot of time that we invested in other challenging parts like changing the data on the map in real-time without generating map tiles again. Optimizing the map was the most time-consuming one but we're satisfied with the quality. Accomplishments that we're proud of Creating a map service from scratch using web3 technologies in such a short time! We're also proud of the UI/UX of Shizo DApp. What we learned Many aspects of NEAR but there is still a lot to learn. What's next for Shizo Enabling users to merge roads and change the geometry of lands Creating a marketplace to buy/sell multiple lands in a single transaction with a discount Enabling users to rent a land Auction Migrating all of the map's data to chain and use Shizo backend just for caching data <div