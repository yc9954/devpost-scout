---
slug: "cropchain-b0hcgm"
url: "https://devpost.com/software/cropchain-b0hcgm"
title: "CropChain"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 597
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "substrate/structured_db"
---

# CropChain

> CropChain is a multilingual agri marketplace connecting farmers and buyers with AI price optimization, real time offer negotiation, analytics dashboards, and access to government schemes.

[Devpost](https://devpost.com/software/cropchain-b0hcgm) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[agriculture_food]] [[civic_government]] [[finance_payments]] [[supply_logistics]]
**user** [[frontline_worker]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** firebase, genkit, next.js-15, react-19, recharts, shadcn-ui, tailwind-css, typescript, vercel, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cropchain

## Body

Login page Dashboard of farmer Buyer side application (Dummy data) Retail section The blur sample button indicates farmer is not providing sample Wholesale section Offers that i have made to farmer from wholesale section Can change languages and appearence Analysis graph for Farmer AI Price Generator as per the market situation and details provided Farmer sales data Farmers can check eligibility and all details related to schemes for them also they can redirect to official Gov website with apply now link Farmers can buy seeds crops pesticides etc. Listing by farmer Toggle button for providing sample or not for this crop All the listing of farmer Buying the crop (buyer side) Farmer notified of the order he received Making offer to farmer to negotiate the price Farmer notified of the offer also appeared in the offer section now he can accept or reject offer Since Farmer rejected offer the buyer was notified Inspiration Farmers often struggle with middlemen, unpredictable pricing, and limited access to real-time market insights. At the same time, buyers face challenges in finding reliable suppliers and negotiating fair deals. We were inspired to build CropChain to create a transparent, technology-driven ecosystem that directly connects farmers and buyers while empowering farmers with data and digital tools. What it does CropChain is a multilingual digital agriculture platform that connects farmers and buyers through a real-time marketplace. Farmers can list crops, manage offers, track revenue, and use an AI Price Optimizer to get smart pricing recommendations. Buyers can browse retail and wholesale listings, negotiate bulk deals, request free samples, and receive real-time offer updates. The platform also provides access to government schemes and a farmer shop for agricultural supplies. How we built it We built CropChain using Next.js 15 with the App Router and TypeScript for a scalable and modern frontend architecture. Firebase Authentication ensures secure login, and Firestore powers the real-time database. We integrated Google Genkit with Gemini models to build the AI Price Optimizer. Tailwind CSS and ShadCN UI were used for responsive design, while Recharts handles dashboard analytics. React Context API manages global state such as authentication, cart, and language preferences. The app is deployed using Firebase App Hosting. Challenges we ran into One of the biggest challenges was implementing real-time offer negotiation while keeping the UI smooth and responsive. Managing multilingual support across dynamic content also required careful state handling. Integrating AI price recommendations in a way that felt practical and useful for farmers was another technical and design challenge. Ensuring role-based access and secure data separation between farmers and buyers required strong backend structuring. Accomplishments that we're proud of We successfully built a fully responsive, production-ready platform with role-based dashboards and real-time features. The AI Price Optimizer adds intelligent decision support rather than just being a demo feature. The multilingual support makes the platform inclusive for regional users. We are proud of creating an end-to-end agriculture ecosystem instead of just a marketplace. What we learned We learned how to architect a scalable full-stack application using Next.js and Firebase. We gained hands-on experience integrating generative AI into real-world workflows. We also learned how important user experience, accessibility, and localization are when building solutions for diverse users. Most importantly, we learned how to design technology that solves real-world problems in agriculture. What's next for CropChain Next, we plan to integrate secure digital payments, logistics tracking, and quality verification systems. We aim to enhance the AI engine with real-time market price datasets and predictive analytics. We remember to add farmer credit scoring, crop demand forecasting, and mobile app support to expand accessibility and scalability. <div