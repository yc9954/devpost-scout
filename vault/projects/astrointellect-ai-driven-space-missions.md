---
slug: "astrointellect-ai-driven-space-missions"
url: "https://devpost.com/software/astrointellect-ai-driven-space-missions"
title: "BlueandCosmos: Exploring the Cosmos. Protecting the Earth."
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 491
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# BlueandCosmos: Exploring the Cosmos. Protecting the Earth.

> Real-time space education platform combining satellite intelligence, lunar data, and virtual telescopes into personalized learning experiences that make astronomy accessible to everyone.

[Devpost](https://devpost.com/software/astrointellect-ai-driven-space-missions) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
  <sub>weak: sensor_fusion</sub>
**domain** [[agriculture_food]] [[civic_government]] [[climate_energy]] [[developer_tools]] [[disaster_emergency]] [[education]] [[scientific_research]]
**user** [[developer]] [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** amazon-dynamodb, amazoncognito, amazonec2, amazonecs, amazoneventbridge, amazonkinesis, amazonrds, amazons3, amazonsagemaker, amazontimestream, anomalydetection, apigateway, awsapigateway, awscloudwatch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blueandcosmos : exploring the cosmos. protecting the earth.

## Body

Earth from Space Inspiration In a world of increasing climate volatility and space activity, there’s no single platform that unifies real-time Earth observations, celestial events, and environmental insights for the public. We created BlueandCosmos to bridge this gap—democratizing access to space and satellite data for educators, researchers, policymakers, and curious minds. What it does BlueandCosmos is an AI-powered platform that aggregates real-time data from Earth-observing satellites and astronomical observatories. It enables users to: View live and forecasted celestial events Monitor short-term weather and natural disasters Track long-term climate trends Explore Earth and space insights in an interactive, public-friendly interface How we built it Kiro (AWS-based AI framework) for celestial event detection and scheduling NASA, ESA, ISRO APIs for satellite data (e.g. MODIS, Copernicus, INSAT) OpenLayers + CesiumJS for 2D/3D globe visualization PostgreSQL with PostGIS for spatial-temporal data storage AWS Lambda & Greengrass (planned) for scalable, serverless computing Integrated with GitHub Actions and .kiro specs/hooks for reproducible AI workflows Challenges we ran into Navigating satellite data licensing across jurisdictions Normalizing diverse data formats (HDF, GeoTIFF, JSON) from different agencies Ensuring real-time performance for rendering multi-layered geospatial data Designing an interface that’s both beautiful and meaningful across Earth and space Accomplishments that we're proud of Built a fully functional MVP that unifies celestial and Earth observability Integrated public satellite feeds for live weather and environmental data Designed a growth roadmap for Asia-first deployment and global scaling Developed a clear value proposition against commercial providers like Maxar What we learned The power of open data when paired with AI-driven automation How celestial event detection can be integrated with Earth monitoring Regional sensitivities around satellite data transparency and access Why modular, open-access tools matter for public climate and space literacy What's next for BlueandCosmos : Exploring the Cosmos. Protecting the Earth. Build an “Earth–Orbit Intelligence Hub” Combine satellite imagery, celestial analytics, and weather/disaster data in a single modular platform—optimized for educators, NGOs, and researchers in Asia and beyond. Onboard ISRO & Regional Satellite Feeds Incorporate regional missions like CartoSAT, ScatSAT, and INSAT for localized forecasting and disaster tracking. Launch a Visual Analytics Dashboard Provide interactive heatmaps, anomaly timelines, and multi-layer visualizations for public health, agriculture, and city planning. Partner with Open Satellite Projects Contribute to and federate with citizen science missions like OpenSpace, Libre Space Foundation, and NASA’s OpenET. Release a Mobile-First Experience Deliver BlueandCosmos as a progressive web app for low-bandwidth, disaster-prone, and rural regions—especially in Asia-Pacific. Fine-Tune AI on Regional Events Train BlueandCosmos AI models using historic floods, heatwaves, and satellite imagery from India, Bangladesh, Philippines, etc. ESG & SDG Reporting Toolkit Provide a reporting module for climate NGOs and governments to monitor UN Sustainable Development Goals using spatial insights. Transparent Data Licensing Layer Tag each data source with its terms of use, provenance, and country-of-origin transparency compliance. Community & Contributor Portal Build a GitHub-like hub for researchers, students, and developers to share plugins, observatory feeds, or event detection models (aka Zooniverse) <div