---
slug: "neural-payments-p2p-integration"
url: "https://devpost.com/software/neural-payments-p2p-integration"
title: "Neural Payments P2P Integration"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 283
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Neural Payments P2P Integration

> We combined the new Neural Payments P2P service with Fusion Fabric to provide an integrated end-to-end solution. Our network, plus PayPal and Venmo, creates a network unlike anything in the market.

[Devpost](https://devpost.com/software/neural-payments-p2p-integration) · hackathon [[Hack to the Future 2020]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** ffdc, fis, google-cloud, paypal, react, rust, venmo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neural payments p2p integration

## Body

Inspiration The idea of creating a true end-to-end P2P solution for Finastra clients that connected them to a larger network that allowed them to be competitive in their P2P offering. What it does We use the power of Fusion Fabric.cloud to enable a simplified integration to our platform. We can pull all the data needed to connect a user to the network and send/receive funds securely. We built a unique connector to PayPal/Venmo that allows us to also expand who can receive these funds to the largest P2P networks in the US. This is done with PANs, sharing PCI or PII data creating a secure transaction. The cost is also below or at market for a P2P transaction. How we built it We leveraged our existing solution and then created connectors for getting customer and account data for Finastra Financial Institutions. When possible we use the Good Funds API to debit/credit accounts at Finastra in real-time. This will save fees and charges from the networks. Challenges we ran into The team built the POC in under 2 weeks - mainly because the Fusion Fabric.cloud solution allowed for a simple and straightforward integration. Accomplishments that we're proud of We believe with another few weeks and the support of the Maluazai team we could turn this into a production-ready solution. What we learned Fusion Fabric.cloud allows us to simplify CORE integrations for Finastra clients. It lets us keep backend support needs to a minimum (ie Settlement will be a single line item on a report). We can do real-time debits and credits to Finastra clients. What's next for Neural Payments P2P Integration Hopefully, a commercial agreement to do a production integration of this POC. <div