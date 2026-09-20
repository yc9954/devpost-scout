---
slug: "trust-enterprises"
url: "https://devpost.com/software/trust-enterprises"
title: "Trust Enterprises"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 941
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# Trust Enterprises

> Bridge the gap between web development and decentralization, in 5 minutes.

[Devpost](https://devpost.com/software/trust-enterprises) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[structural_withholding]] [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** hashgraph, hedera, laravel, nextjs, node.js, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trust enterprises

## Body

Web top Deployment REST API Laravel docs Inspiration I've been working in the blockchain space since 2017 and from a business perspective, especially for tight-budget startups, it is extremely difficult to attract the talent and pay them. We saw a need for a set of tools that empowers web and application developers to easily at web3 or "blockchain" capability to their current SaaS products, quickly using their own technology stacks with no additional cost. Sometimes product teams have no interest in learning decentralized technology, it doesn't mesh with the business needs. There is more and more demand for services to be accountable, to be trusted, and to display proof publically. Fortunately, the days are disappearing where trust is given blindly, we as a society are more aware of our right and our privacy, we need to do what we can to protect ourselves. What it does At the core, we are an API for creating publically provable accountability. This provides the generic ability for any application for any use case to share any intent or a log of an event. In other words, the service hooks into the "real-life" business branded trust of a company that has taken years to cultivate. The developer tools from Trust Enterprises are the intersection of low-cost, decentralization, serverless, and ease of use. No previous blockchain experience required, no additional infrastructure or maintenance cost, and at scale. The current production release of the tools comprises of 3 items: A REST API A serverless deployment, with a rich testing suite. Larvel client Everything is fully documented and allows product teams to add public trust logs or prove intent into any part of their application. Traditionally in blockchain applications, all code tends to be public in nature but in many cases, this has regulatory, compliance, and privacy implications. Using these tools empowers a business with a huge degree of flexibility of displaying business elements that will be beneficial for public accountability whilst keeping clients and users privacy in check. How we built it The core of the project uses Hedera Hashgraph as the trust engine using their Hedera Consensus Service (HCS), we built a NextJS client on top of Vercel for serverless deployments. Making it unique as a decentralized project in that is native serverless by default. The focus was on using a subset of the HCS features to create a simple but powerful tool. We designed a new architecture for building NextJS serverless apps, to optimize readability, reusability, and simplicity whilst being easily extendable. All services are fully tested and production-ready with GitHub actions targeting test suites against NodeJS 10, 12, and 14. The docs are rich and we have a 30-minute video walkthrough comprising of 5 parts that go in-depth. Finally, we built a Laravel client that consumes the API client. There is no other library that exists today which empowers PHP focused developers to start building decentralized/blockchain applications within 5 minutes. Challenges we ran into Naturally, every software project will have difficulties when it comes to writing code, our vision was to have around 70% of planning complete then start executing. Creating our internal architecture to be to the level we demanded took refining and overcoming the limits that are linked with pub/sub protocols within a serverless context required creativity. The greatest challenge right now is adoption and getting the word out, with the range of blockchain projects out that have millions in funding it is hard to stand out from the crowd. We've achieved an exceptional amount with zero external funding and garnered the attention of many of the core team members at Hedera and the DLT community as a whole. Accomplishments that we're proud of Trust Enterprises democratizes access for any budget-tight business into the decentralized arena. As an example DOVU created and deployed their "Proof of Carbon" protocol in less than a day, using our tools. This API and tooling is a gamechanger for every SaaS company that wants to add blockchain or trust features into their services. We stand by the claim that the budget to integrate our free service is minimal, there is no need for blockchain experience or infrastructure cost. What does this mean in real terms? Move your business into the 21st century, don't spend $10k+ "trying out" blockchain, prove the market for your idea or vision using our tools then raise money. What we learned The entire blockchain ecosystem has grown tremendously since 2017, there are more opportunities than ever for projects to build incredible projects, new concepts are being created but with that comes the care that protections to help individuals from risk and harm are still rampant. All everyone wants is for their family, for themselves to have a better life, more work needs to be deployed with protections in place to help the community. This world will grow to become truly cross-chain, where lines are blurred and all users are blind to the complexity and risk behind the scenes. Different blockchains and protocols will be used for different needs. We are simply part of that journey. What's next for Trust Enterprises We are building new Decentralized Finance (DeFi) protocols that run natively on Hedera's ecosystem, we are creating new bridges that connect the Ethereum ecosystem into Hedera which will enable more possibilities in the DeFi space than has previously been possible. Making it safer, more compliant, and cheaper for retail and institutional investors to get involved with crypto markets with Unibar . Solving the risks that come with a lack of liquidity in young open markets and mitigating the risk of fraudulent actors. We are taking part in Hedera Hashgraph 21 hackathon . <div