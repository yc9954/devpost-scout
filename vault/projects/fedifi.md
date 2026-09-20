---
slug: "fedifi"
url: "https://devpost.com/software/fedifi"
title: "FediFi"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 806
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# FediFi

> Ad platforms like Google make $10+ a click. None of that makes it to you. Fedifi: the first-ever decentralized financial infra for web3, built with automated smart contracts to cut out the middleman.

[Devpost](https://devpost.com/software/fedifi) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** activitypub, airtable, bun, bun.js, caldera, ethereum, javascript, next.js, node.js, python, ruby-on-rails, solidity, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into/accomplishments that we're proud of
- what we learned
- what's next for fedifi

## Body

Fediverse Client Displaying Ad Github Repo to download Ad Modules Creator Dashboard to view monetization Inspiration Current advertising platforms like Google make up to $10 a click. None of that makes it to the users. These traditional web2 advertising methods also face intense resistance by the web3 community, and thus monetization methods should be reimagined to fit the new decentralized format of social media. Platforms like Threads, BlueSky, and Mastodon have entered into the Fediverse (decentralized social media platforms). They also have brought along with millions of users. FediFi helps ethically monetize web3 stakeholders with a user-centric and privacy focused approach. What it does FediFi allows instance owners and clients to install and display monetization modules quickly, making it as simple as just 'npm install'. In web3, users reward good content. FediFi allows users to support content and creators with donations and advertisements. Creators, Instances, and Advertisers bid to find an optimal pay structure, which is then automatically executed by a smart contract. By using Caldera and smart contracts, users can take out their money at any time and not be bound to a biweekly payment schedule of web2 platforms. Caldera's layer-2 transaction layer also acts as protection against gas price spikes. 100% of revenue goes towards the intended recipient. Instance moderators can also according choose which ads that best fit their community. Further web3 social monetization features will be added such as super-likes, creator shops, and more. Users can view dashboards to see advertising and post view analytics. Developers can access our documentation to and landing page to answer any questions they may have. How we built it Our tooling consists of many interconnected components: FediFi-Module. A React component developers can easily add to their platforms. Integrate with any instance with npm install. Resembles Google Ad’s Pixel*, and enables creation of autonomous smart contracts to manage transactions. FediFi-Demo. Sample client with FediFi-Module installed. We chose to build a proof of concept on top of Mastodon, but it could be anything. FediFi-Dashboard. Custom Next.js webpage; A one-stop-shop for both advertisers and creators to view advertising, traffic analytics, bidding, and transactions in real time. FediFi-Controller. Bun.js backend with SQLite database. Automatically writes and deploys Smart Contracts to the Caldera chain. Boosted with Caldera's rollups. FediFi-LandingPage. Deployed with Vercel to show documentation and context behind the creation of FetiFi for instance owners to learn more. Challenges we ran into/Accomplishments that we're proud of Our team is really proud to have tackled a difficult project with many complex interacting systems, while having limited exposure to the world of web3. We are proud to have learned so much about web3 technologies and the Fediverse. So much of what we worked on was either in codebases that we did not personally write, or unfamiliar technologies with little documentation. Some of the biggest challenges we faced were: Defining the initial limited feature set because there were so many different avenues that we could have gone down to implement within 36 hours. Lack of documentation with new technologies, where it was up to a lot of (educated) trial and error to finally debug and figure out what was going wrong. Complex interacting systems, as we have 4 or 5 separate components that are all communicating with each other and working together to act as a monetization system. We had to implement smart contracts, backend, frontend, analytics dashboard, and more. What we learned Concretely there were a ton of new technologies that we were all exposed to such as Solidity, Bun.js, and more. However, we also learned a lot about planning out software systems and drawing system diagrams to make sure we didn't waste much time when we jumped in to code. We also had the opportunity to improve our communication, as everyone was working on separate components in tandem before eventually integrating our components together. What's next for FediFi We have many features that we would love to implement if we were given more time. For example: Direct revenue share with fans. We could allow creators to automatically give away percentages of their revenue to people who consume their content. This could be an interesting and new way for creators to grow their audiences and give back to the community. Zero Knowledge Proofs in advertising. Currently we use context based advertising in order to preserve user privacy, but with ZK proofs we could have targeted advertising based on the users interest while still maintaining privacy. Automated Micro Payments. Our users right now need to decide for themselves when to cash out, but eventually we could support an instant deposit into their account per view of their content. We could form a DAO as a decentralized governing entity to ensure a higher level of transparency and trust amongst the community, and allow the community to help make decisions for the future of FetiFi. <div