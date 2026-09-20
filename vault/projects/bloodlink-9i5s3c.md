---
slug: "bloodlink-9i5s3c"
url: "https://devpost.com/software/bloodlink-9i5s3c"
title: "BloodLink"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 711
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# BloodLink

> BloodLink: An intelligent blood bank platform that connects donors, hospitals, and inventory in real time to ensure the right blood reaches the right patient at the right moment.

[Devpost](https://devpost.com/software/bloodlink-9i5s3c) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[structured_db]]

**stack** axios, bcryptjs, context-api, express.js, jwt, mongodb, netlify, node.js, passport.js, python, react, react-router, render, rest-apis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bloodlink

## Body

Inspiration In emergencies, the difference between life and death often comes down to whether the right blood is available at the right time in the right hospital.[page:1] While building this project, we realized how fragmented today’s blood ecosystem is: blood banks use manual records or isolated systems, hospitals lack real-time visibility into inventory, and donors are rarely engaged beyond a single donation.[page:1] We wanted to create a single connected platform that makes blood availability transparent, reduces wastage from expired units, and makes it easier for healthcare teams to coordinate instead of scrambling on phone calls and spreadsheets.[page:1] What it does BloodLink is an end-to-end blood bank management platform that connects blood banks, hospitals, donors, and emergency services in one system.[page:1] It provides smart inventory management across all blood groups, hospital request handling, donor registration and tracking, emergency request flows, and detailed analytics dashboards for decision-makers.[page:1] The platform also supports blood donation camp management, real-time notifications (low stock, expiries, emergency needs), and a communication hub so admins and hospitals can coordinate directly inside the system.[page:1] How we built it We built BloodLink as a full-stack application with a React frontend, a Node.js + Express backend, and MongoDB as the primary database.[page:1] The frontend uses React 18, Tailwind CSS, React Router, Context API, and Axios to deliver a responsive, dashboard-style experience for different user roles.[page:1] On the backend, we designed modular controllers, routes, and models to handle donors, hospitals, blood units, requests, and camps, secured by JWT-based authentication, Passport.js, and role-based access control.[page:1] MongoDB schemas capture complex relationships between donations, specimens, and hospital requests, and we added a small Python utility ( blood-stock-finder ) to support stock lookup workflows.[page:1] The app is deployed with a live frontend on Netlify and a live API on Render, using environment variables for secure configuration.[page:1] Challenges we ran into One major challenge was modeling and maintaining the relationships between donors, blood units, hospitals, and requests while keeping the data consistent as states change (donated → tested → available → reserved → used/expired).[page:1] Designing real-time-ish inventory behavior was also non-trivial: when a hospital raises a request, we need to reflect reservations, prevent double allocation, and handle cancellations gracefully.[page:1] Implementing robust role-based access (admin, staff, hospital, donor) with different permissions and views required careful structuring of both backend middleware and frontend routing.[page:1] Finally, coordinating separate frontend and backend deployments (CORS, environment configuration, seeding data, and handling failures) added additional complexity during testing and demo preparation.[page:1] Accomplishments that we're proud of We’re proud that BloodLink feels like a complete operational system rather than just a UI demo.[page:1] From login to dashboard, inventory, donors, hospitals, requests, camps, and analytics, each feature is wired to real data models and flows that match how a blood bank actually works.[page:1] The expiry tracking, low stock alerts, and structured hospital request workflow showcase how software can directly reduce wastage and delays in real scenarios.[page:1] Having a working live deployment for both frontend and backend, plus API docs, database schema docs, and Postman collections, makes the project usable and extensible for others.[page:1] What we learned We learned how challenging it is to design data models for healthcare systems where every record and state transition matters.[page:1] Working with MongoDB at this scale taught us the importance of clean schema design, indexing, and validation to keep queries performant and data consistent.[page:1] We also deepened our understanding of security best practices in multi-role systems, including JWT auth, password hashing, and minimizing data exposure per role.[page:1] On the frontend side, we gained experience in building complex dashboards with React + Tailwind, managing global state with Context API, and designing UX that works for both admins and clinical staff.[page:1] What's next for BloodLink Next, we want to expand BloodLink beyond a single-center tool into a networked platform connecting multiple blood banks and hospitals across regions.[page:1] This includes adding smarter demand forecasting (e.g., ML-based predictions for blood usage), integrating with national blood bank or ABDM-style registries, and eventually supporting mobile apps for donors and staff.[page:1] We also plan to explore IoT integration for monitoring storage conditions (like refrigeration temperature) and blockchain or audit trails for fully transparent donation-to-transfusion tracking.[page:1] With further iterations and real-world pilots, our goal is to make BloodLink a reliable backbone for blood management in high-impact healthcare settings.[page:1] <div