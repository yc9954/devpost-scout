---
slug: "innobrix-the-3d-aec-configuration-platform"
url: "https://devpost.com/software/innobrix-the-3d-aec-configuration-platform"
title: "Innobrix - The 3D AEC configuration platform"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 663
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Innobrix - The 3D AEC configuration platform

> A powerful 3D configuration platform for the Architecture, Engineering & Construction (AEC) Industries. The SAAS platform creates BIM-based Digital Twins within the immersive world of Google 3D Maps.

[Devpost](https://devpost.com/software/innobrix-the-3d-aec-configuration-platform) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[developer_tools]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[geospatial]] [[web_dom]]

**stack** fiber, google-3d, google-geocoding, google-maps, javascript, map-tiles-api, mysql, node.js, react, socket.io, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for innobrix

## Body

Innobrix innercity housing development example Innobrix San Jose property development example Innobrix San Jose property development example BIM inspection Innobrix Netherlands property development example (note to Awards organisers: We submitted to category Immersive, as this is where Innobrix stands out. Category Real Estate would certainly fit too. Thank you) Inspiration The Architecture, Engineering and Construction (AEC) industry is undergoing a digital transformation, yet many professionals working in these industries often struggle to gather real benefit. At Innobrix, we were inspired by this challenge. Our mission is to bridge the gap between traditional architectural design and presentation methods and user-friendly 3D experiences. We believe that designing urban and residential plans should be intuitive, interactive, engaging and collaborative – from exploring plots to easily configuring layouts and housing styles – all in 3D and with real-world context. What it does Innobrix is a 3D configuration platform tailored for the AEC (Architecture, Engineering & Construction) industry. It allows stakeholders, such as property developers, architects, municipalities and homebuyers to: Create and explore housing developments via an interactive plot map integrated with Google 3D Maps. Select a building plot and configure future homes and infrastructure in real time. Visualize building designs in detailed 3D with Autodesk BIM (Building Information Modeling) integration. Experience the home in Virtual Reality or via a web-based 3D viewer. Collaborate with architects and contractors through digital twin models. The Google Maps Platform enables us to provide geospatial context for building developments, helping stakeholders understand not just the houses, but its neighborhood, orientation, and infrastructure. How we built it The Innobrix team comprises 5 software engineers and is based in the Netherlands. We built Innobrix as a cloud-based web application using modern front-end technologies such as React and Three.js. For mapping and geolocation functionality, we integrated Google 3D Map tiles JavaScript API and Geocoding API. These services allow us to: Embed accurate parcel locations, cities and environments. Offer worldwide address lookup and auto-completion. Provide orientation-aware previews and real-world landmarks. Our back-end supports integrations with Revit, GLB, OBJ and other industry standards. This makes Innobrix a seamless layer between BIM data and user experience. Challenges we ran into Geospatial accuracy: Aligning BIM-based geometry with real-world GIS data required careful coordinate transformations and precision tuning. Performance: Rendering high-quality 3D models in the browser while integrating live 3D map data presented performance challenges, especially for mobile users. Yet, we succeeded, also thanks to the highly optimised Google 3D Map tiles. Adoption curve: Many of our clients in the construction industry were used to static workflows. Demonstrating the value of interactive 3D and location-based features required targeted onboarding and change management. Accomplishments that we're proud of Successfully deployed Innobrix in multiple large-scale housing developments, allowing thousands of users to configure plan variants in 3D and Geospatical context. Over 50 AEC enterprises now actively using Innobrix Reduced time-to-decision for homebuyers by giving them visual, interactive insights. Created a platform that bridges Revit-based BIM data and web visualization. Leveraged Google 3D Maps to add real-world relevance to each 3D configuration session. What we learned Users deeply value context: being able to see where a projected home or building will be located, what’s nearby and what's having impact enhances decision-making. Our software developers appreciated Google's APIs: Highly optimised Map Tiles allowed us to build without compromising on performance on the web. The AEC industry is ready for change, especially when digital tools improve communication between stakeholders. What's next for Innobrix We’re expanding the platform in several directions: International rollout : Bringing Innobrix to the UK, Nordics and DACH region, with local geospatial context. AI-powered visualisations : Using AI to further improve realism Sustainability insights : Visualizing energy performance and building material choices during the configuration phase. Deeper Google Maps integrations : Embedding Street View and elevation profiles to offer even richer context. At Innobrix, we believe the future of construction lies in making complexity understandable and collaborative. Thanks to Google Maps Platform, we’re putting that vision into practice. Innobrix company website <div