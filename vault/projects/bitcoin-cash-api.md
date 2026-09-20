---
slug: "bitcoin-cash-api"
url: "https://devpost.com/software/bitcoin-cash-api"
title: "Bitcoin Cash API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 396
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Bitcoin Cash API

> Using this public workspace you can get your BCH or SLP token balance, send BCH to someone, get fee of a transaction, and create BCH wallet easily

[Devpost](https://devpost.com/software/bitcoin-cash-api) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** bchjs, node.js, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bitcoin cash api

## Body

Inspiration My inspiration came from when i was working on a project called Repo Marketplace i'm struggling to find an API that can easily integrate bitcoin cash to accept payment and send payment in my platform after looking around i found this gem called bchjs but it was an SDK not an API so i made that into an API and voila this workspace is born What it does There are many things that this workspace can do i will list it here : Request Name Description Check BCH Balance In this public workspace you can pass your BCH address whether it's mainnet or testnet and get the balance out of it Generate QR Code Often when we try to send money we need to get the QR Code of that BCH Address you can generate your BCH or SLP using this public workspace API Create Wallet Using this public workspace, you can also create BCH Wallet easily Get Transaction Fee Using this public workspace you can get transaction fee before you send the money Send BCH You can send BCH to any BCH address in the network using this Public Workspace Get SLP Balance Using this public workspace you can get list of SLP Token Balance and their token name easily Convert BCH to SLP You can convert BCH to SLP easily How we built it We are using nextjs api routes to create our API then we deploy it to vercel, after that we documented all of our api into Postman Public workspace Challenges we ran into Because this is my first time using postman public workspace i dont know how to make it public Accomplishments that we're proud of We are documenting all of our api, from my own server What we learned Using postman public workspace we can easily share our api collection to the world so that everybody can try our API, we are also learning about environment variable that we can use to globally set the values using this {{values}} syntax we also learn that using tests we can use our own html to see the result much more dynamically let's say we want to see image from base64 we can easily do that using postman What's next for Bitcoin Cash API I'm gonna keep on developing this api so that i can manage my bitcoin cash api easily <div