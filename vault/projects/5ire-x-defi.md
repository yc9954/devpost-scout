---
slug: "5ire-x-defi"
url: "https://devpost.com/software/5ire-x-defi"
title: "Poly X Defi"
hackathon: "Hack The League Chapter 2"
organization: "Hack The League"
winner: true
words: 423
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
---

# Poly X Defi

> Empowering You to Stake, Earn, and Borrow with Confidence with complete anonimity

[Devpost](https://devpost.com/software/5ire-x-defi) · hackathon [[Hack The League Chapter 2]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]

**stack** 5ire, apyhub, nextjs, polygonid, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Inspiration I've always been passionate about exploring new ways to use it for real-world applications. And as someone who's had personal experiences with the shortcomings of traditional banking systems, I was particularly drawn to the potential of decentralized finance. I was inspired by the idea of creating a platform that would allow people to take control of their own finances, without the need for middlemen or centralized institutions. I wanted to create a platform that would provide users with the tools and resources they need to manage their assets effectively, and earn competitive rates of interest without incurring hidden fees or other unnecessary costs. What it does Are you tired of traditional banking systems that leave you with low interest rates and high fees? Look no further than our DeFi platform. Our platform allows users to stake their assets, borrow against them, and earn competitive rates of interest - all while utilizing the security and efficiency of the Polygon network. But we didn't stop there. We've also integrated PolygonID, allowing for easy and secure authentication for our users. No more cumbersome passwords or clunky two-factor authentication systems. With our DeFi platform, we're revolutionizing the way people manage their finances. Join us in the future of finance and start earning today How we built it Adding PolygonID for authentication was a great task , I was new to this stack so it took time to figure out how things are bind up. learnt a lot about VC's. after exploring platform and architecture I created My custom schema, went for setting up issuer but seem to took more time as i have not worked previously with Docker so used Demo issuer To issue claim, then setup on Chain verification. Now comes the smart contract Part , written my defi platform contract using remix debugged it many a times and after hour long session of debugging deployed it to 5ire chain. Now for issuing claim, I set up a template we used Apyhub api to fetch if the email entered is an edu email if it found to be true user is issued a claim and is eligible to get credit. Challenges we ran into Integerating PolygonID and apyhub Api took time, got lot of errors, but resolving them We got our work done. Accomplishments that we're proud of Proud that I have completed integerating PolygonID, deployed contract on 5ire Chain, integrated apyhub api, i was made familliar to apyhub platform which I found interesting and is thinkinf of using it in my later projets <div