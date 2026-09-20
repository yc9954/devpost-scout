---
slug: "canibuild-yc2okp"
url: "https://devpost.com/software/canibuild-yc2okp"
title: "Canibuild"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 766
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Canibuild

> Know What's Possible Instantly

[Devpost](https://devpost.com/software/canibuild-yc2okp) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[civic_government]] [[disaster_emergency]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** 45?, address, address-autocomplete-api, aerial, amazon-cloudfront-cdn, aws-lambda, cesiumjs, cloudfront), directions, ec2, eks, elevation, geocoding, geoserver

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for canibuild

## Body

Inspiration Canibuild was born out of the frustration of watching builders and homeowners waste weeks figuring out whether they could build something on a property. Every build idea required manual checks, interpretation of council rules, and back-and-forth between salespeople, drafters, and engineers. Often, the final answer was simply “it doesn’t fit.” We believed there had to be a smarter way to answer the question: “Can I build this here?” And not in days or weeks, but instantly. Google Maps Platform gave us the foundation to bring that vision to life with real-world context, aerial views, terrain, and property-level intelligence. What it does Canibuild is a web platform that lets users: • Instantly check if a home, ADU, pool, or shed fits on a specific lot • Apply zoning rules, setbacks, slope analysis, and overlays in real time • Drag and drop building designs on an interactive map • Visualize the project in 2D, 3D, or using photorealistic imagery • Share, refine, and move toward approvals without manual drafting or quoting Builders use it to close more sales during the first meeting. Councils use it to visualise planning impacts. Property owners use it to explore options without needing to hire a full team. How we built it We built Canibuild using a combination of frontend mapping libraries, a dynamic backend rules engine, and deep integrations with the Google Maps Platform. Frontend React.js, Leaflet.js, CesiumJS, Turf.js Backend Node.js (Express), AWS Lambda, PostgreSQL (with PostGIS), SQL Server Cloud Infrastructure AWS (EKS, EC2, S3, RDS, CloudFront), Kubernetes GIS and 3D Tools Martin, GeoServer, CesiumJS, Leaflet.js, Turf.js Google Maps Platform APIs • Maps JavaScript API • Geocoding API • Address Autocomplete API • Elevation API • Street View • 45° Imagery • Photorealistic 3D Tiles • Aerial Imagery • Static Maps • Directions API (used in Lead Converter) Our GIS layer is powered by PostGIS and Martin for fast tile rendering. The planning logic runs through a flexible rules engine, tightly integrated with our mapping and design components. Challenges we ran into • Complexity of zoning rules: Each region has its own rules for setbacks, overlays, access, and terrain. We had to design a scalable rules engine that could support local planning logic across multiple regions and countries. • Real-world terrain alignment: Getting designs to behave accurately on real slopes required combining elevation data from the Maps Platform with CesiumJS terrain layers and custom geometry adjustments. • Performance at scale: Rendering real-time, interactive designs on thousands of properties required tile caching, smart spatial indexing, and optimised API responses. • Imagery and data alignment: Ensuring that property boundaries, satellite imagery, and design overlays lined up precisely across multiple data providers was a constant challenge. • Tech selection and learning curve: Evaluating and adopting tools like CesiumJS, Martin, and various GIS libraries took time. Many technologies had steep learning curves, and it took significant research to understand which ones could support our specific use cases both now and in the long term. Accomplishments that we're proud of • Enabled thousands of builders to assess projects on the first client call • Let property owners visualise options before committing to a build • Scaled to support different planning rules across Australia, the US, and beyond • Combined GIS, 3D, and elevation data into a fast and user-friendly workflow • Brought mapping technology to non-technical users with zero training required What we learned • Speed and visual clarity are what users care about most • Planning rules are often non-standard, and flexibility is key • High-accuracy spatial rendering builds trust in design feasibility • The Google Maps Platform gives us the tools to deliver accuracy, performance, and familiarity • Choosing the right technology early is crucial, but you have to leave room for experimentation and learning What's next for Canibuild We’re now focused on making Canibuild smarter, faster, and even more helpful, especially through AI and deeper automation. • AI assistant to guide users in-app: A context-aware agent that helps users navigate the platform, explains feasibility results, and suggests next steps during a design session. • AI permit pre-assessment tool: This feature will automatically analyse uploaded site plans and building documents against local rules and zoning codes, providing instant feedback on compliance or likely issues. • Partnerships with government and councils: Supporting local planning teams, especially for disaster recovery or high-growth areas, by helping them visualise and pre-screen large volumes of build requests. Canibuild’s goal remains the same: reduce friction, remove uncertainty, and help users go from idea to build-ready with total clarity, all within minutes, and now with even more intelligence built in. <div