---
slug: "b2b-invoicing"
url: "https://devpost.com/software/b2b-invoicing"
title: "B2B Invoicing"
hackathon: "Square Developer Hackathon 2023 "
organization: "Square"
winner: true
words: 690
team_size: 10
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/financial_record"
---

# B2B Invoicing

> Add B2B capabilities to your Square account, allow your customers to log in, view, pay, or make partial payments to invoices inside their account, and add credit limits and additional fees.

[Devpost](https://devpost.com/software/b2b-invoicing) · hackathon [[Square Developer Hackathon 2023]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[financial_record]]

**stack** artifact-registry, auth0, cards, ccs3, checkout, cloud-functions, cloud-run, customers, docker, figma, firestore, google-cloud, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for b2b invoicing

## Body

Members API Members API Members API Merchant's log in portal. Admin panel to connect with Square and to set up custom fees. Connect with Square account. Payment method available and fees for set up. Merchant's dashboard with main information for overview and forecast. My customer's list featuring a customer detail when clicking on a customer. Customer's credit line setup section when clicking edit icon. Plans and pricing for review and compare. My plan information and changes. Customer's log in portal. Customer's dashboard for account overview, full payments (icon) or partial payments (side section). Inspiration It's been a long journey, this is not our first Square app, but it's the first one with a mission to be the first app exclusive for Square on the marketplace. And to solve the issue that all our other Hackathon Winner apps had, we couldn't deploy them automatically or bill and manage merchants from a centralized console, making the development of those apps pointless. We now have a very decent B2B invoicing platform and the ability to go to market with apps in weeks instead of months. B2B invoicing was created based on hundreds of interactions with Square customers, small and mid-sized businesses needed a way to manage open invoices and process partial payments. It's also a complete makeover of last year's winner's custom payments that live as a feature inside the new platform. What it does B2B Invoicing for Square by SEEED is an app that allows merchants to manage invoices, accept payments, and set up customer credit lines. With a dedicated dashboard, merchants can view their account summary, manage invoices and receive payments. The app also includes a unique customer portal where customers can manage invoices, make full or partial payments and view their account credit limit. How we built it We build B2B Invoicing on top of our multi-tenant platform Wanda, a platform with the ability to manage and bill merchants using Squares subscriptions API and our own middleware called “Members” B2B invoices also uses the invoices API to view and pay invoices; payments API to process partial payments, customer API to retrieve customer data, etc. Challenges we ran into B2B Invoicing was a challenging project. We had to create a completely automatic customer provisioning backend that allowed us to develop new merchant accounts, deploy their client apps under their own subdomain and manage monthly billing automatically; monthly billing was particularly complicated because we needed a way to bill customers on a monthly basis or by a percentage of invoices paid, we had to build our own API on top of the square subscriptions API, this way we could create additional plans and charges that are not currently supported. Accomplishments that we're proud of Some of our accomplishments that we are proud of are that now we have a complete multi-tenant provisioning platform with billing capabilities that we plan to turn into an API so more developers like us can create apps for Square without having to do all the things we had to do to launch the first Square exclusive app on the market. This also means that now we can focus on app development and launch as many apps as possible for Square, and also, a super admin portal that will allow us to view, manage and get information from the merchants, monitor monthly payments, and provide BI to adjust monthly billing. What we learned We learned that we have the potential to create complete SaaS platforms on top of the Square ecosystem to maximize the benefits of what the market needs. What's next for B2B Invoicing The future of B2B Invoicing is more billing plans. We want to make our apps extremely affordable and easy to adapt to any merchant's needs; we want to be able to bill customers by the number of clients, processing volume, amount of invoices paid, monthly active clients, etc. For Merchants: Create, edit, and customize invoices, Hard credit limits, and multi-user support for companies. For clients: Reorder, view most popular items, and self-service in general, multi-user support. Multi Square accounts support and manage all your invoices from multiple Square merchants from one location. <div