---
slug: "orderiq"
url: "https://devpost.com/software/orderiq"
title: "OrderIQ"
hackathon: "Google Cloud Vertex AI Agent Builder Hackathon"
organization: "Google"
winner: true
words: 588
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# OrderIQ

> Struggling with long lines and frustrated customers? OrderIQ streamlines ordering with an AI-powered system. Customers order directly, staff focuses on service, and everyone enjoys a better experience

[Devpost](https://devpost.com/software/orderiq) · hackathon [[Google Cloud Vertex AI Agent Builder Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[health_clinical]] [[supply_logistics]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** google-storage, google-translate, next, node.js, vertexaiagent

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for orderiq

## Body

Normal Crud operations on cart Edge cases + another language Inspiration Imagine this: You're starving after a long day, rushing to grab a bite at your favourite fast-food joint. But instead of the delicious aroma of burgers🍔, you're greeted by a sight that makes your stomach churn – a seemingly endless line snaking towards the register. And even after battling the line, the ordeal isn't over. You finally place your order, only to face another 10-minute wait⏳ for your food to arrive. The real culprit behind these slow lines and extended waits isn't the overworked staff!!! The problem often lies behind the counter, with outdated Point-of-Sale(POS) systems creating a bottleneck. Having worked at one of these stores myself, I've seen firsthand the struggles of both customers and employees. But what if there was a better way? Well, there is... What it does OrderIQ swaps your traditional POS for a user-friendly, AI-powered system with voice recognition. The key to having fast moving queues is having multiple OrderIQ kiosks nestled together enclosed in a little plastic barrier to keep the orders separate. Customers order the way they're accustomed to , but with a brilliant assistant by their side. OrderIQ automates order processing, freeing your staff to focus on what matters the most: exceptional customer service and creating delicious food. WHY OrderIQ: Order in Any Language: No need for language barriers! OrderIQ understands your order, no matter the language you speak. This smoothens the process for everyone and helps boost sales. Better Answers: OrderIQ is using a macro and menu document stored in google bucket and an API to keep track of products and inventory, which means it is updated at all times. So customer can ask questions like "How much calories does a latte have?" or "Whats the caffeine does a americano have?", which a cashier usually cannot answer. How we built it The demo in the video showcases a presentation agent that accesses a datastore tool. This tool holds detailed information about each menu item, including prices and nutritional information. The system is designed to be flexible; you can easily swap out the current file for an updated menu from a different store, and a new agent will handle the new menu seamlessly. The agent is also connected to openAPI specifications, enabling translation and saving the current cart to a database. The frontend regularly polls this database, parsing the data into a table for display. In a real-world setting, there would be no need for a separate database. Instead, the openAPI spec would send the updated cart information directly to the POS system, which would then be parsed and displayed to the customer in real-time. What's next for OrderIQ Hidden Insights : Traditional sales analytics only tell part of the story. They capture completed purchases, but what about the customers who start an order and change the order or never finish?This could be a cool roadmap for OrderIQ which could beyond the final sale, capturing valuable data throughout the customer journey to product actionable insights like: Customer Behaviour : Analyze common questions and cart edits. Menu Optimization : Discover which items are frequently added or removed. Streamline the ordering process : Identify confusing menu sections or cumbersome steps. Voice Assistance Integration : I want to integrate OrderIQ with smart systems like Google Assistant, Siri or Alexa that would allow customers to order hands free, even while driving. Events & Hospitality : Ordering food and drinks at events or in hospitality settings could be streamlined with Verve's AI system. <div