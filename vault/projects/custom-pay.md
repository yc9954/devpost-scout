---
slug: "custom-pay"
url: "https://devpost.com/software/custom-pay"
title: "Custom Payments"
hackathon: "Square Unboxed Hackathon"
organization: "Square"
winner: true
words: 558
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Custom Payments

> Stop using donation links for partial or complete payments Custom Payments allows your customers to view pending invoices, pay one or multiple invoices at once or pay custom amounts to an open invoice

[Devpost](https://devpost.com/software/custom-pay) · hackathon [[Square Unboxed Hackathon]]

## Facets

**domain** [[finance_payments]] [[housing_homeless]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[web_dom]]

**stack** cloud-functions, cloud-run, firestore, gcp, invoices-api, javascript, nestjs, nextjs, orders-api, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for custom payments

## Body

Merchant settings, add extra transaction fees Log in Merchant settings Customer dashboard, My Payments Customer dashboard, My invoices Inspiration Every business owner works hard for their business growth and success, but they shouldn't waste time waiting to get paid. So we've built a simple integration that helps the merchant get paid faster so they can focus on what's important: growing their business! Last year, we encountered the same problem with different customers. They did not have the capability of getting partial payments on any amount for their services unless the customer paid in full or used their last resource, "the donation link," which, let's be honest, doesn't look good in the books. Merchants and customers were having difficulty keeping track of donation link transactions. This is why we built Custom Payments. We came up with the idea of creating an integration capable of managing invoices and payments for merchants and customers that also enable the possibility of receiving partial payments for services that haven't been completed yet, or for credit lines that are always open. What it does Custom Payments—is a Square integration that lets merchants accept any amount of partial payments on invoices or credit lines without having to use a donation link. It's more professional-looking and provides a complete B2B invoice manager. Custom payments will help merchants to: Accept different payment methods like cash app, Afterpay, Square gift cards, ACH, Apple pay, Google pay, and credit cards. Add an extra percentage for the transaction fee, so the cost is not on the merchant. Allows you to accept payments of any amount without having to use a donation link Reduce the time you spend managing payments from individual clients. Get paid faster! And increase cash flow. Custom payments will help merchant's customers to: Manage and pay invoices, make a partial payment, or reduce the balance on credit lines. Review past payment history, and partial payments, so customers will always know where they stand. Allows customers to manage their payments in one place. How we built it We are processing the payments with custom amounts using the checkout API, invoice API to view and pay invoices in full, and the customer API for access and invoice management. We built it using our multi-tenant platform Wanda as a base, the idea was to develop something that would allow us to host and collect payments from multiple tenants, and Wanda provided that out of the box. Challenges we ran into We wanted to allow customers to pay multiple invoices at once or to pay part of an invoice directly, but we couldn’t do it due to limitations on the invoice API Accomplishments that we're proud of It’s a pretty good invoice management system that solves many merchant issues. What we learned A lot as usual. Especially the fact that we can add unlimited features to the app and make it a true B2B solution for Square Merchants. Now we are aware of new API limitations that we are eager to share and address with the Square team. What's next for Custom Payments Pay multiple invoices at once (Limited by the API) Set customer credit limits and send email alerts Send email reminders for merchants to check for payments and update invoices. Add Custom payments to invoices (Limited by the API) Embed the Custom payments dashboard into the merchant's website <div