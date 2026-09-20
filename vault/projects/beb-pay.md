---
slug: "beb-pay"
url: "https://devpost.com/software/beb-pay"
title: "Beb Pay"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 1047
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Beb Pay

> Bringing fast, contactless payments to every store!

[Devpost](https://devpost.com/software/beb-pay) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[accessibility]] [[developer_tools]] [[finance_payments]] [[labor_employment]] [[legal_justice]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** azure, azure-app-configuration, azure-cosmos-db, azure-function-apps, bebapps/rapyd-sdk, cheerio, cloudflare-pages, cloudflare-workers, jwt, node.js, quaggajs, rapyd, react, scss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for beb pay

## Body

Customise the user experience Go live Example stores Try Beb Pay yourself! Inspiration Over the past year, we noticed everyone around us starting to use contactless payment methods such as Apple pay. We also noticed more and more stores offering a 'Click and Collect' alternative to in-store shopping. We found a niche between these two options where you don't have to plan your purchases hours in advance, like with 'Click and Collect', or stand in long lines with strangers at checkouts to use your contactless payment method. When we looked into this further we saw a few horror stories about companies taking years and spending a fortune trying to roll out a solution to this problem. What it does Beb Pay offers a quick and easy way for people to shop at their favorite stores. All a user has to do is scan a QR when they enter a store, scan an item they want to purchase, pay on their phone, and then leave the store. The setup experience is just as important for Beb Pay to become commonplace, which is why we've made it so simple to get up and running. Included in our project (and now open source) is a Rapyd Node.js SDK that makes it super easy for developers to get started with the Rapyd platform. How we built it The backend of Beb Pay is built from the ground up using only serverless offerings from Azure and Cloudflare. The backend is made up of two micro-services - a user service, and a store service. They are hosted on the Azure Functions Consumption plan and have a pretty well-optimized cold start time. For the database, we opted to use Azure CosmosDB - also using the Consumption plan. We also used Azure Storage to host all the store resources (like logos and product images). Because the system is made up of micro-services, we needed a way to route requests between them without having to hard code a bunch of endpoint URLs. For this, we used Cloudflare Workers - another serverless offering that provides limitless potential in a variety of different ways. We built a small worker that used route prefixes to determine the backend the requests should be routed to. This greatly simplified things, as it means the frontend, store resources, and API endpoints could all be served from one site. When it came to the backend integration with Rapyd, we started by looking at the landscape, and quickly noticed a lack of official support for Node.js (via the means of a simple-to-install SDK), we chose to spend some time nailing down a solid SDK. It was pretty time-consuming and ended up taking much longer than we had set out. But ultimately, it gave us a much better understanding of the Rapyd API, which meant when it did come to implementing the integration with Rapyd, it took minutes - not even exaggerating. The SDK worked exactly as we had expected it to. As for the store-front and management portal - it was written in TypeScript using React. For barcode scanning, we used a library called quaggaJS. If we had more time, we would have probably investigated using a more battle-tested tool for the barcode detection, as it can sometimes be a little finicky. We made heavy use of CSS variables to make customizing parts of the UI dead simple. This, along with a rich set of re-usable components has meant we were able to make the most of React to rapidly put together Beb Pay. Challenges we ran into Certainly two of the most challenging hurdles we faced were; time, and building the SDK. Just over a month to build what we had set out to just simply wasn't enough, but we pushed through and ended up managing to show our vision. We ran into numerous challenges with building the SDK. Well… building the code that builds the SDK - as it's almost all auto-generated code. We knew we wanted to build something that would require no manual intervention when new APIs are introduced in the future, or changes are made to existing ones. Accomplishments that we're proud of When we were looking for a sample logo we found a variety of logos with very different design languages. When we put them into Beb Pay we were happy to find that we were able to make it feel like the entire UI was built around the logo, after adjusting only a few sliders We truly believe that the javascript SDK will make the lives of developers wanting to get started with Rapyd easier. We were happy with our work on it once we had it up and running, but then after using it to develop Beb Pay opened our hours to how much of a difference a good SDK can make What we learned Our project management skills were put to the test because of the tight deadline, but we've learned how important it is to set achievable goals and to think carefully about what the key features are We also learned that choosing the right platform to use can make handling payments as easy as 123. Before using Rapyd's APIs it always seemed so out of reach. What's next for Beb Pay Completing MVP features: Email verification for account creation Payout mechanisms for shop owners Any tax and legal information that needs to be collected Email receipts for customers to give them a record of their purchase Features that we are excited about but did not get time to complete Integrations with POS systems to allow easier loading of products into Beb Pay A monitor view that allows a store owner to see all active/recent carts in their store (for security, store improvement, etc) Customer accounts to save their details/purchase history Customizable flags that will ask a user to go to a physical checkout if certain conditions are met (e.g. purchases over $x, purchases for items that are kept behind a counter with just their boxes on display, etc) Deals based on a users cart (e.g. allowing a user to save $x on their purchase if they also purchase a paired item) We're super eager for the judging to complete so we can jump right back in making our vision come to life <div