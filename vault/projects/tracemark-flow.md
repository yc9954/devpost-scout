---
slug: "tracemark-flow"
url: "https://devpost.com/software/tracemark-flow"
title: "TraceMark Flow"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 1029
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# TraceMark Flow

> TraceMark™ Flow is a Google powered next-generation traffic monitoring and insights tool for public sector transport organisations to help them combat congestion, improve operations and safety

[Devpost](https://devpost.com/software/tracemark-flow) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[scientific_research]] [[supply_logistics]] [[transportation]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** angular.js, apigee, azure-devops, google-app-engine, google-apps-marketplace, google-bigquery, google-cloud-sql, google-compute-engine, google-directions, google-firebase, google-maps, google-places, google-prediction, google-roads-management-insights

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tracemark flow

## Body

TraceMark Flow Congestion Dashboard Inspiration The core inspiration behind TraceMark Flow stems from the critical need to combat urban congestion and promote sustainable movement within cities. With increasing livability and sustainability policy targets globally, there's a clear drive to reduce the environmental, social, and economic impact of traffic. TraceMark Flow was developed by NGIS, a company with over 30 years of experience in geospatial solutions, to empower public sector and logistics organizations with data-driven decision-making to address these pressing challenges. Our purpose at NGIS is to create 'Impact Through Geospatial' and we do this by transforming complex geospatial data into actionable insights. We are inspired by the advanced mapping, satellite imagery, and AI from Google and use our geospatial development capabilities and know-how to tackle critical challenges, such as transport and sustainability, which ultimately contributes to fostering a more sustainable and resilient world. What it does TraceMark Flow is a next-generation traffic monitoring and insights product. It provides city-wide traffic monitoring and delivers actionable intelligence through a visualization web dashboard and a data access API. Its primary functions include: Monitoring Traffic Flow and Journey Time Reliability: It uses Google Maps big data location-based services to track traffic movement and travel time to determine on-time journeys. Providing Actionable Congestion Insights: Offers easy-to-use map-based visualization dashboards for operational stakeholders to be notified of unusual congestion. The solution pinpoints current and future unusual traffic events and monitors the journey resilience of key transport corridors. Increasing Traffic Flow Coverage: Demonstrated by a 10x increase in coverage for the Abu Dhabi Integrated Transport Centre (ITC) by integrating travel time data and analytics. Enabling Integration with Internal Systems: Allows aggregated traffic intelligence and metrics to be embedded into existing business systems via a dynamic Access API. Supporting Flood Mitigation: As seen in Abu Dhabi, it can provide real-time data and dashboards during heavy rain events to manage traffic disruptions and infrastructure challenges. How we built it TraceMark Flow was built by NGIS as a sustainable cities communication tools for public sector organisations, leveraging robust geospatial capabilities and cloud technology. Key aspects of its construction include: Google Cloud Technology: It is a 100% Google Cloud solution, leveraging Google's unique geospatial tools like Google Maps, Earth Engine, and BigQuery. This allows TraceMark to process vast amounts of mapping and satellite data to detect changes and provide insights. Google Cloud infrastructure enables ingesting, storing, and processing of large volumes of complex Google Maps Platform mapping, traffic, and environmental data at scale. This enables the storage and analysis of accurate, timely, and relevant traffic information over time. AI and Machine Learning: Incorporates AI and machine learning algorithms for predicting congestion and optimizing traffic flow. Web Dashboard and API: Developed with a visualization web dashboard for user interaction and communication, and a dynamic Access API for seamless integration with other business systems. Challenges we ran into The challenges for TraceMark Flow's development include: Handling Enormous Google Maps Data Volumes: Ingesting, storing, and processing enormous amounts of complex mapping, traffic, and environmental data is a significant technical challenge. Google Cloud scalability helps overcome this challenge. Data Accuracy and Timeliness: Ensuring the data is "accurate, timely, and relevant" for real-time traffic monitoring requires robust data pipelines, significant amounts of testing and quality assurance. This challenge is elevated when working in emerging countries. Predictive Accuracy: Developing AI and machine learning models that reliably predict congestion in dynamic urban environments is a continuous challenge. Scalability: Ensuring the system can rapidly increase traffic flow coverage demands a highly scalable architecture, requiring several solution options to be tested and validated, which required significant work. Regulatory Compliance: Addressing new and evolving regulatory requirements in the transport and sustainability sectors, especially across varied jurisdictions. Accomplishments that we're proud of TraceMark Flow has achieved notable accomplishments, demonstrating its effectiveness and impact by empowering Abu Dhabi's Department of Municipalities and Transport (DMT), UAE, and Thessaloniki City, Greece. Specifically for Abu Dhabi, TraceMark Flow proved instrumental in managing traffic disruptions and infrastructure challenges during a heavy rain event in April 2024, providing real-time data for swift, informed decision-making and flood mitigation. Furthermore, TraceMark Flow has enabled significant increase in traffic flow coverage, saving the City millions in physical infrastructure costs. Lastly through our work in Greece with Thessaloniki research group CERTH, we have been promoted by Google to conduct a webinar to showcase TraceMark Flow through Europe and beyond. What we learned Based on the product's capabilities and the context of our work, key learnings include: The Power of Geospatial Data and Cloud Technology: The ability to ingest and process massive amounts of location-based data from Google Maps in the cloud is crucial for effective traffic intelligence. Importance of AI/ML in Prediction: Machine learning is essential for moving beyond reactive monitoring to proactive congestion prediction, and ensuring there are many data points and significant amounts of data to support ML techniques. Value of Actionable Insights: Raw data is not enough; presenting insights through user-friendly dashboards and accessible APIs is vital for operational stakeholders to make informed decisions. Maps when they are done well are an unbelievable communication tool - everyone understands a map! Collaboration is Key: The success in Abu Dhabi highlights the importance of connecting government authorities and other stakeholders through shared data and collaborative approaches. What's next for TraceMark Flow The next big thing for TraceMark Flow is to build upon our solid foundation and create the next generation (Gen 3) communication and mapping platform for transport and sustainability, taking advantage of Google Cloud advancements in AI and data analytics. This includes: Enhancing resilience tools so cities can be confident their transport networks hold up during natural disasters. Strengthening the ability to share real-time data with emergency services, public transport authorities, and utility companies to ensure unified efforts, by fostering collaborative ecosystems. Further embedding aggregated traffic intelligence into a wider range of business systems and potentially expanding its application to more cities and logistics organizations globally. Continuously refining the predictive models to offer even more accurate and timely insights into traffic patterns and congestion, embedding Google's AI/ML capabilities and advancements. Continuing to contribute to cities' efforts to reduce carbon emissions and achieve livability targets through optimized traffic management. <div