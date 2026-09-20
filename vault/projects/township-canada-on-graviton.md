---
slug: "township-canada-on-graviton"
url: "https://devpost.com/software/township-canada-on-graviton"
title: "Township Canada on Graviton"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 657
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Township Canada on Graviton

> Geocoding Canadian legal land locations made easy & fast

[Devpost](https://devpost.com/software/township-canada-on-graviton) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[legal_justice]]
  <sub>weak: agriculture_food</sub>
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-rds-relational-database-service, graviton, mapbox, node.js, postgis, postgresql, serverless

## How they structured the write-up

- challenge
- solution

## Body

Township Canada is a web application that allows users to geocode Canadian legal land descriptions and get turn-by-turn navigation between two points of interest. What is a legal land description? Any parcel of land in Canada can be located by its legal land description. Legal land descriptions are based on survey grid networks that divide the country into equal-sized parcels of land. Many industries including oil and gas and agriculture use legal land descriptions to identify their assets such as wells, facilities, and land parcels. Read more about legal land description here . Challenge Township Canada provides two main pieces of functionality: Search, which empowers users to find legal land descriptions, geographical coordinates, and places in Canada. It provides real-time recommendations as users type in their search term and allows them to convert legal land descriptions to geographical coordinates and vice versa. Batch conversion, which empowers users to geocode and reverse geocode many records at once, i.e., up to 1,000 records in a single API call. The search and batch conversion APIs are the heart of the application; in fact, those APIs are the building blocks of townshipcanada.com and developer.townshipcanada.com . As the number of supported provinces and their survey grid systems grew over time, the performance of the search and batch conversion APIs has been one of the main challenges that I have had to deal with since I started this project. They are resource-intensive operations that run on the database side. In Township Canada, the search and batch conversion functions work on around 25 millions records (36 GB of spatial data) and provide results in (near) real-time. So for this hackathon, my goal was to evaluate the performance of the Graviton-powered RDS PostgreSQL and Lambda functions behind the search and batch conversion APIs and modernize the stack behind townshipcanada.com and developer.townshipcanada.com if there was a significant improvement. The following section presents the technical architecture and describes how the system works. It also presents the results of a performance evaluation between Graviton-powered instances used in this project and their x86-based counterparts. Solution Township Canada is built using open source software, open standards, and open data and hosted on Amazon’s AWS infrastructure. As mentioned in the previous section, the focus here is on the search and batch conversion APIs, which are in fact simple REST APIs (API Gateway + Lambda function) built using NodeJS and Express and backed by a RDS PostgreSQL. The workflow starts with an API call from the client. The lambda functions then parse the HTTP request, perform regular expression operations, form the SQL query and send it to PostgreSQL/PostGIS for execution, and finally return the results as GeoJSON. PostgreSQL/PostGIS stores the data and executes two types of queries: exact match and spatial point in polygon. To evaluate the performance of Graviton-powered vs. x86-based stack, two different RDS PostgreSQL were created using two different instance families, db.t4g.micro and db.t3.micro, and the Lambda functions were deployed using two different architectures, x86_64 and arm64. Apache JMeter was used to send geocoding (legal land description to geographical coordinates) and reverse geocoding (geographical coordinates to legal land description) HTTP requests to the search and batch conversion APIs and measure the response time. The experiment was repeated 30 times to get representative results. The results suggest that the Graviton-based architecture provides more than 64% and 20% better performance over the x86-based architecture when handling geocoding requests using the search and batch conversion APIs, respectively. Similarly, the Graviton-based stack outperformed their x86-based counterparts by more than 15% and 27% when handling reverse geocoding requests using the search and batch conversion APIs, respectively. So, I have migrated the search and batch conversion APIs and the RDS PostgreSQL behind them to arm64 in production, since they provide a more efficient solution to deal with real-time, concurrent queries at scale. townshipcanada.com and developer.townshipcanada.com now run on a Graviton-powered stack. See the full report here to get more details on the performance evaluation. <div