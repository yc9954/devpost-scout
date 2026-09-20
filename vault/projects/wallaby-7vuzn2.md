---
slug: "wallaby-7vuzn2"
url: "https://devpost.com/software/wallaby-7vuzn2"
title: "Wallaby Markets"
hackathon: "Square's Local Community Hackathon"
organization: "Square"
winner: true
words: 754
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Wallaby Markets

> Markets provide creators a storefront to their local community. Wallaby extends these in-person experiences with an online marketplace that provides stall bookings and local pickups for online orders.

[Devpost](https://devpost.com/software/wallaby-7vuzn2) · hackathon [[Square-s Local Community Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** algolia, firebase, react-native, square

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what's next for wallaby markets

## Body

Inspiration I have friends and family that operate their own small businesses and sell at markets. I have seen them struggle with pen & paper booking systems or market managers that just never answer their phone so you're unable to book a stall, or hauling all these products to the market not knowing if they will even sell them. I've also noticed that almost every seller at a market is already using Square to take in-person payments. With not much extra effort they could be selling their products online, and I thought that why not integrate the in-person and online experiences together and treat the markets as a collection point for local pickups, and eventually offer a handmade retail platform with local deliveries that could essentially be "Etsy but local and powered by Square" I chose the Fostering Local Business category as I created an app that caters to small businesses and artists, who might need some extra help to get more sales and access new opportunities for getting their products out to their community. You could go from never having made a sale to booking a stall at a market and selling to hundreds of customers all with just a Square account and the Wallaby Markets app. "Wallaby" because it's keeps where you shop within one hop. (and i'm Australian) What it does It allows any number of Square sellers to join a retail marketplace that has a focus on buying locally from small businesses and artists, giving them a platform to gain more sales and customers from their local community. It will serve as a stall directory for customers to browse who is attending their local markets and when. It can allow sellers to easily locate markets in their area to sell at and book a stall. It allows sellers that work from home to offer local pickup for online orders without having to give out their home address. Customers can buy from multiple sellers in a single transaction. It filters markets, sellers and products based on your location to keep things local (but in the demo I locked it to just one location since there is limited mock data and would be empty for other locations) How I built it I built the app using React Native. Firebase was used for database, authentication and cloud functions. Square was used for it's API's. Algolia was used for product search. Once authorised a new mobile location is created in the Square account to represent the Wallaby app and the sellers catalog is synced to firebase Firestore. Any catalog changes to items available at the Wallaby App location will sync across. Sellers can then browse local markets and book an available stall. Customers can browse products from local sellers and markets upcoming in their area. They can see which sellers are attending each market and view their products and add to cart to order. Orders from multiple sellers are batched into a single checkout experience where customers can select which market they would like to collect their order from. Customers can also view the sellers stall location on a map to help find them at the market when collecting their order. Order statuses are synced with Square and update to reflect when an order is marked as collected. Challenges I ran into I joined the hackathon half way through thinking I still had an abundance of time but I'm writing this submission now with only 6 hours to spare... Everything takes longer than you think it will, and recording the video demo will take far more takes than I ever thought it would. I probably spent too much time on design elements instead of focusing on functionality first. Accomplishments that I’m proud of I love the way it looks and feels and I think it's a great little MVP of what could be a valuable platform for Sellers, Customers and Square too. There definitely seems to be a gap in the market (no pun intended) for great software for markets and I think it's an awesome idea to try and encourage people to buy as much locally as they can, rather than buying something 5000km away that you could get 500m away. What I learned I learned a lot about Firebase cloud functions and also how to implement search features into an app. What's next for Wallaby Markets Local deliveries Proper stall booking with payment, applications and approval, and access for market managers. Chat between sellers and customers for enquiries and custom products. <div