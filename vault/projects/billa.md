---
slug: "billa"
url: "https://devpost.com/software/billa"
title: "Billa"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 304
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Billa

> Billa, a Universal Payment Profile Link

[Devpost](https://devpost.com/software/billa) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]]

**stack** bolt, netlify, nextjs, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for billa

## Body

Inspiration People shouldn’t have to send five different payment details to get paid. Whether you're a freelancer, small business, or creator, collecting money across banks, crypto, and fintech apps is a mess. We wanted a simple way to unify all payment methods into one clean, shareable profile — something like Linktree, but for payments. What it does Billa is a Universal Payment Profile. With one link, users can collect payments through: Traditional bank accounts Crypto wallet addresses (manual input) Digital wallets like PayPal, Cash App, etc. A clean, simple interface for anyone to say: "Here’s how to pay me — pick what works for you." Each user gets a public profile like billa.xyz/username, and can customize it with their payment methods. How we built it Bolt for working MVP Supabase for authentication (Google sign-in) and user/payment data Netlify for deployment TailwindCSS for styling Challenges we ran into Mapping a simple UX that worked across very different payment methods Avoiding feature bloat — we postponed transaction history, wallet connect, and fiat verification Ensuring mobile-first experience worked as well as desktop Accomplishments that we're proud of Built a working MVP: login, create profile, add payment methods, and share your link Got testers to say: “This is what I’ve needed for a long time.” No fluff. Just a tool that helps people get paid. What we learned Simplicity trumps features. The biggest win was reducing steps Most users don't need automation at first — they just want to share how to get paid It’s possible to build something globally useful with a lean stack in days What's next for Billa Add visual analytics (views, payment link clicks) Enable temporary payment links and disposable crypto addresses Integrate direct payment APIs (Stripe, Paystack, TON) Launch public beta and collect live user feedback Custom branding for creators and freelancers <div