---
slug: "movement-f4nyob"
url: "https://devpost.com/software/movement-f4nyob"
title: "Movement"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 688
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Movement

> Movement is the disruptive blockchain crowdfunding platform - no fees, no middlemen. Every contribution is direct, transparent, and secure, giving real-world peace of mind to backers and creators.

[Devpost](https://devpost.com/software/movement-f4nyob) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: revocation_withdrawal</sub>
**domain** [[civic_government]] [[developer_tools]]
**substrate** [[financial_record]] [[video_visual]]

**stack** css, move, next.js, sui, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for movement

## Body

Explore page Your campaigns Campaign details page Campaign voting Campaign funds withdrawn Campaign failed votes, donators get refunded Homepage Inspiration We all have dreams. But sometimes, we need a little help to realize lofty aspirations. That’s why crowdfunding exists, leveraging the power of community to make big goals a reality, and blockchain-based solutions will only serve to enhance transparency, enforce trust, and eliminate fees to maximize contribution efficiency. We were inspired by the limitations and costs of traditional crowdfunding sites, where backers face platform fees, slow fund disbursements, and an overall lack of transparency. Blockchain’s power to eliminate middlemen and offer verifiable transparency presented an opportunity: what if crowdfunding could be trustless, cost-free, and open to all? What it does Movement is the first blockchain-based crowdfunding platform where every donation is direct, fully transparent, and recorded on-chain. There are no platform fees or third parties, since smart contracts automatically manage fund disbursement and milestone tracking, ensuring 100% of all contributions reach their intended recipient with transparent accountability. We believe that this is the future of crowdfunding. How we built it Movement is built as a TypeScript Next.js web app using React 19 and Tailwind CSS for fast, responsive design, with layout.tsx and globals.css driving our global shell and design tokens. For blockchain integration, we leverage the SUI stack (@mysten/sui, @mysten/dapp-kit), connecting to testnet via networkConfig.ts and surfacing wallet and transaction flows through our dedicated UI components. The app uses React Query for data fetching and caching, and even image content is hosted entirely on chain using Walrus. Content is typed and managed via campaign.ts, and the development environment includes ESLint, Prettier, and simple npm/package.json scripts for local setup. All these tools combine to deliver a secure, scalable, and user-friendly crowdfunding platform on SUI. Challenges we ran into The most difficult challenge for us was learning and applying the Move language, since none of us have worked with Move before this Hackathon. The resources provided definitely helped us learn, but getting used to a new language within a few hours really pushed us out of our comfort zone and tested our adaptability. We faced many other challenges as well, encountering various bugs and errors (one in particular took us 3+ hours to fix, as we eventually found out it was caused by an update to the Sui frontend SDK about 5 days before the Hackathon which caused infinite loops and failure to serialize strings). Huge thanks to the SUI team (shoutout to Zihe and Daniel in particular) for taking the time to help us with our issues, we couldn’t have done it without them! Accomplishments that we're proud of We’re proud of creating a working platform in less than 36 hours, and keeping a positive mindset throughout. For all of our team members, this was our first ever hackathon, and we are proud of what we have achieved despite our inexperience, especially since for most of our team, this was our first time working with blockchain as well. Most of all, we are proud of how much we were able to learn and grow throughout the course of Cal Hacks 12.0! What we learned We learned so much about blockchain and SUI the past few days, about the benefits, applications, and limitations. We now know that blockchain integration helps improve platform reliability and lowers operating costs, and we learned how blockchain can provide immutable record of transactions, playing a major part in transparency. Ultimately, we learned how cool blockchain as a concept is and how much potential it holds for the future. And of course, on a personal level we have learned so much about ourselves, our working style, our physical and mental limits, and our bond as teammates. What's next for Movement Looking ahead, Movement has already added decentralized community voting, and building on that we want to continue rewarding backers with NFT-based incentives. We also want to potentially explore the addition of analytics for campaign creators, and expand support for additional blockchain ecosystems and global currencies. Our vision is a future where anyone, anywhere, can transparently fund and launch world-changing projects, powered by the Movement community. <div