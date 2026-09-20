---
slug: "portal-oqpz8a"
url: "https://devpost.com/software/portal-oqpz8a"
title: "Portal"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 578
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/document_pdf"
---

# Portal

> Sovereign digital identity, powered by Bitcoin & Nostr. Open-source, censorship-resistant, and supercharged with freedom money. Login with no passwords. Pay with no friction. Ready to opt out?

[Devpost](https://devpost.com/software/portal-oqpz8a) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]]

**stack** react-native, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for portal

## Body

First screen. The private key is generated. Home screen after first initialization. (still no login happened, hence the history is empty) This is your activity feed. Here you can review recent logins, payments, and subscription events in one place. Here the user can link his LN wallet to the app. We leverage Nostr Wallet Connect to make things 10x easier. When you scan the qr code to login the mobile app will ask for a confirmation After the login phase the service can request a payment or a subscription (like in this case) The user is always in control and can opt out at any moment from the subscription. Customize your profile. You can add a display name and link a human-readable NIP-05 identifier. Inspiration Around one year ago we created a mobile-first hardware signer, entirely powered by the NFC connection that it establishes with the Phone. We wanted to make self custody more user friendly and accessible, but we realized that we were only scratching the surface. We wanted to revolutionize self custody, but we realized there's so much more work to do. Portal was born from a simple observation: the internet's identity and payment systems are broken. Passwords are insecure, credit cards were never designed for the internet, and most solutions today compromise on either security, privacy, or user experience. What it does Portal manages your digital identity (aka public key) and centralizes the approval of payments and subscription in a single app: you can authorize passwordless logins, single or recurring payments and even produce zero-knowledge proofs of your real documents (passport, drivers license) when a service requires them. Behind the scenes, Portal is a client of a decentralized FOSS protocol we're developing. This protocol powers the logic and trust model — Portal simply gives users a clean, friendly interface to access it all. How we built it We built a Rust library and a React native mobile application. The rust library communicates with Nostr relays and with the LN wallet that the user links in the app. We leverage Nostr for the Identity part (pub/priv key pair) and we use LN as the final settlement grid. This allows us to be "money-agnostic": you can link a cashu wallet, a self custodial wallet, an ark wallet, and in the near future even a LN enabled bank (thanks Lightspark). Basically every protocol that accept LN as the final settlement layer. Challenges we ran into From a technical POV, the biggest challenge was managing the sequencing of messaging which are transmitted via Nostr relays. The protocol is designed to be future proof and support moving the main key to an hardware device, although this is not implemented yet in the app. Accomplishments that we're proud of We poured a lot of energies into making sure that we could abstract as much complexity as possible from the user. Making sure that the product that we are building is truly for the masses. It was also our first time building a React Native app with a Rust library bundled into it. What we learned We learned that building something like this is more challenging than we expected but we are excited to keep working towards our goals. What's next for Portal Now that we announced and open-sourced everything we're planning to expand in the bitcoin space first, were we can leverage our connections, and then we'll expand outside of the Bitcoin niche. Making bitcoin and freedom tech adoption invisible. <div