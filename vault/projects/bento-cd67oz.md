---
slug: "bento-cd67oz"
url: "https://devpost.com/software/bento-cd67oz"
title: "Bento"
hackathon: "Square Unboxed Hackathon"
organization: "Square"
winner: true
words: 682
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/structured_db"
---

# Bento

> A solution for managing combo inventory.

[Devpost](https://devpost.com/software/bento-cd67oz) · hackathon [[Square Unboxed Hackathon]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**substrate** [[structured_db]]

**stack** express.js, mongodb, react

## How they structured the write-up

- 💡 inspiration
- 🧪 what it does
- 🔨 how we built it
- 🖥️ how the terminal api was implemented
- ⚔️ challenges we ran into & what we learned from them
- 🏆 accomplishments that we're proud of
- ⏩ what's next for bento

## Body

Creating an inventory item Creating a recipe for a catalog item Breakdown of order with inventory deductions Terminal API usage 💡 Inspiration While I was browsing the Square community threads, I noticed that sellers wanted a solution to track the inventory of items sold in bundles or combos. That's where I got the inspiration to create 🍱 Bento! 🧪 What it does With Bento, sellers can: Create inventory items in the database to track stock Create a recipe for a catalog item (an item available for sale in the POS) using inventory items: When a recipe is created for a catalog item, every time a customer buys that catalog item, the corresponding "ingredients" will be deducted from inventory. View an itemized breakdown of a customer order: For each item sold, what was deducted from inventory? Track the history of inventory item changes over time 🔨 How we built it My project uses React for the frontend, Express for the backend, and MongoDB for the database. Deployment was done via Heroku. The app also relies on the following Square APIs: Catalog API Orders API Terminal API 🖥️ How the Terminal API was implemented I implemented the Terminal API in the following ways: Sending test orders: A seller can send a test order to ensure that their recipes are working as intended. These orders are processed via the createTerminalCheckout endpoint of the Terminal API using a device ID provided by Square (link here ). Processing orders when payment is completed at the terminal: My app has a subscription to the Terminal API webhook and listens for a terminal.checkout.updated event. When it receives event data, my app checks for a payment_status of "COMPLETED" , indicating that a customer has just finished paying for their order at the Square Terminal. My app can then use the order_id field to retrieve order details, compare those details against the seller's recipes, and deduct ingredients from inventory. ⚔️ Challenges we ran into & what we learned from them Conditional form fields: Since the user could add as many ingredients as they wanted for each recipe (or even choose not to add ingredients at all!), most of my form fields were conditional. This made it a little challenging to control my components, because I'm used to following the [name, setName] pattern that comes when you know all your form fields beforehand. I figured out a way to give each input an identifier that was unique yet still tied the input to a specific variation/modifier. Data structures: While I definitely tried to plan ahead and draft a database schema that would work, I constantly found myself editing my schema as my application evolved. I fell into the trap of premature optimization, where I kept thinking about how to organize the data most efficiently rather than what my specific use cases would be, both now and in the future. Timezones: I was pretty baffled when my server-side JS parsed an RFC 3339 timestamp from a Square order and gave me a time that was 4 hours in the future. I realized, after a bit of research and experimentation, that that happened because I live in the GMT-4 timezone and the server was returning a GMT+0 time. The browser did not have this issue, and processing timestamps in the frontend with .toLocaleTimeString() gave me the correct time. 🏆 Accomplishments that we're proud of This app was both my first MERN stack app and my first time using a server to handle webhooks! I'm really proud that I managed to get it up and running. ⏩ What's next for Bento I have so many ideas about where to go next! For one, I want to implement a feature that notifies sellers when their inventory runs below a certain threshold. I'm thinking about using the Twilio API to send text message notifications. In addition, when a seller runs out of an inventory item, I want to mark catalog items that depend on that inventory item as out of stock. That way, customers can't purchase those catalog items from the POS until inventory is replenished. <div