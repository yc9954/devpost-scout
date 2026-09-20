---
slug: "save-the-orangutans"
url: "https://devpost.com/software/save-the-orangutans"
title: "Save the Orangutans!"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 519
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/retail_commerce"
---

# Save the Orangutans!

> Food has a massive impact on climate change and the survival of all species. We can make a difference by measuring the environmental impact of the products we buy.

[Devpost](https://devpost.com/software/save-the-orangutans) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[agriculture_food]] [[climate_energy]] [[retail_commerce]]

**stack** javascript, nest, typescript

## How they structured the write-up

- inspiration
- what it does
- save orangutans!
- how we built it
- challenges we ran into
- what we learned
- what's next for save the orangutans!
- source files
- example request

## Body

Inspiration It's no secret that our climate is changing, and food production is one of the biggest contributors. From greenhouse gas emissions, to water usage, to fertilizer run-off into water sources, agriculture and livestock farming play a major role in our health and climate. Check out these statistics from Our World in Data Food accounts for over a quarter (26%) of global greenhouse gas emissions; Half of the world’s habitable (ice- and desert-free) land is used for agriculture; 70% of global freshwater withdrawals are used for agriculture; 78% of global ocean and freshwater eutrophication (the pollution of waterways with nutrient-rich pollutants) is caused by agriculture; 94% of mammal biomass (excluding humans) is livestock. This means livestock outweigh wild mammals by a factor of 15-to-1. Of the 28,000 species evaluated to be threatened with extinction on the IUCN Red List, agriculture and aquaculture is listed as a threat for 24,000 of them. Source: Our World in Data What it does Given a product isbn (barcode) or ingredient search, receive statistics on the estimated environmental impact of producing that product including: Land use Greenhouse gas emissions Acidifying emissions Eutrophying emissions (i.e. fertilizer run-off) Freshwater used Save orangutans! In the spirit of saving the orangutans , the API also specifies if the product contains palm oil. Palm oil is the leading cause of orangutan extinction, and is commonly found in food and household products. How we built it We used Open Food Facts API to look up products and get an array of ingredients and their approximated proportion. We compiled a file of 170+ common ingredients with their impact in 5 categories using data from a study done in 2018 Challenges we ran into Open Food Facts API has an extensive catalog of products, but it is not all-encompassing. What we learned How to use a Node.js framework called Nest How to create a mock server in Postman How to deploy a Nest app on Vercel How much impact our choices have on the environment What's next for Save the Orangutans! This API could be implemented in a few ways, some that we'd be excited to see: Showing the impact of purchasing food items once-per-month during online checkout Scanning items in-store when trying to choose an eco-friendly option Using graphical representations, such as the equivalent distance traveled by car, or land use in terms of soccer fields. Be mindful of your consumption, let's take the little steps to save our planet. Source files Thanks to Postman for sponsoring this hackathon! All of our materials are open source: Postman workspace Github Example request GET /:productISBN { "brandOwner": "Nestle USA Inc.", "brands": "Hot Pockets", "containsPalmOil": false, "mayContainPalmOil": false, "numIngredients": 84, "productName": "Four cheese pizza with parmesan, cheddar & reduced fat provolone & mozzarella cheeses in a garlic buttery crust sandwiches", "servingKilograms": 0.12, "stats": { ... "ghg_emissions": { "mean": 0.7055285098522162, "median": 0.5320506804187187 }, "land_use": { "mean": 2.552801114532017, "median": 0.7542392580049255 }, "stress_weighted_water_use": { "mean": 7378.098337130538, "median": 3123.8892692118206 } ... }, "ingredients": [ { "functionUnit": 0.0548689655172414, "id": "en:flour", "stats": { ... "ghg_emissions": { "mean": 0.08779034482758624, "median": 0.07132965517241383 } ... }, "text": "flour" } ... ] } <div