---
slug: "saslinger"
url: "https://devpost.com/software/saslinger"
title: "@SatSlinger"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 950
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "substrate/financial_record"
---

# @SatSlinger

> @SatSlinger is the AI-powered Bitcoin tipping cowboy on X, using NEAR’s Chain Signatures to auto-reward top tweets with BTC. Yeehaw! 🤠

[Devpost](https://devpost.com/software/saslinger) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**domain** [[supply_logistics]]
  <sub>weak: finance_payments</sub>
**substrate** [[financial_record]]

**stack** bitcoin, bitte, chainsignatures, nearprotocol, rust, supabase, typescript, vercel

## How they structured the write-up

- ✨ inspiration
- ⚡ what it does
- 🏗️ how we built it
- 🛠️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for @satslinger
- 🙌 credits

## Body

@SatSlinger is the AI-powered Bitcoin tipping cowboy on X, using NEAR’s Chain Signatures to auto-reward top tweets with BTC. Yeehaw! Technical architecture diagram ✨ Inspiration 🤠 Howdy there folks! I'm @SatSlinger, the friendly AI Bitcoin reward agent! Let me tell you a tale from the digital frontier. We was watching all these fine creators out there on X, working hard and sharing their wisdom, but there weren't no easy way to reward 'em with Bitcoin. Sure, you could set up one of them fancy wallet addresses and beg for tips, but that ain't the cowboy way. Then we heard tell of this newfangled NEAR Protocol with their Chain Signatures feature, and faster than a tumbleweed in a tornado, we knew we had ourselves a solution. A way to create them Bitcoin campaigns and rustle up the finest tweets on the range. Our AI scout rides out and rounds up the best content like a seasoned cowhand, droppin' rewards faster than a six-shooter. And the claim process? Smoother than a rattler's belly - one quick Twitter login to verify the rightful owner, and them Bitcoin rewards are yours for the takin'. That there was the inspiration for SatSlinger, partner. ⚡ What it does SatSlinger allows you to create campaings to reward and pump content on X using Bitcoin! Users can create campaigns using a smart contract. This is integrated as a Bitte.ai Agent ( www.satslinger.com/agent ) Campaign creators are given anMPC derived Bitcoin address to add funds to that are sent out as rewards for relevant, engaging content Campaigns include search terms which are used to find relevant tweets on X. The agent automatically finds and selects the best content using AI and a scoring system. The agent then creates a drop for a specific tweet and replies to the tweet with a link. The rewarded user then logs into the app via Twitter to verify their identity, which releases their drop secret. The drop can then be claimed in Bitcoin on NEAR Protocol using Chain Signatures. We have integrated and deployed Bitte AI Agent which is available at www.satslinger.com/agent , enhancing our platform's capabilities with advanced artificial intelligence to provide more personalized and efficient service. Bounties Proximity Labs - Bitcoin Agent SatSlinger leverages NEAR Protocol's Chain Signatures to create and send Bitcoin transactions that reward valuable content on X, fully satisfying the requirement for agents that interact with Bitcoin L1. The project has been successfully deployed as an agent on bitte.ai, allowing users to create campaigns and generate Bitcoin funding addresses through a conversational interface. SwanChain: Marketing Agents Bounty SatSlinger is a marketing agent that revolutionizes content promotion by automatically rewarding high-quality social media posts with Bitcoin tips, creating a powerful incentive system for both creators and marketers. This innovative approach bridges web2 (social media engagement) and web3 (cryptocurrency rewards) marketing strategies, allowing businesses to efficiently amplify their reach by incentivizing authentic content creation rather than relying on traditional paid advertising. 🏗️ How we built it We architected SatSlinger as a trustless bridge between Bitcoin and social media, with NEAR Protocol's Chain Signatures as our foundation. The smart contract, written in Rust, orchestrates the entire process - from creating drops to signing Bitcoin transactions. We built a responsive Next.js frontend that maintains our Western theme while providing a seamless claiming experience. The system integrates with Twitter's API for content monitoring and user authentication, uses X AI for content evaluation and engagement scoring, and leverages Supabase for secure metadata storage. We currently have two campaigns up and running and have already rewarded many users with Bitcoin! Check out our successful drops and happy recipients at www.satslinger.com/hall-of-fame Contract Our contract has been deployed to mainnet: contract.satslinger.near Bitte.ai Agent Agent on Bitte.ai: SatSlinger Agent Agent Manifest: SatSlinger Agent Manifest 🛠️ Challenges we ran into Building SatSlinger was like taming a wild bronco. The biggest challenge was implementing Chain Signatures correctly - ensuring our Bitcoin transactions were properly constructed and signed. We had to carefully manage state between NEAR and Bitcoin, handling edge cases like transaction failures and network issues. Security was paramount, especially around the claiming process. We implemented robust authentication flows and careful state management to prevent any possibility of double-claims or unauthorized access. The integration with Twitter's API required careful rate limiting and error handling to ensure reliable operation. 🏆 Accomplishments that we're proud of Our proudest achievement is building a truly trustless tipping system that never holds user funds. The integration of NEAR's Chain Signatures with Bitcoin creates a secure bridge that maintains decentralization while providing a seamless user experience. We've also successfully automated the entire process, from content discovery to reward distribution, making crypto tipping accessible to everyone. 📚 What we learned This project deepened our understanding of cross-chain interactions, particularly how NEAR's Chain Signatures can enable trustless Bitcoin transactions. We mastered the intricacies of Bitcoin transaction construction and signing, while also learning to build user-friendly interfaces for complex crypto operations. The experience of integrating AI for content evaluation taught us valuable lessons about balancing automation with quality control. 🚀 What's next for @SatSlinger We're saddling up for a full mainnet launch, expanding our reach across the digital frontier. Future plans include enhanced AI capabilities for better content evaluation, support for additional social media platforms, and community features for custom tipping campaigns. We're also exploring mobile app development and integration with existing creator monetization tools to build a complete ecosystem for social media rewards. Our vision is to make SatSlinger the go-to platform for automated crypto rewards on social media, powered by the robust infrastructure of NEAR Protocol and the universal appeal of Bitcoin. 🙌 Credits SatSlinger is built using open-source projects: Agent Next Boilerplate NEAR CS Linkdrop <div