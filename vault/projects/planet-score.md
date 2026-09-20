---
slug: "planet-score"
url: "https://devpost.com/software/planet-score"
title: "Planet Score"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 502
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "user/general_public"
  - "substrate/structured_db"
---

# Planet Score

> Fight carbon emissions one informed purchase at a time! 🌍💚

[Devpost](https://devpost.com/software/planet-score) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[climate_energy]]
**user** [[general_public]]
**substrate** [[structured_db]]

**stack** exiobase, javascript, python

## How they structured the write-up

- 🌍 fighting carbon, one purchase at a time 🌱
- planetscore: powered by open-source tools
- faq 🤔

## Body

PP0 PPT1 PPT2 PPT3 PPT4 PPT5 🌍 Fighting Carbon, One Purchase at a Time 🌱 Reducing carbon emissions is one of the most pressing challenges of our time. Consumers increasingly want to make eco-friendly choices, but how can we be sure which products are truly sustainable? Many of us have encountered greenwashing or felt uncertain about what to trust. That’s where PlanetScore comes in! Our tool empowers consumers to easily understand the environmental impact of their purchases with reliable, transparent data. Businesses also benefit, gaining consumer trust and meeting carbon-reduction goals through more informed, sustainable choices. It’s a win-win for everyone! PlanetScore: Powered by Open-Source Tools PlanetScore leverages open-source tools, including OpenLCA and the Exiobase database, to deliver accurate environmental assessments. OpenLCA is an advanced modeling tool that enables us to analyze the full environmental impact of products via its powerful API. Exiobase provides comprehensive data on how products and materials impact the planet, combining economic models, material flows, and environmental accounts. For those interested in diving deeper, check out resources like the European Commission’s Life Cycle Data Network , Environmental Footprints , and GreenDelta’s expert webinars . FAQ 🤔 What is an LCA? A Life Cycle Assessment (LCA) is a way to measure the environmental impact of a product, from raw material extraction to its end-of-life disposal. This includes everything—how the materials are sourced, manufactured, transported, and eventually discarded or recycled. LCAs are critical because they give us a complete picture of a product’s footprint, highlighting areas where improvements can be made to reduce carbon emissions. How PlanetScore Uses Exiobase Exiobase is one of PlanetScore’s core tools for estimating carbon emissions. It consolidates information from national accounts, economic systems, and material flows to calculate emissions in terms of kg CO₂/EUR—how much CO₂ is emitted for every euro spent in production. By combining this data with product price and material composition, PlanetScore provides an accurate estimate of a product’s carbon footprint. How the App Works PlanetScore is a simple Chrome extension that does some seriously smart work behind the scenes. When you browse a product, the app “reads” the product description and uses keyword matching to figure out what materials are involved and where the product might have been produced. Using OpenLCA’s API, we then calculate the carbon footprint of each material using kg CO₂/EUR and multiply it by the price of the product. The result? You get an easy-to-understand estimate of the product’s carbon emissions tied to its cost, all in real time. Here’s the magic formula: {kg CO₂/unit} = (kg CO₂/EUR) × (Price per unit [EUR/unit]) Dreaming Bigger: Ecoinvent Integration While Exiobase provides valuable insights, we envision taking PlanetScore to the next level with Ecoinvent—the world’s leading database for life cycle data. Ecoinvent offers unparalleled accuracy and detail, enabling the most precise carbon footprint calculations available. However, the licensing cost of 4,000 Euros currently makes this goal a challenge. For now, PlanetScore proudly uses robust open-source tools, but we look forward to future opportunities to enhance our capabilities further. <div